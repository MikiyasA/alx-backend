// Create a queue with Kue
// Create a queue named push_notification_code, and create a job with the object created before
// When the job is created without error, log to the console Notification job created: JOB ID
// When the job is completed, log to the console Notification job completed
// When the job is failing, log to the console Notification job failed

import kue from 'kue';
const push_notification_code = kue.createQueue({ name: 'push_notification_node' });


const jobData = {
  phoneNumber: '0921162566',
  message: 'Hello, Everyone!',  
};

const job = push_notification_code
  .create('notification', jobData)
  .save((error) => {
    if (error) console.error(error);
    else console.log(`Notification job created: ${job.id}`); 
  });

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
