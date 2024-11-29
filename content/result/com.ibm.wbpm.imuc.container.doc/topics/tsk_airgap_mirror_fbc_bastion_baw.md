# Option 1a: Mirroring catalogs to a private registry with a bastion server

You can use a bastion host to mirror the catalogs to a private registry for an airgap
deployment.

## About this task

The bastion host must be connected to both the private registry and the Red Hat OpenShift® Container
Platform cluster. When you
mirror the images, you must run the oc mirror commands on the bastion host. The IBM
Catalog Management plug-in or ibm-pak uses File-based catalogs (FBC) to mirror all
the catalogs. The FBC is in JSON or YAML format that contains information that is needed to install
an operator into the OpenShift Container
Platform.

## Procedure

1 Generate the required mirror manifests. Restriction: Currently, you cannot select the images to mirror by their targetarchitecture because image registries do not support sparse manifests (manifests that referenceimage digests outside of the package).
    1. Define the environment variable $TARGET\_REGISTRY by running the following
command. export TARGET\_REGISTRY=<target-registry>The
<target-registry> refers to the registry (hostname and port) where the
images are mirrored to and accessed by the OpenShift Container
Platform cluster. For example:
172.16.0.10:5000.
    2. Create the following environment variables with the installer image name and the version. export CASE\_NAME=ibm-cs-bawautomation
export CASE\_VERSION=2.7.x
Note: Releases with interim fixes are packaged in archives with a new minor version. The version
numbers follow the release.major.minor standard. For example, the first interim fix
for 23.0.2 is packaged in the archive
ibm-cs-bawautomation-2.7.0.tgz. The value for 'x' is '0' for 23.0.2. For fix
pack, like 23.0.2-IF001, the value of 'x' is '1'.
    3. Run the following command to set the preferred tool parameter in the YAML file to
oc-mirror.oc ibm-pak config mirror-tools --enabled oc-mirror
    4. Run the following command to generate mirror manifests to be used when mirroring the catalog to
the target registry. The $TARGET\_REGISTRY refers to the registry where the
catalogs are mirrored to and accessed by the OpenShift Container
Platform
cluster.oc ibm-pak generate mirror-manifests $CASE\_NAME $TARGET\_REGISTRY \
  --version $CASE\_VERSIONImportant: The generate
mirror-manifests command provides an output that lists the command for mirroring. Save the
command for later use.
The following example shows sample
output.oc ibm-pak generate mirror-manifests ibm-cs-bawautomation --version 2.7.x docker-na-public.artifactory.swg-devops.com/ecm-containerization-docker-local/cp4ba-2302
Generating mirror manifests of CASE: ibm-cs-bawautomation, version: 2.7.x is complete
Note: After
an upgrade, you can remove images from the previous version of the local registry. For this, include
an alternative namespace to copy the images to instead of the default path. For example, the
following CASE command copies the images to a locationX
namespace.oc ibm-pak generate mirror-manifests $CASE\_NAME $TARGET\_REGISTRY/locationX \
  --version $CASE\_VERSION
A new directory
$IBMPAK\_HOME/.ibm-pak/mirror is created when you issue the oc ibm-pak
generate mirror-manifests command. The mirror directory stores the
catalog-sources.yaml, image-content-source-policy.yaml,
and image-set-config.yaml files.
Tip: If you are using a Red
Hat® Quay.io registry and need to mirror the images to a specific organization in the registry, you
can set the target to that organization. Specify the organization name in the generate
mirror-manifests
command:export ORGANIZATION=<your-organization> \
oc ibm-pak generate mirror-manifests $CASE\_NAME $TARGET\_REGISTRY/$ORGANIZATION \
   --version $CASE\_VERSION
2 Authenticate the registries. You must store authentication credentials for all the Cloud Pak for Business Automation source Dockerregistries. The following registries require authentication: Run the following command to configure credentials for all target registries that requireauthentication. Run the command separately for each registry. export REGISTRY\_AUTH\_FILE=<path to the file that has the auth credentials generated on podman login>podman login cp.icr.iopodman login <TARGET\_REGISTRY> Important: When you log in to cp.icr.io , you must specify the user ascp and the IBM entitlement key as the password. Forexample:podman login cp.icr.ioUsername: cpPassword: xxxxxxxxxxxxxxxxxxxxxLogin Succeeded! The password can be copied from the IBMcontainer library . If you see "cert error " messages, you can add--tls-verify=false to the command. If you export REGISTRY\_AUTH\_FILE=~/.ibm-pak/auth.json , and then run thepodman login command, you can see that the file is populated with registrycredentials. If you use docker login , the authentication file is typically located in$HOME/.docker/config.json on Linux or%USERPROFILE%/.docker/config.json on Windows. After you run the dockerlogin command, you can export REGISTRY\_AUTH\_FILE to point to thatlocation. For example, on Linux you can run the following command: export REGISTRY\_AUTH\_FILE=$HOME/.docker/config.json

