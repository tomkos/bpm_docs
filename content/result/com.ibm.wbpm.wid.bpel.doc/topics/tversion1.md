<!-- image -->

# Creating a new version of your process - migrate running instances

## Before you begin

## About this task

To create a new process version that is enabled for instance
migrations at run time, you need to define a process migration specification.
You deploy and install the new process version and the process migration
specification to your runtime environment. Existing instances of the
process in the runtime environment can then be migrated to the new
version of the process by an administrator. When creating a new process
version in IBM® Integration
Designer,
a new version of the module created which contains the process version
is contained (since you need a new deployment container). If the process
originated from IBM
WebSphere® Business Modeler, new
versions of all projects are also created during export from IBM
WebSphere Business Modeler.

## Procedure

1 In order to create a new process version, there are severallaunch points where you can start the New Process Version Wizard:
    - From the Module in the Business Integration view: In the Business
Integration view, right-click the module that contains the business
process and select New Process Version.
    - From the process in the Business Integration view: In the Business
Integration view, right-click the BPEL process and select New Process
Version.
    - From a component in the assembly diagram: In the Assembly diagram
select the BPEL process component to copy, right-click and select
New Process Version.
2 On the first page of the wizard, specify either a new Nameor a new module version. Which one you specify depends on whetherthe process is contained in a non-versioned module (default) or aversioned module. The first page of the wizard presentsthe following: In case the process you create is a new version of theoriginal module from IBMWebSphere Business Modeler , youmay need to provide names and versions for more than one module andlibrary. When a process is exported from IBMWebSphere Business Modeler to IBM IntegrationDesigner ,there are various export settings: The recommended export settingin IBMWebSphere Business Modeler is2 Modules + 1 Library, but you can also choose Module + library, ormodule only. Depending on the option that has been chosen in Modeler,the new process version wizard detects these project sets and treatsthem as a single unit.

- Non-versioned Business Integration Module: On the first wizard
page, specify the new module name. The wizard leaves the original
module untouched and creates a new module with the newly specified
name for further editing.
- Versioned Business Integration Module: On the first wizard page,
specify the new module version. The wizard creates a backup copy of
the original module for IBM Integration Developer internal use only
(not used by IID users), and updates the module version of the current
module for further editing.
- If the process came from IBM
WebSphere Business Modeler, you
may be prompted to specify new versions for more than one module and
a library.

In case the process you create is a new version of the
original module from IBM
WebSphere Business Modeler, you
may need to provide names and versions for more than one module and
library. When a process is exported from IBM
WebSphere Business Modeler to IBM Integration
Designer,
there are various export settings: The recommended export setting
in IBM
WebSphere Business Modeler is
2 Modules + 1 Library, but you can also choose Module + library, or
module only. Depending on the option that has been chosen in Modeler,
the new process version wizard detects these project sets and treats
them as a single unit.

3 Once you have specified new names, new versions, or both,specify your new BPEL process settings.

1. Specify date and time: You must specify the date and
time (validFrom) when the new process versions will become valid.
Specify either "Now" or an actual date and time. If you enter an invalid
date/time, the Finish button is disabled. Ensure that the copy becomes
valid after the original.
2 Create process migration specifications: In order tomigrate running process instances, you must select the process componentsthat you want to enable for instance migration at run time. The Processmigration specifications field shows all process components containedin the original module. If you select process components that do notapply for process instance migration, the Finish button is disabled.Component examples that may not apply for process migration are shownin Table 1. Table 1. Component examples Reason for invalid processes User Action to recover Process contains no validFrom date Add a validFrom date to the process Process is not long-running (Microflow) Refactor the process to become long-running Process was created with WebSphere IntegrationDeveloper in a version earlier than 7.0.0.0 Open the Process in WebSphere Integration Developer7.0.0.0 or higher and save it once. Process was created with Modeler in a versionearlier than 7.0.0.2 Process contains compensation logic Not supported (Remove compensation logic) Process contains Information Server activities Not supported (Remove Information Server activities) A process migration specification is created in the new modulefor each process you select. The source of this process migrationspecification points to the process version in the original versionof the module. The target points to the process version in the newversion of the module.

