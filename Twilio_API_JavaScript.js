// npm install twilio

const Twilio = require("twilio");

const client = new Twilio(
    "{Enter Your Account SID}",
    "{Enter Your Auth Token}"
    );

client.messages
    .list()
    .then(messages =>
        console.log(`The most recent message is ${messages[0].body}`)
    ).catch(error => console.error(error));

console.log('Gathering your message log'); 

// run it from your terminal w/ node {file name}.js