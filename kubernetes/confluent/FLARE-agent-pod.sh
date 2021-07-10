echo "Sending Flare for <AGENT_POD>: " $1 "to support ticket: " $2
echo "\n"
echo "Usage Example: ./F-agent-pod.sh datadog-agent-7l8bm 123456"
echo "\n"
# kubectl exec datadog-agent-nkhp8 -it agent flare <TICKET_NUMBER>
kubectl exec -it $1 -- agent flare $2