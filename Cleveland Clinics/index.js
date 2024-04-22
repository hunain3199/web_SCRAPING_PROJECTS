const functions = require("firebase-functions");
const admin = require("firebase-admin");
admin.initializeApp();

const puppeteer = require("puppeteer");
const crypto = require("crypto");

const firestoreClient = admin.firestore();

async function scrapePhysiciansLinks(firstPage, lastPage) {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  const linksList = [];

  for (let i = firstPage; i <= lastPage; i++) {
    linksList.push(
      `https://jobs.clevelandclinic.org/job-search-results/?keyword=Medicine%20Physician&pg=${i}&category[]=Physician`
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

        console.log(jobLink);
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

async function scrapePhysiciansData(links) {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  for (const link of links) {
    await page.goto(link);
    await page.evaluate(() => {
      window.scrollTo(0, document.body.scrollHeight);
    });

    try {
      const hopistalName = "Cleveland Clinic";
      const reqNoElement = await page.$x('(//div[@class="jd-item"]/span)[1]');
      const reqNo = await page.evaluate(
        (element) => element.textContent,
        reqNoElement[0]
      );

      const nameElement = await page.$x(
        '//div[@class="fusion-text fusion-text-4"]/h1'
      );
      const name = await page.evaluate(
        (element) => element.textContent,
        nameElement[0]
      );

      const locationCityElement = await page.$x(
        '(//div[@class="jd-item"]/span)[2]'
      );
      const locationCity = await page.evaluate(
        (element) => element.textContent,
        locationCityElement[0]
      );
      
      // Additional lines for processing the text
      const firstWordCity = locationCity.split(',')[0].trim();

      const locationStateElement = await page.$x(
        '//div[@class="fusion-text fusion-text-4"]/p/span'
      );
      const locationState = await page.evaluate(
        (element) => element.textContent,
        locationStateElement[0]
      );
      
      const parts = locationState.split(',');
      const secondElement = parts[1].trim();
      const thirdElement = parts[parts.length - 1].trim();
      const concatState = secondElement + "," + thirdElement;

      const departmentElement = await page.$x(
        '//div[@class="jd-item jd-dept2"]'
      );
      const departmentText = await page.evaluate(
        (element) => element.textContent,
        departmentElement[0]
      );
      const updatedDepartment = departmentText
        ? departmentText.replace(/^Department: /, "")
        : "";

      const jdLink = link;

      const jobTypeElement = await page.$x('(//div[@class="jd-item"]/span)[4]');
      const jobType = await page.evaluate(
        (element) => element.textContent,
        jobTypeElement[0]
      );

      const professionalAreaElement = await page.$x(
        '(//div[@class="jd-item"]/span)[3]'
      );
      const professionalArea = await page.evaluate(
        (element) => element.textContent,
        professionalAreaElement[0]
      );

      storeJob(
        hopistalName,
        reqNo,
        name,
        updatedDepartment,
        jdLink,
        firstWordCity,
        concatState,
        jobType,
        professionalArea
      );
    } catch (error) {
      console.error(error);
      // Handle errors here
    }
  }

  await browser.close();
}

const storeJob = async (
  hopistalName,
  reqNo,
  name,
  department,
  jdLink,
  firstWordCity,
  concatState,
  jobType,
  professionalArea
) => {
  const md5_hash = crypto.createHash("md5").update(jdLink).digest("hex");
  const docId = md5_hash;

  const collectionRef = firestoreClient.collection("jobdd");
  const existingDoc = await collectionRef.doc(docId).get();

  if (existingDoc.exists) {
    console.log(`Document with ID ${docId} already exists. Not adding again.`);
  } else {
    const addData = {
      hopistalName,
      req_no: reqNo,
      name,
      department,
      job_description_link: jdLink,
      location_city: firstWordCity,
      location_state: concatState,
      job_type: jobType,
      professional_area: professionalArea,
      md5_hash,
    };

    const docRef = collectionRef.doc(docId);
    await docRef.set(addData);
    console.log(`Document added with ID: ${docId}`);
  }
};

async function main() {
  const firstPage = 1;
  const lastPage = 5; // Modify this according to your requirement

  console.log("Scraping links...");
  const links = await scrapePhysiciansLinks(firstPage, lastPage);
  console.log("Scraping job data...");
  await scrapePhysiciansData(links);
}
// main()

exports.clevelandClinic = functions
  .runWith({ timeoutSeconds: 300, memory: "4GB" })
  .https.onRequest(async (req, res) => {
    await main();
    res.send("Done");
  });