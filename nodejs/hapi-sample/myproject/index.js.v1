'use strict';
// This line must come before importing any instrumented module.
// const tracer = require('dd-trace').init();

// https://docs.datadoghq.com/tracing/connect_logs_and_traces/nodejs/
const tracer = require('dd-trace').init({
    logInjection: true
});

const Hapi = require('@hapi/hapi');
const appRoot = '/u01/nodejs/hapi-sample/myproject'

const { createLogger, format, transports } = require('winston');

const logger = createLogger({
  level: 'info',
  exitOnError: false,
  format: format.json(),
  transports: [
    new transports.File({ filename: `${appRoot}/logs/hapi-sample.log` }),
  ],
});

module.exports = logger;

const init = async () => {

    const server = Hapi.server({
        port: 4000,
        host: 'localhost'
    });
    
    server.route({
            method: 'GET',
            path: '/',
            handler: (request, h) => {
              
              logger.log('info', 'Here is some info in a simple log!');
              logger.log('warn', 'I need to warn you of something!');
              logger.info('Hello log with metas',{color: 'blue' });
              logger.warn('This is another way to warn',{color: 'red' });
	            logger.error('Oh no! Error!',{notify: 'devops'});
              console.log('I am writing a console log also!');
              
              return 'Hello World!';
            }
        });


    await server.start();
    console.log('Server running on %s', server.info.uri);
};

process.on('unhandledRejection', (err) => {

    console.log(err);
    process.exit(1);
});

init();
