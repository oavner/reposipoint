#!/usr/bin/env bash

if [ $# -eq 2 ]; then
    echo "Using $1 GitHub Personal Access Token to create repositories"
    echo "Using $2 GitHub owner to create repositories"

    brew install k3d kubectl helm # docker

    # docker run hello-world

    k3d cluster delete -a # delete all running k3d clusters

    k3d cluster create reposipoint -p "8081:80@loadbalancer"
    # the port-mapping construct 8081:80@loadbalancer means:
    # “map port 8081 from the host to port 80 on the container which matches the nodefilter loadbalancer“
    # the loadbalancer nodefilter matches only the serverlb that’s deployed in front of a cluster’s server nodes
    # all ports exposed on the serverlb will be proxied to the same ports on all server nodes in the cluster

    kubectl get nodes

    helm upgrade --install reposipoint ./reposipoint/deploy/backend --set config.githubPersonalAccessToken=$1 --set config.owner=$2  # it will only install since the cluster gets recreated

    kubectl wait --for=condition=available deployment/reposipoint-backend-deployment --timeout=60s

    echo "reposipoint is up and running, you can access it at http://localhost:8081"

    echo "use curl to create a new repository 'curl -X POST -H \"Content-Type: application/json\" -d '{\"repo_name\": \"example\", \"description\": \"Example repository\"}' http://localhost:8081/create'"

else
    echo "Usage: $0 <GitHub Personal Access Token> <GithHub owner>"
    exit 1
fi 




