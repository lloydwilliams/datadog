This project creates a custom docker image that adds the DD agent to Tomcat and registers it in docker hub.

Docker Hub: lloydwilliams/tomcatdd 

---
```
docker push lloydwilliams/tomcatdd
% ./docker-push.sh 
Using default tag: latest
The push refers to repository [docker.io/lloydwilliams/tomcatdd]
```

---

**How do I \**SSH into\** a running \**container\****

1. Use **docker** ps **to** get the name of the existing **container**.
2. Use the command **docker** exec -it <**container** name> /bin/bash **to** get a bash shell **in the container**.
3. Generically, use **docker** exec -it <**container** name> <command> **to** execute whatever command you specify **in the container**.

