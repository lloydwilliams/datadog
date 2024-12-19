package dogstatsd;

//sending custom metrics using Dogstatsd
//https://docs.datadoghq.com/metrics/dogstatsd_metrics_submission/

import com.timgroup.statsd.NonBlockingStatsDClientBuilder;
import com.timgroup.statsd.StatsDClient;
import java.util.Random;

	public class DogStatsdClient {

	    public static void main(String[] args) throws Exception {
	    	
	        StatsDClient Statsd = new NonBlockingStatsDClientBuilder()
	            .prefix("statsd")
	            .hostname("localhost")
	            .port(8125)
	            .build();
	        
	       
	        for (int i = 1; i <= 1000; i++) {
	        	
		    	Random random = new Random();
	        	int r = random.nextInt(100);
		        System.out.println(i);

	        	
	            Statsd.incrementCounter("example_metric.increment", new String[]{"env:iot"});
	            Statsd.decrementCounter("example_metric.decrement", new String[]{"env:iot"});
	            Statsd.recordGaugeValue("example_metric.gauge", r, new String[]{"env:iot"});
	            
	            Statsd.count("example_metric.count", 3, new String[]{"env:iot"});
	            System.out.println("Sent some metrics called: example_metric [" + r + "] for env:iot");
	            
	            Thread.sleep(1000);
	            //
	            //https://docs.datadoghq.com/developers/faq/data-collection-resolution-retention/
	            //Infrastructure	Custom metrics (StatsD)	Datadog Agent (built-in statsD collector)	15 seconds	1 second	15 months
	            //statsd.example_metric.gauge
	        }
	    }
}
