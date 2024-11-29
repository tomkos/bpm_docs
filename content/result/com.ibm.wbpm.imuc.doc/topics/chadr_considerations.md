# Considerations for HADR setup and configuration

- Ensure that the read on standby (ROS) feature is disabled
- Verify status of databases for takeover
- Configure data sources for HADR
- Set up programmatic transaction retry properties
- Specify user roles for HADR
- Start the messaging engine after the takeover
- Access additional information

## Ensure that the read on standby
(ROS) feature is disabled

Although DB2 HADR supports the
read on standby (ROS) feature, it is not supported by IBM BPM and
can cause unexpected results when it is enabled. To ensure that the
ROS feature is disabled, complete the following steps:

1. Open a DB2 command window.
2 Run the db2set command. If the DB2\_HADR\_ROS propertyis set to YES , complete the followingsteps:
    1. Run the following command to set the DB2\_HADR\_ROS property
to NO: db2set DB2\_HADR\_ROS=NO
    2. Stop and then restart the DB2 instances for the update to take
effect.

## Verify status of databases for
takeover

When a site failure occurs, HADR enables the standby
database to take over as the primary database, with full DB2 functionality.
Before the takeover occurs, verify the DB2 HADR status of both the
primary database and the standby database to see if the takeover is
allowed or if an error is returned. Sometimes, the takeover might
cause an error or might not be allowed.

```
db2pd -hadr -db MEDB9
```

```
db2pd -hadr -alldbs
```

For more information, see the TAKEOVER HADR command topic. Review the command parameters and the usage
notes to determine whether to perform the takeover.

## Configure data sources for HADR

Configure
the DB2 data sources for HADR in the IBM® Business Automation Workflow admin
console, as described in the Configuring client reroute for applications that
use DB2 databases topic.

- In order for client side connections to
be automatically rerouted to the alternate database server, you must
enable automatic client reroute when setting up DB2 HADR.
- For messaging engine and cell level data sources, the Alternate
server names and Alternate port numbers properties
must be configured.
- The alternate port must be the external port for the DB2 server,
not the HADR service port that is specified in /etc/services.
For example, if the HADR service port DB2\_HADR\_1,
specified in /etc/services, is 55001,
and the DB2 server uses the external port 50000,
you must specify port 50000 for the data source
alternate port in the admin console.

## Set up programmatic transaction
retry properties

```
<transaction-reroute-retries>3</transaction-reroute-retries>
<transaction-reroute-retry-delay-in-millis>10000<transaction-reroute-retry-delay-in-millis>
```

1 Locate 100Custom.xml configuration file:
    - For a network deployment environment, the file path is DMGR\_profile\_root\config\cells\cell\_name\nodes\custom\_node\_name\servers\server\_name\server\_type\config\100Custom.xml.
    - For a stand-alone server environment, the file path is standalone\_profile\_root\config\cells\cell\_name\nodes\standalone\_node\_name\servers\server\_name\server\_type\config\100Custom.xml.
2. Edit the 100Custom.xml file. Edit the following
section to look like this example:<server merge="mergeChildren">
  <transaction-reroute-retries merge="replace">10</transaction-reroute-retries>
  <transaction-reroute-retry-delay-in-millis merge="replace">3000<transaction-reroute-retry-delay-in-millis>
</server>
3. Save your changes.

Provide all the client reroute properties for all your
data sources.

## Specify user roles for HADR

- For Windows, use the DB2 administrative user: db2admin
- For Linux, use the DB2 instance user, db2inst1,
rather than the administrative user, dasusr1.

For example, if the DB2 instance user is specified, the db2inst1 user
backs up the primary database, copies the backup image to the standby
server, and then restores or starts the standby server using this
image.  If the administrative user is specified, the dasusr1 user
is the owner of the copied image, which the db2inst1 user
who performs the backup and restore actions cannot access. Because
the two users belong to different groups and have different access
rights to files, the HADR setup might fail.

## Start the messaging engine after
the takeover

If the auto restart for the messaging engine
is disabled, you must manually start the messaging engine after the
database takeover occurs.

1. The database that the messaging engines use has been taken over.
2. Messaging engine server 1 shut down to prevent data loss.
3. Messaging engine server 2 started all the messaging engines and
is working as the active server while the messaging engine server
1 is still down.
4. Another takeover of the database occurred.
5. Messaging engine server 2 shut down to prevent data loss.
6. Both messaging engine servers 1 and 2 are down.

## Access additional information

- If an outage occurs in your DB2 HADR environment, see Detecting and responding to system outages in a high availability
solution.
- After the failover occurs, if the DB2 HADR status is not peer andif some data loss occurs, configure the DB2 HADR status to peer asdescribed in the following topics:
    - Performing an HADR failover operation
    - Reintegrating a database after a takeover operation

## Related concepts

- System requirements

## Related tasks

- Preparing operating systems for product installation
- Configuring Oracle Data Guard for IBM Business Automation Workflow