package com.example.payroll;

class EmployeeNotFoundException extends RuntimeException {

	private static final long serialVersionUID = -1084603004891318733L;

	EmployeeNotFoundException(Long id) {
	    super("Could not find employee " + id);
	  }
	
}