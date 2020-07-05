## Playing with Kubernetes and Docker

First of all you need to understand some architecture of Kubernetes.

The kubernates guide that I'm following can be found in https://kubernetes.io/docs/setup/scratch/#downloading-and-extracting-kubernetes-binaries

Once we have a VM running, we need to download the kubernates binaries from https://github.com/kubernetes/kubernetes/releases/tag/v1.11.8


## Playing with Docker

(!) If in your company you have a server where you don't have root access you can play with https://docs.docker.com/engine/security/rootless/ 

## Adding Kubernetes to power to your docker.

### Your friend kubeadm
kubeadm it's a tool that help you initializate a cluster. If you automatizate the initialization as some of my collegues using salt, you won't need to use it. But it's interesting to first play with and check the files this tools creates. After this you can play with whatever tool you know to automate a cluster installation.

kubeadm init
