# DevOps
For Cykl Życia i Narzędzi DevOps in WSEI

# Build outside of Docker and then run in container

`docker build -t demoweb .`

`docker run -itd demoweb .`

`docker run -itd -p 8080:8080 demoweb`

`docker run -itd --name demoweb -p 8080:8080 demoweb`

# Build and run inside Docker

`docker build -t demowebbuild -f DockerfileBuild .`

`docker run -itd -p 8080:8080 demowebbuild`

`docker run -itd -p 8080:8080 --name demowebbuild demowebbuild`



# Przydatne komendy
Budowanie obrazów
`docker-compose build`

Uruchomienie kontenerów
`docker-compose up`

Uruchomienie kontenerów w tle
`docker-compose up -d`

Zatrzymanie kontenerów, usunięcie sieci i wolumenów
`docker-compose down`

# Przydatne komendy K8s
`minikube start --driver=docker`

`minikube status`

`eval $(minikube -p minikube docker-env)`

`docker build -t your-spring-boot-image .`

`kubectl apply -f mysql-deployment.yaml`

`kubectl apply -f spring-boot-deployment.yaml`

`kubectl get pods`

`kubectl get services`

`minikube service spring-boot-service --url`

`kubectl port-forward service/spring-boot-service 8080:8080`