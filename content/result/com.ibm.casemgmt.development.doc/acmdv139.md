# Defining an action definition file

When you develop an action, create a IBM® class that
inherits from the com.ibm.ecm.extension.PluginAction class. In your class,
override the getAdditionalConfiguration() method to return a JSON object.

```
{"ICM\_ACTION\_COMPATIBLE": true,
    "context": null,
    "name": "Custom Add Case Action",
    "description": "An action to add cases from other solution",
    "properties": [
       {
          "id": "label",
          "title": "Add a custom Case",
          "defaultValue": "Custom Add Case",
          "type": "string",
          "isLocalized":false
       },
       {
          "id": "solution",
          "title": "Solution",
          "type": "string",
          "isLocalized":false
       },
       {
          "id": "caseType",
          "title": "Case Type",
          "defaultValue": "",
          "type": "string",
          "isLocalized":false
       }
    ],
    "events":[
       {
          "id":"icm.OpenAddCasePage",
          "title":"Open Add custom Case Page",
          "direction":"published",
          "type":"broadcast",
          "description":"Open Add Custom Case Page"
       }
    ]
};
```

| Property              | Required or Optional   | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------------|------------------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ICM\_ACTION\_COMPATIBLE | Required               | Boolean | Set to true if the action can be used in the IBM Business Automation Workflow action framework. This framework extends the IBM Content Navigator action framework to provide case-related functions. Always set this property to true for IBM Business Automation Workflow.                                                                                                                                                                                                                              |
| type                  | Optional               | String  | Indicates special processing for the action. The following values are valid for the type property: iterator Specify this value if the action is defined by using a method such as getIterator(). The method returns a series of items that are rendered as buttons or menu items. checkbox The action is rendered as a check box in the toolbar or menu. If you specify this value, you must also set the fieldname property value.                                                                      |
| fieldname             | Required               | String  | If the type property is set to checkbox, set this property to the identifier of a property that is defined in the properties array. If the type property is not set to checkbox, omit the fieldname property.                                                                                                                                                                                                                                                                                            |
| description           | Required               | String  | A brief description of the action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| context               | Required               | Array   | Indicates the contexts in which the action can be used. The array elements can take the following formats: [["Context 1", "Context 2"]] The action requires both Context 1 and Context 2 to run. ["Context 1", "Context 2"]  The action requires either Context 1 or Context 2 to run. [[“Context 1”, “Context 2”],[“Context 1”, “Context 3”], “Context 4”] The action requires Context 1 and Context 2 or Context 1 and Context 3 or Context 4 to run. [] The action does not require a context to run. |
| name                  | Required               | String  | The name that is displayed in the user interface for the action.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| properties            | Required               | Array   | The properties that a user can configure for an action in a toolbar or menu for a page widget or that are used internally by the action at run time.                                                                                                                                                                                                                                                                                                                                                     |
| events                | Required               | Array   | The events that are published by the action. This array can be empty if the action does not publish any events.                                                                                                                                                                                                                                                                                                                                                                                          |