| Reason for invalid processes                                                               | User Action to recover                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Process contains no validFrom date                                                         | Add a validFrom date to the process                                                                                                                                                                                                          |
| Process is not long-running (Microflow)                                                    | Refactor the process to become long-running                                                                                                                                                                                                  |
| Process was created with WebSphere Integration Developer in a version earlier than 7.0.0.0 | Open the Process in WebSphere Integration Developer 7.0.0.0 or higher and save it once.                                                                                                                                                      |
| Process was created with Modeler in a version earlier than 7.0.0.2                         | Reexport the process in WebSphere Business Modeler 7.0.0.2 or later. During Export, make sure the "Enable generated BPEL for process versioning" check box is enabled.  Synchronize the export to the process that resides in your workspace |
| Process contains compensation logic                                                        | Not supported (Remove compensation logic)                                                                                                                                                                                                    |
| Process contains Information Server activities                                             | Not supported (Remove Information Server activities)                                                                                                                                                                                         |

4. If your module(s) contains Business state machines, you
must specify the date (validFrom) when the new Business state machine
will become valid. Specify either Now or an actual date and time.
If you enter an invalid date/time, the Finish button is disabled.
Ensure that the copy becomes valid after the original.
5. If your module(s) contains Human Tasks, you must specify
the date (validFrom) when the new Human Task will become valid. Specify
either Now or an actual date and time. If you enter an invalid date/time,
the Finish button is disabled. Ensure that the copy becomes valid
after the original.
6. If your module(s) contains Business Rule Groups, you must
specify (at the minimum) a new namespace for each Business Rule Group.
The wizard suggests a unique namespace for every Business Rule Group.
For the associated rule logic artifacts (Decision Table and Rule Set),
a unique name/namespace combination must be provided as well. The
wizard suggests a unique name/namespace combination for every rule
logic artifact. If you are satisfied with the wizard suggestions,
click next. Otherwise, click in the appropriate table row in the New
Name column to start a dialog box and adjust the name or namespace
to your needs.
7. If your module(s) contains Selectors, you must specify
at least a new namespace for each Selector. The wizard suggests a
unique namespace for every Selector. If you are satisfied with the
wizard suggestions, click Next. Otherwise, click in the appropriate
table row in the New Name column to start a dialog box and adjust
the name or namespace to your needs.
8. It might happen that after finishing the New Process Version
Wizard, an "Unhandled Artifacts" dialog box appears. If so, manual
adjustments might be needed. For Details, refer to Table 2.
9. Once the versioning process has completed, you now have
your new process version residing in your new module. Make the changes
you want to the new version of the BPEL process.
10. Inspect the generated process migration specification for
problems. If problems exist, the migration specification in the Business
Integration view (navigate to: Integration Logic -> Process Migration
Specification) is flagged with an error, with the problems being displayed
in the Problems view.  The migration specification is
an artifact that relates two process versions to each other and opens
the Process Migration Specification editor. The Process Migration
Specification editor has two tabs: Overview which provides details
about the source and target, and Differences which provides a visual
representation of the modifications that have been applied to the
target process. You must solve all the reported problems. 
In
order to analyze the impact these changes might have on running instances
in IBM Workflow
Server,
see the technote available at http://www-01.ibm.com/support/docview.wss?rs=2307&uid=swg27017383.
 If you decide after reviewing the process migration specification to not fix all the errors, you
can still deploy and install the new process version. However, you must delete the process migration
specification and deploy the new version without a process migration specification. See Creating a new version of your process - running instances use old version for more details.
11. Save your work.
12 You can deploy this new module as you would any other module. Table 2 defines artifacts that are not automatically handledduring the creation of a process version, and need a manual adjustmentas described in the user action column if they are used. Table 2. Artifacttypes and actions Artifact Type User Action Dynamic Assembler Configure the newly created Dynmic Assemblerin your new Module version using the Studio tools available in WebSphereIntegration Developer HTTP Export Binding Clients would need to be updated in order to use the new version. Web Service Export Binding (JAX-WS and JAX-RPC) Clients would need to be updated in order to use the new version. Generic JMS Export Binding Must not be shared between modules and need to be manuallychanged. Generic JMS Import Binding Must not be shared between modules and need to be manuallychanged. Care should be taken to set a matching send destination ifthe target module end point has also changed JMS Export Binding Must not be shared between modules and need to be manuallychanged. JMS Import Binding Must not be shared between modules and need to be manuallychanged. Care should be taken to set a matching send destination ifthe target module end point has also changed. MQ Export Binding Must not be shared between modules and need to be manuallychanged. Clients would need to be updated to new queue names. MQ Import Binding Must not be shared between modules and need to be manuallychanged. Care should be taken to set a matching send destination ifthe target module end point has also changed. Clients would need tobe updated to new queue names. MQ JMS Export Binding Must not be shared between modules and need to be manuallychanged. Clients would need to be updated to new queue names. MQ JMS Import Binding Must not be shared between modules and need to be manuallychanged. Care should be taken to set a matching send destination ifthe target module end point has also changed. Clients would need tobe updated to new queue names.

