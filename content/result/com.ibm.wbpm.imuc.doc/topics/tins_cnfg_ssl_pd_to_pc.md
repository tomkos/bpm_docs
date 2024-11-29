# Changing the Secure Socket Layer (SSL) configuration for desktop Process Designer to access Workflow Center
(deprecated)

## Procedure

To change the SSL configuration for desktop Process Designer to access Workflow Center, complete the following steps:

1. In the pd\_install\_root/eclipse.ini file, specify the
correct Workflow Center URL for the
-Dcom.ibm.bpm.processcenter.url property.
This setting is based on what is returned by the EXTERNAL\_CLIENT endpoint (or PROCESS\_CENTER
endpoint, if it is set) when you download the desktop Process Designer installer.This property value must
always match your endpoint settings. If you change the related endpoint setting, then you must
manually update the property value for any clients that you already installed.
For more
information about desktop Process Designer
communications, see Connections from Process Designer to Process
Center.
For more information about setting the external client endpoint, see Customizing Business Automation Workflow to work with a web server.
2. Optional: 
Review the desktop Process Designer SSL settings
in pd\_install\_root/resources/ssl.client.props. The
pd\_install\_root variable represents the desktop Process Designer installation directory, for example,
C:/IBM/ProcessDesigner.
This file enables SSL by default for the desktop Process Designer Java virtual machine (JVM) and
pre-populates it with various default settings such
as:com.ibm.ssl.protocol=SSL\_TLSv2
com.ibm.ssl.securityLevel=HIGH
com.ibm.ssl.trustStore=etc/trust.p12See
the file for the full set of defaults. The default settings can be modified only after the desktop Process Designer client is installed. For more
information about this file, see ssl.client.props client configuration file.
3 Review and update the default or custom truststores as per your configuration. In addition to the ssl.client.props file, the following truststore-relatedeclipse.ini properties are always set when desktop Process Designer isinstalled:-Djavax.net.ssl.trustStoreType=PKCS12-Djavax.net.ssl.trustStore=./etc/trust.p12-Djavax.net.ssl.trustStorePassword=WebAS
    - The desktop Process Designer truststore mustinclude the correct signer certificates to work with Workflow Center , online Workflow Server , or any intermediate servers that desktop Process Designer connects to. The default truststore included with the desktop Process Designer installer is based on the followingtruststore from Workflow Center : You can work with the contents of this truststore in the WebSphere® ApplicationServer administrative console under Global Security > SSL certificate and key management > Key stores and certificates .

The desktop Process Designer truststore must
include the correct signer certificates to work with Workflow Center, online Workflow Server, or any intermediate servers that desktop Process Designer connects to.

        - Stand-alone configuration: NodeDefaultTrustStore
        - Network deployment configuration: CellDefaultTrustStore

You can work with the contents of this truststore in the WebSphere® Application
Server administrative console under Global Security >  SSL certificate and key management >  Key stores and certificates.

- If you created and configured your own truststore, include it with thedesktop Process Designer download package instead ofthe Workflow Center truststore.
    - Name the custom truststore trust.p12. It must be of type
PKCS12 with the password WebAS.
    - Add the truststore under
bpm\_install\_root/BPM/Lombardi/tools/designer/trust.

```
-Djavax.net.ssl.trustStoreType=PKCS12
-Djavax.net.ssl.trustStore=./etc/trust.p12
-Djavax.net.ssl.trustStorePassword=WebAS
```

4 Verify your configuration.

1. Log in to desktop Process Designer.
2. Right-click the Process Apps tab
and select Properties.
3. Confirm that the Address: (URL) section contains the expected URL that
matches the URL in the eclipse.ini file.

## Related information

- Troubleshooting and support for IBM Business Automation Workflow
- How do I update Process Designer so that it only uses the TLS 1.2 protocol?