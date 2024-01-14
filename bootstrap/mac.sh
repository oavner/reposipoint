#!/usr/bin/env bash

brew install k3d kubectl 

# TODO  start dockerd

k3d cluster delete -a

k3d cluster create reposipoint

kubectl get nodes




