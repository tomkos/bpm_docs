# Troubleshooting
your deployment environment

## Before you begin

## About this task

- Unavailable applications
- Sluggish applications
- Stopped applications
- Decreased
throughput
- Sluggish performance

## Procedure

1. Display the topology layout that describes this deployment environment
to determine the status of the topology.
2. Display
the topology to determine the state of the various roles
in the topology. Note the roles with unexpected states or warning
for further
investigation.
3. Locate the nodes that are causing
the error state for each role.
4. Make sure all
nodes are synchronized. On the Nodes page
in the administrative console select any unsynchronized nodes and
click Synchronize.
5. Make
sure that the messaging engines associated with all the buses
are running. If they are not running, stop and start
the messaging
engines.
6. Locate the logs associated with
the nodes in error and view the
logs for error messages.
7. Take any actions prescribed
by the error messages to affect the
correction.
8. Correct any errors and restart
the affected nodes.

## Results

## What to do next

- Trying to download a document might fail with a NullPointerException

When you try download a document after upgrading to IBM Business Process Manager V8.5 or later versions, the download might fail with the following NullPointerException.
- Nodes may fail to synchronize automatically when two deployment environments exist in the same cell

If you have a running deployment environment and you use the Deployment Environment wizard to create another deployment environment in the same cell, the nodes may fail to synchronize automatically when you save the new deployment environment configuration in the administrative console.
- Numerous synchronous AIS requests can slow performance

In IBM Business Process Manager Advanced V8.0.1, the default buffer size of the StaX parser was changed from 64K to 2K, which can cause performance issues when there are numerous synchronous Advanced Integration service (AIS) requests.
- AIS does not refresh automatically in the Inspector view

When you run a business process definition (BPD) in IBM Business Automation Workflow, the process status does not automatically update in the Inspector view. An Advanced Integration service can take some time to run, depending on the service implementation.
- AIS does not participate in the same transaction as business process

In an Advanced deployment environment, process navigation of business process definitions (BPDs) does not participate in the same transaction context as an advanced integration service (AIS). Therefore, a runtime failure in the BPD navigation that causes the BPD transaction to roll back does not roll back the transaction under which the currently executing AIS might be running. As a result, the AIS might be executed a second time.
- SSL fails when host name configuration fails

IBM Business Automation Workflow uses host name verification for outbound connections that use Secure Sockets Layer (SSL). Connections are refused if the host name that the server connects to does not match the common name (CN) in the SSL certificate. This problem is most likely to occur when the initial configuration used localhost as a host name.
- SSL handshake failure when connecting with an external HTTP server

If you receive an SSL handshake failure when connecting with an external HTTP server, you may need to add the signer to the local trust store.
- Authors cannot drill down in a report

When a report is present in Coach technology and you run it in playback mode using IBM Workflow Center for IBM Business Automation Workflow, you might not be able to drill down in the report.
- Error occurs when importing process applications

When you try to import process applications and toolkits into IBM Workflow Center, the import process might fail if you do not have proper rights in your operating system.
- Process Portal: 404 Not found error

Users receive an HTTP 404 "Not found" error when they log in to Process Portal.
- Process Portal: Troubleshooting problems with search results

After users run a search in Process Portal, they receive error messages that indicate too many results exist for the search criteria, and that the search must be refined.
- Process Portal does not support automatic session rollover

Process Portal does not support automatic session rollover if one of the nodes in a cluster becomes unavailable.
- Process Portal stream comments do not allow at characters (@) that are not enclosed in double quotes or followed by a user name

The Process Portal stream comments do not support at characters (@) that are not enclosed in double quotation marks, unless they are followed by a user name, as in an email address.
- Failure when sending tracking definitions

Installing a snapshot from IBM Workflow Center to IBM Workflow Server is successful, however there are errors in SystemOut.log (CWLLG2229E and sql error com.microsoft.sqlserver.jdbc.SQLServerException: The specified schema name "sa" either does not exist or you do not have permission to use it). Tracking definitions are not sent successfully.
- Server fails to start due to version validation

During server start, the version of software is checked for consistency between IBM Business Automation Workflow (BPM) profiles and the Workflow Server and Performance Data Warehouse databases. If the versions are not consistent, the related servers fail to start.
- Errors when you create second deployment environment

When you are creating a second deployment environment, you might see errors in the application server log of the first deployment environment.
- Error when the server starts after copying the deployment environment

If you copy the deployment environment or create an environment to test the upgrade procedure, you might see a server error involving the BPM document store when the server first starts.
- SQL Error when starting multiple nodes in a cluster

After a migration, you might see an SQL exception in the SystemOut.log file when you start more than one node at a time.