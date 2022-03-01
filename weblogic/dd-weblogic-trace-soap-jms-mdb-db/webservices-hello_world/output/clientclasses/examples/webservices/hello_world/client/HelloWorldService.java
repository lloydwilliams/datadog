
package examples.webservices.hello_world.client;

import java.net.MalformedURLException;
import java.net.URL;
import javax.xml.namespace.QName;
import javax.xml.ws.Service;
import javax.xml.ws.WebEndpoint;
import javax.xml.ws.WebServiceClient;
import javax.xml.ws.WebServiceException;
import javax.xml.ws.WebServiceFeature;


/**
 * This class was generated by the JAX-WS RI.
 * JAX-WS RI 2.3.0-b170214.1743
 * Generated source version: 2.2
 * 
 */
@WebServiceClient(name = "HelloWorldService", targetNamespace = "http://hello_world.webservices.examples/", wsdlLocation = "http://localhost:7101/HelloWorldImpl/HelloWorldService?WSDL")
public class HelloWorldService
    extends Service
{

    private final static URL HELLOWORLDSERVICE_WSDL_LOCATION;
    private final static WebServiceException HELLOWORLDSERVICE_EXCEPTION;
    private final static QName HELLOWORLDSERVICE_QNAME = new QName("http://hello_world.webservices.examples/", "HelloWorldService");

    static {
        WebServiceException e = null;
        URL url = null;
        try {
            url = new URL(examples.webservices.hello_world.client.HelloWorldService.class.getResource("."), "http://localhost:7101/HelloWorldImpl/HelloWorldService?WSDL");
        } catch (MalformedURLException murl) {
            e = new WebServiceException(murl);
        }
        HELLOWORLDSERVICE_WSDL_LOCATION = url;
        HELLOWORLDSERVICE_EXCEPTION = e;
    }

    public HelloWorldService() {
        super(__getWsdlLocation(), HELLOWORLDSERVICE_QNAME);
    }

    public HelloWorldService(WebServiceFeature... features) {
        super(__getWsdlLocation(), HELLOWORLDSERVICE_QNAME, features);
    }

    public HelloWorldService(URL wsdlLocation) {
        super(wsdlLocation, HELLOWORLDSERVICE_QNAME);
    }

    public HelloWorldService(URL wsdlLocation, WebServiceFeature... features) {
        super(wsdlLocation, HELLOWORLDSERVICE_QNAME, features);
    }

    public HelloWorldService(URL wsdlLocation, QName serviceName) {
        super(wsdlLocation, serviceName);
    }

    public HelloWorldService(URL wsdlLocation, QName serviceName, WebServiceFeature... features) {
        super(wsdlLocation, serviceName, features);
    }

    /**
     * 
     * @return
     *     returns HelloWorldPortType
     */
    @WebEndpoint(name = "HelloWorldPortTypePort")
    public HelloWorldPortType getHelloWorldPortTypePort() {
        return super.getPort(new QName("http://hello_world.webservices.examples/", "HelloWorldPortTypePort"), HelloWorldPortType.class);
    }

    /**
     * 
     * @param features
     *     A list of {@link javax.xml.ws.WebServiceFeature} to configure on the proxy.  Supported features not in the <code>features</code> parameter will have their default values.
     * @return
     *     returns HelloWorldPortType
     */
    @WebEndpoint(name = "HelloWorldPortTypePort")
    public HelloWorldPortType getHelloWorldPortTypePort(WebServiceFeature... features) {
        return super.getPort(new QName("http://hello_world.webservices.examples/", "HelloWorldPortTypePort"), HelloWorldPortType.class, features);
    }

    private static URL __getWsdlLocation() {
        if (HELLOWORLDSERVICE_EXCEPTION!= null) {
            throw HELLOWORLDSERVICE_EXCEPTION;
        }
        return HELLOWORLDSERVICE_WSDL_LOCATION;
    }

}
