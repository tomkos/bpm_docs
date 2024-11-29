# migrateBSpaceData command-line utility

The migrateBSpaceData command-line utility migrates the Business Space data for
an installation with the Business Space server host name specified by hostname,
Business Space server port number specified by SOAP Port Number, Business Space
administrative user ID specified by username, and password specified by
password.

## Syntax

```
migrateBSpaceData 
[options] 
-host host\_name 
-port SOAP\_Port\_Number 
-user user\_name 
-password password
```

## Parameters

If there is no cluster in the ND environment, you can set this option to
none. For example, -cluster none.

## Examples

- In a stand-alone environment, to migrate Business Space data with a Business Space server hostlocalhost , port 8880 , Business Space administrative user IDadmin and password admin , use one of the following commands:
    - migrateBSpaceData.sh -host localhost -port 8880 -user admin -password admin -server server1 -node leoNode01
    - migrateBSpaceData.bat -host localhost -port 8880 -user admin -password admin -server server1 -node leoNode01
- In an ND environment, to migrate Business Space data with a Business Space server hostlocalhost , port 8880 , Business Space administrative user IDadmin and password admin , use one of the following commands:

- migrateBSpaceData.sh -host localhost -port 8880 -user admin -password admin -cluster cluster1
- migrateBSpaceData.bat -host localhost -port 8880 -user admin -password admin -cluster cluster1

If you are migrating from version 7.0.x, use the following examples, for both stand-alone and ND
environments.

- Use the script for your operating system to copy the Business Space data from V7.0.x:
    - migrateBSpaceData.bat -host localhost -port 8880 -user admin -password admin -dbcopy
    - migrateBSpaceData.sh -host localhost -port 8880 -user admin -password admin -dbcopy
- Use the script for your operating system to upgrade the Business Space data from V7.0.x:

- migrateBSpaceData.bat -host localhost -port 8880 -user admin -password admin -dbupgrade
- migrateBSpaceData.sh -host localhost -port 8880 -user admin -password admin -dbupgrade