# Option 2: Mirroring images to a private registry

## Before you begin

Verify that you completed the prerequisites, prepared a host, set the environment variables, and
created registry namespaces if the registry does not allow automatic creation of top-level
namespaces.

## About this task

If your cluster is not connected to the internet, you can install Business Automation Workflow in your cluster by
using a file system. The portable storage and compute scenarios are enabled with a file system. The
custom resource file must use the default settings for the sc\_image\_repository
parameter in an air gap environment. The running pods show the public image addresses even though
the private registry is being used.

Choose the type of host that you want to set up. Your choice determines how you mirror the images
to the private registry. A portable compute device can be used with or without the use of a portable
storage device.

## Procedure

1 Generate the required mirror manifests. Tip: If you are using a Red Hat Quay.io registry and need to mirror the images to aspecific organization in the registry, you can set the target to that organization. Specify theorganization name in the generate mirror-manifests command:export ORGANIZATION=<your-organization> \oc ibm-pak generate mirror-manifests $CASE\_NAME file://cp4ba \ --version $CASE\_VERSION \ --final-registry $TARGET\_REGISTRY/$ORGANIZATION If you do not know the value of the final registry where the images are to be mirrored, you canprovide a placeholder value of TARGET\_REGISTRY . For example:oc ibm-pak generate mirror-manifests $CASE\_NAME file://cp4ba \ --version $CASE\_VERSION \ --final-registry TARGET\_REGISTRY Note: TARGET\_REGISTRY used without any environment variable expansion is just aplain string that must be replaced later with the actual image registry URL when it is known toyou. Restriction: Currently, you cannot select the images to mirror by their targetarchitecture because image registries do not support sparse manifests (manifests that referenceimage digests outside of the package).
    1. Define the environment variable $TARGET\_REGISTRY by running the following
command. export TARGET\_REGISTRY=<target-registry>The
<target-registry> refers to the registry (hostname and port) where the
images are mirrored to and accessed by the OpenShift® Container
Platform (OCP) cluster. For
example: 172.16.0.10:5000.
    2. Create the following environment variables with the installer image name and the version. export CASE\_NAME=ibm-cs-bawautomation
export CASE\_VERSION=2.7.x
Note: Releases with interim fixes are packaged in archives with a new minor version. The version
numbers follow the release.major.minor standard. For example, the first interim fix
for 23.0.2 is packaged in the archive ibm-cs-bawautomation-2.7.x.tgz.
    3 Run the following command to generate mirror manifests to be used when mirroring the image tothe target registry. The $TARGET\_REGISTRY refers to the registry where the imagesare mirrored to and accessed by the OCPcluster.oc ibm-pak generate mirror-manifests $CASE\_NAME file://cp4ba \ --version $CASE\_VERSION \ --final-registry $TARGET\_REGISTRY/cp4ba Where file://cp4ba indicates to the plug-in that the images are first mirrored to a local file system (to thecp4ba directory) on the machine that runs the oc image mirror command. The final-registry $TARGET\_REGISTRY/cp4ba argument generates a mappingfile that is used by the oc image mirror commands. The final URL in your targetregistry includes the new cp4ba namespace in the mirrored namespace path. Thenamespace path can be multi-level if your target registry supports it. howNote: After an upgrade,you can remove images from the previous version of the local registry by using an alternativenamespace to copy the images to. For example, to a locationX namespace. The generate mirror-manifests command generates the followingfiles in ~/.ibm-pak/data/mirror/$CASE\_NAME/$CASE\_VERSION :

```
oc ibm-pak generate mirror-manifests $CASE\_NAME file://cp4ba \
   --version $CASE\_VERSION \
   --final-registry $TARGET\_REGISTRY/cp4ba
```

Where file://cp4ba
indicates to the plug-in that the images are first mirrored to a local file system (to the
cp4ba directory) on the machine that runs the oc image mirror
command. The final-registry $TARGET\_REGISTRY/cp4ba argument generates a mapping
file that is used by the oc image mirror commands. The final URL in your target
registry includes the new cp4ba namespace in the mirrored namespace path. The
namespace path can be multi-level if your target registry supports it.

