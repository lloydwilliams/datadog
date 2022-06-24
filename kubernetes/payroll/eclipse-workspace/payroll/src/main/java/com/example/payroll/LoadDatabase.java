package com.example.payroll;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.MDC;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import datadog.trace.api.CorrelationIdentifier;

@Configuration
class LoadDatabase {

  private static final Logger logger = LoggerFactory.getLogger(LoadDatabase.class);

  @Bean
  CommandLineRunner initDatabase(EmployeeRepository repository) {
	  
    return args -> {
      	try {
      	    MDC.put("dd.trace_id", CorrelationIdentifier.getTraceId());
      	    MDC.put("dd.span_id", CorrelationIdentifier.getSpanId());

              logger.info("Starting initializing Database");
              logger.info("Preloading " + repository.save(new Employee("Bilbo Baggins", "burglar")));
              logger.info("Preloading " + repository.save(new Employee("Frodo Baggins", "thief")));
      	    
      	} finally {
      	    MDC.remove("dd.trace_id");
      	    MDC.remove("dd.span_id");
      	}  
      
    };
  }
}