
export default function createPushNotificationsJobs(jobs, queue) {
  if (Array.isArray(jobs) !== true) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((job) => {
    const newJob = queue.create('notification', job);
    newJob.save((err) => {
      if (err) console.error(`Notification job ${newJob.id} failed: ${err}`);
    });
    newJob.on('enqueue', () => {
    console.log(`Notification job created: ${newJob.id}`);
    })
      .on('complete', () => {
        console.log(`Notificationn job #${newJob.id} completed`);
      })
      .on('progress', (progress, _) => {
        console.log(`Notification job #${newJob.id} ${progress}% complete`);
      });
  });
}
