package examples.webservices.hello_world;

import javax.jms.JMSException;
//Import the @WebService annotation
import javax.jws.WebService;

@WebService(name="HelloWorldPortType", serviceName="HelloWorldService")
/**
* This JWS file forms the basis of simple Java-class implemented WebLogic
* Web Service with a single operation: sayHelloWorld
*/

public class HelloWorldImpl {
    // By default, all public methods are exposed as Web Services operation
	public String sayHelloWorld(String message) {
	
	   String helloMessage = "Hello " + message + "!";
	   try {
	  
		   sendMessage(helloMessage);
		   System.out.println("sayHelloWorld:" + helloMessage);
		   
	   } catch (Exception ex) { 
		   ex.printStackTrace(); 
	   }

	   return "Here is the message: '" + helloMessage + "'";
	}

	private void sendMessage(String message) throws JMSException {
		 
		QueueSend qs = new QueueSend();  
	    
		try {
			 qs.send(message);
			 qs.close();
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
	 }
	 
}