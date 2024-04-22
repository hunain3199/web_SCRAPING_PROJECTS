const functions = require("firebase-functions");
const admin = require("firebase-admin");
admin.initializeApp();

const puppeteer = require("puppeteer");
const { Storage } = require("@google-cloud/storage");
const crypto = require("crypto");

// Create a Firestore client
const firestoreClient = admin.firestore();

async function scrapingPhysiciansLinks(firstPage, lastPage) {
  const browser = await puppeteer.launch({ headless: true, timeout: 60000 }); // 60 seconds timeout

  const page = await browser.newPage();
  const linksList = [];

  for (let i = firstPage; i <= lastPage; i++) {
    linksList.push(
      `https://jobs.northwell.edu/job-search-results/?keyword=physician%20jobs&pg=${i}`
    );
  }

  const physicianLinks = [];

  for (const link of linksList) {
    await page.goto(link);
    await page.evaluate(() => {
      window.scrollTo(0, document.body.scrollHeight);
    });

    try {
      const jobTitlesLinks = await page.$x('//div[@class="jobTitle"]/a');

      for (const jobLinkElement of jobTitlesLinks) {
        const jobLink = await page.evaluate(
          (link) => link.href,
          jobLinkElement
        );

        physicianLinks.push(jobLink);
      }
    } catch (error) {
      console.error(error);
      continue;
    }
  }

  await browser.close();
  return physicianLinks;
}

async function scrapingPhysiciansData(links) {
  const browser = await puppeteer.launch({ headless: true, timeout: 60000 }); // 60 seconds timeout
  const page = await browser.newPage();

  for (const link of links) {
    await page.goto(link);
    await page.evaluate(() => {
      window.scrollTo(0, document.body.scrollHeight);
    });

    try {
      const reqOnlyElement = await page.$x('//div[@class="job-field"][1]');
      const reqOnlyText = await page.evaluate(
        (element) => element.textContent,
        reqOnlyElement[0]
      );
      const reqNoList = reqOnlyText.match(/\d+/);
      const reqNo = reqNoList ? reqNoList[0] : null;

      const hospitalName = "Northwell Health";
      const nameElement = await page.$x('//h1[@id="Job Title"]');
      const name = await page.evaluate(
        (element) => element.textContent,
        nameElement[0]
      );

      const locationElement = await page.$x('//span[@class="location"]');
      const location = await page.evaluate(
        (element) => element.textContent,
        locationElement[0]
      );
      const locationParts = location.split(',');
      const locationCity = locationParts[locationParts.length - 2].trim();
      const locationState = locationParts[locationParts.length - 1].trim();

      const departmentElement = await page.$x(
        '//div[@class="job-field"][4]/span'
      );
      const department = await page.evaluate(
        (element) => element.textContent,
        departmentElement[0]
      );

      const jdLink = link;

      const jobTypeElement = await page.$x(
        '//div[@class="job-field job-shift"]/span'
      );
      const jobType = await page.evaluate(
        (element) => element.textContent,
        jobTypeElement[0]
      );

      const professionalAreaElement = await page.$x(
        '//div[@class="job-field"][2]/span'
      );
      const professionalArea = await page.evaluate(
        (element) => element.textContent,
        professionalAreaElement[0]
      );

      const salaryElement = await page.$x('//div[@class="job-field"][5]/span');
      const salary = await page.evaluate(
        (element) => element.textContent,
        salaryElement[0]
      );

      // Write data to physicians_dataa.csv
      // You can add the logic to write data to a CSV file here

      const url = jdLink;
      const md5Hash = crypto.createHash("md5").update(url).digest("hex");

      const docId = md5Hash;
      const collectionRef = firestoreClient.collection('jobsss');
      const existingDoc = await collectionRef.doc(docId).get();

      if (existingDoc.exists) {
        console.log(`Document with ID ${docId} already exists. Not adding again.`);
      } else {
        const addData = {
          hospital_name: hospitalName,
          req_no: reqNo,
          name: name,
          department: department,
          job_description_link: jdLink,
          location_city: locationCity,
          location_state: locationState,
          job_type: jobType,
          professional_area: professionalArea,
          md5_hash: md5Hash,
          salary: salary
        };

        const docRef = collectionRef.doc(docId);
        await docRef.set(addData);
        console.log(`Document added with ID: ${docId}`);
      }
    } catch (error) {
      console.error(`Error processing link ${link}: ${error}`);
    }
  }

  await browser.close();
}

async function main() {
  const firstPage = 1;
  const lastPage = 2; // Modify this according to your requirement

  console.log("Scraping links...");
  const links = await scrapingPhysiciansLinks(firstPage, lastPage);
  console.log("Scraping data...");
  await scrapingPhysiciansData(links);
}
// main()
exports.northwellHealth = functions
  .runWith({ timeoutSeconds: 300, memory: "4GB" })
  .https.onRequest(async (req, res) => {
    await main();
    res.send("Done");
  });