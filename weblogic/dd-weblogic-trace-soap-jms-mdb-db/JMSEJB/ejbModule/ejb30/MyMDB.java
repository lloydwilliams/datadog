package ejb30;

import javax.ejb.MessageDriven;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageListener;
import javax.jms.TextMessage;
import javax.ejb.ActivationConfigProperty;

import datadog.trace.api.DDTags;
import datadog.trace.api.Trace;
import io.opentracing.Scope;
import io.opentracing.Span;
import io.opentracing.SpanContext;
import io.opentracing.Tracer;
import io.opentracing.propagation.Format;
import io.opentracing.util.GlobalTracer;
//import io.opentracing.log.Fields;
//import io.opentracing.tag.Tags;

//import org.slf4j.MDC;
//import datadog.trace.api.CorrelationIdentifier;

import java.sql.*;

// https://docs.datadoghq.com/tracing/setup_overview/open_standards/java/

@MessageDriven(
activationConfig = {
	@ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Queue") ,
	@ActivationConfigProperty(propertyName="connectionFactoryJndiName",propertyValue="jms/TestConnectionFactory"),
	@ActivationConfigProperty(propertyName="destinationJndiName", propertyValue="jms/TestJMSQueue")
	}
	,mappedName="jms/TestJMSQueue"
)
 
public class MyMDB implements MessageListener {
	public void onMessage(Message message) {
		
		String traceid = null ;
		String parentid = null ;
		String sampling = null ;
		String text = null ;
		
		try {
	        TextMessage textMessage = (TextMessage) message;
	        traceid = textMessage.getStringProperty("x__dash__datadog__dash__trace__dash__id");
	        parentid = textMessage.getStringProperty("x__dash__datadog__dash__parent__dash__id");
	        sampling = textMessage.getStringProperty("x__dash__datadog__dash__sampling__dash__priority");
	        text = textMessage.getText();
			System.out.println("MyMDB Received: " + text);
	        System.out.println("Trace ID is:" + traceid);
	        System.out.println("Parent ID is:" + parentid);
	        System.out.println("Sampling Priority is:" + sampling);
		} catch (JMSException e){
			e.printStackTrace();
		}
        		
		Tracer tracer = GlobalTracer.get();
		
		MyExtractAdapter myExtract = new MyExtractAdapter();
		myExtract.put("x-datadog-trace-id", traceid);
		myExtract.put("x-datadog-parent-id", parentid);
		myExtract.put("x-datadog-sampling-priority", sampling);
		
		
		final SpanContext extractedContext = 
		GlobalTracer.get().extract(Format.Builtin.TEXT_MAP_EXTRACT,myExtract);
		
		Span span = tracer.buildSpan("MDB")
				.asChildOf(extractedContext)
				.withTag(DDTags.SERVICE_NAME, "mdb")
				.withTag(DDTags.RESOURCE_NAME, "MyMDB")
				.start();	
		
        try (Scope scope = tracer.activateSpan(span)) {
				

			span.setTag("queue.message", text);
			span.setTag("dd.traceid", traceid);
			span.setTag("dd.parentid", parentid);
			span.setTag("dd.sampling", sampling);	
			
			long id = 0 ; 
			String greeting = text ;
			
			String url = "jdbc:oracle:thin:@localhost:1521/ORCLPDB1.localdomain";
			Connection conn = getDatabaseConnection(url,"lloyd","lloyd");
			
			if (conn != null) {
				id = getGreetingID (conn) ;
				if (id != 0) { 
					insertOracle(conn, id, greeting);
				}
			}

	    } catch (Exception e) {
	        // Set error on span
	    	e.printStackTrace();
	    } finally {
	        // Close span in a finally block
	        span.finish();
	    }
	}
	
	
	@Trace(operationName = "database.connection", resourceName = "Oracle12c")
	public Connection getDatabaseConnection (String url, String username, String password)  {

		
        Connection conn = null ;
		try {
			conn = DriverManager.getConnection(url,username,password);
		} catch (SQLException e) {
			
			e.printStackTrace();
		}
		
		return conn ;
		   
	}
	
	
	@Trace(operationName = "database.select", resourceName = "Oracle12c")
	public long getGreetingID (Connection conn)  {
	
		long myId = 0 ;
		
		String sqlIdentifier = "select LLOYD.GREETING_SEQ.NEXTVAL from dual";
		PreparedStatement pst;
		try {
			pst = conn.prepareStatement(sqlIdentifier);
			synchronized( this ) {
				   ResultSet rs = pst.executeQuery();
				   if(rs.next())
				     myId = rs.getLong(1);
				}
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		return myId ;
		   
	}
	
	@Trace(operationName = "database.persist", resourceName = "Oracle12c")
	public void insertOracle (Connection conn, long id, String greeting)  {
        try {
            try {
            	synchronized( this ) {
	               // create our java preparedstatement using a sql insert query
	              PreparedStatement ps = conn.prepareStatement("INSERT INTO GREETINGS (ID, GREETING) VALUES (?, ?)");	              
	              ps.setLong(1, id);
	              ps.setString(2, greeting);            
	              // call executeUpdate to execute our sql update statement
	              ps.executeUpdate();
	              ps.close();
            	}
            }
            catch (SQLException se)
            {
              // log the exception
              System.out.println("SQLException");
              System.out.println(se.toString());
              throw se;
            }
            conn.close();
        } catch (Exception e) {
        	System.out.println("Got an exception!");
        	System.out.println(e.getMessage());
        	System.out.println(e.toString());
        }
        
    }
	
	
	
	
}
	
