# Extending the maximum number of characters in tracked performance
data

## Procedure

1. Open the 00Static.xml file in a text
editor. See the topic Location of 100Custom configuration files for the location of
the 00Static.xml file.
2. Copy the following property: <max-length-of-string-columns>64</max-length-of-string-columns>
3. Open each 100Custom.xml file in your
topology, as described in the topic Location of 100Custom configuration files.
4. Paste the following property into each 100Custom.xml file
from the 00Static.xml and make the indicated
edits. <performance-server>
   <max-length-of-string-columns merge="replace">200</max-length-of-string-columns>
</performance-server>Note: You need to make this change
globally in the Performance Data Warehouse because the server does
not have field- or group-level specificity for the maximum string
length setting. Although you can use a larger string length for a
field, you should be somewhat conservative and apply this setting
across the board.
5 In the performance database, change the size of the followingfields depending on the value of the max-length-of-string-columns property. The size varies depending on the database management systemand the encoding. For some database management systems, the fieldscan have the same value as the max-length-of-string-columns property.However, for DB2 and UTF-8 encoding, multiply the string size by 4to get the size of the fields in the performance database. Important: Ifyou change the size of the tracking group fields, you still need toapply the change for the maximum string length to the PerformanceData Warehouse configuration in order for Business Automation Workflow to writedata larger than the default maximum string length. Anything largerthan the default maximum string length value will go into the errorslist in the Performance Admin Console. If you increase the maximumstring length value but do not increase the size of the other stringfields, the amount of data written could exceed the capacity of thesefields.
    1. Change the column width of all tracking group fields
in the TG\_* tables that are VARCHAR parameters.
    2. Change the column width of the STRING\_VALUE column
in the LSW\_OPTIMIZER\_DATA table.
    3. On DB2, drop the STRING\_VALUE constraint from the
LSW\_OPTIMIZER\_DATA table.
6. After changing the TG\_* tables, update
the tracking definitions to re-create the corresponding views.
7. Restart the Performance Data Warehouse.

## Results

```
2007-08-08 18:05:26,156 [DataTransfer Thread #2] ERROR com.lombardisoftware.server.ejb.tracking.APIServicesBean - Exception in EJB call com.lombardisoftware.core.TeamWorksException: (PFS-0062) The tracked field with external ID t193b943b74411 has a value that is 96 characters long. The maximum is 64. ...
```