# Installing Business Automation Workflow catalogs and operators in an offline cluster

For an airgap deployment, you need to mirror the catalogs or images to a private registry
to install IBM® Business Automation
Workflow.

## About this task

Mirror the catalogs or images that your deployment needs from the public registries to the
private registry. An ImageContentSourcePolicy is also needed to redirect the image
pull requests from the public registries to the private registry.

You can use the oc mirror  command to select the catalogs that are needed to
install the Business Automation Workflow
in an airgap environment. Or, you can use the oc image mirror command to mirror all
the images in the CASE (Container Application Software for Enterprise) file.

- Using the oc mirror  command. See Option 1: Mirroring catalogs to a private registry using oc mirror.
- Using the oc image mirror command. See Option 2: Mirroring images to a private registry using oc image mirror.