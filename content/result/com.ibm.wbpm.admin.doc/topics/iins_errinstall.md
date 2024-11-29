# Messages and known issues during installation and profile creation

<!-- image -->

<!-- image -->

<!-- image -->

If you do not see an error message that resembles yours, or if the information provided does not
solve your problem, contact IBM Business Automation Workflow support at IBM
 for further assistance.

## Informational messages

- Sample applications feature is not available for installation because the WAS
Samples feature is not installed.
- Installation Manager cannot remove feature import.productProviders.feature from an
installation package that was imported to Installation Manager.
- Installation Manager cannot remove feature import.configLauncher.feature from an
installation package that was imported to Installation Manager.

## Null pointer exception

```
Provisioning managed node Node1.                                
Creating cluster members.                        
The HTTP and HTTPS ports for server SingleClusterMember1 on node     
Node1 are added to the virtual hosts list.                           
FATAL ERROR:  'java.lang.NullPointerException'                       
          :null                                                      
Configuring the REST services end points.                            
Saving configuration changes...                                      
Synchronizing node Node1                                             
....
```

The command successfully creates the deployment environment. This message can be ignored.

## CRIMA1168E error received when installing IBM Process Federation
Server in IBM Business Automation Workflow

```
CRIMA1168E: The installation directory ("/opt/im") must not be a parent or sub-directory of the shared resources directory ("/opt/im/IMShared")
```

## Configuration errors were detected during the installation

If you are installing either the Advanced or Advanced - Process Server editions of IBM Business
Process Manager 24.0.0.0
with Installation Manager, and you selected to install only the client, you might get the following
warning message: The packages are installed with warnings. View Log
file

If you see this warning message after installing the client feature of Business Process Manager,
either the Advanced or the Advanced - Process Server edition, on a Windows system with just the client feature selected, examine the logs. If,
in the logs, you see the following message, then you cannot use the Windows add or remove programs function to remove the client:
2464 WARNING 27:29.66 com.ibm.ws.exec.command.ExecCommand
"C:\IBM\WebSphere\AppServer/util/bpm\_configManagerLauncher.bat" cannot be found

To remove the client, you must use Installation Manager.

## An earlier instance exists

- An earlier instance exists in drive where DB2 is being
installed/BPMINST. Either delete or rename this folder. Press "Re-Validate" button once
you have taken these steps.
- An earlier instance exists in
instance\_user\_home/instance\_user. Either delete or rename this folder. Press
"Re-Validate" button once you have taken these steps.
- The DB2 instance folder folder already exists at
path. Delete the DB2 instance folder folder and then retry the
installation.

- The DB2 instance folder folder already exists at
path. Delete the DB2 instance folder folder and then retry the
installation.

## Invalid command line argument

```
<message>
 <key>Error occurred in phase: {0}
 SU: {1} {2}
 IU: {3}
 Message: {4}</key>
 <arg>install</arg>
 <arg>com.ibm.ws.db2exp.winia64.core</arg>
 <arg>9.7.3.20111109\_0314</arg>
 <arg>db2exp.winia64.exec null-&gt;9.7.3000&lt;/ag>
 <arg>Installation of DB2 Express has failed.
Log location: D:\IBM\BPM85\logs\db2install.log
Installation failure reason: Invalid command line argument. </arg>
</message>
```

The DB2install.log file is not generated during the installation
process.

- When IBM
DB2® was previously uninstalled, the DB2 components were not removed completely from the system.
- A previous IBM
DB2 installation process did not complete.
- The IBM
DB2 installation under the
install\_root directory was deleted without using
Installation Manager or the Microsoft
Windows Programs and Features control panel.

Check the Programs and Features control panel and Services to determine if any DB2-related
components are listed.

For information about how to troubleshoot and cleanup the DB2 uninstallation issues, see the Troubleshooting of DB2 Install/uninstall issues FAQ technote at http://www.ibm.com/support/docview.wss?uid=swg21447545.

If you do not have the DB2 installation image so that you
can use the db2unins.bat command, you can use the DB2 native installer from your Db2 Installation
Manager repository. This installer is packaged with the IBM Business Automation Workflow installation. To
access the command, decompress the
isntall\_root\repository\DB2\_64\native\db2express-winia64\_version.zip
file into a temporary directory and use the db2unins.bat command. The
db2unins –f command removes all the DB2
copies and products that are installed on the system.

After you clean up DB2, follow the IBM Business Automation Workflow instructions to
complete the installation process.

## Supported IBM JDK was not found. The IBM JDK shipped with this product must be located at
install\_root/JDK. Correct this problem and try again.

If you use symbolic links to point to the IBM
Java™ Development Kit (JDK) shipped with the product, or to a
JDK found in the PATH environment variable on your system, IBM
SDK for Java validation might fail, resulting in a failed
installation. This problem is caused by the way IBM SDK for
Java validation code detects whether the JDK shipped with the
product is the current JDK used for installation.

To resolve this problem, do not use symbolic links in JVMs supplied with the installation image
of IBM Business Automation Workflow and remove
symbolic links from all JVMs that appear in your system's PATH environment variable.

## Warning: Cannot convert string <type\_name> to type FontStruct

If you install the web server plug-ins for WebSphere
Application Server, you also install the ikeyman utility. The ikeyman utility is part of the Global
Services Kit 7 (GSKit7).

<!-- image -->

```
Warning: Cannot convert string 
   "-monotype-arial-regular-r-normal--*-140-*-*-p-*-iso8859-1"
   to type FontStruct
```

You can safely ignore the warning and use the ikeyman utility.

<!-- image -->

## CWWBB0627E error during installation with Db2 on Linux systems

