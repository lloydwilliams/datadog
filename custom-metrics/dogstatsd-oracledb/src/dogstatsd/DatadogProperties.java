package dogstatsd;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class DatadogProperties {

	private String prefix ;
	private String host ;
	private int port ;
//	private int delay ;
	
	public String getPropValues() throws IOException {
		
		String result = null ;
		InputStream inputStream = null;
		
		try {
			Properties prop = new Properties();
			String propFileName = "datadog.properties";
	
			inputStream = getClass().getClassLoader().getResourceAsStream(propFileName);
	
			if (inputStream != null) {
				prop.load(inputStream);
			} else {
				throw new FileNotFoundException("property file '" + propFileName + "' not found in the classpath");
			}
	
			//Date time = new Date(System.currentTimeMillis());
			
			prefix = prop.getProperty("prefix");
			host = prop.getProperty("host");
			port = Integer.parseInt(prop.getProperty("port"));
//			delay = Integer.parseInt(prop.getProperty("delay"));
	
			result = "prefix: " + prefix + "\nhost: " + host + "\nport: " + port + "\n";
			
			System.out.println(result);
			
	
		} catch (Exception e) {
			System.out.println("Exception: " + e);
		} finally {
			if (inputStream != null) {
				inputStream.close();
			}
			
		}
		return result;
	}

	public String getPrefix() {
		return prefix;
	}

	public void setPrefix(String prefix) {
		this.prefix = prefix;
	}

	public String getHost() {
		return host;
	}

	public void setHost(String host) {
		this.host = host;
	}

	public int getPort() {
		return port;
	}

	public void setPort(int port) {
		this.port = port;
	}
	
}
