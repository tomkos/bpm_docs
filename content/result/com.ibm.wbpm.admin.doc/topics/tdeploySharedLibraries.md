<!-- image -->

# Deploying shared libraries

## Before you begin

## Procedure

1. Create a directory to contain the necessary shared libraries. You can use one directory to
contain all libraries or multiple if you want to break up which libraries are in which scope. It is
recommended to keep the files in the config directory to make sure they are synchronized with the
cluster members. For example this path:
<DMgr Profile>/config/cells/<cell name>/clusters/<cluster\_name>/<shared
lib directory>.Note: Avoid having your share libraries in other locations (like /lib/ext/)
for the cluster members.
2. Create an environment variable for the shared library path at the cluster scope, which you can
find in the administrative console under Environment > WebSphere Variables, for example SHARED\_LIB\_PATH with a value of
${USER\_INSTALL\_ROOT}/config/cells/<cell\_name>/clusters/<cluster\_name>/<shared lib
directory>. 

Note: Using this structure ensures the path is correct on each cluster member.
3. Create the shared library at the cluster scope by using the variable for the class path, which
you can find in the WebSphere administrative console under Environment > Shared libraries. 
For more information, see  Creating shared libraries in the
WebSphere® Application
Server documentation.
4 Choose whether you will be associating your shared library with the server classloader or theclassloader for your applications.
    - Add the shared library to each application cluster member server: For more information, see Associating shared libraries withservers in the WebSphere ApplicationServer documentation.
        1. Create a class loader for the server by selecting Servers > Server Types > WebSphere application servers > server\_name > Java and Process Management > Class loader.
        2. Add the shared library to the classloader which you have created.
- Add the shared library to each application. With this method you will be mapping the shared
library to specific application modules either during deployment or after deployment. For more
information, see Associating shared libraries with
applications or modules in the WebSphere Application
Server
documentation.
5 After creating the shared library or when you must modify the files in the shared library,perform these steps:

1. Add the necessary library files to the shared directory in the deployment manager
configuration.
2. Perform a full node synchronization so the files are propagated to all the nodes.
3. Restart the cluster members to pickup the changes.

## What to do next