| Artifact Type                                   | User Action                                                                                                                                                                                                                                                                         |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dynamic Assembler                               | Configure the newly created Dynmic Assembler in your new Module version using the Studio tools available in WebSphere Integration Developer                                                                                                                                         |
| HTTP Export Binding                             | HTTP endpoint needs to be unique Context root must be renamed  Clients would need to be updated in order to use the new version.                                                                                                                                                    |
| Web Service Export Binding (JAX-WS and JAX-RPC) | Endpoint needs to be unique For SOAP/HTTP, context root must be renamed accordingly For SOAP/JMS, the destination queue must be renamed accordingly  Clients would need to be updated in order to use the new version.                                                              |
| Generic JMS Export Binding                      | Endpoint configuration Receive destination Listener Port Name (if defined)   Must not be shared between modules and need to be manually changed.                                                                                                                                    |
| Generic JMS Import Binding                      | Endpoint configuration Receive destination Listener Port Name (if defined)   Must not be shared between modules and need to be manually changed. Care should be taken to set a matching send destination if the target module end point has also changed                            |
| JMS Export Binding                              | Endpoint configuration Receive destination Listener Port Name (if defined)   Must not be shared between modules and need to be manually changed.                                                                                                                                    |
| JMS Import Binding                              | Endpoint configuration Receive destination  Listener Port Name (if defined)   Must not be shared between modules and need to be manually changed. Care should be taken to set a matching send destination if the target module end point has also changed.                          |
| MQ Export Binding                               | Endpoint configuration Receive destination queue  Must not be shared between modules and need to be manually changed. Clients would need to be updated to new queue names.                                                                                                          |
| MQ Import Binding                               | Endpoint configuration Receive destination queue  Must not be shared between modules and need to be manually changed. Care should be taken to set a matching send destination if the target module end point has also changed. Clients would need to be updated to new queue names. |
| MQ JMS Export Binding                           | Endpoint configuration Receive destination queue  Must not be shared between modules and need to be manually changed. Clients would need to be updated to new queue names.                                                                                                          |
| MQ JMS Import Binding                           | Endpoint configuration Receive destination queue  Must not be shared between modules and need to be manually changed. Care should be taken to set a matching send destination if the target module end point has also changed. Clients would need to be updated to new queue names. |

## Modeling considerations for Process Instance Migration

### About this task

- The target process version must be created using the New process version
wizard.
- The target process version of a process migration specification needs to be a newer version ofthe source process:
    - Component names and target namespace of source and target versions must be identical.
    - The validFrom date of the target version needs to be in the future
compared to the validFrom date of the source version. Note: The
validFrom must be explicitly specified in both the source version and the
target version.
- The source process version and the target process version must not contain any compensation
logic such as compensate activities, compensation handlers, or compensation service specification.
- The processes must be long-running.
- The source process version and target process version must have been created with WebSphere
Integration Developer V7.0.0. They must not originate from another authoring environment or be
created with a earlier version of WebSphere Integration Developer.

Validation of a process migration specification also ensures that only supported model
changes have been applied to the new (target) version. Unsupported changes are rejected
accordingly.

For more information about process instance migration refer to Migrating running process instances to a new version of the BPEL process.

### Example

To work through an example of process
instance migration, go to http://publib.boulder.ibm.com/bpcsamp/index.html?processTechniques&processModelingTechniques/instanceMigration.html.