# Defining a widget event

| Property     | Required or Optional   | Type   | Description                                                                                                                                                                  |
|--------------|------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id           | Required               | String | The unique identifier for the event.                                                                                                                                         |
| title        | Required               | String | The title of the event or event handler.                                                                                                                                     |
| functionName | Required               | String | For an incoming event, the name of the function that handles the event. This property is not used for outgoing events.                                                       |
| direction    | Required               | String | Indicates whether the event is incoming or outgoing. Set to subscribed for an incoming event and published for an outgoing event.                                            |
| type         | Required               | String | For an outgoing event, indicates whether the event is broadcast or wired. Set to broadcast for an event that is broadcast and set to wiring for an event that must be wired. |
| description  | Optional               | String | A description of the event. This text is used as hover help for the event in the Wiring window.                                                                              |

```
"events":[
                     {
                         "id":"icm.RoleChanged",
                         "title":"Role selected",
                         "functionName":"handleReceiveRole",
                         "direction":"subscribed",
                         "description":"Update the In-baskets widget to display the
                         in-baskets that are associated with the specified role."
                     },
                     {
                         "id":"icm.SelectRow",
                         "title":"Row selected",
                         "functionName":"handleSelectRow",
                         "direction":"published",
                         "type":"wiring",
                         "description":"The user clicked a row or pressed enter
                         in the in-basket to select the work item."
                     },
                     {
                         "id":"icm.OpenCase",
                         "title":"Open Case",
                         "functionName":"handleOpenCase",
                         "direction":"published",
                         "type":"broadcast",
                         "description":"Open a case object."
                     }
]
```