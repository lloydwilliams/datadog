package dogstatsd;


/**
 * sending custom metrics using Dogstatsd
 * https://docs.datadoghq.com/metrics/dogstatsd_metrics_submission/
 * 
 * This code is an example to be used as a guide. It is not supported by Datadog.
 */


import com.timgroup.statsd.NonBlockingStatsDClientBuilder;
import com.timgroup.statsd.StatsDClient;

	public class DogStatsdClient {

	    public static void main(String[] args) throws Exception {

	        StatsDClient Statsd = new NonBlockingStatsDClientBuilder()
	            .prefix("statsd")
	            .hostname("localhost")
	            .port(8125)
	            .build();
	        
	        for (int i = 0; i < 10000; i++) {

		        System.out.println(i);

	        	
	            Statsd.incrementCounter("example_metric.increment", new String[]{"environment:dev"});
	            Statsd.decrementCounter("example_metric.decrement", new String[]{"environment:dev"});
	            Statsd.recordGaugeValue("example_metric.gauge", i, new String[]{"environment:dev"});
	            
	            Statsd.count("example_metric.count", 3, new String[]{"environment:dev"});
	            Thread.sleep(100);
	            //
	            //https://docs.datadoghq.com/developers/faq/data-collection-resolution-retention/
	            //Infrastructure	Custom metrics (StatsD)	Datadog Agent (built-in statsD collector)	15 seconds	1 second	15 months
	            //statsd.example_metric.gauge
	        }
	    }
}
