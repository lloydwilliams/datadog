'use strict';
// This line must come before importing any instrumented module.
// const tracer = require('dd-trace').init();

// https://docs.datadoghq.com/tracing/connect_logs_and_traces/nodejs/
const tracer = require('dd-trace').init({
    appsec: true,
    logInjection: true
});

const Hapi = require('@hapi/hapi');

const { createLogger, format, transports } = require('winston');
require('winston-daily-rotate-file');
const fs = require('fs');
const path = require('path');
const logDir = 'logs';

// Create the log directory if it does not exist
if (!fs.existsSync(logDir)) {
  fs.mkdirSync(logDir);
}

//https://github.com/winstonjs/winston-daily-rotate-file
const transport1 = new transports.DailyRotateFile({
  level: 'info',
  filename: `${logDir}/application-%DATE%.log`,
  datePattern: 'YYYY-MM-DD-HH-MM',
  zippedArchive: false,
  maxFiles: '4d',
  maxSize: '2m',
  createSymlink: true,
  symlinkName: 'current.log'
});

const logger = createLogger({
  // change level if in dev environment versus production
  level: 'info',
  format: format.combine(
    format.timestamp({
      format: 'YYYY-MM-DD HH:mm:ss'
    }),
    format.json()
  ),
  transports: [
    transport1
  ]
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
              logger.warn('This is another way to warn',{color: 'yellow' });
	            logger.error('Oh no! Error!',{color: 'red'});
              console.log('I am writing a console log also!');
              
              return 'Hello World!';
            }
        });


    server.route({
            method: 'GET',
            path: '/error',
            handler: (request, h) => {
              
              logger.error('Oh no! There was an Error! This is something important you need to know when this error happens.',{color: 'red'});
              
              return 'Hi! There was an error processing the business logic!';
            }
        });

    server.route({
            method: 'GET',
            path: '/warn',
            handler: (request, h) => {
              
              logger.warn('I need to warn you of something that happened during the execution of business logic!',{color: 'yellow' });
              
              return 'Hi! There was a warning during processing the business logic!';
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
