# Setting up a host to mirror images to a private registry

## Before you begin

You can use a bastion server, a portable compute device, or two compute devices with portable
storage as your host.

A bastion host is a server that is provisioned with a public IP address that is accessible
through remote access Secure Shell (SSH). When configured, the bastion server acts as an
intermediate server that allows a secure connection to the instances made available without a public
IP address.

A portable compute device, such as a laptop, can be used to download images from the entitled
registry to a portable image registry that is running locally on the device. You can then bring the
device behind your firewall and copy the images from your portable registry on the device to the
local private registry.

A portable storage device, such as a hard disk drive, can be connected to a compute device
external to your firewall to download the images. The portable storage can then be connected to a
device behind the firewall so that the images can be loaded to the local private registry.

No matter what medium you choose for your air-gapped installation, the host must satisfy the
following prerequisites:

- The host must be able to access the OpenShift® Container
Platform (OCP) cluster, an
internal image registry, and the internet.
- The host must be on a Linux® x86\_64 or Mac platform with any operating system that the IBM Cloud
Pak® command line interface (CLI) and the OCP CLI support. If you are on a Windows platform, you
must run the actions in a Linux® x86\_64 VM or from a Windows Subsystem for Linux (WSL)
terminal.

## Procedure

1. Install the oc OCP CLI tool 4.12.xx or greater. For more information, see
OCP CLI tools.
2. Install Podman on a Red Hat Enterprise Linux (RHEL) machine. For more information, see Podman
installation instructions.
3 Download and install the most recent version (v1.11.0 or greater) of the IBM CatalogManagement Plug-in . Option 1 Option 2 The plug-in is also provided in a container imagecp.icr.io/cpopen/cpfs/ibm-pak:TAG where TAG must be replaced withthe corresponding plug-in version. For example,cp.icr.io/cpopen/cpfs/ibm-pak:v1.4.0 for the v1.4.0 of the plug-in. Thefollowing command creates a container and copies the plug-ins for all the supported platforms in adirectory (plugin-dir ). Note: The command requires that you have Dockerinstalled. For more information about how to install Docker on an RHEL machine, see How to Install Docker CE . id=$(podman create cp.icr.io/cpopen/cpfs/ibm-pak:TAG - )podman cp $id:/ibm-pak-plugin plugin-dirpodman rm -v $idcd plugin-dir You can specify any directory name. After the plug-ins are copied, thetemporary container is deleted, and the target directory contains all the binaries and artifacts inthe IBM/ibm-pak-plugin GitHub repository.
    1. Download the file based on the host operating system from IBM/ibm-pak-plugin/releases.
    2. Extract the binary file by entering the following command:
tar -xf oc-ibm\_pak-linux-amd64.tar.gz
    3. Run the following command to move the file to the /usr/local/bin
directory:mv oc-ibm\_pak-linux-amd64 /usr/local/bin/oc-ibm\_pakNote: If you
install as a non-root user, you must use sudo.
    4. You can confirm that oc ibm-pak -h is installed by running the following
command:oc ibm-pak --helpThe plug-in usage is displayed.

The plug-in is also provided in a container image
cp.icr.io/cpopen/cpfs/ibm-pak:TAG where TAG must be replaced with
the corresponding plug-in version. For example,
cp.icr.io/cpopen/cpfs/ibm-pak:v1.4.0 for the v1.4.0 of the plug-in.

The
following command creates a container and copies the plug-ins for all the supported platforms in a
directory (plugin-dir).

```
id=$(podman create cp.icr.io/cpopen/cpfs/ibm-pak:TAG - )
podman cp $id:/ibm-pak-plugin plugin-dir
podman rm -v $id
cd plugin-dir
```

You can specify any directory name. After the plug-ins are copied, the
temporary container is deleted, and the target directory contains all the binaries and artifacts in
the IBM/ibm-pak-plugin GitHub repository.

4 Download and install oc mirror with version 4.14.0 or greater to mirrorimages.

1. Download the oc-mirror based on the host operating system from here.
2. Extract the binary file by entering the following
command.tar -xf oc-mirror.tar.gz
3. Run the following command to move the file to the /usr/local/bin
directory.mv oc-mirror /usr/local/bin/oc-mirrorNote: If you install as a non-root user, you must use
sudo.
4. You can confirm that oc ibm-pak -h is installed by running the following
command.oc mirror helpThe command usage is
displayed.
5 Make sure that the following network ports are available on the host. Tip: If the bastion host is unable to retrieve the source images from the publicregistries, you might need to allow specific access to these sites. A HTTP 403response is an indication of such a parsing error. If you see images that are blocked, checkwhether it is related to the Docker or quay image registries as they might use proxies or mirrorsites. If one of the registries is blocked, you must add that URL to the website allowlist. Thefollowing websites can be added to the allowlist to prevent pulling imageerrors:cp.icr.io/cp*.quay.io/opencloudio*.icr.io/cpopen

- *.icr.io:443 for the IBM Entitled Registry.
- *.quay.io:443 for foundational services. For more information, see Important
firewall changes for customers pulling container images.
- github.com for CASE and tools.
- redhat.com for OpenShift upgrades.

```
cp.icr.io/cp
*.quay.io/opencloudio
*.icr.io/cpopen
```

## What to do next