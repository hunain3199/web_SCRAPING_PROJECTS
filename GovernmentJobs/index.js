const functions = require("firebase-functions");
const admin = require("firebase-admin");
admin.initializeApp();

const puppeteer = require("puppeteer");
// const crypto = require("crypto");

const firestoreClient = admin.firestore();

async function scrapingPhysiciansLinks(firstPage, lastPage) {
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();
    const linksList = [];

    for (let i = firstPage; i <= lastPage; i++) {
        const link = `https://www.governmentjobs.com/careers/umcsn?category[0]=Physicians&sort=PositionTitle%7CAscending&page=${i}`;
        await page.goto(link, { timeout: 60000 }); // Increase timeout to 60 seconds

        await page.waitForSelector('li.list-item > h3 > a');

        const jobTitlesLinks = await page.$$eval('li.list-item > h3 > a', links => links.map(link => link.href));
        linksList.push(...jobTitlesLinks);
    }

    await browser.close();
    console.log(linksList);
    console.log(linksList.length);
    return linksList;
}

async function scrapingPhysiciansData(links) {
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();

    for (const link of links) {
        try {
            console.log(link);
            await page.goto(link, { timeout: 60000 }); // Increase timeout to 60 seconds

            await page.waitForTimeout(30000); // Wait for 30 seconds

            const jobIDElement = await page.$x('(//div[@class="term-container-new"]/div/div/div/div)[8]');
            const jobID = await page.evaluate(element => element.textContent, jobIDElement[0]);

            const hospitalNameElement = await page.$x('//div[@class="agency-info agency-name"]/dl/dd');
            const hospitalName = await page.evaluate(element => element.textContent, hospitalNameElement[0]);

            const locationElement = await page.$x('(//div[@class="term-container-new"]/div/div/div/div)[4]');
            const location = await page.evaluate(element => element.textContent, locationElement[0]);
            const [city, state] = location.includes(',') ? location.split(', ') : ['', ''];

            const departmentElement = await page.$x('(//div[@class="term-container-new"]/div/div/div/div)[10]');
            const department = await page.evaluate(element => element.textContent, departmentElement[0]);

            const jdLink = link;

            const nameElement = await page.$x('//h2[@class="entity-title"]');
            const name = await page.evaluate(element => element.textContent, nameElement[0]);

            const jobTypeElement = await page.$x('(//div[@class="term-container-new"]/div/div/div/div)[6]');
            const jobType = await page.evaluate(element => element.textContent, jobTypeElement[0]);

            const salaryElement = await page.$x('(//div[@class="term-container-new"]/div/div/div/div)[2]');
            const salary = await page.evaluate(element => element.textContent, salaryElement[0]);


            const url = jdLink;
            const md5Hash = require('crypto').createHash('md5').update(url).digest('hex');
            console.log("MD5 hash:", md5Hash);

            

            const collectionRef = firestoreClient.collection("jobdd");
            const existingDoc = await collectionRef.doc(md5Hash).get();

            if (existingDoc.exists) {
                console.log(`Document with ID ${md5Hash} already exists. Not adding again.`);
            } else {
                const addData = {
                    hospital_name: hospitalName,
                    req_no: jobID,
                    name: name,
                    department: department,
                    job_description_link: jdLink,
                    location_city: city,
                    location_state: state,
                    job_type: jobType,
                    salary: salary,
                    md5_hash: md5Hash
                };
                await collectionRef.doc(md5Hash).set(addData);
                console.log(`Document added with ID: ${md5Hash}`);
            }
            continue;
        } catch (error) {
            console.error(error);
            // Handle errors or log URLs to a file
            
        }
    }

    await browser.close();
}

async function main() {
    const firstPage = 1;
    const lastPage = 2; // Modify this according to your requirement
    const links = await scrapingPhysiciansLinks(firstPage, lastPage);
    await scrapingPhysiciansData(links);
}

main();