<!-- image -->

# Deploying your application with an embedded adapter

## Before you begin

Ensure that the module was created with With module for use by single
application selected. Ensure that the Dependencies editor in IBM® Integration
Designer shows that the RAR file module is included
and Deploy with Module is selected.

Ensure that steps related to external software dependencies or event processing resources are
reviewed for your specific adapter types. These dependencies might require you to add external files
to the application for deployment when you create the binding.

- Set up database tables, directories, environment variables, or other staging resources that are
associated with a certain adapter's event processing.
- Create missing J2C authentication data entries.
- Complete necessary additional steps for each application cluster member's external software
dependencies.

## About this task

If your application contains adapter bindings that use an embedded adapter RAR file, some
additional tasks might be required:

## Procedure

1. Deploy your application by using the normal preferred method for your Advanced
deployment environment.
2 Review the deployment manager and application cluster logs for errors related to thedeployment. Some adapter binding deployment tasks might fail after the EAR file is installed, whichprevents the EAR file from being used at run time. If you find errors, complete the followingsteps.
    1. Ensure the adapter RAR file and necessary external JAR files are added to the application and
included in the EAR file.
    2. Confirm that you did not configure Java Naming and Directory Interface (JNDI) resources for the
binding. These JNDI adapter resources cannot be created until the associated RAR file is installed,
so they must not be used if the RAR file is installed with the EAR file. The application's adapter
binding must include the needed configuration settings. To change the environment-specific
configuration changes, modify the associated activation specification or connection factory when the
application is installed. For details, see the Administering the adapter
module section in your adapter's documentation.