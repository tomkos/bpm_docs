# Configuring proxy settings

## About this task

| Setting            | Required or Optional   | Description                                                                                                                                                                                                                            |
|--------------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| host               | Required               | IP address or host name of the proxy server.                                                                                                                                                                                           |
| port               | Required               | Port number that is used by the proxy server for client connections.                                                                                                                                                                   |
| user-name          | Optional               | User name used by the proxy server for client connections.                                                                                                                                                                             |
| password           | Optional               | Password used by the proxy server for client connections.                                                                                                                                                                              |
| password-encrypted | Optional               | Encryption status for the password. The value is true if the password is encrypted; otherwise, the value is false. For more information, see the topic Enabling encrypted passwords in proxy settings.                                 |
| excluded-hosts     | Optional               | IP addresses or host names of any hosts for which proxy settings should not be applied. localhost , 127.0.0.1 , and 0:0:0:0:0:0:0:1 are excluded by default. Use a comma-separated string of IP addresses to exclude additional hosts. |
| proxy-auth-alias   | Optional               | Name of a Java Authentication and Authorization Service (JAAS) authentication alias containing the user and password information.                                                                                                      |

```
<server>
    <connection merge="replace">
        <proxy-settings>
            <host>myproxy.com</host>
            <port></port>
            <proxy-auth-alias>ProxyAuthAlias</proxy-auth-alias>
            <excluded-hosts></excluded-hosts>
        </proxy-settings>
    </connection>
</server>
```

```
<server>
    <connection merge="replace">
        <proxy-settings protocol="http">
            <host></host>
            <port></port>
            <user-name></user-name>
            <password></password>
            <password-encrypted></password-encrypted>
            <excluded-hosts></excluded-hosts>
        </proxy-settings>
        <proxy-settings protocol="https">
            <host></host>
            <port></port>
            <user-name></user-name>
            <password></password>
            <password-encrypted></password-encrypted>
            <excluded-hosts></excluded-hosts>
        </proxy-settings>
    </connection>
</server>
```

For information about the 100Custom.xml file's location, and how to create,
modify, and deploy it, see The 100Custom.xml file and configuration.

- Encrypting passwords for proxy settings

 Traditional: 
 If you need to encrypt passwords for use in proxy settings, you can use the Business Automation Workflow EncryptPassword utility.