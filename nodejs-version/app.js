const nodemailer = require('nodemailer');
const fs = require('fs');
const path = require("path");


let rawdata = fs.readFileSync("user_input.json");
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
  let info = await transporter.sendMail({
    from: 'harshasandamal10@gmail.com', // sender address
    to: to, // list of receivers
    subject: subject, // Subject line
    // text: text, // plain text body
    html: "<div>Message</div>",
  });

  console.log("Message sent to- %s", to);
}
