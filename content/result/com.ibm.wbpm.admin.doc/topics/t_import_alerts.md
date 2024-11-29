# Copying alert definitions from one system to another

## About this task

## Procedure

1 In the source system, use the following API to retrievethe alert definitions that you want to copy The filter is to retrieve just process instance alert definitions,just task alert definitions, or the alert definitions from both categories.
    - REST:GET /rest/bpm/wle/v1/system/alertDefinitions[?categories={category1,category2,...}]
    - JavaScript: BPMAlertDefinition[] getAlertDefinitions(String[] categoryFilter , Boolean checkAuthorization)
2 Use the following API to save the alert definitions tothe target system: The importMode parameter determinesthe following behaviors: If the importMode parameter is false, thedefault value, the alert definitions are saved only if the processapplication, snapshot, and process exists on the target system. Ifan alert definition with the same name already exists in the targetsystem, the API updates that definition. If the importMode parameteris true, the alert definitions are saved regardless of whether thetarget system has the process application, snapshot, and process.If an alert definition with the same name already exists in the targetsystem, the API generates a new name to create a different alert definition.This action preserves the original alert definition so that the originaldefinition and the newly-saved definition can coexist. The API saves an alert definition if it complies withthe following restrictions:

- REST:PUT/POST /rest/bpm/wle/v1/system/alertDefinitions[?importMode=false]
- JavaScript:BPMAlertDefinition[] saveAlertDefinitions(BPMAlertDefinition[], Boolean importMode, Boolean checkAuthorization)

- Whether you want to save the alert definitions that are monitoring
only the process applications, snapshots, and process (business process
definition) that are on the server or save all of the alert definitions
regardless of what they are monitoring.
- Whether to update existing alert definitions or create new ones
if there are matching names.

- The name of the alert definition must be specified.
- The threshold value and the operator must be specified and valid.
- The instance status and the task status values must be empty or
valid.
- In the BPMAlertDefinition object, the projectId, snapshotId,
and bpdId, properties are valid IDs in external
String format and the category property has a
value of INSTANCE or TASK. Alert
definitions created in Process Admin Console have valid property values.
3. Open the Process Admin Console on the new system.
4 Review the imported alert definitions and edit them wherenecessary. In particular, the following fields might havestrange values if what the definition is monitoring does not existon the server: For example, if you save an alert definition with the importMode parameterset to true and the snapshot being monitored by the definition doesnot exist on the target server, the snapshot field for the definitioncan have a set of random-looking characters. In this case, edit thealert definition to point to the appropriate snapshot.

- Process App
- Snapshot
- Process

For example, if you save an alert definition with the importMode parameter
set to true and the snapshot being monitored by the definition does
not exist on the target server, the snapshot field for the definition
can have a set of random-looking characters. In this case, edit the
alert definition to point to the appropriate snapshot.