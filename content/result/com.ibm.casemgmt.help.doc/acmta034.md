# Problems occur when you import solutions with IBM
FileNet Deployment Manager

## Symptoms

1. You receive an error that states that the security principal was not found when the solution is
imported by using the Case administration client .
2. LoggingStream errors are returned when the solution is imported:2013-06-25
23:59:43,731 WARN [pool-5-thread-1]filenet\_error.api.com.filenet.apiimpl.imex.LoggingStream - The current
import process is attempting to update system properties and the current user does not have security
right to do this for object store TOS01\_cmicmint2vm15. Some or all of this import may fail until the
current user is assigned the "modify certain system properties" right on the object
store.
2013-06-25 23:59:44,121 ERROR [pool-5-thread-1]filenet\_error.api.com.filenet.apiimpl.imex.LoggingStream - Object has
failed the import process because of an error
classid="PropertyTemplateInteger32&objectid="{AAD2FAB6-2708-4D0A-B590-0156A03D130D}&objectStore={51D125E0-D03C-4808-9A41-4CEE42DCF245}
Method failed because an object or property is read-only. LastModifier is a read-only property and
cannot be updated at this time.

## Resolving the problem

- If you receive an error that the security principal was not found when you use the Case administration client to import the solution,use the Case configuration tool toimport the solution. The Case configuration tool does not map securityprincipals that are associated with solution assets.Alternatively, if you want to use theCase administration client to import thesolution, disable principal mapping for imported assets:

Alternatively, if you want to use the
Case administration client to import the
solution, disable principal mapping for imported assets:

    1. In the web client, open the IBM Content
Navigator administration
tool.
    2. Click Plug-ins > IBM Business Automation
Workflow administration
plug-in.
    3. Under Additional Properties, clear the Allow target principal
mapping when assets are imported check box.
    4. Save your changes.
- If the import operation fails due to LoggingStream errors, clear the Use originalcreate/update timestamps and users check box on the FileNet DeploymentManager Import Options page. Alternatively, if you need to select the Useoriginal create/update timestamps and users check box because you want to use theoriginal time stamps from the source environment instead of new time stamps, grant theModify certain system properties permission:

Alternatively, if you need to select the Use
original create/update timestamps and users check box because you want to use the
original time stamps from the source environment instead of new time stamps, grant the
Modify certain system properties permission:

1. In Administration Console for Content Platform
Engine, open the IBM Business Automation
Workflow design object store and select the
Security tab.
2. Select the user that does the import operation and click Edit.
3. In the Edit Permissions window, select the Modify certain system
properties check box.
4. Save your changes.