The generate mirror-manifests command generates the following
files in ~/.ibm-pak/data/mirror/$CASE\_NAME/$CASE\_VERSION:

        - images-mapping-to-filesystem.txt
        - images-mapping-from-filesystem.txt
        - image-content-source-policy.yaml
        - catalog-sourcesxxx.yaml

```
export ORGANIZATION=<your-organization> \
oc ibm-pak generate mirror-manifests $CASE\_NAME file://cp4ba \   
   --version $CASE\_VERSION \
   --final-registry $TARGET\_REGISTRY/$ORGANIZATION
```

```
oc ibm-pak generate mirror-manifests $CASE\_NAME file://cp4ba \
   --version $CASE\_VERSION \
   --final-registry TARGET\_REGISTRY
```

2 Authenticate the registries. You must store authentication credentials for all the Business Automation Workflow source Dockerregistries. The following registries require authentication: Run the following command to configure credentials for all target registries that requireauthentication. Run the command separately for each registry. export REGISTRY\_AUTH\_FILE=<path to the file that has the auth credentials generated on podman login>podman login cp.icr.iopodman login <TARGET\_REGISTRY> Important: When you log in to cp.icr.io , you must specify the user ascp and the IBM entitlement key as the password. Forexample:podman login cp.icr.ioUsername: cpPassword: xxxxxxxxxxxxxxxxxxxxxLogin Succeeded! The password can be copied from the IBMcontainer library . If you export REGISTRY\_AUTH\_FILE=~/.ibm-pak/auth.json , and then run thepodman login command, you can see that the file is populated with registrycredentials. If you use docker login , the authentication file is typically located in$HOME/.docker/config.json on Linux or%USERPROFILE%/.docker/config.json on Windows. After you run the dockerlogin command, you can export REGISTRY\_AUTH\_FILE to point to thatlocation. For example, on Linux you can run the following command: export REGISTRY\_AUTH\_FILE=$HOME/.docker/config.json

You must store authentication credentials for all the Business Automation Workflow source Docker
registries. The following registries require authentication:

- cp.icr.io
- registry.redhat.io
- registry.access.redhat.com

Run the following command to configure credentials for all target registries that require
authentication. Run the command separately for each registry.

```
export REGISTRY\_AUTH\_FILE=<path to the file that has the auth credentials generated on podman login>
podman login cp.icr.io
podman login <TARGET\_REGISTRY>
```

```
podman login cp.icr.io
Username: cp
Password: xxxxxxxxxxxxxxxxxxxxx
Login Succeeded!
```

The password can be copied from the IBM
container library.

If you export REGISTRY\_AUTH\_FILE=~/.ibm-pak/auth.json, and then run the
podman login command, you can see that the file is populated with registry
credentials.

If you use docker login, the authentication file is typically located in
$HOME/.docker/config.json on Linux or
%USERPROFILE%/.docker/config.json on Windows. After you run the docker
login command, you can export REGISTRY\_AUTH\_FILE to point to that
location. For example, on Linux you can run the following command:

```
export REGISTRY\_AUTH\_FILE=$HOME/.docker/config.json
```

3 Mirror the images to the file system.

1. Mirror images to the TARGET\_REGISTRY.oc image mirror \
  -f ~/.ibm-pak/data/mirror/$CASE\_NAME/$CASE\_VERSION/images-mapping-to-filesystem.txt \
  -a $REGISTRY\_AUTH\_FILE \
  --filter-by-os '.*' \
  --insecure \
  --skip-multiple-scopes \
  --max-per-registry=1The command creates a v2 folder in the current
directory where all the images are copied. For example, if file://cp4ba is used as
the input to generate the mirror-manifests, then the command creates a subdirectory
cp4ba under v2 and copies the images in this folder.
The
following command can be used to see all the available options.

oc image mirror --helpYou can use the
continue-on-error parameter to continue the mirroring even if an error
occurs.
Based on the number and size of the images to mirror, the oc image
mirror command can take a considerable amount of time. If you are running the command on a
remote machine, run the command in the background with the nohup POSIX command so
that it does not stop if the user logs out. The following command starts the mirroring process in
the background and writes the log to a my-mirror-progress.txt file.

