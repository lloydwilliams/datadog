package dogstatsd;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class DatabaseProperties {

	private String dburl ;
	private String user ;
	private String password ;
	private String updatesql ;
	private String selectsql ;
	private int delay ;

	public String getPropValues() throws IOException {
		
		String result = null ;
		InputStream inputStream = null;
		
		try {
			Properties prop = new Properties();
			String propFileName = "config.properties";
	
			inputStream = getClass().getClassLoader().getResourceAsStream(propFileName);
	
			if (inputStream != null) {
				prop.load(inputStream);
			} else {
				throw new FileNotFoundException("property file '" + propFileName + "' not found in the classpath");
			}
	
			//Date time = new Date(System.currentTimeMillis());
			
			dburl = prop.getProperty("dburl");
			user = prop.getProperty("user");
			password = prop.getProperty("password");
			updatesql = prop.getProperty("updatesql");
			selectsql = prop.getProperty("selectsql");
			delay = Integer.parseInt(prop.getProperty("delay"));
			
			result = "URL: " + dburl + "\nuser: " + user + "\npassword: " + password + "\nselectsql: " + selectsql + "\nupdatesql: " + updatesql + "\n";
	
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

	public String getDburl() {
		return dburl;
	}

	public void setDburl(String dburl) {
		this.dburl = dburl;
	}

	public String getUser() {
		return user;
	}

	public void setUser(String user) {
		this.user = user;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String getUpdatesql() {
		return updatesql;
	}

	public void setUpdatesql(String updatesql) {
		this.updatesql = updatesql;
	}

	public String getSelectsql() {
		return selectsql;
	}

	public void setSelectsql(String selectsql) {
		this.selectsql = selectsql;
	}

	public int getDelay() {
		return delay;
	}

	public void setDelay(int delay) {
		this.delay = delay;
	}
	
	
}