You must store authentication credentials for all the Cloud Pak for Business Automation source Docker
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
container library. If you see "cert error" messages, you can add
--tls-verify=false to the command.

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

3. When you generate the mirror-manifests to mirror the catalogs, run the command generated in
step 1d .
 An example command is
shown.oc mirror --config /root/cp4ba/.ibm-pak/data/mirror/ibm-cs-bawautomation/2.7.x/image-set-config.yaml docker://docker-na-public.artifactory.swg-devops.com/ecm-containerization-docker-local/cp4ba --dest-skip-tls --max-per-registry=6
Run the command on the host that is connected to both the local Docker registry and the OpenShift Container
Platform cluster.

The command does not produce any console logs for about 6 - 8 minutes as it prepares the list
from the CASE package. If you want, you can add verbose (-v) to the command with possible values of
1 to 9.

The following command can be used to see all the available
options.oc mirror --help

Note: By default the oc mirror command mirrors all the images from all channels in
the Cloud Pak for Business Automation
multi-pattern catalog and Cloud Pak for Business Automation
FileNet® Content
Manager
catalog. You can edit the
$IBMPAK\_HOME/.ibm-pak/data/mirror/ibm-cs-automation/2.7.x/image-set-config.yaml
file to remove the operator lifecycle manager (OLM) channels and keep only the v23.2 channel. This
is only applicable for new installations.

Based on the number and size of the images to mirror, the oc mirror command can
take a considerable amount of time. If you are running the command on a remote system, run the
command in the background with the nohup POSIX command so that it does not stop if
the user logs out. The following command starts the mirroring process in the background and writes
the log to a cp4ba-260.txt file.
nohup oc mirror -f ~/.ibm-pak/data/mirror/$CASE\_NAME/$CASE\_VERSION/image-set-config.yaml \
  --filter-by-os '.*' -a $REGISTRY\_AUTH\_FILE \
  --insecure \
  --skip-multiple-scopes \
  --max-per-registry=6 \
  --continue-on-error=true > /opt/cp4ba-260.txt 2> &

The following example shows sample output.

nohup: ignoring input
Logging to .oc-mirror.log
Checking push permissions for docker-na-public.artifactory.swg-devops.com
Creating directory: oc-mirror-workspace/src/publish
Creating directory: oc-mirror-workspace/src/v2
Creating directory: oc-mirror-workspace/src/charts
Creating directory: oc-mirror-workspace/src/release-signatures
No metadata detected, creating new workspace
1145 related images processed in 1m2.231903162s
Writing image mapping to oc-mirror-workspace/operators.1697865931/manifests-ibm-cs-bawautomation-catalog/mapping.txt
57 related images processed in 6.853202235s
Writing image mapping to oc-mirror-workspace/operators.1697865931/manifests-ibm-fncm-catalog/mapping.txt
--
--
--
info: Mirroring completed in 1h11m19.09s (4.185MB/s)
Rendering catalog image "docker-na-public.artifactory.swg-devops.com/ecm-containerization-docker-local/cp4ba510-1025/root/ibm-cs-bawautomation-catalog:9c5d8c" with file-based catalog
Writing image mapping to oc-mirror-workspace/results-1698276172/mapping.txt
Writing CatalogSource manifests to oc-mirror-workspace/results-1698276172
Writing ICSP manifests to oc-mirror-workspace/results-1698276172
4. Update the global image pull secret for your OpenShift Container
Platform cluster to have
authentication credentials in place to pull images from your $TARGET\_REGISTRY as
specified in the image-content-source-policy.yaml file. For more information,
see Updating the global cluster pull secret.
5. Run the following command to create ImageContentsourcePolicy. 
oc apply -f imageContentSourcePolicy.yaml
6. Verify that the ImageContentsourcePolicy resource is created. 
oc get imageContentSourcePolicy
7. Verify your cluster node status. 
oc get MachineConfigPool -w
After the ImageContentsourcePolicy and global image pull secret are applied, the
configuration of your nodes is updated sequentially. Wait until all the
MachineConfigPools are updated before you move on to the next step.
8. Create a project for the CASE commands (cp4ba is an example) by running
the following commands. Before you run the command in this step, you must be logged in to your
OpenShift Container
Platform
cluster. 
export NAMESPACE=cp4ba
oc new-project $NAMESPACE
9. Optional: If you use an insecure registry, you must add the target registry to the
cluster insecureRegistries list. 
oc patch image.config.openshift.io/cluster \
  --type=merge -p '{"spec":{"registrySources":{"insecureRegistries":["'${TARGET\_REGISTRY}'"]}}}'

## What to do next