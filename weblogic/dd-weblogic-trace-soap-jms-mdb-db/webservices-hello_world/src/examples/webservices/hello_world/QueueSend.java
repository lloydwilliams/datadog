package examples.webservices.hello_world;

import java.util.Hashtable;
import javax.jms.*;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;

public class QueueSend
{
 // Defines the JNDI context factory.
 public final static String JNDI_FACTORY="weblogic.jndi.WLInitialContextFactory";

 // Defines the JMS context factory.
 public final static String JMS_FACTORY="jms/TestConnectionFactory";

 // Defines the queue.
 public final static String QUEUE="jms/TestJMSQueue";

 private QueueConnectionFactory qconFactory;
 private QueueConnection qcon;
 private QueueSession qsession;
 private QueueSender qsender;
 private Queue queue;
 private TextMessage msg;

	 /**
	  * Creates all the necessary objects for sending
	  * messages to a JMS queue.
	  *
	  * @param ctx JNDI initial context
	  * @param queueName name of queue
	  * @exception NamingException if operation cannot be performed
	  * @exception JMSException if JMS fails to initialize due to internal error
	  */
	 public void init(Context ctx, String queueName)
	    throws NamingException, JMSException
	 {
	    
		System.out.println("Attempting to connect to WebLogic Queue!...");
		 
		qconFactory = (QueueConnectionFactory) ctx.lookup(JMS_FACTORY);
	    qcon = qconFactory.createQueueConnection();
	    qsession = qcon.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
	    queue = (Queue) ctx.lookup(queueName);
	    qsender = qsession.createSender(queue);
	    msg = qsession.createTextMessage();
	    qcon.start();
	 }
	
	 /**
	  * Sends a message to a JMS queue.
	  *
	  * @param message  message to be sent
	  * @exception JMSException if JMS fails to send message due to internal error
	  * @throws NamingException 
	  */
	 public void send(String message) throws JMSException, NamingException {
		 
		String weblogicURL = "t3://127.0.0.1:7101" ;
		InitialContext ic = getInitialContext(weblogicURL);		 
		init(ic, QUEUE);
		 
		msg.setText(message);
	    qsender.send(msg);
	 }
	
	 /**
	  * Closes JMS objects.
	  * @exception JMSException if JMS fails to close objects due to internal error
	  */
	 public void close() throws JMSException {
	    qsender.close();
	    qsession.close();
	    qcon.close();
	 }
	
	 @SuppressWarnings({ "unchecked", "rawtypes" })
	public InitialContext getInitialContext(String url)
	    throws NamingException
	 {
	    Hashtable env = new Hashtable();
	    env.put(Context.INITIAL_CONTEXT_FACTORY, JNDI_FACTORY);
	    env.put(Context.PROVIDER_URL, url);
	    return new InitialContext(env);
	 }
	


}