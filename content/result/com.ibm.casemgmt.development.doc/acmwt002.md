# Adding an event action to a widget toolbar or menu

For example, you might add an event action to the In-basket widget toolbar for a custom event
that filters work items based on a predefined property value. You might add an event action to the
Case Information widget document menu for a custom event that enables users to
select and add a case document as an attachment to the case.

1. In Case Builder, open the page that contains the
widget in Page Designer.
2. Click the Edit Settings icon for the widget that you want to add the
event action to.
3. Click the Menus or Toolbars tab and, if necessary,
select the specific menu or toolbar to add the event action to.
4. Click the Add Menu Item icon or the Add Button
icon.
5. From the Action list, select Event Action.
6. If you are adding an event action to a toolbar, select a position from the
Alignment list.
7. For Label, enter the display name for the event action.
8. For Menu Identifier, enter an identifier that can be used by the event
handler to determine the menu or toolbar that the event action is triggered from.
9. For Event Name, enter the name of the handler for this event.
10. From the Event Type list, select how to publish the event.
Broadcast
Select Broadcast if the event is received by any event that has a
corresponding incoming event.
Wiring
Select Wiring if the event must be wired to an incoming event.
11. For Show this event action, enter a script that is
run to determine whether the button or menu item for this event action is visible. If you do not
enter a script, the button or menu item is always visible.
12. For Enable this event action, enter a script that
is run to determine whether the button or menu item for this event action is enabled. If you do not
enter a script, the button or menu item is always enabled.
13. Click OK.
14. Save and redeploy your solution.

## Event action payload definition

| Property      | Description                                                                                                                                                                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| menuId        | Identifier that can be used by the event handler to identify the source of the event.                                                                                                                                                             |
| eventName     | Name of the handler for the event.                                                                                                                                                                                                                |
| eventType     | Value that indicates how the event is published. This property is set to Broadcast if the event is received by any event that has a corresponding incoming event. This property is set to Wiring if the event must be wired to an incoming event. |
| actionContext | Action contexts that are set on the page widget that this event action is triggered from.                                                                                                                                                         |

## Example payloads

```
payload = {
menuId:     "customSearchMenu",
eventName:	 "customSearchEvent",
eventType:	 "broadcast",
Solution:	 icm.model.Solution
}
```

```
payload = {
menuId:        "customAttachMenu",
eventName:	    "customAttachEvent",
eventType:	    "broadcast",
Case:          icm.model.CaseEditable,
CurrentFolder: ecm.model.ContentItem,
ResultSet:	    ecm.model.ResultSet,
Folder:        ecm.model.ContentItem+,
Document:      ecm.model.ContentItem+
}
```