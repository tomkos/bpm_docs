# Specifying an absolute URL for the TWManagedFile JavaScript
API

## About this task

```
tw.system.model.findManagedFileByPath('myimage.png', TWManagedFile.Types.Web).url;
```

By
default, a relative URL is retrieved for the .url property of the TWManagedFile
JavaScript API. The URL is relative to the Teamworks webapp context root.
However, you can retrieve an absolute URL instead by adding the
use-managed-asset-full-url configuration setting in the
100Custom.xml file. For detailed information about using configuration settings
in the 100Custom.xml file, see The 100Custom.xml file and configuration.

## Procedure

To add and enable the use-managed-asset-full-url configuration
setting in the 100Custom.xml file, complete the
following steps:

1. Stop the playback or workflow server.
2. Open each 100Custom.xml file. For information about the individual
100Custom.xml files that need to be updated and their locations, see Location of 100Custom configuration files.
3. In each 100Custom.xml file, add the use-managed-asset-full-url setting
and associated elements under the <properties> element,
as shown in the following example: <properties>
   <server>
      <managed-asset-config>
         <use-managed-asset-full-url>true
         </use-managed-asset-full-url>
      </managed-asset-config>
   </server>
</properties>(If you later decide that you want to
use a relative URL instead of an absolute URL, change the value to false.)
4. In each 100Custom.xml file, save your
changes.
5. In a browser, open each 100Custom.xml file
to ensure that it contains no special characters.
6 Complete one of the following steps:
    - In a clustered environment, ensure that the changes are propagated
to the nodes by forcing a synchronization and restarting the deployment
environment.
    - In a stand-alone server environment, restart the server.