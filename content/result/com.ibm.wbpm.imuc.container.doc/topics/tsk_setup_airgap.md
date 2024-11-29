# Setting up the cluster for an air gapped (offline) deployment

## About this task

The IBM Catalog Management plug-in or ibm-pak for short, uses standard
tooling for registry and cluster access. A CASE (Container Application Software for Enterprise)
package specifies the composition of the product and the images that must be copied into an
air-gapped environment.

The following diagram shows the steps that are involved in installing
in an air gap environment on OpenShift® Container
Platform(OCP).

<!-- image -->

It is common in production to have a
cluster that cannot access the internet. In these cases, you can still install IBM Business Automation
Workflow and OpenShift Container
Platform (OCP) in an air-gapped
(otherwise known as offline or disconnected) environment. An air-gapped installation uses the IBM
operator catalog to mimic a typical online installation except that the Cloud Pak images are in your
own registry. You can use a bastion host or a compute device (like a laptop), with or without
portable storage (like an external hard disk drive) to transfer the images to an air-gapped network.

All of these scenarios use CASE files to mirror content from a source to a target. CASE is a
specification that defines metadata and structure for packaging, managing, and unpacking
containerized applications.

The following diagram provides an overview of the air-gapped
installation options.

<!-- image -->

## What to do next