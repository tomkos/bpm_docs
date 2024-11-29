# Setting up Box collaboration

## Procedure

To set up Box collaboration:

1 Create a Box application for serverauthentication in the IBM® Business AutomationWorkflow environment.
    1. Go to https://developer.box.com/ and log in.
    2. In the My Applications window, click Create a Box Application.
    3. Select Enterprise Application as an application type.
    4. Select OAuth 2.0 with JWT (Server Authentication) as the authentication
method.
    5. In the Application Name field, enter the name of your IBM Business Automation
Workflow server and then click Create
Application.
    6. Click View Application and configure the following settings:

Setting
Value

Application Access
Enterprise

Application Scope
Leave the default settings

Advance Features
Generate User Access Token
    7. Click Save Application to save your changes.
2 Create a Box application for clientauthentication.

1. In the My Applications window, click Create a Box Application.
2. Select Enterprise Application as an application type.
3. Select Standard OAuth 2.0 (User Authentication) as the authentication
method.
4. In the Application Name field, enter the name of your IBM Business Automation
Workflow server and then click Create
Application.
5. Click Save Application to save your changes.
3 Authorize the Box application for IBM Business AutomationWorkflow to access your Box enterprise account.

1. Log in to your Box application as an administrative
user.
2. Click Admin Console, click the gear icon, and select Elite
Settings.
3. From the Account Info tab, record the value of the Enterprise
ID field. 
You must specify this value later when you run the Case configuration tool.
4. Select the Apps tab, go to the Custom
Applications section, and click Authorize New App. 
In the Api Key field, specify the client\_id
value that was displayed when you created the application and click Next.
Click Authorize.
4 Generate a JSON web token and Box server token. For moreinformation, see the Box documentation at https://developer.box.com/ .

1 Generate an RSA key pair.
    1. To generate the RSA key pair on a Windows system, download the Cygwin application and run the
following OpenSSL commands on the Cygwin terminal. Otherwise, enter the commands on a Linux
system.
    2. Generate a private key by running the following command at the command prompt: openssl
genrsa -aes256 -out private\_key.pem 2048. After you enter a passphrase, record the value
for use in the next step.
    3. Generate a private key in PKCS8 format by running the following command: openssl pkcs8
-topk8 -inform pem -in private\_key.pem -outform der -nocrypt -out private\_pkcs8.der.
Specify the passphrase that you used in the previous step.
    4. Generate a public key by running the following command: openssl rsa -pubout -in
private\_key.pem -out public\_key.pem
    5. Locate the generated key files. For example, look for the key files under your Cygwin
installation directory, such as in the
c:\cygwin64\home\LoginName directory.
2 Submit the public key:

1. Go to https://developer.box.com/ and log in.
2. Click the Edit Application button for your application.
3. In the Public Key Management section, click Add Public
Key. You might be prompted to enable two-factor authentication and be asked to give your
mobile phone number to receive a verification code. You can disable this two-factor authentication
feature after you submit the public key.
4. Copy your public key from your key file and paste it in the Public Key
field. Then, click Verify. After the key is verified, click
Save. Your public key and key ID are now displayed in the Public
Key Management section. Record the Key ID value. You must specify
this value later when you run the Case configuration tool.
5. Scroll down and click Save Application.
6. Disable two-factor authentication. Scroll back up, click the gear icon and select
Account Settings. Click the Security  tab and clear
the Login verification check box.
5 Configure a connection to the Box server inyour development and productions environments by using the Case configuration tool or Case administration client .

- In the Case configuration tool, run the Configure
Box Collaboration task and then run the Register
Project Area or Register Target Environment task. Tip: For new profiles, select the
Configure Box
collaboration option in the new profile wizard. For existing profiles, add the Configure
Box Collaboration task after the Register the
IBM Business Automation
Workflow Administration Client Plug-in task
but before the Register Project Area or Register Target Environment task.
- In the Case administration client, open a target object
store and click New Box
Connection.
6. Enable case types to support Box collaboration.
In Case Builder, edit each case type for which you want case
workers to be able to collaborate with external users in Box
and select Case workers can use Box to collaborate
with external users.
7. To use Box collaboration in existing
solutions that were created before Box
collaboration was enabled, see the topic Adding Box collaboration actions for existing solutions for information on editing the
solution in Case Builder.
 For solutions that are created after Box
collaboration was enabled, the Box collaboration
actions are displayed by default in the Documents view.
8 Optional: Enable additional Box integration features that you wantto use. Feature Procedure Box as an external repository Enable case types to support external documents. In Case Builder ,edit each case type for which you want users to be able to add documents or attachments fromBox to the case and select Allow documents andattachments from repositories other than the case management object stores . This optionis not required if you use Box only to share case documentsand task attachments that are in an IBMFileNet® Content Manager or IBM ContentManager repository. Sharing case documents and attachments

| Feature                                | Procedure                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Box as an external repository          | Enable case types to support external documents. In Case Builder, edit each case type for which you want users to be able to add documents or attachments from Box to the case and select Allow documents and attachments from repositories other than the case management object stores. This option is not required if you use Box only to share case documents and task attachments that are in an IBM FileNet® Content Manager or IBM Content Manager repository.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Sharing case documents and attachments | Manually set the Share administrator  field for the Box repository. In the IBM Content Navigator administration tool of the web client, click Repositories, select your Box repository, and set the Share administrator field. Enable the Box share option for your IBM Business Automation Workflow desktop and for each IBM FileNet Content Manager or IBM Content Manager repository that you want to share documents from: IBM Business Automation Workflow desktop   In the IBM Content Navigator administration tool, click Desktops and open your IBM Business Automation Workflow desktop. On the General tab, enable the Box share services option and select the Box repository for shared files.   IBM FileNet Content Manager or IBM Content Manager repository   In the IBM Content Navigator administration tool, click Repositories and open each IBM FileNet Content Manager or IBM Content Manager repository. On the Configuration Parameters tab, enable the Optional Features > Box share option.     If you want to share documents in existing solutions that were created before IBM Business Automation Workflow V5.2.1 Fix Pack 3, see the topic Adding Box Share menu actions for existing solutions. The Box Share and Delete Box Share menu actions are displayed by default in the Documents view. |

9. Deploy your solution.
10. Configure SSL on the application server for your solution to access Box. For more information,
see Configuring SSL for Box.