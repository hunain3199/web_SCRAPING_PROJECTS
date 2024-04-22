const functions = require("firebase-functions");
const admin = require("firebase-admin");
admin.initializeApp();

const puppeteer = require("puppeteer");
// const crypto = require("crypto");

const firestoreClient = admin.firestore();

async function scrapingPhysiciansLinks(firstPage, lastPage) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    const linksList = [];

    for (let i = firstPage; i <= lastPage; i++) {
        linksList.push(`https://careers.pennmedicine.org/search/physician/jobs/in?page=${i}&q=physician#`);
    }

    const physicianLinks = [];

    for (const link of linksList) {
        await page.goto(link);
        await page.evaluate(() => {
            window.scrollTo(0, document.body.scrollHeight);
        });

        const jobTitlesLinks = await page.$$('div.jobs-section__item.padded-v-small div div a');
        for (const jobLink of jobTitlesLinks) {
            const href = await jobLink.getProperty('href');
            const jobLinkText = await href.jsonValue();
            physicianLinks.push(jobLinkText);
        }
    }

    await browser.close();
    console.log(physicianLinks);
    console.log(physicianLinks.length);
    return physicianLinks;
}

async function scrapingPhysiciansData(links) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    for (const link of links) {
        try {
            console.log(link);
            await page.goto(link);
            await page.evaluate(() => {
                window.scrollTo(0, document.body.scrollHeight);
            });
            await page.waitForTimeout(2000);
            let jobIDText = await page.evaluate(() => {
                const jobIDStrong = document.evaluate("//div[contains(@class, 'similar-jobs-element-js')]//strong[contains(text(), 'Job ID:')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                return jobIDStrong.nextSibling.textContent.trim();
            });
            jobIDText = jobIDText || " ";
            let department = await page.evaluate(() => {
                const departmentStrong = document.evaluate("//div[contains(@class, 'similar-jobs-element-js')]//strong[contains(text(), 'Category:')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                return departmentStrong.nextSibling.textContent.trim();
            });
            department = department || " ";
            let jobType = await page.evaluate(() => {
                const jobTypes = document.evaluate("//div[contains(@class, 'similar-jobs-element-js')]//strong[contains(text(), 'Work Schedule:')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                return jobTypes.nextSibling.textContent.trim();
            });
            jobType = jobType || " ";
            let location = await page.evaluate(() => {
                const locationTypes = document.evaluate("//div[contains(@class, 'similar-jobs-element-js')]//strong[contains(text(), 'Location:')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                let locationTypesText = locationTypes.nextSibling.textContent.trim();
                const firstCommaIndex = locationTypesText.indexOf(',');
                const cityFirstComma = locationTypesText.slice(0, firstCommaIndex).trim();
                const secondCommaIndex = locationTypesText.indexOf(',', firstCommaIndex + 1);
                const stateSecondComma = locationTypesText.slice(firstCommaIndex + 1, secondCommaIndex).trim();
                return { cityFirstComma, stateSecondComma };
            });
            location = location || { cityFirstComma: " ", stateSecondComma: " " };
            let name = await page.evaluate(() => {
                const nameElement = document.querySelector("h1.heading-2");
                return nameElement ? nameElement.textContent.trim() : " ";
            });
            let professional = " ";
            if (name) {
                const firstDashIndex = name.indexOf('-');
                const secondDashIndex = name.indexOf('-', firstDashIndex + 1);
                const professionalArea = name.slice(firstDashIndex + 1, secondDashIndex).trim();
                if (professionalArea === "Internal Medicine" || professionalArea === "Family Medicine" || professionalArea === "Family Medicine or Internal Medicine" || professionalArea === "Family or Internal Medicine") {
                    professional = professionalArea;
                } else {
                    professional = "Family Medicine";
                }
            }
            let jdLink = link;
            const jobTitle = jdLink.split('/').slice(-1)[0].split('-').slice(1, 4);
            const formattedTitle = jobTitle.map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ').replace('-', ' ');
            const url = jdLink;
            const md5Hash = require('crypto').createHash('md5').update(url).digest('hex');
            console.log("MD5 hash:", md5Hash);
            const collectionRef = firestoreClient.collection("jobs");
            const existingDoc = await collectionRef.doc(md5Hash).get();
            if (existingDoc.exists) {
                console.log(`Document with ID ${md5Hash} already exists. Not adding again.`);
            } else {
                const addData = {
                    'hospital_name': "Penn Presbyterian Medical Center",
                    'req_no': jobIDText,
                    'name': formattedTitle,
                    'department': department,
                    'job_description_link': jdLink,
                    'location_city': location.cityFirstComma,
                    'location_state': location.stateSecondComma,
                    'job_type': jobType,
                    'professional_area': professional,
                    'md5_hash': md5Hash
                };
                await collectionRef.doc(md5Hash).set(addData);
                console.log(`Document added with ID: ${md5Hash}`);
            }
            continue;
        } catch (error) {
            console.log(error);
        }
    }
    await browser.close();
}

async function main() {
    const firstPage = 1;
    const lastPage = 2;  // Modify this according to your requirement
    const links = await scrapingPhysiciansLinks(firstPage, lastPage);
    await scrapingPhysiciansData(links);
}

main();