# Viewing data in a
data store

## Before you begin

## About this task

Volatile data is lost when
a messaging engine stops, in either
a controlled or an uncontrolled manner. Durable data is available
after the
server restarts.

In some cases, you might want to view the data
in a
data store; for example, to examine the messages being processed by
the messaging
engine.

You can use the database tools for the data store to
view data
in the data store for a messaging engine. For example, if the messaging
engine
uses the embedded Derby database, you can use the ij
tool to view request messages.

## Procedure

1 Startthe ij tool. On Windows completethe following sub-steps: Onnon-Windows platforms,complete the following sub-steps:

<!-- image -->

    1. Open a command window
    2. Change
directory to profile\_root\derby\bin\embedded
    3. Type ij.bat

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

    1. Open a command window
    2. Change
directory to profile\_root/derby/bin/embedded
    3. Type ./ij.sh
2 Open the data store for the messaging engine. Use theij tool to complete the following sub-steps:

1. Connect to the required database file. For
a messaging
engine, the database is stored in the directory profile\_root/profiles/profile\_name/databases/com.ibm.ws.sib and
has the name of the messaging engine; for example, for the default
standalone
profile on Windows, the database file for
the messaging engine
localhostNode01.server1-SCA.SYSTEM.localhostNode01Cell.Bus (for server1
on
the SCA.SYSTEM bus) is:
profile\_root\profiles\default\databases\com.ibm.ws.sib\localhostNode01.server1-SCA.SYSTEM.localhostNode01Cell.Bus
2 Use the ij tool to issue SQLcommands and view data.
    1. Change directory to install\_root/derby/bin/embedded
    2. Type ./ij.sh
    3. Type protocol
'jdbc:derby:' ;
    4. Type connect 'profile\_root/profiles/profile\_name/databases/com.ibm.ws.sib/database\_name'
;
3. Optional: 
To display more help about using ij,
type help ;  at the ij> prompt.