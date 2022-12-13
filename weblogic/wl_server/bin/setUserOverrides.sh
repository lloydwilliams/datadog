## setUserOverrides.sh 
## this is called from setDomainEnv.sh and executes after setStartupEnv.sh
echo "**** The server name is: ${SERVER_NAME} ********"

if [ "${SERVER_NAME}" = "AdminServer" ] ; then
   echo "**** Setting Datadog settings for: ${SERVER_NAME} ********"
   USER_MEM_ARGS="-Xms256m -Xmx512m -XX:+UnlockCommercialFeatures -XX:+FlightRecorder -XX:FlightRecorderOptions=stackdepth=256"
   JAVA_VM="-javaagent:/Users/lloyd.williams/u01/datadog/dd-java-agent.jar ${JAVA_VM}"
   # Change the logging format in the Admin Console, under Server, Logging, General Advanced = MMM d, y, h:mm:ss,SSS a z
   DATADOG_OPTIONS="-Ddd.trace.config=/Users/lloyd.williams/u01/weblogic/dd-config.properties -Ddd.tags=wls:adminserver,domain:domain1 -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.local.only=false -Dcom.sun.management.jmxremote.port=9090 -Dcom.sun.management.jmxremote.rmi.port=9090 -Djavax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder -Ddd.profiling.enabled=true"
   JAVA_OPTIONS="${JAVA_OPTIONS} ${DATADOG_OPTIONS}"
fi

if [ "${SERVER_NAME}" = "ManagedServer_1" ] ; then  
   echo "**** Setting Datadog settings for: ${SERVER_NAME} ********"
   USER_MEM_ARGS="-Xms512m -Xmx1024m -XX:+UnlockCommercialFeatures -XX:+FlightRecorder -XX:FlightRecorderOptions=stackdepth=256"
   JAVA_VM="-javaagent:/Users/lloyd.williams/u01/datadog/dd-java-agent.jar ${JAVA_VM}"
   DATADOG_OPTIONS="-Ddd.trace.config=/Users/lloyd.williams/u01/weblogic/dd-config.properties -Ddd.tags=wls:managed_server1,domain:domain1 -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.local.only=false -Dcom.sun.management.jmxremote.port=9091 -Dcom.sun.management.jmxremote.rmi.port=9091 -Djavax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder -Ddd.profiling.enabled=true"
   JAVA_OPTIONS="${JAVA_OPTIONS} ${DATADOG_OPTIONS}"
fi

if [ "${SERVER_NAME}" = "ManagedServer_2" ] ; then
   echo "**** Setting Datadog settings for: ${SERVER_NAME} ********"
   USER_MEM_ARGS="-Xms512m -Xmx768m -XX:+UnlockCommercialFeatures -XX:+FlightRecorder -XX:FlightRecorderOptions=stackdepth=256"
   JAVA_VM="-javaagent:/Users/lloyd.williams/u01/datadog/dd-java-agent.jar ${JAVA_VM}"
   DATADOG_OPTIONS="-Ddd.trace.config=/Users/lloyd.williams/u01/weblogic/dd-config.properties -Ddd.tags=wls:managed_server2,domain:domain1 -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.local.only=false -Dcom.sun.management.jmxremote.port=9092 -Dcom.sun.management.jmxremote.rmi.port=9092 -Djavax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder -Ddd.profiling.enabled=true"
   JAVA_OPTIONS="${JAVA_OPTIONS} ${DATADOG_OPTIONS}"
fi
