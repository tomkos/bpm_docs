# Navigation Controller

## Restrictions and limitations

- This view does not use the visibility property.

## Configuration properties

| Configuration property      | Property variable              | Description                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Human service end event URL | navigationURL (String)         | The URL that can be used to navigate to the end event node in a client-side human service.  If you specify a URL, the Navigation Controller can be used to trigger a boundary event to end a human service. If a URL is not specified, you can still use the Navigation Controller to navigate between dashboards without the use of an end node. Default: None |
| Disable boundary event      | disableBoundaryEvent (Boolean) | Determines whether the Navigation Controller is prevented from triggering a boundary event. When the variable is set to true, the Navigation Controller does not fire a boundary event. Use this setting to prevent navigation away from the coach in specific circumstances, for example, if the current coach has unsaved local changes.  Default: false      |