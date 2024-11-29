# Enabling custom password encryption

## Procedure

1. Immediately after you install the new version of IBM Business Automation Workflow, copy the custom encryption JAR file to
install\_root\_24.x/lib/ext.
2 Before you run BPMConfig -create -de to create the deployment environment,enable the command script to support custom encryption.
    1. From install\_root\_24.x/bin on all Business Automation Workflow
24.x installations,
including the deployment manager and all nodes, open BPMConfig.bat for Windows
or BPMConfig.sh for Linux or UNIX.
    2. Find the Enabling custom password encryption comment block. Read the comments and then
uncomment the lines to enable custom password encryption.
    3. Set a WebSphere property to point to your encryption implementation class, by changing the
value of the com.ibm.wsspi.security.crypto.customPasswordEncryptionClass
property to the name of your encryption implementation class.
    4. Set any further properties that your encryption implementation class needs, by adding
-Dkey=value for any further properties. 
If the custom password encryption class has additional properties and you want them to be
handled automatically, the properties must be prefixed by the package name of the custom encryption
class. 
For example, if the class is
com.ibm.wsspi.security.crypto.customPasswordEncryptionClass=com.acme.crypto.CustomPwEncryption
then the properties would be named
com.acme.crypto.keystore=${WAS\_INSTALL\_ROOT}/acme/crypto.jceks
com.acme.crypto.certalias=BPMRestriction: If the additional properties do not follow this naming convention, the properties
cannot be recognized as belonging to custom password encryption and you must add them manually as
Java system properties for the WebSphere JVMs.

## Related information

- Enabling custom password encryption