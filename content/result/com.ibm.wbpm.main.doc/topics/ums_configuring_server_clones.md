# Creating User Management Service server
clones

1. The quickest and most reliable way to create server clones on
the same machine is to create copies of a server subdirectory after
the server was started at least once with basic configuration, for
example, copying the contents of wlp/usr/servers/ums to wlp/usr/servers/ums2.
This will contain the generated SSL certificate and LTPA key, however,
this approach requires re-sharing the keys when they are regenerated.
2. After copying a server configuration, you must customize the values
that are specified for http\_port and https\_port in wlp/usr/servers/serverName/configDropins/overrides/umsVariables.xml because
different server instances on a single machine cannot listen on the
same port.Alternative: For each required
clone, you could perform Creating a User Management Service server instance then Specifying basic User Management Service configuration settings.
3. Make sure that all server instances have an identical user registry
configuration. Alternative: An alternative
way of sharing configuration is to store shared configuration files
in wlp/usr/shared/config and refer to the ${shared.config.dir} from
within each server’s configuration. For more information, see Liberty: Directory locations and properties and Using include elements in configuration files.
Ensure that each server clone listens to a different port by keeping
this configuration information in an XML file that is not shared.
4. All User Management Service servers
must share the same LTPA key, which by default is stored in generated
keystore in wlp/usr/serverName/resources/security/ltpa.keys. Tip: An easy way for sharing LTPA keys is described in Configuring LTPA in Liberty. You can point
to a shared LTPA key file in ${shared.resource.dir} from
the keysFileName of a new ltpa configuration
element, as detailed in Liberty: Directory locations and properties.

Next, perform Configuring a web server.