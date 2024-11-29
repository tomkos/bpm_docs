# Creating a deployment manager and managed-node profiles with
the BPMConfig command

You can use the BPMConfig command
to create the deployment manager and managed node profiles separately
from creating the deployment environment.

## Before you begin

If you have an existing WebSphere® Application
Server profile
that you want to augment, you must use the manageprofiles command-line
utility instead.

## Procedure

To create the deployment manager and managed node profiles
separately from creating the deployment environment, complete the
following steps.

1. On the computer where you
want to create the profiles, locate the appropriate sample properties
file: install\_root\BPM\samples\config.
2. Find the sample properties file that most closely represents your target
deployment environment and make a copy of this file.  For
more information about the sample configuration files, refer to Configuration properties for the BPMConfig command.
3 Modify your versionof the properties file so that the values correspond to your own configuration. Allof the deployment environment properties (cell name, node name, hostname) in the properties file must match exactly the values you willuse later to create the deployment environment with the DeploymentEnvironment wizard.Note: Your modified properties file must use UTF-8encoding. To create a deployment manager profile, youmust specify the following minimum set of properties for the profilethat you are creating: The bpm.cell.authenticationAlias.1.user and bpm.cell.authenticationAlias.1.password propertiesare used to create the WebSphere Application Server primary adminuser, which is the user for the Business Automation Workflow CellAdmin role. It isalso recommended that you set values for: To create a managed node profile, you must specify thefollowing minimum set of properties for the profile that you are creating: It is recommended that you also set: The bpm.dmgr.soapPort property mustbe set to the actual value of the deployment manager SOAP\_CONNECTOR\_ADDRESSendpoint. This property is not used during deployment manager profilecreation. It is read during profile creation for managed nodes, andtogether with the bpm.dmgr.hostname property,it identifies the deployment manager that manages the node profile.If the deployment manager resides on the computer where the BPMConfig commandis invoked, then the command will run successfully even when thisproperty is set incorrectly. A warning regarding the incorrect settingwill appear in the log files. Before using this same property fileto run the BPMConfig command on other computers,check the log files to ensure that there are no warnings about incorrectsettings for SOAP port numbers. Donot add any custom properties to this file when you perform your modificationsor the BPMConfig command will fail when it is run. If you need to use a backslash character (\) in your properties file,for example when specifying path names or passwords, you must use an escape backslash before it, forexample bpm.dmgr.installPath=c:\\IBM\\BPM\_ 24.x . Formore information about the available properties, read the commentsin the sample files, or see the BPMConfig command-line utility and the sample property filedescriptions in Configuration properties for the BPMConfig command .
    - bpm.dmgr.hostname=Important: To use an external Content Platform Engine, the hostname property value must have a domain
name suffix, for example
MyDmgrHost.my\_domain.com.
    - bpm.dmgr.installPath=
    - bpm.cell.authenticationAlias.1.user=
    - bpm.cell.authenticationAlias.1.password=
    - bpm.cell.name=
    - bpm.dmgr.nodeName=
    - bpm.dmgr.profileName=
    - bpm.dmgr.soapPort=
    - bpm.node.#.hostname=
    - bpm.node.#.installPath=
    - bpm.node.#.nodeName=
    - bpm.node.#.profileName=

The bpm.dmgr.soapPort property must
be set to the actual value of the deployment manager SOAP\_CONNECTOR\_ADDRESS
endpoint. This property is not used during deployment manager profile
creation. It is read during profile creation for managed nodes, and
together with the bpm.dmgr.hostname property,
it identifies the deployment manager that manages the node profile.
If the deployment manager resides on the computer where the BPMConfig command
is invoked, then the command will run successfully even when this
property is set incorrectly. A warning regarding the incorrect setting
will appear in the log files. Before using this same property file
to run the BPMConfig command on other computers,
check the log files to ensure that there are no warnings about incorrect
settings for SOAP port numbers.

Do
not add any custom properties to this file when you perform your modifications
or the BPMConfig command will fail when it is run.

If you need to use a backslash character (\) in your properties file,
for example when specifying path names or passwords, you must use an escape backslash before it, for
example bpm.dmgr.installPath=c:\\IBM\\BPM\_24.x.

For
more information about the available properties, read the comments
in the sample files, or see the BPMConfig command-line utility and the sample property file
descriptions in Configuration properties for the BPMConfig command.

4. Run the BPMConfig command
on the computer that has the deployment manager, passing it the name
of the properties file you created.
install\_root\bin\BPMConfig -create -profile my\_environment.properties

## What to do next