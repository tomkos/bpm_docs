<!-- image -->

# Exporting modules for deployment or development

## About this task

The following topics explain how to export modules for
deployment or development and how to configure dependency libraries
for adapters that have been deployed on a server.

If you want
to author artifacts in IBM Integration
Designer and
deploy them to an IBM Business Automation
Workflow runtime
environment, the major versions of the two products must match.

- Exporting modules as EAR files

In IBM Integration Designer, you can export modules and libraries as EAR files and then deploy them on  Workflow Server by using the administrative console or command-line tools.
- Exporting modules and libraries as serviceDeploy files

In IBM Integration Designer, you can export modules and libraries as compressed files and then use the serviceDeploy command of  Workflow Server to build and deploy them as EAR files.
- Exporting modules and libraries as project interchange files

In IBM Integration Designer, you can export modules and libraries as project interchange files. This enables you to share modules and their projects for development work.
- Configuring dependency libraries for adapters

The deployed adapter running in the server requires the same dependency libraries as it does in IBM Integration Designer to process requests. The method for adding these library files depends on the mode of the adapter deployment: deployed as a stand-alone adapter; or embedded in the EAR file.