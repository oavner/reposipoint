#!/usr/bin/env bash

if [ $# -ge 1 ]; then
    echo "Using $1 GitHub Personal Access Token to create repositories"

    brew install k3d kubectl helm # docker

    # docker run hello-world

    k3d cluster delete -a # delete all running k3d clusters

    k3d cluster create reposipoint -p "8081:80@loadbalancer"
    # the port-mapping construct 8081:80@loadbalancer means:
    # “map port 8081 from the host to port 80 on the container which matches the nodefilter loadbalancer“
    # the loadbalancer nodefilter matches only the serverlb that’s deployed in front of a cluster’s server nodes
    # all ports exposed on the serverlb will be proxied to the same ports on all server nodes in the cluster

    kubectl get nodes

    helm upgrade --install reposipoint ./reposipoint/deploy/backend --set config.githubPersonalAccessToken=$1 # it will only install since the cluster gets recreated

else
    echo "Usage: $0 <GitHub Personal Access Token>"
    exit 1
fi 




