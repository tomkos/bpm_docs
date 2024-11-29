# Setting up a private registry

## About this task

Make sure that your image registry meets the following requirements:

- Ensure that your image registry is equipped to handle Docker
Manifest V2, Schema 2.
- Verify that your image registry can manage and store multi-architecture images.
Note: Do not use the OpenShift image registry as your private registry. The OpenShift registry does
not support multi-architecture images.
- Confirm that your image registry is reachable from both the host and the nodes within your
OpenShift Container
Platform cluster
nodes.
- Ensure that the image registry is configured with a valid username and password, granting the
necessary write permissions for a user from the host to interact with the target registry.
- Verify that the image registry is equipped with the appropriate username and password, enabling
a user on OpenShift Container
Platform
cluster nodes to read from the target registry.
- Validate that the image registry allows the use of path separators in image names.

To pull all images, you need at least 80 GB of disk space. The actual size depends on the
registry type being used because some registries require more storage than other types of registry.
All the images in the groups are pulled irrespective of architecture.

When the images are mirrored to your private registry, the namespaces where images are mirrored
must exist or the image push must create them automatically. If your registry does not allow
automatic creation of namespaces, you must create them manually. If you need to create the
namespaces manually, create the following namespaces at the root of your registry.

## Procedure

1. Create a cp namespace to store the images from the IBM Entitled Registry
cp.icr.io/cp.

The cp namespace needs an entitlement key and credentials to pull the images.
The namespace must have a user who can write and create repositories, and read all repositories.
2. Create a ibmcom namespace to store all images from all IBM images that do not
require credentials to pull.
3. Create a cpopen namespace to store all images from the
icr.io/cpopen repository.

IBM hosts publicly available images in the cpopen namespace that do not require
credentials to pull.
4. Create a opencloudio namespace to store the images from
quay.io/opencloudio.

The opencloudio namespace is for select IBM open source component images that
are available on quay.io. The IBM Cloud® Platform Common Services
images are hosted on opencloudio.

## What to do next

- Ensure that each namespace is configured to support the automatic creation of repositories.
- Verify that the namespace is associated with user credentials on the host that possess the
necessary permissions to both write to and create repositories within that namespace.
- Confirm that the namespace is configured with user credentials on the OpenShift Container
Platform cluster, specifically
granting read permissions for all repositories within that namespace.