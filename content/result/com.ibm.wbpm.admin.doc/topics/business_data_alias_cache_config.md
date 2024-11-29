# Business data alias cache configuration

You use the TWSearch API and REST Search API to look up the alias
names or create saved searches with them. The list of alias names
that is available to create saved searches or the aliases that are
visible to these APIs are determined by what is contained in the business
data alias cache. By default, the cache is populated at server start-up
by a search on all processes for possible aliases.

The number of processes and snapshots in the repository affects
how long it takes to initialize the cache because all processes are
retrieved from the database. Depending on the size of the data or
the speed of the database connection, the cache could take several
minutes to load. While the cache is loading, other server functions
must wait to access it. Building the cache also blocks server functions
that try to update process models, which affects IBM® Process
Designer.
For example, when the cache building operation is running, some Process
Admin Console pages might become unresponsive. This can result in
a delay in saving data in Process Designer and
you might receive a timeout error. To optimize performance or to improve
the server start-up time, change the business data alias cache configuration
to receive the business data aliases for only the aliases that have
associated instances. Configuring the cache in this way eliminates
the need to search all processes and only loads aliases used in existing
process instance data.

You might want to change the cache refresh interval
when the number of instances in the system is small or when instances
start and are deleted before the cache is refreshed. This property
should have a shorter value in a Workflow Center than
in a Workflow Server because Workflow Center instances
tend to have fewer process instances running and the processes change
much more frequently.

## Changing the configuration in the 100Custom.xml configuration
file

1. Open the 100Custom.xml file for each application
cluster member server, which is located in the following directory: dmgr\_profile\_root\config\cells\cellname\nodes\nodename\servers\servername\server\_type\config\100Custom.xml.
2. Copy the following XML to 100Custom.xml under
the <properties> tag.<server>
     <portal merge="mergeChildren">
          <use-business-aliases-for-process-instances merge="replace">true</use-business-aliases-for-process-instances>
          <init-bdac-on-startup merge="replace">true</init-bdac-on-startup>
     </portal>
     <repository merge="mergeChildren">
          <bdac-refresh-interval merge="replace">1800</bdac-refresh-interval>
     </repository>
</server>
3. Make the changes to the property values as required and save the
file.
4. Confirm that the changes are carried to the nodes by doing a full
node synchronization and then restarting the application cluster.
5. Verify that the changes are correct in the TeamWorksConfiguration.running.xml file
located here: node\_profile\_root\config\cells\cellname\nodes\nodename\servers\servername\server\_type. If
you find an issue, then open the 100Custom.xml file
in a browser to ensure that there are no special characters or syntax
mistakes.