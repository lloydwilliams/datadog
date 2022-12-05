/*
 *  https://spring.io/guides/tutorials/rest/
 */

package com.example.payroll;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.ProtocolException;
import java.net.URL;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.logging.LogManager;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.MDC;
import okhttp3.* ;

import datadog.trace.api.DDTags;
import datadog.trace.api.Trace;
import io.opentracing.Scope;
import io.opentracing.Span;
import io.opentracing.SpanContext;
import io.opentracing.Tracer;
import io.opentracing.propagation.Format;
import io.opentracing.util.GlobalTracer;


@RestController
class EmployeeController {

	private static final Logger logger = LoggerFactory.getLogger(PayrollApplication.class);
	
	private final EmployeeRepository repository;

  EmployeeController(EmployeeRepository repository) {
    this.repository = repository;
  }


  // Aggregate root
  // tag::get-aggregate-root[]
  @GetMapping("/employees")
  List<Employee> all() {
    
	  logger.info("Getting all employees!!!");
	  
	  return repository.findAll();
  }
  // end::get-aggregate-root[]

  @PostMapping("/employees")
  Employee newEmployee(@RequestBody Employee newEmployee) {
    
	  logger.info("Adding new employee: " + newEmployee.getName());
	  
	  return repository.save(newEmployee);
  }

  @SuppressWarnings("deprecation")
  @PostMapping("/testmule")
  Employee testmule(@RequestBody Employee newEmployee) {

	  logger.info("Testing mulesoft integration with new employee: " + newEmployee.getName());
	  
	  Tracer tracer = GlobalTracer.get();
	  
	  Span span = tracer.buildSpan("testmule")
//				.asChildOf(extractedContext)
				.withTag(DDTags.SERVICE_NAME, "payroll")
				.withTag(DDTags.RESOURCE_NAME, "/testmule")
				.start();	
		
      try (Scope scope = tracer.activateSpan(span)) {

			
    	  long x = 1234567000L;
    	  long y = 23456789000L;
    	  Random r = new Random();
    	  long number = x+((long)(r.nextDouble()*(y-x)));
			try {
				  
				OkHttpClient client = new OkHttpClient().newBuilder().build();
				MediaType mediaType = MediaType.parse("application/json");


				okhttp3.RequestBody body = okhttp3.RequestBody.create(mediaType, "{\n    \"name\": \"Lloyd Williams\",\n    \"role\": \"Enterprise Solutions Engineer\"\n}\n");
				okhttp3.Request request = new okhttp3.Request.Builder()
				  .url("http://localhost:9501/mulesoft")
				  .method("POST", body)
				  //.addHeader("x-datadog-trace-id", String.valueOf(number))
				  .addHeader("content-type", "application/json")
				  .build();
				okhttp3.Response response = client.newCall(request).execute();
				logger.debug("** Response is: " + response);
				
				
			} catch (ProtocolException e) {
				e.printStackTrace();
				logger.error("com.example.payroll.EmployeeController", "Error Occurred", e, e, newEmployee, tracer, span, scope, r, e);
			} catch (IOException e) {
				logger.error("com.example.payroll.EmployeeController", "Error Occurred", e, e, newEmployee, tracer, span, scope, r, e);
				e.printStackTrace();
			}
	    } catch (Exception e) {
	        // Set error on span
	    	e.printStackTrace();
	    } finally {
	        // Close span in a finally block
	        span.finish();
	    }
      
      return repository.save(newEmployee);
	}  
	  
  
  @PostMapping("/mulesoft")
  Employee muleSoft(@RequestBody Employee newEmployee) {
	  
    logger.info("Mulesoft integration with new employee: " + newEmployee.getName());
	  
	try {
		//URL url = new URL("http://localhost:8081/helloworld");
		URL url = new URL("http://localhost:9501/mulesoft");
		HttpURLConnection con = (HttpURLConnection) url.openConnection();
		//con.setRequestMethod("GET");
		con.setRequestMethod("POST");
		Map<String, String> parameters = new HashMap<>();
		//parameters.put("param1", "val");
		con.setRequestProperty("Content-Type", "application/json");
		con.setConnectTimeout(5000);
		con.setDoOutput(true);
		DataOutputStream out = new DataOutputStream(con.getOutputStream());
		out.writeBytes(ParameterStringBuilder.getParamsString(parameters));
		out.flush();
		out.close();
		
		int status = con.getResponseCode();
		System.out.println("Status is: " + status);
		BufferedReader in = new BufferedReader(
				  new InputStreamReader(con.getInputStream()));
		String inputLine;
		StringBuffer content = new StringBuffer();
		while ((inputLine = in.readLine()) != null) {
		    content.append(inputLine);
		}
		in.close();
		con.disconnect();
		System.out.println("*** Disconnected *** ");

		
	} catch (ProtocolException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	  
	  return repository.save(newEmployee);
  }
  
  

  // Single item
  
  @GetMapping("/employees/{id}")
  Employee one(@PathVariable Long id) {
	
	logger.info("Getting employee with id: " + id);
	  
    return repository.findById(id)
      .orElseThrow(() -> new EmployeeNotFoundException(id));
  }

  @PutMapping("/employees/{id}")
  Employee replaceEmployee(@RequestBody Employee newEmployee, @PathVariable Long id) {
    
	 logger.info("Replacing employee with id: " + id);
	  
	  
    return repository.findById(id)
      .map(employee -> {
        employee.setName(newEmployee.getName());
        employee.setRole(newEmployee.getRole());
        return repository.save(employee);
      })
      .orElseGet(() -> {
        newEmployee.setId(id);
        return repository.save(newEmployee);
      });
  }

  @DeleteMapping("/employees/{id}")
  void deleteEmployee(@PathVariable Long id) {
	  
	  logger.info("Deleting employee with id: " + id);
	  
	  repository.deleteById(id);
  }
}