# Adding a script action to a widget toolbar or menu

## About this task

To add a script action to a widget toolbar or menu:

## Procedure

1. In Case Builder, open the page that contains the
widget in Page Designer.
2. Click the Edit Settings icon for the widget that you want to add the
script action to.
3. Click the Menus or Toolbars tab and, if
necessary, select the specific menu or toolbar that you want to add the script action to.
4. Click the Add Menu Item icon or the Add Button
icon.
5. From the Action list, select Script Action.
6. If you are adding a script action to a toolbar, select a position from the
Alignment list.
7. For Label, enter the display name for the script action.
8. For Execute, enter the script to run when this script action is selected
from the toolbar or menu.
9. Optional: 
For Show this script action, enter a script that
is run to determine whether the button or menu item for this script action is visible. If you do not
enter a script, the button or menu item is always visible.
10. Optional: 
For Enable this script action, enter a script that
is run to determine whether the button or menu item for this script action is enabled. If you do not
enter a script, the button or menu item is always enabled.
11. Click OK.
12. Save and redeploy your solution.

## Example

The following example script action is intended to run in the context of the action
implementation. For more information, see Class icm.action.Action.

```
var selectedDocuments = this.getActionContext("Document");
if (dojo.isArray(selectedDocuments))
{
   var i;
   for (i=0; i<selectedDocuments.length; i++)
   {
      // attach selected document: selectedDocuments[i]
      ...
   }
}
else
{
    // attach selected document: selectedDocuments
    ...
}
```