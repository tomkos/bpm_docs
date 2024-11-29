# Configuring a key for credential encryption

## About this task

```
<common>
   <security>
      <cipher-pass-passphrase merge="replace">key\_value</cipher-pass-passphrase>
   </security>
</common>
```

For information about the individual 100Custom.xml files that need to be
updated and their locations, see the topic Location of 100Custom configuration files.

However, to consistently and reliably change the value of the setting in all of the
100Custom.xml files in your Business Automation Workflow deployment environment, it is recommended that
you use the updateBPMConfig command as described in the following procedure:

## Procedure

Traditional:  Perform the following
steps.

1. Stop the servers for Workflow Server and
Workflow Center.
2. Start the scripting client in disconnected mode as described in the topic updateBPMConfig command.
3. Run the following commands to simultaneously update all affected servers:

wsadmin -connType none -lang jython
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/common' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/common/security' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/common/security/cipher-pass-passphrase', '-xNodeValue', 'key\_value' ] )
wsadmin> AdminConfig.save()
4. Restart the servers.

## Results

The recommended way of updating the 100Custom.xml files is by running the
updateBPMConfig command. However, if the updates are unsuccessful, you can
manually update the files by following the steps in the topic Creating a 100Custom.xml configuration file.

- The password in a REST server, see Specifying a REST server.
- The passwords in the binding of an external service of type REST, see Invoking a REST service.

Traditional:  These
passwords are encoded using the WebSphere® Application
Server mechanism. You should
store your credentials in an authentication alias and reference it using invocation credentials. To
encrypt passwords in an authentication alias that you can use AES encryption, as described in Enabling AES password encryption for the server environment, or use a custom
password encryption, as described in Implementing custom password encryption and Enabling custom password encryption.

Containers:  These passwords are
encoded using the WebSphere Application
Server
mechanism. You should store your credentials in an authentication alias and reference it using
invocation credentials.

Setting a custom encryption key in Workflow Center applies to encrypting
credentials in the database and encrypting credentials in exported applications in both
.twx for exchange between multiple Workflow Center servers, and
.zip format for offline installation on Workflow Server.

If you need other servers to successfully decrypt credentials in these exported applications, you
must set the same encryption key for all of the servers.

Configuring unique keys per environment is more secure as you avoid exchanging keys. Sharing keys
is typically not required because you would not want to enter your production credentials into the
development system. You can deploy your app snapshot and then set your credentials in the target
environment. In many environments, such as the runtime environment, you need to periodically update
the credentials for backend access. Specifying production credentials in Workflow Center adds another place
that becomes out-of-sync. Setting credentials uses the target environment's key.

When you decide to change the key in any environment, this environment is no longer able to
decrypt credentials stored in its own database. Use Process Admin Console or a REST API to
set these credentials for deployed applications.