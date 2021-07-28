# Kubernetes

July 15, 2021

## docker

Start a local container registry
```
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

build image
```
cd ./example-cars/
docker-compose build
```

tag image
```
docker tag example-cars:latest localhost:5000/example-cars
```

push image to local registry
```
docker push localhost:5000/example-cars
```

## kubectl

```powershell
kubectl apply -f .\app.yaml
```

## az (Azure)

```powershell
az login
az aks list
az acr login --name <registry name>
```

Create network
```
az network public-ip create --resource-group aksdemo --name example-cars-ip
```

## Reference

[https://github.com/philspokas/deploying-kubernetes/blob/main/create-cluster.ps1](https://github.com/philspokas/deploying-kubernetes/blob/main/create-cluster.ps1)
