const nodemailer = require('nodemailer');
const fs = require('fs');
const path = require("path");


let rawdata = fs.readFileSync("input.json");
let input = JSON.parse(rawdata);

const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: input.email_address,
    pass: input.app_password,
  },
  port: 465,
  secure: true, 
});

const addresses = input.addresses;

console.log("Email Sending Started");
for (let i = 0; i < addresses.length; i++) {
  let toEmail = addresses[i];
  sendEmail(toEmail,input.subject,input.text,transporter).catch(
    console.error
  ) 
}


async function sendEmail(to,subject,text,transporter) {

  // send mail with defined transport object
  // let info = await transporter.sendMail({
  //   from: 'harshasandamal10@gmail.com', // sender address
  //   to: to, // list of receivers
  //   subject: subject, // Subject line
  //   // text: text, // plain text body
  //   html: "<div>Dear sir,<div><br></div><div>I am one of the thousand Engineers who obtained 476 visa in order to work in Australia which will fulfill&nbsp;Australia's&nbsp;skill shortage. But unfortunately, the&nbsp;Australian border was closed due to Covid19 and it was open almost 2 years later. Thousands of 476 Visa holder's visas got expired due to this.&nbsp;&nbsp;</div><div><br></div><div>Recently Prime Minister has informed that Government is allowing extending 485 expired visas but has not mentioned anything regarding the 476 Visas. I had&nbsp;spent lot of time, money, and effort on granting this visa, yet expired it with no fault&nbsp;of me.&nbsp;</div><div><br></div><div>I kindly request from you raise&nbsp;your&nbsp;voice on behalf of thousands of expired 476 visa holders like me. Please help thousands of engineers to restore their expired visas. This action will help to drastically reduce the skill shortage in Australia.<br></div><div><br></div><div>Thanks,</div><div><br></div><div>Name: Harsha Sandamal Siriwardana</div><div>Mobile Number: 94716315445</div><div>Residential&nbsp;Address: Gamachchige watta, Malimbada,Palatuwa,Matara,Sri Lanka.<wbr>81050</div></div>",
  // });

  console.log("Message sent to- %s", to);
}
