docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ibmwas

docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' datadog-agent