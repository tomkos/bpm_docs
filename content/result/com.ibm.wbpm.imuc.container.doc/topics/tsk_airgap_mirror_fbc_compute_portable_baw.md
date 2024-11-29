# Option 1b: Mirroring catalogs to a private registry with a portable compute or a storage
device

If your cluster is not connected to the internet, you can install Cloud Pak for Business Automation on your cluster.

## Before you begin

Verify that you completed the prerequisites, prepared a host, set the environment variables, and
created registry namespaces if the registry does not allow automatic creation of top-level
namespaces.

## Procedure

1 Generate the required mirror manifests. Tip: If you are using a Red Hat® Quay.io registry and need to mirror the images to aspecific organization in the registry, you can set the target to that organization. Specify theorganization name in the generate mirror-manifests command:export ORGANIZATION=<your-organization> \oc ibm-pak generate mirror-manifests $CASE\_NAME $TARGET\_REGISTRY/$ORGANIZATION \ --version $CASE\_VERSION If you do not know the value of the final registry where the images are to be mirrored, you canprovide a placeholder value of TARGET\_REGISTRY . For example:oc ibm-pak generate mirror-manifests $CASE\_NAME file://cp4ba \ --version $CASE\_VERSION \ --final-registry TARGET\_REGISTRY Note: TARGET\_REGISTRY used without any environment variable expansion is just aplain string that must be replaced later with the actual image registry URL when it is known toyou. Restriction: Currently, you cannot select the images to mirror by their targetarchitecture because image registries do not support sparse manifests (manifests that referenceimage digests outside of the package).
    1. Define the environment variable $TARGET\_REGISTRY by running the following
command. export TARGET\_REGISTRY=<target-registry>The
<target-registry> refers to the registry (hostname and port) where the
images are mirrored to and accessed by the OpenShift Container Platform cluster. For example:
172.16.0.10:5000.
    2. Create the following environment variables with the installer image name and the version. export CASE\_NAME=ibm-cs-bawautomation
export CASE\_VERSION=2.7.x
Note: Releases with interim fixes are packaged in archives with a new minor version. The version
numbers follow the release.major.minor standard. For example, the first interim fix
for 23.0.2 is packaged in the archive ibm-cs-bawautomation-2.7.0.tgz.
    3. Run the following command to set the preferred tool parameter in the YAML file to
oc-mirror.oc ibm-pak config mirror-tools --enabled oc-mirror
    4 Run the following command to generate mirror manifests to be used when mirroring the image tothe target registry. The $TARGET\_REGISTRY refers to the registry where the imagesare mirrored to and accessed by the OpenShift Container Platformcluster.oc ibm-pak generate mirror-manifests $CASE\_NAME file://cp4ba \ --version $CASE\_VERSION \ --final-registry $TARGET\_REGISTRY/cp4ba Where file://cp4ba indicates to the plug-in that the images are first mirrored to a local file system (to thecp4ba directory) on the machine that runs the oc mirror command. The final-registry $TARGET\_REGISTRY/cp4ba argument generates a mappingfile that is used by the oc mirror commands. The final URL in your target registryincludes the new cp4ba namespace in the mirrored namespace path. The namespace pathcan be multi-level if your target registry supports it. Important: Thegenerate mirror-manifests command provides an output that lists the commands for: Save the commands for later use. The following is a sampleoutput.Generating mirror manifests of CASE: ibm-cs-bawautomation, version: 2.7.x is completeNext steps- To mirror the catalog:oc mirror --config /root/airgap-3.0/.ibm-pak/data/mirror/ibm-cs-bawautomation/2.7.x/image-set-config.yaml file://cp4ba --dest-skip-tls --max-per-registry=6oc mirror --dest-skip-tls --from=sequence\_file.tar docker://docker-na-public.artifactory.swg-devops.com/ecm-containerization-docker-local/cp4ba Note: Afteran upgrade, use an alternative namespace to copy the images, by removing images from the previousversion of the local registry. For example, to a locationX namespace. Thegenerate mirror-manifests command generates the following files in~/.ibm-pak/data/mirror/$CASE\_NAME/$CASE\_VERSION :

```
oc ibm-pak generate mirror-manifests $CASE\_NAME file://cp4ba \
   --version $CASE\_VERSION \
   --final-registry $TARGET\_REGISTRY/cp4ba
```

Where file://cp4ba
indicates to the plug-in that the images are first mirrored to a local file system (to the
cp4ba directory) on the machine that runs the oc mirror
command. The final-registry $TARGET\_REGISTRY/cp4ba argument generates a mapping
file that is used by the oc mirror commands. The final URL in your target registry
includes the new cp4ba namespace in the mirrored namespace path. The namespace path
can be multi-level if your target registry supports it.

        - Write to disk.
        - Write from disk to a target registry.

```
Generating mirror manifests of CASE: ibm-cs-bawautomation, version: 2.7.x is complete

Next steps

- To mirror the catalog:

oc mirror --config /root/airgap-3.0/.ibm-pak/data/mirror/ibm-cs-bawautomation/2.7.x/image-set-config.yaml file://cp4ba --dest-skip-tls --max-per-registry=6
oc mirror --dest-skip-tls --from=sequence\_file.tar docker://docker-na-public.artifactory.swg-devops.com/ecm-containerization-docker-local/cp4ba
```

The
generate mirror-manifests command generates the following files in
~/.ibm-pak/data/mirror/$CASE\_NAME/$CASE\_VERSION:

        - catalog-sources.yaml
        - image-content-source-policy.yaml
        - image-set-config.yaml

