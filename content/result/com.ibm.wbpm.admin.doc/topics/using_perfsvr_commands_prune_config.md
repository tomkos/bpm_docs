# Updating the Performance Data Warehouse configuration file
(optional)

For information about updating the configuration file, see The 100Custom.xml file and configuration.

The configuration properties are located in the 00Static.xml file.
You copy those properties to the 100Custom.xml and
then make the updates in the 100Custom.xml file.

## Configuration properties

You can increase the number if the default value produces
unacceptable performance. However, if the value is set too high, the increased load on the
transaction log might result in errors.

If there is more pruning to be done, a request to run the
prune command again is placed on the queue. The Performance Data Warehouse is
then free to perform other tasks, such as processing tracking definition updates or transferring
data from the workflow server, while the prune command is on the queue.

For example, if the
prune-operation-time-box is set to 10800 (3 hours) and the
prune-operation-time-box-retry is set to 4, the prune
operation follows this sequence:

1. The request from the original perfDWTool call arrives on the queue. The request can be on the
queue three more times.
2. The operation times out.
3. The request is requeued. This is the second time on the queue.
4. The operation times out.
5. The request is requeued. This is the third time on the queue.
6. The operation times out.
7. The request is requeued. This is the fourth time on the queue. No more attempts are
allowed.
8. The operation times out and exits.

In this example, the prune operation runs for a total of 12 hours (the original call and the
three reattempts).

The retry value prevents the prune operation from running forever.

## Procedure

1. Stop the support cluster member or members.
2. Open the 00Static.xml file and the 100Custom.xml file
in a text editor. The files are in the following directory: dmgr\_profile\_name\config\cells\cell\_name\nodes\node\_name\servers\server\_name\performance-data-warehouse\config\
3. Locate the performance server properties section in the 00Static.xml file,
as shown in the following snippet from the file:
<properties>
   ...
   ... 
   <performance-server merge="mergeChildren">
      ...
      ...
      <prune-batch-size>50000</prune-batch-size> 
      ...
      ...
      <prune-operation-time-box>10800</prune-operation-time-box>
      ...
      ...
      <prune-operation-time-box-retry>4</prune-operation-time-box-retry>
      ...
      ... 
   </performance-server>
</properties>
4. Copy the entire <performance-server> section 
from the 00Static.xml file to the 100Custom.xml file,
and then close the 00Static.xml file.
5. In the 100Custom.xml file, update the property
or properties.
6. Save your changes.
7. Start the support cluster member or members.

## Example

- prune-batch-size (from the default of 50000 to
15000)
- prune-operation-time-box (from the default
of 10800 to 14400)
- prune-operation-time-box-retry (from the
default of 4 to 5)

1. Stop the support cluster member.
2. Locate the 00Static.xml and 100Custom.xml files
and open them in a text editor. In this example, the configuration
files are in the following directory: C:\IBM\WebSphere\AppServer\profiles\DmgrProfile\config\cells\PCCell1\nodes\Node1\servers\SingleClusterMember1\performance-data-warehouse\config\
3. Locate the performance server properties section
in the 00Static.xml file.
4. Copy the entire section (everything from <performance-server> to </performance-server>)
to the 100Custom.xml file.
5. Close the 00Static.xml file.
6. In the 100Custom.xml file, update the entries,
as shown in the following example: <properties>
   ...
   ... 
   <performance-server merge="mergeChildren">
      ...
      ...
      <prune-batch-size merge="replace">15000</prune-batch-size>
      ...
      ... 
      <prune-operation-time-box merge="replace">14400</prune-operation-time-box>
      ...
      ...
      <prune-operation-time-box-retry merge="replace">5</prune-operation-time-box-retry>
      ...
      ... 
      </performance-server>
   ...
   ... 
</properties>Notice that you must add merge="replace" to
the entries in addition to changing the value.
7. Save your changes.
8. Start the support cluster member.