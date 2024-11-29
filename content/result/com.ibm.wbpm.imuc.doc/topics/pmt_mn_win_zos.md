# Creating managed-node profiles using the Profile Management
Tool

## About this task

<!-- image -->

<!-- image -->

- To run the Profile Management Tool on Windows, you
must elevate your Microsoft Windows user account privileges.
Whether you are an administrative user or a non-administrative user,
right-click the pmt.bat file and select Run
as administrator. Alternatively, use the runas command
at the command line. For example, the following command can be run
from the installation\_root\bin\ProfileManagement directory:runas /user:MyAdminName /env pmt.batNon-administrative
users are prompted for the administrator password.
- If you install multiple instances of IBM® Business Automation Workflow as
the root user and give a nonadministrative user access to only a subset
of those instances, the Profile Management Tool does not function
correctly for the nonadministrative user. In addition, a com.ibm.wsspi.profile.WSProfileException or Access
is denied message occurs in the installation\_root\bin\ProfileManagement\pmt.bat file.
By default, nonadministrative users do not have access to the Program
Files directory, which is the default installation location
for the product. To resolve this issue, nonadministrative users must
either install the product by themselves or be given permission to
access the other product instances.

## Procedure

1. If you want to federate the node to a deployment
manager while creating the managed-node profile, start the deployment
manager.
2 Use one of the following methods tostart the Profile Management Tool.
    - Start the tool from the Quick Start console.
    - Click
Linux\_operating\_system\_menus\_to\_access\_programs > IBM >
your\_product > Profile Management Tool.
    - Run the command installation\_root/bin/ProfileManagement/pmt.sh.
3. On the Welcome page,
click Launch Profile Management Tool or select
the Profile Management Tool tab.
4. On the Profiles tab,
click Create.  The Environment
Selection  page opens in a separate window.
5. On the Environment Selection page,
locate the IBM Business Automation
Workflow configuration
and expand the section. Select the Business Automation Workflow managed
node profile template and click Next.
6 On the Profile Name and Location page,complete the following steps:

1. In the Profile name field, specify
a unique name or accept the default value.  Each profile
that you create must have a name. When you have more than one profile,
you can tell them apart at their highest level by this name.
2. In the Profile directory field,
enter the directory for the profile or use the Browse button
to go to the profile directory. The directory you specify
will contain the files that define the runtime environment, such as
commands, configuration files, and log files. The default directory
is installation\_root\profiles\profile\_name.
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
7 On the Node and Host Names page,complete the following actions for the profile you are creating: Click Next .

- In the Node name field, enter a name for
the node or accept the default value. Try keeping the node name as
short as possible, but ensure that node names are unique within your
deployment environment.
- In the Host name field, enter a name for
the host or accept the default value.

Click Next.

8 On the Federation page,choose to federate the node into the deployment manager now as partof the profile augmentation, or at a later time and apart from profileaugmentation. If you choose to federate thenode as part of the profile creation, specify the host name or IPaddress and SOAP port of the deployment manager, and an authenticationuser ID and password to be used to authenticate with the deploymentmanager. Important: Select Federate thisnode later if any one of the following situations is true: Note: Note the processing that is associated with federatingthe node as part of the managed-node profile creation: Click Next .

- Another profile is being federated. (Node federation must be serialized.)
- The deployment manager is not running or you are not sure if it
is running.
- The deployment manager has the SOAP connector disabled
- The deployment manager has not yet been augmented into a IBM Business Automation Workflow deployment
manager.
- The deployment manager is not at a release level the same or higher
than the release level of the profile you are creating.
- The deployment manager does not have a JMX administrative port
enabled.
- The deployment manager is re-configured to use the non-default
remote method invocation (RMI) as the preferred Java™ Management Extensions (JMX) connector.
(Select System administration > Deployment manager > Administration
services in the administrative console of
the deployment manager to verify the preferred connector type.)

- The Profile Management Tool verifies that the deployment manager
exists and can be contacted, and that the authentication user ID and
password are valid for that deployment manager (if it is secured).
- If you attempt to federate a custom node when the deployment manager
is not running or is not available for other reasons, a warning box
prevents you from continuing. If this warning box appears, click OK and
then make different selections on the Federation page.

Click Next.

9 On the Security Certificate (Part1) page, specify whether to create new certificates orimport existing certificates.

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
10 On the Security Certificate (Part2) page, verify that the certificate information is correct. If you create the certificates, you can use the default valuesor modify them to create new certificates. The default personal certificateis valid for one year by default and is signed by the root signingcertificate. The root signing certificate is a self-signed certificatethat is valid for 15 years by default. The default keystore passwordfor the root signing certificate is WebAS . Changethe password. The password cannot contain any double-byte characterset (DBCS) characters because certain keystore types, including PKCS12,do not support these characters. The keystore types that are supporteddepend on the providers in the java.security file. Whenyou create either or both certificates, or import either or both certificates,the keystore files that are created are: These files all have the same password when you create or importthe certificates, which is either the default password, or a passwordthat you specify. An imported certificate is added to the key.p12 fileor the root-key.p12 file. If you import any certificatesand the certificates do not contain the information that you want,click Back to import another certificate.

If you create the certificates, you can use the default values
or modify them to create new certificates. The default personal certificate
is valid for one year by default and is signed by the root signing
certificate. The root signing certificate is a self-signed certificate
that is valid for 15 years by default. The default keystore password
for the root signing certificate is WebAS. Change
the password. The password cannot contain any double-byte character
set (DBCS) characters because certain keystore types, including PKCS12,
do not support these characters. The keystore types that are supported
depend on the providers in the java.security file.

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
11. On the Profile Summary page,
review the information. Click Create to create
the profile or Back to change the characteristics
of the profile.
12. On the Profile Complete page,
review the information. To proceed to the Quick Start console, make
sure that Launch Quick Start console is selected
and click Finish.

## What to do next

After
you have finished adding managed-node profiles, configure the deployment
environment.