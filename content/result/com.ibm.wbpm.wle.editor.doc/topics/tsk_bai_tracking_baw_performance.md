# Disabling the emission of tracking data

## About this task

Follow this procedure to disable the emission of all tracking data. It prevents data from being
inserted in the Performance Data Warehouse tables.

## Procedure

1. Open each 100Custom.xml file in your topology, as described in the
topic. See Location
of 100Custom configuration files.
2. Edit the 100Custom.xml file to include a performance-server-communication element as a
child of the properties and common elements: 
<properties>
   <common>
     <performance-server-communication>
       <enabled merge="replace">false</enabled>
     </performance-server-communication>
   </common>
</properties>
3. Restart the environment.