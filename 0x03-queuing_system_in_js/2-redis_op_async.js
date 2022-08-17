// Using Babel and ES6, write a script named 0-redis_client.js.
// It should connect to the Redis server running on your machine:

import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('error', (error) => {
  if (error) console.log(`Redis client not connected to the server: ${error}`);
}).on('ready', () => {
  console.log('Redis client connected to the server');
});


// setNewSchool:  It accepts two arguments schoolName, and value.
//        It should set in Redis the value for the key schoolName
//        It should display a confirmation message using redis.print

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, reply) => {
    redis.print(`Reply: ${reply}`);
  });
}

// Using promisify, modify the function displaySchoolValue to use ES6 async / await

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  const response = await getAsync(schoolName);
  console.log(response);    
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
