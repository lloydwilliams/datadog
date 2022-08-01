package com.graphqljava.tutorial.bookdetails;

import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.alibaba.fastjson.JSONObject;

import io.opentracing.Span;
import io.opentracing.util.GlobalTracer;

import graphql.ExecutionResult;
import graphql.execution.ExecutionId;
import graphql.execution.instrumentation.InstrumentationContext;
import graphql.execution.instrumentation.SimpleInstrumentation;
import graphql.execution.instrumentation.SimpleInstrumentationContext;
import graphql.execution.instrumentation.parameters.InstrumentationExecutionParameters;
import graphql.language.AstPrinter;
import graphql.language.Document;
import graphql.parser.Parser;

final class RequestLoggingInstrumentation extends SimpleInstrumentation {

    private static final Logger logger = LoggerFactory.getLogger(RequestLoggingInstrumentation.class);

    @Override
    public InstrumentationContext<ExecutionResult> beginExecution(InstrumentationExecutionParameters parameters) {
        long startMillis = System.currentTimeMillis();
        ExecutionId executionId = parameters.getExecutionInput().getExecutionId();
        
        if (logger.isInfoEnabled()) {
            logger.info("GraphQL execution {} started", executionId);

            String query = parameters.getQuery();            
            Parser parser = new Parser();
            Document doc = parser.parseDocument(query);
            String astString = AstPrinter.printAstCompact(doc);
            logger.info("[{}] query: {}", executionId, astString);
            
            final Span span = (GlobalTracer.get()).activeSpan();
            if (span != null) {	
              span.setTag("graphql.query", astString);
            }

            if (parameters.getVariables() != null && !parameters.getVariables().isEmpty()) {
                
            	Map<String,Object> variablesMap = parameters.getVariables();
            	JSONObject varsJSON = new JSONObject(variablesMap);
            	logger.info("[{}] variables: {}", executionId, varsJSON.toString());
                
                if (span != null) {
                	span.setTag("graphql.variables", varsJSON.toString());
                }               
            }
        }

        return new SimpleInstrumentationContext<ExecutionResult>() {
            @Override
            public void onCompleted(ExecutionResult executionResult, Throwable t) {
                if (logger.isInfoEnabled()) {
                    long endMillis = System.currentTimeMillis();

                    if (t != null) {
                        logger.info("GraphQL execution {} failed: {}", executionId, t.getMessage(), t);
                    } else {
                    	
                    	Map<String,Object> resultMap = executionResult.toSpecification();                    	
                    	JSONObject resultJSON = new JSONObject(resultMap);
                    	                        
                    	long execTime = endMillis - startMillis ;
                    	final Span span = (GlobalTracer.get()).activeSpan();
                        if (span != null) {
                        	span.setTag("graphql.execution.id", executionId.toString());
                        	span.setTag("graphql.exectime.millis", execTime);
                        	
                        	// you probably don't want to monitor the result on a span
                        	// in cases where it could potentially be large
                        	span.setTag("graphql.result", resultJSON.toString());
                        	// /
                        }
                    	
                        logger.info("[{}] completed in {} ms", executionId, execTime);
                        logger.info("[{}] result: {}", executionId, resultJSON.toString());
                    }
                }
            }
        };
    }
    
    
}

