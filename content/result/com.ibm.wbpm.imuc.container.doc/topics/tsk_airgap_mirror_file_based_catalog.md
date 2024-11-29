# Option 1: Mirroring catalogs to a private registry

You need to mirror the catalogs from a public registry to a private registry to install
IBM® Business Automation
Workflow for an airgap
deployment.

## About this task

Set up an airgap environment for testing, quality assurance (QA), and user acceptance testing
(UAT). These environments ensure error-free software before deploying the tested Cloud Pak operator
version or interim fix to production. Use the same bastion host, portable compute device, or
portable storage device to mirror the tested catalogs in all your deployment environments. When
testing is complete in your test/QA/UAT environments and you are ready to roll the deployment out to
production do not mirror the catalogs again. Mirroring the catalogs again pulls the latest versions
of Cloud Pak foundational services. These catalogs might be different from what you tested in your
test, QA, UAT, or pre-production environments.

## What to do next

- Using the oc mirror  command. See Option 1a: Mirroring catalogs to a private registry with a bastion server.
- Using the oc image mirror command. See Option 1b: Mirroring catalogs to a private registry with a portable compute or a storage device.