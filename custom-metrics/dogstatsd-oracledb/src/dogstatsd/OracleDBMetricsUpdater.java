/**
 * sending custom metrics using DogStatsd
 * https://docs.datadoghq.com/metrics/dogstatsd_metrics_submission/
 * 
 * This code is an example to be used as a guide. It is not supported by Datadog.
 */

package dogstatsd;

import java.io.IOException;
import java.sql.*;


public class OracleDBMetricsUpdater {
	
	public static void main(String[] args) {
	
		OracleDBMetricsUpdater u = new OracleDBMetricsUpdater();
		DatabaseProperties props = new DatabaseProperties() ;	
		
	   try {
		 props.getPropValues();
		 u.updateMetrics(props.getDburl(), props.getUser(), props.getPassword(), props.getUpdatesql(), props.getDelay());
	   } catch (IOException e) {		
		 e.printStackTrace();
	   }
		
	}
	
	
	public void updateMetrics(String dburl, String user, String password, String sql, int delay) {
				
		Connection con = null;

        try {
 
            con = DriverManager.getConnection(dburl, user, password);
            if (con != null) {
                System.out.println("Connected with service connection!");
                
                
                while (true) {
                
	                for (int i = 1; i <= 5; i++) {
	                
		                String metricID = "Metric" + i ;               
		                Float value1 = nextFloatBetween(10f,50f);
		                Float value2 = nextFloatBetween(50f,99f);
		                
		                try (PreparedStatement stmt = con.prepareStatement(sql)) {
		        		    stmt.setFloat(1, value1);
		        		    stmt.setFloat(2, value2);
		        		    stmt.setString(3, metricID);
		        		    int rows = stmt.executeUpdate();
		        		    
		        		    if (rows > 0) {
		        		    	System.out.println("Metric: " + metricID + " updated with values: " + value1 + " and " + value2 );
		        		    }   
		        		    
		        		} catch (Exception ex) {
		        			ex.printStackTrace();
		        			
		        		} finally {
		        			//con.close();
		        		}
		                
	                } // end for
	            System.out.println("-----------\n");
                Thread.sleep(delay);
                
                } // end while
                
            } // if
            
        
	    } catch (SQLException ex) {
	        ex.printStackTrace();
	    } catch (InterruptedException e) {
			e.printStackTrace();
		} finally {
	        try {
	            if (con != null && !con.isClosed()) {
	                con.close();
	            }
	        } catch (SQLException ex) {
	            ex.printStackTrace();
	        }
	    }
        
	} // main
	
	public float nextFloatBetween(float min, float max) {
		
		double r = (Math.random() * (max - min)) + min;
	    return (float) (Math.round(r * 100.0) / 100.0);
	}
	
	
}
