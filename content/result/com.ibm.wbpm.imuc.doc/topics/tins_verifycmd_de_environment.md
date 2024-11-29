# Verifying the status of your environment using the BPMConfig
command

## About this task

- The associated resources for every component are checked to determine
whether they are usable. For example, each component's database is
checked to determine whether it has been created and a connection
can be established.
- The security configuration is checked to determine whether the
essential requirements have been met.
- IBM Workflow Server, Workflow Center, and Performance Data Warehouse
are checked to determine whether they are usable. Several runtime
checks are performed, such as whether the associated applications
and message engines have started.

## Procedure

1. If your environment has not yet been started, start the environment by following the
instructions in the Starting and stopping your environment using the command line
topic.
2. Run the following command, where profile\_name is
the name of the profile, DE\_name is the name of
the deployment environment, and output\_directory is
the optional name of a directory where you want to generate the status
report: install\_root/bin/BPMConfig -validate -profile profile\_name [-de DE\_name] [-outputDir output\_directory]
For
example:
install\_root/bin/BPMConfig -validate -profile DmgrProfile -de De1 -outputDir E:/OutputIf
there is only one deployment environment in the WebSphere® Application
Server cell, you can omit the -de
option.
3. Change to the output directory where the status report
was generated. If you used the -outputDir option
to specify an output directory, the status report is generated into
a subdirectory named html that resides under
the output directory. For example, if you specified E:/Output as
the output directory, the status report is generated into E:/Output/html.
If you did not specify an output directory, the status report is generated
into an html directory that resides under the
directory where you ran the BPMConfig command. For example, install\_root/bin/html.
4. Open the generated status report. The name of the report
is ConfigValidationReport\_DE\_name.html,
where DE\_name is the name of the deployment environment.
For example, ConfigValidationReport\_De1.html.
The report is divided into multiple sections. There is one
section for each configured component, such as ProcessServer.
5 In each section of the report, perform the following tasks:
    - Examine the Status area, which indicates
the configuration status of the component. For the Cell Database,
Cell Security, and Deployment Environment Security components, there
is never a configuration status. For the Deployment Environment Bootstrap
component, the configuration status can be Finished, Unfinished,
or Unknown. For all other components,
the configuration status is always Configured.
    - Examine the associated resources area, which indicates the
status of the resources that are associated with the component. Depending
on the component, there are five main types of associated resources,
as shown in the following table:

Resources
Description

Applications
Applications are associated with many
different components, such as the ProcessServer, ProcessCenter, and
PDW components. In the Applications area, review the status in the Installed and Started columns
to determine whether each application is installed and started.

Authentication aliases
Authentication aliases are associated
with the Cell Security and Deployment Environment Security components.
In the Authentication Aliases area, review the status in the Created column
to determine whether each authentication alias has been created.

Messaging
Messaging engines are associated with
the Messaging component. In the Messaging area, review the status
in the Started column to determine whether
each messaging engine has been started.

Bootstrap
Bootstraps are associated with the
Deployment Environment Bootstrap component. In the Bootstrap area,
review the status in the Imported column to
determine whether the bootstraps have been imported.

Databases
Databases are associated with many
different components, such as the ProcessServer, PDW, BusinessSpace,
and BPC components. In the Databases area, review the status in the Created and Connected columns
to determine whether each database is installed and connected.
6. Optional: 
For security reasons, you might want to delete the Task Manager credentials from the
config.properties file.
See the Task Manager change in IBM Content
Navigator 3.0.5 iFix 1 Security Enhancement.

## Related tasks

- Starting and stopping the deployment environment using the command line

## Related information

- Verifying the status of your environment using the Health Center