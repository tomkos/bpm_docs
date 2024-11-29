# Installing the User Management Service

The User Management Service is delivered as an optional product extension on Liberty in a self-extracting JAR file, as
described in Installing Liberty by extracting a Java archive file.

You can either install the User Management Service on one (or
more) dedicated hosts, or it can be collocated with other IBM Business Automation Workflow runtime
components.

1. Ensure that your environment conforms to the supported platforms.
2. If you do not have Java 17, download IBM JDK 17 for Java 17 from IBM Semeru Runtimes Downloads.
3. Ensure that your JAVA\_HOME and PATH environment variables are
set to point to your Java 17 installation, as described in Installing Liberty by extracting a Java archive file.
4. Create a directory for your User Management Service installation,
for example on Windows, you might choose to create C:\ums.
5. Copy the Archive Install file into your newly created directory
and run the install by invoking the following command: java -jar ums-install-VersionNumber.jarWhere VersionNumber is
the version number, for example, 1.0.0.0Tip: For
a list of additional options, see Java archive file extraction options.
6. Archive Install will display the license agreement, license information,
and prompt you for your agreement. You will then be able to provide
a target installation directory. If you do not specify a target directory,
the installer extracts all files into a subdirectory wlp (
WebSphere
 Liberty Profile)
relative to your current working directory.
7 Check whether updates are available for the Liberty server:
    1. Display the User Management Service product
information by changing to the server's wlp\bin directory,
and running the command:productInfo versionThe Liberty version
that the installed User Management Service is
using is the product version that is listed for the WebShphere
Application Server .
    2. Check if there is a newer fix pack by checking the support page: Latest fix packs for WebSphere
Application Server, if so, install the latest fix pack.

- Installing User Management Service iFixes

 Traditional: 
 User Management Service interim fixes are cumulative ifixes that contain all previous User Management Service fixes and replace all User Management Service specific files in the /wlp/ibmUserManagement directory.