# Starting and shutting down the system

## About this task

Components in your IBM® Business Automation
Workflow environment on an AIX®, Linux®, or Linux for System z
server must be started manually. You need to restart or shutdown your system for server maintenance
or software updates.

- Starting the system
- Shutting down the system

If you have a single server Business Automation Workflow environment that is
installed on a Windows server, all of your components and
applications restart automatically. You must have the passwords for your components and applications
to complete the steps.

## Starting the system

System restarts are necessary for server maintenance or software updates. Any changes or
updates can be properly implemented and integrated into the system. Restarting the system allows for
a fresh start, boosting optimal performance and stability after the maintenance or
updates.

### Procedure

To start IBM Business Automation
Workflow components:

1. Log in as the root user.
2. Start Db2® by
entering the following command: su - dsrdbm01 -c db2start
3 Start Security Directory Server :
    1. Change to the Security Directory Server directory by entering the
following command: cd /install\_root/ldap/V6.3/bin
    2. Start Security Directory Server
by entering the following command: ./ibmdirctl -h localhost -D cn=root -w
password start
    3. Make sure that Security Directory Server is running by entering the
following command: ./ibmdirctl -h localhost -D cn=root -w password
status
4 Start the web application server.

1. Change to the profile\_root/bin directory.
profile\_root is the directory path that contains your profile, for example:
/install\_root/WebSphere/AppServer.
2. Run the following command: 
./startServer.sh server1

## Shutting down the system

In addition to restarting, sometimes it is necessary to shutdown your system for server
maintenance or software updates. This process involves temporarily powering off the entire system to
run essential tasks such as hardware upgrades or system configuration adjustments. A system shutdown
creates a clean and controlled environment for making changes, minimizing the risk of errors or data
corruption.

### Procedure

To shutdown Business Automation Workflow:

1. Stop the web application server. In a distributed system architecture, first shutdown the
nodes, and then shutdown the main server.
2. Change to the profile\_root/bin directory.
profile\_root is the directory that contains your profile, for example:
/opt/ibm/WebSphere/AppServer.
3. Run the command to shutdown the server:

Server type
Command

Windows
stopServer.bat server1

AIX, Linux,
or Linux for System z
 

If global security is enabled, you must specify a user name and password for authentication. You
can wait to be prompted for the user name and password, or append the following options to the
stopServer command:
-username user\_name -password password