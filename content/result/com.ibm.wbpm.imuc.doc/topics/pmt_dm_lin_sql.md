# Creating deployment manager profiles using the Profile Management Tool (deprecated)

## About this task

<!-- image -->

You cannot select the name of the
Business Automation Workflow CellAdmin authentication alias when
using the Profile Management Tool. The name automatically defaults
to CellAdminAlias. (Using the BPMConfig command,
you can set the bpm.cell.authenticationAlias.1.name property
in the configuration properties file. And using the manageprofiles command,
you can supply the -adminAliasName parameter
with a customized authentication alias name.)

## Procedure

1 Use one of the following methods tostart the Profile Management Tool.
    - Start the tool from the Quick Start console.
    - Click
Linux\_operating\_system\_menus\_to\_access\_programs > IBM >
your\_product > Profile Management Tool.
    - Run the command installation\_root/bin/ProfileManagement/pmt.sh.
2. On the Welcome page,
click Launch Profile Management Tool or select
the Profile Management Tool tab.
3. On the Profiles tab,
click Create.  The Environment
Selection  page opens in a separate window.
4. On the Environment Selection page,
locate the IBM® Business Automation
Workflow configuration
and expand the section. Select the Business Automation Workflow deployment
manager profile template and click Next.
5 On the Profile Name and Location page,complete the following steps:

1. In the Profile name field, specify
a unique name or accept the default value.  Each profile
that you create must have a name. When you have more than one profile,
you can tell them apart at their highest level by this name.
2. In the Profile directory field,
enter the directory for the profile or use the Browse button
to go to the profile directory. The directory you specify
will contain the files that define the runtime environment, such as
commands, configuration files, and log files. The default directory
is installation\_root/profiles/profile\_name.
3. Optional: Select Make this profile
the default to make the profile you are creating the default
profile. This check box is shown only if you have an existing
profile on your system. When a profile is the default profile,
commands work automatically with it. The first profile that you create
on a workstation is the default profile. The default profile is the
default target for commands that are issued from the bin directory
in the product installation root. When only one profile exists on
a workstation, every command operates on that profile. If more than
one profile exists, certain commands require that you specify the
profile to which the command applies.
4. Click Next. If you
click Back and change the name of the profile,
you might have to manually change the name on this page when it is
displayed again.
6 On the Node, Host andCell Names page, complete the following actions for theprofile you are creating: Click Next .

- In the Node name field, enter a name for
the node or accept the default value. Try keeping the node name as
short as possible, but ensure that node names are unique within your
deployment environment.
- In the Host name field, enter a name for
the host or accept the default value.
- In the Cell name field, enter a name for
the cell or accept the default value.

Click Next.

7. Required: On the Administrative
Security page, enter values for the User name, Password,
and Confirm password. The user entered must
exist and must have administrative privileges. The Next button
is enabled only after you enter the values.Click Next.
8 On the Security Certificate (Part1) page, specify whether to create new certificates orimport existing certificates.

- To create a new default personal certificate and a new root
signing certificate, select Create a new default personal
certificate and Create a new root signing certificate,
and click Next.
- To import existing certificates, select Importan existing default personal certificate and Importan existing root signing certificate and provide the followinginformation: When you import a personal certificate as the default personalcertificate, import the root certificate that signed the personalcertificate. Otherwise, the Profile Management Tool adds the signerof the personal certificate to the trust.p12 file.
    - In the Path field, enter the directory
path to the existing certificate.
    - In the Password field, enter the password
for the certificate
    - In the Keystore type field, select the
keystore type for the certificate you are importing.
    - In the Keystore alias field,  select the
keystore alias for the certificate you are importing.
    - Click  Next to display the Security