```
export ORGANIZATION=<your-organization> \
oc ibm-pak generate mirror-manifests $CASE\_NAME $TARGET\_REGISTRY/$ORGANIZATION \
   --version $CASE\_VERSION
```

```
oc ibm-pak generate mirror-manifests $CASE\_NAME file://cp4ba \
   --version $CASE\_VERSION \
   --final-registry TARGET\_REGISTRY
```

2 Authenticate the registries. You must store authentication credentials for all the Cloud Pak for Business Automation source Dockerregistries. The following registries require authentication: Run the following command to configure credentials for all target registries that requireauthentication. Run the command separately for each registry. export REGISTRY\_AUTH\_FILE=<path to the file that has the auth credentials generated on podman login>podman login cp.icr.iopodman login <TARGET\_REGISTRY> Important: When you log in to cp.icr.io , you must specify the user ascp and the IBM entitlement key as the password. Forexample:podman login cp.icr.ioUsername: cpPassword: xxxxxxxxxxxxxxxxxxxxxLogin Succeeded! The password can be copied from the IBMcontainer library . If you export REGISTRY\_AUTH\_FILE=~/.ibm-pak/auth.json , and then run thepodman login command, you can see that the file is populated with registrycredentials. If you use docker login , the authentication file is typically located in$HOME/.docker/config.json on Linux or%USERPROFILE%/.docker/config.json on Windows. After you run the dockerlogin command, you can export REGISTRY\_AUTH\_FILE to point to thatlocation. For example, on Linux you can run the following command: export REGISTRY\_AUTH\_FILE=$HOME/.docker/config.json

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

3. Run the first command generated in step 1d to write the data to disk. 
The following is an example command.

oc mirror --config /root/airgap-3.0/.ibm-pak/data/mirror/ibm-cs-automation/2.7.x/image-set-config.yaml file://cp4ba2302 --dest-skip-tls --max-per-registry=6 " as oc mirror --config /root/airgap-3.0/.ibm-pak/data/mirror/ibm-cs-bawautomation/2.7.x/image-set-config.yaml file://cp4ba2302 --dest-skip-tls --max-per-registry=6
The command generates the mirror\_seq1\_000000.tar file in
/root/cp4ba/mirror\_seq1\_000000.tar.
4. Run the second command generated in step 1d to write data from the local disk to the target
registry.  
The following is an example command.

oc mirror --dest-skip-tls --from=sequence\_file.tar docker://docker-na-public.artifactory.swg-devops.com/ecm-containerization-docker-local/cp4ba
Replace sequence\_file.tar with generated output from Step 3. For example →
/root/cp4ba/mirror\_seq1\_000000.tar.

Run the commands on the host that is connected to both the local Docker registry and the
OpenShift Container Platform cluster.

The command does not produce any console logs for about 6 - 8 minutes as it prepares the list
from the CASE package. If you want, you can add verbose (-v) to the command with possible values of
1 to 9.

The following command can be used to see all the available
options.oc mirror --help

Based on the number and size of the images to mirror, the oc mirror command can
take a considerable amount of time. If you are running the command on a remote system, run the
command in the background with the nohup POSIX command so that it does not stop if
the user logs out. The following command starts the mirroring process in the background and writes
the log to a cp4ba-2.7.x.txt file.
nohup oc mirror -f ~/.ibm-pak/data/mirror/$CASE\_NAME/$CASE\_VERSION/image-set-config.yaml \
  --filter-by-os '.*' -a $REGISTRY\_AUTH\_FILE \
  --insecure \
  --skip-multiple-scopes \
  --max-per-registry=6 \
  --continue-on-error=true > /opt/cp4ba-2.7.x.txt 2> &

The following is a sample output.info: Mirroring completed in 17.08s (0B/s)
Wrote release signatures to oc-mirror-workspace/results-1700028859
Rendering catalog image "docker-na-public.artifactory.swg-devops.com/ecm-containerization-docker-local/cp4ba2302-file/root/ibm-cs-bawautomation-catalog:125749" with file-based catalog
Writing image mapping to oc-mirror-workspace/results-1700028859/mapping.txt
Writing CatalogSource manifests to oc-mirror-workspace/results-1700028859
Writing ICSP manifests to oc-mirror-workspace/results-1700028859
5. Update the global image pull secret for your Red Hat OpenShift cluster to have
authentication credentials in place to pull images from your $TARGET\_REGISTRY as
specified in the image-content-source-policy.yaml file. For more information,
see Updating the global cluster pull secret.
6. Run the following command to create ImageContentsourcePolicy. 
oc apply -f imageContentSourcePolicy.yaml
7. Verify that the ImageContentsourcePolicy resource is created. 
oc get imageContentSourcePolicy
8. Verify your cluster node status. 
oc get MachineConfigPool -w
After the ImageContentsourcePolicy and global image pull secret are applied, the
configuration of your nodes is updated sequentially. Wait until all the
MachineConfigPools are updated before you move on to the next step.
9. Create a project for the CASE commands (cp4ba is an example) by running
the following commands. Before you run the command in this step, you must be logged in to your Red
Hat OpenShift cluster. 
export NAMESPACE=cp4ba
oc new-project $NAMESPACE
10. Optional: If you use an insecure registry, you must add the target registry to the
cluster insecureRegistries list. 
oc patch image.config.openshift.io/cluster \
  --type=merge -p '{"spec":{"registrySources":{"insecureRegistries":["'${TARGET\_REGISTRY}'"]}}}'

## What to do next

You can now go ahead and install the Cloud Pak operator. For more information, see Installing the Cloud Pak catalog and an operator instance.