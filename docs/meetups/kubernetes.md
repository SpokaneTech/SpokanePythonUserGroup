---
title: Kubernetes
description: Learn how to use Kubernetes to run a FastAPI application!
---

# Kubernetes

_July 15, 2021_ | [:fontawesome-brands-meetup: Meetup](https://www.meetup.com/Spokane-DevOps-Meetup/events/278709256/){target=_blank} | [:fontawesome-brands-github: Code Samples](https://github.com/python-spokane/kubernetes-and-python){target=_blank}

As a guest co-host for Spokane's DevOps Meetup, I talked briefly about how to run a FastAPI application using Kubernetes.

<img src="/img/deploying-to-kubernetes.jpeg" width="600" height="337.5">

## Recording

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/todSDrCjMl0?start=3640" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Notes

### docker

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

### kubectl

```powershell
kubectl apply -f .\app.yaml
```

### az (Azure)

```powershell
az login
az aks list
az acr login --name <registry name>
```

Create network
```
az network public-ip create --resource-group aksdemo --name example-cars-ip
```

### Reference

[https://github.com/philspokas/deploying-kubernetes/blob/main/create-cluster.ps1](https://github.com/philspokas/deploying-kubernetes/blob/main/create-cluster.ps1){target=_blank}
