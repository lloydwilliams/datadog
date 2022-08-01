package com.graphqljava.tutorial.bookdetails;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.MDC;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import datadog.trace.api.CorrelationIdentifier;
//import datadog.trace.api.Trace;

@SpringBootApplication
public class BookDetailsApplication {

	private static Logger logger = LoggerFactory.getLogger(BookDetailsApplication.class);

    //@Trace(operationName = "BookDetailsApplication.main", resourceName = "BookDetailsApplication.main")
	public static void main(String[] args) {
				
		// There must be spans started and active before this block.
    	try {
    	    MDC.put("dd.trace_id", CorrelationIdentifier.getTraceId());
    	    MDC.put("dd.span_id", CorrelationIdentifier.getSpanId());

    	  //logger.debug("Debug Starting BookDetailsApplication");
            logger.info("Starting BookDetailsApplication");
    	    
    	} finally {
    	    MDC.remove("dd.trace_id");
    	    MDC.remove("dd.span_id");
    	}  
		
		SpringApplication.run(BookDetailsApplication.class, args);
	}

}
