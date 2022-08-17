// Using Babel and ES6, write a script named 0-redis_client.js.
// It should connect to the Redis server running on your machine:

import redis from 'redis';

const client = redis.createClient();

client.on('error', (error) => {
  if (error) console.log(`Redis client not connected to the server: ${error}`);
}).on('ready', () => {
  console.log('Redis client connected to the server');
});
