# Configuring integration with IBM Business Automation
Workflow
fails

## Symptoms

Step 5: --error message: Define Target
Environment * Configure Case Integration with IBM Business Automation Workflow ***********An error
occurred while running Configure Case Integration with IBM Business Automation Workflow The task
failed because of the following error: The value given for a property or list element lies outside
the permitted range or value set, or exceeds the maximum length allowed. The length of the value
(160) specified for property CmAcmUserName1 exceeds the maximum permitted length
(128).

## Resolving the problem

Alternatively, you can configure IBM® Business Automation
Workflow to support long user name while running the
Configure case integration with IBM Business Automation Workflow task:

1. In the Administrative Console for Content Engine, go to the target object store.
2. Go to Data Design > Classes > Custom Objects and select the OneBPM Integration Data custom object.
3. Go to Property Definitions and select the User Name 1 property
definition.
4. On the More tab, change the maximum string length from 128 to 1056.
5. Repeat this procedure for the User Name 2 property definition.
6. Click Save.