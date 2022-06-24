/*
 *  https://spring.io/guides/tutorials/rest/
 */

package com.example.payroll;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.MDC;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import datadog.trace.api.CorrelationIdentifier;

@RestController
class EmployeeController {

  static Logger logger = LoggerFactory.getLogger(EmployeeController.class);
	
  private final EmployeeRepository repository;

  EmployeeController(EmployeeRepository repository) {
    this.repository = repository;
  }


  // Aggregate root
  // tag::get-aggregate-root[]
  @GetMapping("/employees")
  List<Employee> all() {
    return repository.findAll();
  }
  // end::get-aggregate-root[]

  @PostMapping("/employees")
  Employee newEmployee(@RequestBody Employee newEmployee) {
	  
	// There must be spans started and active before this block.
  	try {
  	    MDC.put("dd.trace_id", CorrelationIdentifier.getTraceId());
  	    MDC.put("dd.span_id", CorrelationIdentifier.getSpanId());

  	    logger.info("Adding new employee with name: " + newEmployee.getName() + " and role: " + newEmployee.getRole());
  	    
  	} finally {
  	    MDC.remove("dd.trace_id");
  	    MDC.remove("dd.span_id");
  	}           	 
	  
    return repository.save(newEmployee);
  }
   
  // Single item  
  @GetMapping("/employees/{id}")
  Employee one(@PathVariable Long id) {
    
	  // There must be spans started and active before this block.
	  	try {
	  	    MDC.put("dd.trace_id", CorrelationIdentifier.getTraceId());
	  	    MDC.put("dd.span_id", CorrelationIdentifier.getSpanId());

	  	    logger.info("Trying to find employee with id: " + id );
	  	    
	  	} finally {
	  	    MDC.remove("dd.trace_id");
	  	    MDC.remove("dd.span_id");
	  	}    
	  
	  
    return repository.findById(id)
      .orElseThrow(() -> new EmployeeNotFoundException(id));
  }

  @PutMapping("/employees/{id}")
  Employee replaceEmployee(@RequestBody Employee newEmployee, @PathVariable Long id) {
    
	    // There must be spans started and active before this block.
	  	try {
	  	    MDC.put("dd.trace_id", CorrelationIdentifier.getTraceId());
	  	    MDC.put("dd.span_id", CorrelationIdentifier.getSpanId());

	  	    logger.info("Upating employee id: " + id + " with name: " + newEmployee.getName() + " and role: " + newEmployee.getRole());
	  	    
	  	} finally {
	  	    MDC.remove("dd.trace_id");
	  	    MDC.remove("dd.span_id");
	  	}     
	  
	  
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
	  
	  // There must be spans started and active before this block.
	  	try {
	  	    MDC.put("dd.trace_id", CorrelationIdentifier.getTraceId());
	  	    MDC.put("dd.span_id", CorrelationIdentifier.getSpanId());

	  	    logger.info("Deleting employee id: " + id );
	  	    
	  	} finally {
	  	    MDC.remove("dd.trace_id");
	  	    MDC.remove("dd.span_id");
	  	}     

    repository.deleteById(id);
  }
}