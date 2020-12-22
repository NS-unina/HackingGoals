Per la lanciare il container docker, usare il comando "docker compose up".
Per accedere al terminale del container docker usare "sudo docker exec -it IDCONTAINER bash".
Per compilare i file grakn andare nella cartella (del container) grakn-core-all-linux ed eseguire i comandi 
./grakn console --keyspace hacking_goal --file /hacking-goals/hackingGoal.gql
./grakn console --keyspace hacking_goal --file /hacking-goals/mydata.gql