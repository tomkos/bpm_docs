# Using the Administration Console for Content Platform
Engine

If you configure Business Automation Workflow to use an external
Enterprise Content Management server, you cannot use the IBM Administration Console for
Content Platform Engine to administer the
embedded content store. You must use the external Enterprise Content Management server's IBM Administration Console for
Content Platform Engine.

## Manually enabling the IBM Administration Console for
Content Platform Engine navigator desktop
(deprecated)

1 Start the Case configuration tool .Using the GUI Using the command line

Using the GUI

    - From the
install\_root/CaseManagement/configure directory, run the
./configmgr file.
    - From the
install\_root\CaseManagement\configure directory, run the
configmgr.exe file.
    - Run
install\_root/CaseManagement/configure/configmgr\_cl
    - Run
install\_root\CaseManagement\configure\configmgr\_cl.exe
2. Run the task to register the Administrator Console for Content Engine (ACCE) plug-in:Using
the GUI
Open the predefined profile for your current development environment and run the
Register the Administrator Console for Content Engine (ACCE) plug-in task. The predefined profile is
located in the following directory:
dmgr\_profile\_root/CaseManagement\_DE\_name/profiles/ICM\_dev.
Using the
command line Run the Register the Administrator Console for Content Engine (ACCE) plug-in
task, referring to the predefined profile for your current development environment, for example
configmgr\_cl execute -taskfile registeracceplugin -profile
dmgr\_profile\_root/CaseManagement\_DE\_name/profiles/ICM\_dev.

## Accessing the IBM Administration Console for
Content Platform Engine

To access the IBM Administration Console for
Content Platform Engine, use a web browser.
The web address has the following format:

```
https://[host\_name]:[port]/acce
```

```
https://myserver.example.com:9443/acce
```

To end an IBM Administration Console for
Content Platform Engine
session, close your browser.

## Authorization

- Container-managed authorization (Java EE roles) to access the web application for the
administration console.
- The appropriate authorization in the access control list for the content store to manage the
objects in the embedded content store, such as folders and documents.

Initially, only the user who has the EmbeddedECMTechnicalUser
role, which defaults to the deployment environment administrator,
can access the IBM Administration Console for
Content Platform Engine.
The DOC\_STORE\_ADMIN\_USERS Java EE role on the IBM\_BPM\_DocStoreAdmin
application controls the access. To allow more users to access the IBM Administration Console for
Content Platform Engine,
update the user assignments for the Java EE role.

To update the users and groups in the technical user role, always use the
maintainDocumentStoreAuthorization admin command and not the IBM Administration Console for
Content Platform Engine. For information, see
maintainDocumentStoreAuthorization command. For information about how to keep the roles in sync, see
Administering the technical user for the BPM document store.

For
more information about IBM Administration Console for
Content Platform Engine,
see Administering Content Platform Engine.

- FNRAC1008E error occurs if Java 2 Security is enabled

 Traditional: 
 When the IBM Administration Console for Content Platform Engine opens, an error message is received if Java™ 2 Security is enabled in IBM Business Automation Workflow (BPM).