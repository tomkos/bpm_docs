# Troubleshooting Service Component Architecture processing and
call chains

Events that can be captured include:

- Errors that occur during processing because of corrupted data
- Errors when resources are not available, or are failing
- Interpretation of code paths

You can access the Cross-Component Trace page from the administrative
console by clicking Troubleshooting > Cross-Component Trace.

## Handling and deleting collected
data

Consider the following with regard to handling and
deleting data collected by Cross-Component Trace:

- SCA call chain information is added to the systemout.log and trace.log
files and is purged as those files are purged.
- Data snapshots capture the input and output data of call chains.The
input and output data is captured as files in the logs\XCT directory.
To display this data, IBM Integration
Designer needs access to
the systemout.log files and the logs\XCT directory.
If IBM Integration
Designer is
not available on the server, copying the logs directory and placing
it on a machine (so that it can be accessed by IBM Integration
Designer) preserves the
file structure so that IBM Integration
Designer can make use of
the log files and the data snapshot files.Note: IBM Integration
Designer can use the data
snapshot files where they are (without moving them) if it can access
the files in the logs directory. If you need to move files, it is
safest to move the entire logs directory. By moving the entire logs
directory, you get the XCT, first failure data capture (FFDC) files,
and the systemout.log and trace.log files.

Data snapshot
files are written to server-specific subdirectories using the following
directory structure: logs\ 
     server 
     ffdc 
     xct\ 
        server-specific\_dir\ 
                            2009-0-25-11 
                            2009-0-26-12 
                            2009-0-26-14 
Where server-specific\_dir name is derived
from the name of the server. For example, server1 is the default
server name for a stand-alone installation.
- Data snapshot files in logs\XCT\server are
referenced from the systemout.log and trace.log files that were created
at the same time by the server. When the old systemout.log and trace.log
files are deleted, the associated Cross-Component Trace data snapshot
files in logs\XCT\server can also be deleted.You
can use the timestamps in the systemout.log and trace.log files to
identify and determine what data snapshot files to delete. It is safe
to delete all the data snapshot files for a server that are older
than the oldest date in the systemout.log and trace.log files. Preferably,
you should use the Delete data snapshot files function
from the administrative console when data snapshot files are no longer
needed. For detailed information on the ways that you can delete data
snapshot files, see Deleting data snapshot files.
- Do not save or add files to the logs\XCT directory.
Do not copy or create new directories into the logs\XCT directory. IBM Business Automation Workflow manages
the content of the logs\XCT directory and deletes
items that are no longer needed. IBM Business Automation Workflow might
consider unrecognized files or directories as unnecessary and delete
them. If you want to save a copy of the data snapshot files, copy
the data to another directory outside of the logs\XCT directory.

## Cross-Component Trace settings and call chain processing

The
information in this section describes the effect that Cross-Component
Trace configuration settings have on call-chain processing. It also
includes a description of various Cross-Component Trace configurations
and explains the call chain events that result from the configurations.

The
following list includes general rules on call chain processing and
Cross-Component Trace configuration decisions:

- If Cross-Component Trace is turned off for a server, then no Cross-Component
Trace records are written to that server's logs.
- Cross-Component Trace configuration settings for a particular
server, affect that server only.For example, if Server A
has Trace all = Yes and Server B has Trace
all = No, Cross-Component call chains are in the logs
for Server A only. Similarly, this rule applies to setting the data
snapshot feature. If Enable data snapshot = Yes on
Server A and Enable data snapshot = No on Server
B, then only Server A will have data snapshot files in its logs directory.
- Application-specific Cross-Component Trace data flows between
servers that have the Enable Cross-Component Trace = Yes. For
example, if both Server A and Server B have Enable Cross-Component
Trace = Yes and Server A has enabled Cross-Component Trace
for a specific SCA module, the calls made from the Cross-Component
Trace-enabled module on Server A (to applications or services on Server
B), will result in Server A having call chains for all of activity
related to the Cross-Component Trace-enabled module. Server B would
also have call chains, but only for those calls that came from the
Cross-Component Trace-enabled module on Server A. The logs of the
two servers can be combined to reveal the entire call chain activity.
- To create a Cross-Component Trace for long-running
BPEL process instances, you must select Enable Cross-Component
Trace and Trace all, or enable
Cross-Component Trace for the SCA module before the BPEL process instance
is created.

The following illustration is of two servers (Server A and
Server B), both with Cross-Component Trace enabled. Server A has the Trace
all value set to Yes, while Server B has Trace
all  set to No.

Figure 1. A remote messaging and remote support topology

<!-- image -->

For the Cross-Component Trace configuration scenario illustrated
in Figure 1, call chain events
would result on Server A, but not on Server B.

The following
illustration is of two servers (Server A and Server B), both with
Cross-Component Trace enabled. Server A has the Trace all value
set to No and it includes Module A as a module on which to enable
Cross-Component Trace. Server B has Trace all  set
to No and has no SCA modules selected for Cross-Component Trace.

Figure 2. A remote messaging and remote support topology

<!-- image -->

For the Cross-Component Trace configuration scenario illustrated
in Figure 2, call chain events
would result on Server A. Trace activity for all Module A operations
are written to the log on Server A. Any calls made from Module A to
applications or services on Server B, results in call chains. The
call chains on Server B would only pertain to those calls that came
from Module A (because that module is configured for Cross-Component
Trace).