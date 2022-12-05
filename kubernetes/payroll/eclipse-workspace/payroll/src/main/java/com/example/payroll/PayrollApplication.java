package com.example.payroll;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
//import org.slf4j.MDC;

@SpringBootApplication
public class PayrollApplication {

	private static final Logger logger = LoggerFactory.getLogger(PayrollApplication.class);
	
	
	public static void main(String[] args) {
		
		logger.info("Starting payroll application.");

		SpringApplication.run(PayrollApplication.class, args);

	}

}
