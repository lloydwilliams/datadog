/**
 * sending custom metrics using DogStatsd
 * https://docs.datadoghq.com/metrics/dogstatsd_metrics_submission/
 * 
 * This code is an example to be used as a guide. It is not supported by Datadog and is meant to be customized to your own needs.
 */

package dogstatsd;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

import com.timgroup.statsd.NonBlockingStatsDClientBuilder;
import com.timgroup.statsd.StatsDClient;

import java.io.IOException;
import java.sql.*; 

public class CustomMetricsToDatadog {
	

	public static void main(String[] args) {
		
		CustomMetricsToDatadog c = new CustomMetricsToDatadog();
		DatabaseProperties db = new DatabaseProperties() ;
		DatadogProperties dd = new DatadogProperties();
		
		try {
		  db.getPropValues();
		  dd.getPropValues();
			 
		  //for (int i = 0; i < 1000; i++) { 
		  while (true) {	  
			  c.retrieveFromDB(db.getDburl(), db.getUser(), db.getPassword(), db.getSelectsql(), db.getDelay(), 
					  dd.getPrefix(), dd.getHost(), dd.getPort()); 
		  }
		
		} catch (InterruptedException | IOException ex) {
			System.out.println("Program Interrupted!");
		}
		 
		
	}
	
	public void retrieveFromDB(String dburl, String user, String password, String selectsql, int delay, String prefix, String host, int port) 
			 throws InterruptedException {
		
		System.out.println("Attempting connection to Datadog agent on host: " + host + " with port: " + port + " to send metrics with prefix: " + prefix);
		
        StatsDClient Statsd = new NonBlockingStatsDClientBuilder()
	            .prefix(prefix)
	            .hostname(host)
	            .port(port)
	            .build();
		
		
		Connection conn1 = null;

        try {
 
            conn1 = DriverManager.getConnection(dburl, user, password);
            if (conn1 != null) {
                System.out.println("Connected with service connection!");
                Statement sqlStatement = conn1.createStatement();
            
	            ResultSet rs = sqlStatement.executeQuery(selectsql);
	            while (rs.next()) {
	           	
	            	String metricid = rs.getString("METRIC_ID") ;
	            	Float value1 = rs.getFloat("VALUE1");
	            	Float value2 = rs.getFloat("VALUE2");
	            	String attr1 = rs.getString("ATTR1") ;
	            	String attr2 = rs.getString("ATTR2") ;
	            	String attr3 = rs.getString("ATTR3") ;
	            	
	            	String tag1 = "server:" + attr1 ; 
	            	String tag2 = "category:" + attr2 ; 
	            	String tag3 = "cluster:" + attr3 ; 
	            	String tags = tag1 + "," + tag2 + "," + tag3 ;
	            	
	            	Statsd.recordGaugeValue("lloyd_metric.one", value1, new String[]{tags});
		            Statsd.recordGaugeValue("lloyd_metric.two", value2, new String[]{tags});
		            Statsd.count("lloyd_metric.count", 2, new String[]{tags});
	            		                    	
	          	    System.out.println("METRIC_ID: " + metricid + " VALUE1: " + value1 + " VALUE2: " + value2 + " Tags: " + tags );
	   	            //METRIC TYPES
			        //https://docs.datadoghq.com/metrics/types/?tab=gauge
	          	    		            
	            }
	            Thread.sleep(delay);
	            
	            rs.close();
	            conn1.close();
            }
            
            

        } catch (SQLException ex) {
            ex.printStackTrace();
        } catch (InterruptedException ex) {
        	throw ex ;
		} finally {
            try {
                if (conn1 != null && !conn1.isClosed()) {
                    conn1.close();
                }
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
        }
		
	}

}
