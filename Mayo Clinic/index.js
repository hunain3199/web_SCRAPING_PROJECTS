const functions = require("firebase-functions");
const admin = require("firebase-admin");
admin.initializeApp();

const puppeteer = require("puppeteer");
// const crypto = require("crypto");

const firestoreClient = admin.firestore();

async function scrapingPhysiciansLinks() {
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();
    await page.goto('https://jobs.mayoclinic.org/search-jobs/physician%20jobs/33647/1');
    await page.waitForSelector('#system-ialert-button');
    await page.click('#system-ialert-button');
    await page.waitForTimeout(5000);

    const physicianLinks = [];
    let pageNum = 0;
    let flag = true;

    while (flag) {
        try {
            await page.evaluate(() => {
                window.scrollTo(0, document.body.scrollHeight);
            });
            const jobTitleLinks = await page.$$eval('section#search-results-list ul li a', links => links.map(link => link.href));
            physicianLinks.push(...jobTitleLinks);

            pageNum += 1;
            console.log(pageNum);

            if (pageNum !== 2) {
                const navigationPromise = page.waitForNavigation({ timeout: 30000 });
                const clickPromise = page.click('div.pagination-paging a:nth-child(2)');
                await Promise.race([navigationPromise, clickPromise]);
                await page.waitForTimeout(5000);
            } else {
                console.log(physicianLinks);
                console.log(physicianLinks.length);
                flag = false;
            }
        } catch (error) {
            console.error('An error occurred:', error);
            break;
        }
    }

    await browser.close();
    return physicianLinks;
}


async function scrapingPhysiciansData(links) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    let firstIteration = true;
    await page.setViewport({ width: 1366, height: 768 });

    try {
        for (const link of links) {
            console.log(link);
            try {
                await page.goto(link);

                if (firstIteration) {
                    // Accept alert button only in the first iteration
                    const acceptButton = await page.waitForXPath("//button[@id='system-ialert-button']", { visible: true, timeout: 10000 });
                    await acceptButton.click();
                    firstIteration = false; // Update flag after first iteration
                }

                await page.waitForSelector('.title-wrapper');

                const reqNoElement = await page.$x("//div[@class='title-wrapper']/span[@class='job-id job-info']");
                const reqNo = await reqNoElement[0].evaluate(node => node.textContent);
                const jobId = reqNo.match(/Job ID (.+)/)[1];
                const hospitalName = "Mayo Clinic";
                const nameElement = await page.$('.title-wrapper h2');
                const name = await (nameElement ? nameElement.evaluate(node => node.textContent) : '');
                const locationElement = await page.$('.title-wrapper ul li:nth-child(1)');
                const location = await (locationElement ? locationElement.evaluate(node => node.textContent) : '');
                const [city, state] = location.split(", ");
                const jdLink = link;
                const jobTypeElement = await page.$('.title-wrapper ul li:nth-child(2)');
                const jobType = await (jobTypeElement ? jobTypeElement.evaluate(node => node.textContent) : '');
                const departmentElement = await page.$('.title-wrapper ul li:nth-child(3)'); // Modified selector
                const department = await (departmentElement ? departmentElement.evaluate(node => node.textContent) : '');
                const url = jdLink;
                const md5Hash = require('crypto').createHash('md5').update(url).digest('hex');
                console.log("MD5 hash:", md5Hash);

                const docId = md5Hash;
                const collectionRef = firestoreClient.collection('jobdsd');
                const existingDoc = await collectionRef.doc(docId).get();

                if (existingDoc.exists) {
                    console.log(`Document with ID ${docId} already exists. Not adding again.`);
                } else {
                    const addData = {
                        'hospital_name': hospitalName,
                        'req_no': jobId,
                        'name': name,
                        'department': department,
                        'job_description_link': jdLink,
                        'location_city': city,
                        'location_state': state,
                        'job_type': jobType,
                        'md5_hash': md5Hash
                    };

                    await collectionRef.doc(docId).set(addData);
                    console.log(`Document added with ID: ${docId}`);
                }
            } catch (error) {
                console.error(`Error processing link ${link}: ${error}`);
            }
        }
    } catch (error) {
        console.error("An error occurred during scraping:", error);
    } finally {
        await browser.close();
    }
}





async function main() {
    const links = await scrapingPhysiciansLinks();
    await scrapingPhysiciansData(links);
}

main();