# Optimizing Performance Data Warehouse

## About this task

You can make changes to the property file for Performance Data Warehouse to reduce the number of
rows in tables.

## Procedure

1 Disable the emission of timing intervals. The use of timing intervals in a businessprocess may emit a lot a data and provoke the insertion of a high number of rows in the PerformanceData Warehouse tables. If timing intervals are not needed in Performance Data Warehouse, you candisable their emission:
    1. Open each 100Custom.xml file in your topology, as described in Location of 100Custom configuration
files.
    2. Edit each 100Custom.xml file and make the indicated
edits.<performance-server>
   <emit-timing-intervals merge="replace">false</emit-timing-intervals>
</performance-server>
    3. Restart the environment.
2 Disable the insertion of the Optimizer data. The data used by the Optimizer(deprecated) are stored in the Performance Data Warehouse LSW\_OPTIMIZER\_DATA table that can contain a large number of rows. If the Optimizer is not used in desktop IBM ProcessDesigner you can disable its insertion:

1. Open each 100Custom.xml file in your topology, as described in Location of 100Custom configuration
files.
2. Edit each 100Custom.xml file and make the indicated
edits.<performance-server>
   <insert-optimizer-data merge="replace">false</insert-optimizer-data>
</performance-server>
3. Restart the environment.
3 Disable the insertion of tracking data for services. By default, services always create Performance Data Warehouse tracking records in theLSW\_TASK table when they run. You can disable the insertion of these records:

1. Open each 100Custom.xml file in your topology, as described in Location of 100Custom configuration
files.
2. Edit each 100Custom.xml file and make the indicated edits in the <server>
section:<server>
     <service-tracking-enabled merge="replace">false</service-tracking-enabled>
</server>
3. Restart the environment.