# The collaboration event handler (deprecated)

## Usage

To
include the default collaboration behavior in your own collaboration(event) logic,
you can invoke the super-class collaboration logic inside your collaboration(event) function
by using the syntax: this.constructor.prototype.collaboration.apply(this,
[event]);

To fire a custom collaboration event, use this.context.triggerCollaboration().
For more information, see The coach view context object.

## event object

| Property     | Type   | Description                                                                                                                                                                            |
|--------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| type         | String | Valid values are "focus" | "blur" | "dataChange" | "custom" Each event type has its own set of properties described in Table 2.                                                        |
| domId        | String | Indicates the dom node with which this collaboration event is associated. For example, on a focus event, domId indicates the dom node that has gained focus in another user's browser. |
| outlineColor | String | Only exists for focus events. Indicates the color to highlight the node.                                                                                                               |
| color        | String | The foreground color of the hover area                                                                                                                                                 |
| bgColor      | String | The background color of the hover area                                                                                                                                                 |
| message      | String | A message string associated with this event                                                                                                                                            |
| userName     | String | The name of the collaborator who triggered this collaboration event. For example, the user who changed data.                                                                           |
| payload      | String | User defined data that is used with the custom event. This property is only used in the custom event.                                                                                  |

| Event type   | Properties                                            |
|--------------|-------------------------------------------------------|
| focus        | type, domId, outlineColor, color, bgColor, message    |
| blur         | type, domId                                           |
| dataChange   | type, domId, color, bgColor, message, userName, value |
| custom       | type, payload                                         |