echo "Running Agent JMX Check for <AGENT_POD>: " $1
echo "\n"
echo "Usage Example: ./E-agent-JMX-everything.sh datadog-agent-7l8bm"
echo "\n"
echo "Make sure you choose an instance of an agent that is running in a node that also has a jmx service running.\n"

kubectl exec -it $1 -- agent jmx list everything