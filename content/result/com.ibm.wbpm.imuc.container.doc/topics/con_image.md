# Getting access to container images

The Cloud Native Computing Foundation (CNCF) platform type or “Other” is the only platform that
supports a local image registry in the script to set up the cluster. The Open Shift Container
Platform (OCP) and RedHat OpenShift Kubernetes Service (ROKS) platform types support only the IBM
Entitled Registry in the cluster setup script. For instructions, see Getting access to images from the public IBM Entitled
Registry.

```
./loadimages.sh -r $(oc registry info --public)/<namespace> -m baw
```

```
docker pull icr.io/cpopen/icp4a-operator:<version>
docker login <localserver>
docker tag icp4a-operator:<version> <localserver>/icp4a-operator:<your\_tag>
docker push <localserver>/icp4a-operator:<your\_tag>
```