<!-- image -->

# Deploying Advanced applications that use shared libraries

## Before you begin

## Procedure

1. Place all required shared library files for the application in the
/lib/ext/ directory of the deployment manager's installation.

Note: This step is required because you can't associate the shared library with the deployment
manager. In some scenarios, the files would be required during the installation for validation or
generation of application content.
2. Restart the deployment manager to pick up the changes to /lib/ext/.
3. Deploy the application as you normally would.
4. If you are using application scoped shared libraries, you would associate the required shared
libraries with the application either during the install or after the app is installed. For more
information, see  Associating shared libraries with
applications or modules in the WebSphere® Application
Server
documentation.
5. Remove the shared library files from /lib/ext/. Optionally, restart the deployment manager if
you want to pick up the classloader changes right away.

Note: This is a good practice to ensure that you don't accidentally leave an old version of a
.jar file, to avoid issues if there are conflicting jars among your
applications, or to avoid issues with cluster members if they shared the same installation.