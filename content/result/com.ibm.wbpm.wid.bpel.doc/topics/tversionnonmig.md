<!-- image -->

# Creating a new version of your process - running instances
use old version

## Before you begin

## About this task

To create a new version of a process, you will need a new module where the process version is
contained (since you need a new deployment container). If the process originated from IBM®
WebSphere® Business Modeler, new versions of all projects are also created
during export from IBM
WebSphere Business Modeler. For clients that use
late binding to invoke this process, the runtime engine is able to recognize that the new process is
actually a more recent version of the other, and will select it over the older one. Running
instances cannot migrate to the new version, unless you also include a migration plan.

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
2 On the first page of the Wizard, specify either a new Nameor a new module version. Which one you specify depends on whetherthe process is contained in a non-versioned module (default) or aversioned module. The first page of the wizard presentsthe following: In case the process you create is a new version of theoriginal module from IBMWebSphere Business Modeler , youmay need to provide names and versions for more than one module andlibrary. When a process is exported from IBMWebSphere Business Modeler to IBM IntegrationDesigner ,there are various export settings: The recommended export settingin IBMWebSphere Business Modeler is2 Modules + 1 Library, but you can also choose Module + library, ormodule only. Depending on the option that has been chosen in Modeler,the new process version wizard detects these project sets and treatsthem as a single unit.

- Non-versioned Business Integration Module: On the first wizard
page, specify the new module name. The wizard leaves the original
module untouched and creates a new module with the newly specified
name for further editing.
- Versioned Business Integration Module: On the first wizard page,
specify the new module version. The wizard creates a backup copy of
the original module for WID internal use only (not used by WID users),
and updates the module version of the current module for further editing.
- If the process came from IBM
WebSphere Business Modeler, in
steps a or b above, you may be prompted to specify new versions for
more than one module and a library. Follow steps a and b shown above.

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
2. You should not create process migration specifications
if you want to achieve that the running instances continue to run
on the old process version.
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
The Wizard suggests a unique namespace for every Business Rule Group.
For the associated rule logic artifacts (Decision Table and Rule Set),
a unique name/namespace combination must be provided as well. The
Wizard suggests a unique name/namespace combination for every rule
logic artifact. If you are satisfied with the Wizard suggestions,
click next. Otherwise, click in the appropriate table row in the New
Name column to start a dialog box and adjust the name or namespace
to your needs.
7. If your module(s) contains Selectors, you must specify
at least a new namespace for each Selector. The Wizard suggests a
unique namespace for every Selector. If you are satisfied with the
Wizard suggestions, click Next. Otherwise, click in the appropriate
table row in the New Name column to start a dialog box and adjust
the name or namespace to your needs.
8. It might happen that after finishing the New Process Version
Wizard, an "Unhandled Artifacts" dialog box appears. If so, manual
adjustments might be needed. For Details, refer to Table 1 below.
9. Once the versioning process has completed, you now have
your new process version residing in your new module. Make the changes
you want to the new version of the BPEL process.
10. Save your work.
11 You can deploy this new module as you would any other module. Refer to the following table for step 8 shown above. Thetable below defines artifacts that are not automatically handled duringthe creation of a process version, and need a manual adjustment asdescribed in the user action column if they are used. Table 1. Artifact Type User Action Dynamic Assembler Configure the newly created Dynmic Assemblerin your new Module version using the Studio tools available in WebSphereIntegration Developer HTTP Export Binding Clients would need to be updated in order to use the new version. Web Service Export Binding (JAX-WS and JAX-RPC) Clients would need to be updated in order to use the new version. Generic JMS Export Binding Must not be shared between modules and need to be manuallychanged. Generic JMS Import Binding Must not be shared between modules and need to be manuallychanged. Care should be taken to set a matching send destination ifthe target module end point has also changed JMS Export Binding Must not be shared between modules and need to be manuallychanged. JMS Import Binding Must not be shared between modules and need to be manuallychanged. Care should be taken to set a matching send destination ifthe target module end point has also changed. MQ Export Binding Must not be shared between modules and need to be manuallychanged. Clients would need to be updated to new queue names. MQ Import Binding Must not be shared between modules and need to be manuallychanged. Care should be taken to set a matching send destination ifthe target module end point has also changed. Clients would need tobe updated to new queue names. MQ JMS Export Binding Must not be shared between modules and need to be manuallychanged. Clients would need to be updated to new queue names. MQ JMS Import Binding Must not be shared between modules and need to be manuallychanged. Care should be taken to set a matching send destination ifthe target module end point has also changed. Clients would need tobe updated to new queue names.

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