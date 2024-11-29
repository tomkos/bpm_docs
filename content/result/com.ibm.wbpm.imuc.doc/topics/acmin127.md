# Preparing to run the case configuration tasks for the production environment

## Before you begin

## Procedure

To configure the production environment:

1 Set the application server timeout values. Higher timeout values help avoid transaction timeoutissues when you run the configuration tool tasks or deploy case solutions.
    - Set timeout values to the following settings (examples for WebSphere® ApplicationServer V8.5.2):
        - Under Servers > ServerTypes > WebSphere application servers > Click on yourserver > Configuration tab > ContainerSettings > Container Services > Transactionservice , set the following timeout values:
            - Total transaction timeout
            - Client inactivity timeout
            - Maximum transaction timeout
    - Under Servers > Server
Types > WebSphere application servers > Click on your
server > Configuration tab > Container
Settings > Container Services > ORB
service, set Request timeout to at least 600 and
Locate request timeout to maximum 300.
    - Under Resources > JDBC > Data
sources >  [Content Engine or Case Manager data source
name] > Connection Pool properties, set
Connection timeout to at least 600.
    - Under Resources > JDBC > Data
sources >  [Content Engine or Case Manager XA data source
name] > Connection Pool properties, set
Connection timeout to at least 600.
2. Restart your entire environment.
3. Start the Case configuration tool.

On AIX, Linux®, or Linux for System z®
Change the directory to
install\_root/CaseManagement/configure and run the
./configmgr command.
On Windows
Change the directory to
install\_root\CaseManagement\configure and run
configmgr.exe.
4 Based on your current production environment, open and edit the predefined profile that islocated indmgr\_profile\_root /CaseManagement/DE\_name /profiles/ICM\_prod .

- Containers:  If you
connect to IBM Business Automation
Navigator in a
container, configure single sign-on (SSO) with the following UMS parameters:
UMS URL
Use the format
https://ums\_server:port. If you specify the
UMS URL, the connection to the Navigator server is first redirected to UMS and
then returned to the Navigator server after the authentication check. If you use LTPA single sign-on
(SSO), leave the UMS URL blank.
UMS user name
The user account that logs in to UMS, for example, umsadmin, otherwise a
placeholder user name.
UMS password
The password of the UMS server or a placeholder password. If you leave UMS
password blank, you are prompted to specify the password when you run the Case configuration tool tasks.
- Traditional:  If
you don't connect to IBM Business Automation
Navigator
in a container and don't configure SSO with UMS, keep the default values for UMS
URL, UMS user name, and UMS password.
5. Save the edited profile, and run the Case configuration tool tasks for the
production environment, as specified in the Running the configuration tasks topic.
6. Restart your entire environment, including Business Automation Workflow, Content Platform Engine, and IBM Content
Navigator.

- Configuring additional target environments

If you want to add new object stores to your production environment, you must also configure a complete target environment. The target environment includes creating the object store, creating a worfklow system, and running additional configuration tasks.