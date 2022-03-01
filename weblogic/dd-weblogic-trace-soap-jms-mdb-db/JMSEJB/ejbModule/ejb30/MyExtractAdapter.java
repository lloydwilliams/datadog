package ejb30;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
//import java.util.Map.Entry;

import io.opentracing.propagation.TextMap;

public class MyExtractAdapter implements TextMap {
    
    private Map<String,String> map = new HashMap<String,String>();
  
	public MyExtractAdapter() {

    }

    @Override
    public void put(final String key, final String value) {
    	System.out.println("### " + key + ":" + value);
        map.put(key, value);

    }


	@Override
	public Iterator<Map.Entry<String, String>> iterator() {
		
		Iterator<Map.Entry<String, String>> itr = map.entrySet().iterator();
		
		return itr;
	}
}