Certificate (Part 2) page
9 On the Security Certificate (Part2) page, verify that the certificate information is correct,and click Next to display the PortValues Assignment page. If you create thecertificates, you can use the default values or modify them to createnew certificates. The default personal certificate is valid for oneyear by default and is signed by the root signing certificate. Theroot signing certificate is a self-signed certificate that is validfor 15 years by default. The default keystore password for the rootsigning certificate is WebAS . Change the password.The password cannot contain any double-byte character set (DBCS) charactersbecause certain keystore types, including PKCS12, do not support thesecharacters. The keystore types that are supported depend on the providersin the java.security file. When you createeither or both certificates, or import either or both certificates,the keystore files that are created are: These files all have the same password when you create or importthe certificates, which is either the default password, or a passwordthat you specify. An imported certificate is added to the key.p12 fileor the root-key.p12 file. If you import any certificatesand the certificates do not contain the information that you want,click Back to import another certificate.

If you create the
certificates, you can use the default values or modify them to create
new certificates. The default personal certificate is valid for one
year by default and is signed by the root signing certificate. The
root signing certificate is a self-signed certificate that is valid
for 15 years by default. The default keystore password for the root
signing certificate is WebAS. Change the password.
The password cannot contain any double-byte character set (DBCS) characters
because certain keystore types, including PKCS12, do not support these
characters. The keystore types that are supported depend on the providers
in the java.security file.

- key.p12: Contains the default personal certificate.
- trust.p12: Contains the signer certificate
from the default root certificate.
- root-key.p12: Contains the root signing certificate.
- default-signers.p12: Contains signer certificates
that are added to any new keystore file that you create after the
server is installed and running. By default, the default root certificate
signer and a DataPower® signer
certificate are in this keystore file.
- deleted.p12: Holds certificates deleted with
the deleteKeyStore task so that they can be recovered if needed.
- ltpa.jceks: Contains server default Lightweight
Third-Party Authentication (LTPA) keys that the servers in your environment
use to communicate with each other.
10 On the Port Values Assignment page,verify that the ports specified for the profile are unique and click Next . The Profile Management Tool detects ports currently used by other WebSphere® products and displays recommended port values that do notconflict with existing ones. If you have applications other than WebSphere ones that use specified ports, verify that the ports do notconflict.Ports are recognized as being in use if the following conditions are satisfied: Although the tool validates ports when you access the Port Values Assignment page, portconflicts can still occur resulting from selections you make on subsequent Profile Management Toolpages. Ports are not assigned until profile creation completes. If you suspect a portconflict, you can investigate it after the profile is created. Determine the ports used duringprofile creation by examining the followingfile:profile\_root /properties/portdef.props Included in thisfile are the keys and values used in setting the ports. If you discover port conflicts, you canreassign ports manually. To reassign ports, see Updating ports in existing profiles in theWebSphere ApplicationServer information center. Run theupdatePorts.ant file through the ws\_ant script detailed in thistopic.

- The ports are assigned to a profile created under an installation performed by the current
user.
- The ports are currently in use.

```
profile\_root/properties/portdef.props
```

11. If you do not have root privileges, skip to the
next step. If you have root privileges, on the Service Definition page,
indicate whether to use a Linux® service to run IBM Business Automation Workflow.
By default, IBM Business Automation Workflow is not selected to run
as a Linux service.If the profile is configured as a Linux
service, IBM Business Automation Workflow attempts to start Linux services for processes that are started by the
startServer or startManager commands. For example, if you
configure a server as a Linux service and issue the
startServer command, the wasservice command starts the defined
services.
You must specify a user name under which the service runs. 
To delete a Linux service, the user must be the root user or have the
required privileges for deleting the service. Otherwise, a removal script is created that the root
user can run to delete the service on behalf of the user.
12. On the Profile Summary page,
review the information. Click Create to create
the profile or Back to change the characteristics
of the profile.
13. On the Profile Complete page,
review the information. To proceed to the Quick Start console, make
sure that Launch Quick Start console is selected
and click Finish.

## What to do next

- Add managed-node profiles to be managed by the deployment manager,
and then configure the deployment environment.