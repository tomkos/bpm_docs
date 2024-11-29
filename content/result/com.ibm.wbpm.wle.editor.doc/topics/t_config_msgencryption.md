# Setting up message-level encryption

## Before you begin

- Add a web service server
- Creating an inbound web service.

Alternately, you can configure a specific encryption using
the 100Custom.xml file as shown in this topic.
First, check that the 100Custom.xml file exists.
See The 100Custom.xml file and configuration.

## About this task

```
<server>
	<webservice-security merge="mergeChildren">
		<keystore-file merge="replace">teamworks.jks</keystore-file>
		<keystore-password-encrypted>password</keystore-password-encrypted>
		<private-key>
			<alias>soaprequester</alias>
			<keyname>soaprequester</keyname>
			<password-encrypted>password</password-encrypted>
		</private-key>

		<private-key>
			<alias>soapprovider</alias>
			<keyname>soapprovider</keyname>
		</private-key>
		<keystore-type>JKS</keystore-type>
		<certificate>path to client certificate</certificate>
</webservice-security>
</server>
```

| Element name                  | Description                                                                                                                                                                                                                                                                                                                                                                         | Example                                              |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <keystore-file>               | Provide a name for the key store file related to the service requester.                                                                                                                                                                                                                                                                                                             | profile\_root/etc/ws-security/dsig-sender.jks         |
| <keystore-password-encrypted> | Provide a key store password for the service requester.                                                                                                                                                                                                                                                                                                                             |                                                      |
| <private\_key>                 | Holds an element that contains information about the private key for the client. This element has two child elements.                                                                                                                                                                                                                                                               |                                                      |
| <alias>                       | Alias for the private key specified during creating of the key store.                                                                                                                                                                                                                                                                                                               |                                                      |
| <keyname>                     | Holds the key name for the alias. If this element is not present, specify the alias name as the key name.                                                                                                                                                                                                                                                                           | KeyName : CN="Bob", OU=IBM, O=US,.. or KeyName : Bob |
| <password-encrypted>          | Provide the encrypted key password for accessing the client private key.                                                                                                                                                                                                                                                                                                            |                                                      |
| <keystore-type>               | Provide the key store type. This element can have one of the following values: JKS Use this value if the keystore uses Java Keystore format. JCEKS Use this value if the Java Cryptography Extension is configured in the application server.  PKCS12KS (PKCS12) Use this value if the keystore file uses the PKCS#12 file format.   If a type is not provided, the default is JKS. | keystore-type="JKS"                                  |
| <certificate>                 | Provide the client certificate path including the certificate file name.                                                                                                                                                                                                                                                                                                            | {Install-Location}\client.cert                       |

## Procedure

1. Stop the deployment manager, workflow server, and Workflow Center server if they are running.
2. Open the 100Custom.xml file in a text
editor.
3. Uncomment the <server> section,
and specify the encryption settings.
4. Specify the encryption settings.
5. Start the workflow server or the Workflow Center server.

## Results

## What to do next