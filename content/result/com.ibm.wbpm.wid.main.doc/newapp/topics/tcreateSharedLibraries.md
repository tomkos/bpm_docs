<!-- image -->

# Creating shared libraries

In IBM® Integration
Designer, you can share your
Java™ binaries, XML schemas, and WSDL definitions by using shared libraries (by-reference) for your
Service Component Architecture (SCA) modules and libraries.

## About this task

When using SCA or Java libraries, the default behavior is to share-by-copy so a copy of each
library is placed in each application EAR using them.

When using shared SCA or Java libraries, you are using by-reference sharing. The application EAR
contains only a reference to the libraries but doesn't include the actual library JAR files. The
shared libraries are deployed separately and can be used by multiple applications.

Depending on the size of the libraries, number of assets, and number of deployed modules, the
share-by-copy module can result in a larger memory footprint. Sharing these assets by-reference can
reduce this memory footprint.

When using shared libraries, you can get different classloading behaviors. See Managing WebSphere shared libraries in the WebSphere® Application
Server documentation for more details about the shared
library features.

- Considerations when using shared libraries

Take these tips into consideration when you use shared libraries.
- Creating shared libraries for Java projects

For Java content, use Java projects to share the content with your modules. If you are writing Java code, avoid having shared Java code and external jars in the same project. For shared external JARs, use a separate java project including all the jars for the application.
- Creating shared libraries for SCA projects

You use an SCA library project in IBM Integration Designer to create and share XML schemas and interface definitions between SCA modules.
- Associating shared libraries with projects

After you create a shared library, you can associate it with your SCA applications.