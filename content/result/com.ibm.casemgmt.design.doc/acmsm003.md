# Restarting components in a single-server environment

## About this task

If your single-server Business Automation Workflow environment is
installed on a Windows server, all your components and
applications restart automatically after a reboot.

You must have the passwords for your components and applications in order to
complete the restart steps.

## Procedure

To start the workflow components:

1. Log in as the root user.
2. Restart the database.
For example, restart Db2® by entering the
following command: su - dsrdbm01 -c db2start
3 Start the LDAP server. For example, to start Security Directory Server :
    1. Change to the Security Directory Server directory by entering the following
command: cd /opt/ibm/ldap/V6.3/bin
    2. Start Security Directory Server by entering the following command:
./ibmdirctl -h localhost -D cn=root -w password start
    3. Make sure that Security Directory Server is running by entering the
following command: ./ibmdirctl -h localhost -D cn=root -w password
status
4 Start the web application server.

1. Change to the profile\_root/bin directory. profile\_root is
the directory path that contains your profile, for example: /opt/ibm/WebSphere/AppServer/profiles/AppSrv01.
2. Run the following command:

./startServer.sh server1