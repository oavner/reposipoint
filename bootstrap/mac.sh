#!/usr/bin/env bash

brew install k3d kubectl helm 

# TODO  start dockerd

k3d cluster delete -a

k3d cluster create reposipoint -p "8081:80@loadbalancer"
# the port-mapping construct 8081:80@loadbalancer means:
# “map port 8081 from the host to port 80 on the container which matches the nodefilter loadbalancer“
# the loadbalancer nodefilter matches only the serverlb that’s deployed in front of a cluster’s server nodes
# all ports exposed on the serverlb will be proxied to the same ports on all server nodes in the cluster

kubectl get nodes

helm upgrade --install reposipoint ./reposipoint/deploy/backend # it will only install since the cluster gets recreated

# curl localhost:8081




