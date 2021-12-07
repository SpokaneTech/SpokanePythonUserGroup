---
title: Kubernetes
description: Learn how to use Kubernetes to run a FastAPI application!
---

# Kubernetes

_July 15, 2021_

## Links
[Code Samples](https://github.com/python-spokane/kubernetes-and-python)

[Meetup event](https://www.meetup.com/Spokane-DevOps-Meetup/events/278709256/)

## Recording

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/todSDrCjMl0?start=3640" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

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
