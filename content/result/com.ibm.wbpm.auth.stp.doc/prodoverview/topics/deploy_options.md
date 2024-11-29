<!-- image -->

# Deployment options for IBM Integration
Designer

## Deployment with Workflow Center

The easiest way to develop services or BPEL processes is to use Integration Designer with Workflow Center. In this case, you
can associate your modules and libraries with process applications and toolkits in the Workflow Center repository. When
the modules and libraries are published to the repository, enterprise archive (EAR) files are
automatically generated and deployed for testing in the Workflow Center server. Then, you
can easily create a snapshot of the process application and use Workflow Center to deploy the
snapshot to a remote IBM Workflow
Server. Again, the
EAR files for the modules within the process application are automatically generated.

You
can still deploy and test your BPEL processes or business integration
services in the local Integration Designer test
environment. Usually you would do that testing before publishing the
modules to the Workflow Center.

Before
you can test modules on the Workflow Center server,
you need to create an entry in the Integration Designer Servers
view. See "Creating servers in the test environment" in the related
links for instructions.

<!-- image -->

## Deployment without Workflow Center

If you
have older processes that were developed for WebSphere Process Server
or WebSphere Enterprise Service Bus, you can still continue to develop
and deploy applications to IBM Process Server. In this case, you do
not associate your modules with process applications or toolkits.

Without IBM Workflow
Center, you need to
keep your artifacts in a source control management system such as Rational Team Concert. From there,
you can use a serviceDeploy command and an ANT script to deploy an EAR file to Workflow Server. Alternatively, you
can export EAR files from Integration Designer to either of the runtime environments.

<!-- image -->

## Related concepts

- Service-oriented architecture
- Service Component Architecture (SCA)
- The runtime environments for IBM Integration Designer
- Task flows

## Related reference

- Keyboard shortcuts for the workbench, Java development tools, and the Debug perspective

## Related information

- Team development in Business Automation Workflow