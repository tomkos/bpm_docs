# Examples: Using the PALService MBean for administrative tasks

```
profile\_root/bin/wsadmin.sh -lang jython -username username -password password
```

There
are several things that you need to know to help you specify the correct syntax for the MBeans
version of the BPMProcessInstancesPurge command. For instance, the command only
accepts the following four data types:

- String java.lang.String
- String array [Ljava.lang.String;
- Boolean java.lang.Boolean (which requires an indirection through a variable
rather than specifying the raw value of true or
false)
- A null value that is represented as a None parameter.

Also, if the endedBefore or endedAfter parameter
is specified and the instance status is set to ALL (instst = [
"ALL" ]), there may be unexpected results because only process instances that are in the
COMPLETED or TERMINATED state can have an end date.
Process instances that are in a different state cannot be purged because they do not fulfill the
time condition.

## Example: Deleting process instances based on instance
IDs

```
import javax.management as mgmt
import java.lang.String
import jarray

mbean = AdminControl.completeObjectName( "type=PALService,node=nodename1,process=server1,*" )

acro = "MBD"

snapshotslist = ["SS0"]
ssarray = jarray.array( snapshotslist, java.lang.String )

instst =[ "ALL"]
statuses = jarray.array( instst, java.lang.String )

instanceIDs = ["841","842"]
instances = jarray.array( instanceIDs, java.lang.String )

force = java.lang.Boolean( "true" )
AdminControl.invoke\_jmx ( mgmt.ObjectName(mbean), "processInstancesPurge", [acro, ssarray, statuses, instances, None, None, "C:/Temp/output.txt", None, None, force, ], ["java.lang.String", "[Ljava.lang.String;", "[Ljava.lang.String;", "[Ljava.lang.String;", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.Boolean"] )
```

## Example: Deleting process instances that occur during
a specific time range

```
import javax.management as mgmt
import java.lang.String
import jarray

mbean = AdminControl.completeObjectName( "type=PALService,node=nodename1,process=server1,*" )

acro = "MBD"

instst =["All"]
statuses = jarray.array( instst, java.lang.String )

force = java.lang.Boolean( "true" )

endedAfter  = "2018-09-14T10:00:00"
endedBefore = "2018-09-14T11:55:00"

AdminControl.invoke\_jmx ( mgmt.ObjectName(mbean), "processInstancesPurge", [acro, None, statuses, None, endedAfter, endedBefore, "C:/Temp/output.txt", None, None, force ], ["java.lang.String", "[Ljava.lang.String;", "[Ljava.lang.String;", "[Ljava.lang.String;", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.Boolean"] )
```

## Example: Deleting process instances that occur before
a specified local time on the server

```
import javax.management as mgmt
import java.lang.String
import jarray

mbean = AdminControl.completeObjectName( "type=PALService,node=nodename1,process=server1,*" )

acro = "MBD"

instst =["All"]
statuses = jarray.array( instst, java.lang.String )

force = java.lang.Boolean( "true" )

endedBefore = "2018-09-13T09:23:00"

AdminControl.invoke\_jmx ( mgmt.ObjectName(mbean), "processInstancesPurge", [acro, None, statuses, None, None, endedBefore, "C:/Temp/output.txt", None, None, force ], ["java.lang.String", "[Ljava.lang.String;", "[Ljava.lang.String;", "[Ljava.lang.String;", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.Boolean"] )
```

## Example: Deleting process instances that occur after
a specified local time on the server

```
import javax.management as mgmt
import java.lang.String
import jarray

mbean = AdminControl.completeObjectName( "type=PALService,node=nodename1,process=server1,*" )

acro = "MBD"

instst =["All"]
statuses = jarray.array( instst, java.lang.String )

endedAfter = "2018-09-13T09:13:10"

force = java.lang.Boolean( "true" )

AdminControl.invoke\_jmx ( mgmt.ObjectName(mbean), "processInstancesPurge", [acro, None, statuses, None, endedAfter, None, "C:/Temp/output.txt", None, None, force ], ["java.lang.String", "[Ljava.lang.String;", "[Ljava.lang.String;", "[Ljava.lang.String;", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.Boolean"] )
```

## Example: Deleting process instances that occur during
a time range and that are based on instance IDs

```
import javax.management as mgmt
import java.lang.String
import jarray

mbean = AdminControl.completeObjectName( "type=PALService,node=nodename1,process=server1,*" )

acro = "MBD"

instst =["All"]
statuses = jarray.array( instst, java.lang.String )

instanceIDs = ["835","836"]
instances = jarray.array( instanceIDs, java.lang.String )

endedBefore = "2018-09-14T09:20:00"
endedAfter  = "2018-09-14T08:00:00"

force = java.lang.Boolean( "true" )

AdminControl.invoke\_jmx ( mgmt.ObjectName(mbean), "processInstancesPurge", [acro, None, statuses, instances, endedAfter, endedBefore, "C:/Temp/output.txt", None, None, force ], ["java.lang.String", "[Ljava.lang.String;", "[Ljava.lang.String;", "[Ljava.lang.String;", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.Boolean"] )
```

## Example: Deleting process instances that occur before
a specified local time on the server and that are based on instance
IDs

```
import javax.management as mgmt
import java.lang.String
import jarray

mbean = AdminControl.completeObjectName( "type=PALService,node=nodename1,process=server1,*" )

acro = "MBD"

instst =["All"]
statuses = jarray.array( instst, java.lang.String )

instanceIDs = ["834","837"]
instances = jarray.array( instanceIDs, java.lang.String )

endedBefore = "2018-09-14T09:30:00"

force = java.lang.Boolean( "true" )

AdminControl.invoke\_jmx ( mgmt.ObjectName(mbean), "processInstancesPurge", [acro, None, statuses, instances,  None, endedBefore, "C:/Temp/output.txt", None, None, force ], ["java.lang.String", "[Ljava.lang.String;", "[Ljava.lang.String;", "[Ljava.lang.String;", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.Boolean"] )
```

## Example: Deleting process instances that occur after
a specified local time on the server and that are based on instance
IDs

```
import javax.management as mgmt
import java.lang.String
import jarray

mbean = AdminControl.completeObjectName( "type=PALService,node=nodename1,process=server1,*" )

acro = "MBD"

instst =["All"]
statuses = jarray.array( instst, java.lang.String )

instanceIDs = ["839","840"]
instances = jarray.array( instanceIDs, java.lang.String )

endedAfter = "2018-09-14T09:30:00"

force = java.lang.Boolean( "true" )

AdminControl.invoke\_jmx ( mgmt.ObjectName(mbean), "processInstancesPurge", [acro, None, statuses, instances, endedAfter, None, "C:/Temp/output.txt", None, None, force ], ["java.lang.String", "[Ljava.lang.String;", "[Ljava.lang.String;", "[Ljava.lang.String;", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.Boolean"] )
```