nohup oc image mirror -f ~/.ibm-pak/data/mirror/$CASE\_NAME/$CASE\_VERSION/images-mapping-to-filesystem.txt \
  --filter-by-os '.*' -a $REGISTRY\_AUTH\_FILE \
  --insecure \
  --skip-multiple-scopes \
  --max-per-registry=1 \
  --continue-on-error=true > my-mirror-progress.txt 2>&1 &You can view
the progress of the mirror command by running the following command on the remote machine:

tail -f my-mirror-progress.txt
2 Move the following items to your file system:
    - The v2 directory.
    - The auth file referred to, by the $REGISTSRY\_AUTH\_FILE
variable.
    - The
~/.ibm-pak/data/mirror/$CASE\_NAME/$CASE\_VERSION/images-mapping-from-filesystem.txt
file.
4 Mirror the images to the target registry from your file system. The following steps to copy the images from the file system to the$TARGET\_REGISTRY must be completed on your file system. Your file system must beconnected to both the local Docker registry and the OpenShift ContainerPlatform cluster. Important: If you used the placeholder value of TARGET\_REGISTRY for the--final-registry parameter when you generated the mirror manifests, replace thestring in the images-mapping-from-filesystem.txt file with the registry whereyou want to mirror the images. For example, if you want to mirror the images tomyregistry.com/mynamespace then replace TARGET\_REGISTRY withmyregistry.com/mynamespace .

The following steps to copy the images from the file system to the
$TARGET\_REGISTRY must be completed on your file system. Your file system must be
connected to both the local Docker registry and the OpenShift Container
Platform cluster.

1. Mirror the images from the v2 directory, to the target registry by running
the following command:oc image mirror \
  -f ~/.ibm-pak/data/mirror/$CASE\_NAME/$CASE\_VERSION/images-mapping-from-filesystem.txt \
  -a $REGISTRY\_AUTH\_FILE \
  --from-dir=${v2\_dir} \
  --filter-by-os '.*' \
  --insecure \
  --skip-multiple-scopes \
  --max-per-registry=1 The $v2\_dir refers to the parent directory on
the file system where you copied the v2 directory. The command does not produce
any console logs for about 6 - 8 minutes as it prepares the list from the CASE (Container
Application Software for Enterprise) package. If you want, you can add verbose (-v)
to the command with possible values of 3, 9, 99, etc.
2. Update the global image pull secret for your OpenShift cluster to have authentication
credentials in place to pull images from your $TARGET\_REGISTRY as specified in
the image-content-source-policy.yaml file. For more information, see Updating the global cluster pull secret.
3. Create the ImageContentsourcePolicy.Note: Before you run the command in this
step, you must be logged in to your OpenShift cluster. You do not need to be a cluster administrator
to run the mirroring commands. Using the oc login command, log in to the Red Hat
OpenShift Container
Platform cluster where
you plan to pull the mirrored images. You can identify your specific oc login by clicking the user
drop-down menu in the Red Hat OpenShift Container
Platform console, then clicking
Copy Login Command. 
Run the following command to create
ImageContentsourcePolicy.
oc apply -f ~/.ibm-pak/data/mirror/$CASE\_NAME/$CASE\_VERSION/image-content-source-policy.yaml
4. Verify that the ImageContentsourcePolicy resource is
created.oc get imageContentSourcePolicy
5. Verify your cluster node status.oc get MachineConfigPool -wAfter the
ImageContentsourcePolicy and global image pull secret are applied, the
configuration of your nodes is updated sequentially. Wait until all the
MachineConfigPools are updated before you move on to the next step.
6. Create a project for the CASE commands (cp4ba is an example) by running the
following commands:Note: Before you run the command in this step, you must be logged in to your
OpenShift cluster. 
export NAMESPACE=cp4ba
oc new-project $NAMESPACE
7. Optional: If you use an insecure registry, you must add the target registry to the
cluster insecureRegistries
list.oc patch image.config.openshift.io/cluster /
  --type=merge -p '{"spec":{"registrySources":{"insecureRegistries":["'${TARGET\_REGISTRY}'"]}}}'

## What to do next