When you install IBM Business Automation Workflow on a 32- or 64-bit Linux system, the server does not start successfully. Also, the
SystemOut.log file includes CWWBB0627E: Failed to create the database
schema.

The problem occurs if you used the Administration server (DAS) user name, which defaults to
bpmadmin, instead of the Instance user name, which defaults to
bpminst.

- When you use the Administration server (DAS) user name during a Custom installation, in which
you create the profile after installation
- During a Typical installation with an existing DB2
database

```
[5/24/11 10:40:27:131 CDT] 00000000 CreateSchemaM E   CWWBB0627E: Failed to create the database schema.
[5/24/11 10:40:27:227 CDT] 00000000 ProcessEngine E
[5/24/11 10:40:27:274 CDT] 00000000 ManagerAdmin  I   TRAS0018I: The trace state has changed. The new trace state is *=info.
[5/24/11 10:40:27:499 CDT] 00000000 CreateSchemaM I   CWWBB0625I: Started creating the database schema.
[5/24/11 10:40:27:502 CDT] 00000000 CreateSchemaM I   CWWBB0658I: Schema qualifier is: 'BPEDB'.
[5/24/11 10:40:27:909 CDT] 00000000 CreateSchemaM I   CWWBB0614E: Database schema creation or migration step failure 
  CREATE TABLE BPEDB.PROCESS\_TEMPLATE\_B\_T ( PTID CHAR(16) FOR BIT DATA NOT NULL , NAME VARCHAR(220) NOT NULL , 
  DEFINITION\_NAME VARCHAR(220) , DISPLAY\_NAME VARCHAR(64) , APPLICATION\_NAME VARCHAR(220) , DISPLAY\_ID INTEGER 
  NOT NULL , DISPLAY\_ID\_EXT VARCHAR(32) , DESCRIPTION VARCHAR(254) , DOCUMENTATION CLOB(4096) , EXECUTION\_MODE 
  INTEGER NOT NULL , IS\_SHARED SMALLINT NOT NULL , IS\_AD\_HOC SMALLINT NOT NULL , STATE INTEGER NOT NULL , 
  VALID\_FROM TIMESTAMP NOT NULL , TARGET\_NAMESPACE VARCHAR(250) , CREATED TIMESTAMP NOT NULL , AUTO\_DELETE 
  SMALLINT NOT NULL , EXTENDED\_AUTO\_DELETE INTEGER NOT NULL , VERSION VARCHAR(32) , SCHEMA\_VERSION INTEGER NOT 
  NULL , ABSTRACT\_BASE\_NAME VARCHAR(254) , S\_BEAN\_LOOKUP\_NAME VARCHAR(254) , S\_BEAN60\_LOOKUP\_NAME VARCHAR(254) , 
  E\_BEAN\_LOOKUP\_NAME VARCHAR(254) , PROCESS\_BASE\_NAME VARCHAR(254) , S\_BEAN\_HOME\_NAME VARCHAR(254) , 
  E\_BEAN\_HOME\_NAME VARCHAR(254) , BPEWS\_UTID CHAR(16) FOR BIT DATA , WPC\_UTID CHAR(16) FOR BIT DATA , BPMN\_UTID 
  CHAR(16) FOR BIT DATA , BUSINESS\_RELEVANCE SMALLINT NOT NULL , ADMINISTRATOR\_QTID CHAR(16) FOR BIT DATA , 
  READER\_QTID CHAR(16) FOR BIT DATA , A\_TKTID CHAR(16) FOR BIT DATA , A\_TKTIDFOR\_ACTS CHAR(16) FOR BIT DATA , 
  COMPENSATION\_SPHERE INTEGER NOT NULL , AUTONOMY INTEGER NOT NULL , CAN\_CALL SMALLINT NOT NULL , CAN\_INITIATE 
  SMALLINT NOT NULL , CONTINUE\_ON\_ERROR SMALLINT NOT NULL , IGNORE\_MISSING\_DATA INTEGER NOT NULL , EAR\_VERSION 
  INTEGER NOT NULL , LANGUAGE\_TYPE INTEGER NOT NULL , DEPLOY\_TYPE INTEGER NOT NULL , MESSAGE\_DIGEST VARCHAR(20) 
  FOR BIT DATA , CUSTOM\_TEXT1 VARCHAR(64) , CUSTOM\_TEXT2 VARCHAR(64) , CUSTOM\_TEXT3 VARCHAR(64) , CUSTOM\_TEXT4 
  VARCHAR(64) , CUSTOM\_TEXT5 VARCHAR(64) , CUSTOM\_TEXT6 VARCHAR(64) , CUSTOM\_TEXT7 VARCHAR(64) , CUSTOM\_TEXT8 
  VARCHAR(64) , PRIMARY KEY ( PTID ) ) IN BPETS8K: com.ibm.db2.jcc.am.SqlSyntaxErrorException: DB2 SQL Error: 
  SQLCODE=-204, SQLSTATE=42704, SQLERRMC=BPETS8K, DRIVER=3.61.65.
[5/24/11 10:40:27:912 CDT] 00000000 CreateSchemaM E   CWWBB0627E: Failed to create the database schema.
[5/24/11 10:40:27:912 CDT] 00000000 CreateSchemaM E   CWWBB0627E: Failed to create the database schema.
[5/24/11 10:40:27:948 CDT] 00000000 TraceBPE      E
```

- Create a new profile using the -manageprofiles command. Specify the Instance
user name, which, by default, is bpminst, for the -dbUserId
parameter.
- Add the Administrative server (DAS) user name, which, by default, is bpmadmin,
to the bpmiadm1 group by running the following
command:usermod -a -G bpmiadm1 bpmadmin