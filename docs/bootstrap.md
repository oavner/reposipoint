### How To Bootsrap Reposipoint Over MacOS

this bootstrap script does not handle docker installation at your local environment, please make sure your docker daemon is up and running before using the bootstrap script.

1. clone this repository: `git clone https://github.com/oavner/reposipoint.git`
2. set execution permissions to the current user over the bootstrap script: `chmod u+x reposipoint/bootstrap/mac.sh`
3. run the bootstrap script like so: `./reposipoint/bootstrap/mac.sh <github personal access token>` (please verify that u cloned the repository successfully and if u already cloned it before please both pull the latest version from `master` branch and `cd` to the father dir of this repo since the bootstrap script uses relative pathes)

the script will:
1. use `brew` to install / update the following packages: `k3d, kubectl, helm`
2. delete any existing `k3d` clusters if they exist (THIS SCRIPT DELETES ALL EXISTING K3D CLUSTERS RUNNING OVER YOUR MAC)
2. set up a new single node k8s cluster (a container serving as control plane) named `reposipoint`
3. use `kubectl` to get nodes info for debug purposes
4. install a helm chart of the reposiopont backend

if everything went properly you should see something similer to the following output (versions might differ):
```
NAME                       STATUS   ROLES                  AGE   VERSION
k3d-reposipoint-server-0   Ready    control-plane,master   9s    v1.27.4+k3s1
```