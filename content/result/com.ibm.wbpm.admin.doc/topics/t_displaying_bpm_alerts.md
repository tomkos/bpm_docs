# Displaying BPM alerts

## About this task

## Procedure

In the application, service, or dashboard that displays
or handles alerts, use the following APIs:

- To retrieve a list of filtered alert definitions:
    - JavaScript API:BPMAlertDefinition[] getAlertDefinitions(String[] categoryFilter , Boolean checkAuthorization)The
filter is to retrieve just process instance alert definitions, just
task alert definitions, or the alert definitions from both categories.
    - REST API:GET /rest/bpm/wle/v1/system/alertDefinitions[?categories={category1,category2,...}]
- To retrieve the specified alert definitions, the valueof what they are monitoring, and whether the alert definition hastriggered an alert:

- JavaScript API:BPMAlertDefinitionStatusResponse getAlertDefinitionsStatus(String[] ids , Boolean checkAuthorization)
- REST API:GET /rest/bpm/wle/v1/system/alertDefinitions/status[?ids={string}]

## Example