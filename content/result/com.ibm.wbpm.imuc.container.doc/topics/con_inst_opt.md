# Installation options

1. Plan and prepare the cluster, including the prerequisites for stand-alone Business Automation Workflow on containers.
2. Install the operator and generate the custom resource.
3. Edit, check, and complete the configuration of the custom resource and then apply it.
4. Do post-installation steps, mostly to do with optional integration and routing.

An air gap configuration supports clusters that might be disconnected from the internet (offline)
to continue to use the operator and components.

OCP includes an API (ImageContentSourcePolicy) that can automatically redirect
image pull requests from a specified registry location to an alternative location. The redirect is
fundamental to enabling an air gap for disconnected installations, as it removes the need to update
image references in every pod definition. To avoid caching and inconsistency problems, it needs all
images to be referenced by an image id or digest rather than a
tag.

The operator catalog index image enables the Cloud Pak containers to be installed as an OLM air
gap. The catalog image can be included as part of a CatalogSource resource to
enable an installation from the Operator Hub catalog.

1. Plan and install the air-gapped environment, and prepare the cluster, including the
prerequisites for stand-alone Business Automation Workflow on containers.
2. Generate the custom resource.
3. Edit, check, and complete the configuration of the custom resource and then apply it.
4. Do post-installation steps, mostly to do with optional integration and routing.

You can deploy stand-alone Business Automation Workflow on containers on a
Cloud Native Computing Foundation (CNCF) platform. See IBM Business
Automation Workflow support statement for Kubernetes platforms. For instructions, see Installing and
upgrading to IBM Business Automation Workflow on containers 24.0.0.0 on Kubernetes.