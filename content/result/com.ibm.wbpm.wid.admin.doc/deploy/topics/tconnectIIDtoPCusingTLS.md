<!-- image -->

# Connecting Integration Designer to a server by using a
protocol other than TLSv1.2

IBM® Business Automation
Workflow 22.0.x uses the Transport Layer Security (TLS) SSL communication protocols v1.2 and v1.3. In
22.0.2,  the default protocol for IBM Integration
Designer changed to
TLSv1.2. To connect to Workflow Center or the unit test
environment (UTE) by using a different TLS protocol, you must set options in the <IID
install root>\eclipse.ini file.

For more information about Federal Information Processing Standard (FIPS) use and TLS settings,
see Transitioning WebSphere Application Server Full Profile to the
SP800-131 security standard; IBM
Rational® Application Developer and IBM WebSphere® Application
Server references are
comparable to Integration Designer
and the unit test environment (UTE).

## About this task

To connect to a server that is not using TLSv1.2, you must set options

## Procedure

1. Open the <IID install root>\eclipse.ini file in a text editor:
2. Add the following lines after -vmargs in this order. Note that the TLS
version must match what is supported by the server. 
However, 
-Dhttps.protocols=TLSv1.3
-Dcom.ibm.ssl.protocol=TLSv1.3
3. Restart Integration Designer.

1. Open the <IID install
root>runtimes\base\_stub\properties\ssl.client.props file in a text editor.
2. Find the line with com.ibm.ssl.protocol and change the property value to
TLSv1.3: com.ibm.ssl.protocol=TLSv1.3
3. Restart Integration Designer.