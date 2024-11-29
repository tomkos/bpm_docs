<!-- image -->

# Keyboard shortcuts for the assembly editor

These shortcut keys apply when working with the assembly
editor.

After you open the assembly diagram with the assembly
editor, you can use keys to add and select elements. All the actions
that you need to perform on a selected element are available from
the element's pop-up menu, which you can invoke with the Shift+F10
keys.

These are the shortcut keys for the assembly editor:

| Key combination                                                 | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| →                                                               | Move to select the next element to the right of the current element. This generally means the next object to the right of the current one, but on the canvas, the element to the upper right or to the lower right might be selected.                                                                                                                                                                                                                                                                                           |
| Alt + ↓                                                         | Move one level down into the artifact. For example, if the component is selected, use this key to select its interface.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Alt + ↑                                                         | Move one level up.  For example, if the interface on a component is selected, use this key to select the component itself.                                                                                                                                                                                                                                                                                                                                                                                                      |
| ←                                                               | Move to select the previous element to the left of the current element. This generally means the next object to the left of the current one, but on the canvas, the element to the upper left or to the lower left  might be selected.                                                                                                                                                                                                                                                                                          |
| ↓                                                               | Move to select the element below the current element. This generally means the next object below the current one, but on the canvas, the element to the lower left or lower right might be selected.                                                                                                                                                                                                                                                                                                                            |
| ↑                                                               | Move to select the element above the current element. This generally means the next object above the current one, but on the canvas, the element to the upper left or upper right might be selected.                                                                                                                                                                                                                                                                                                                            |
| '.' or '>'                                                      | If an artifact (component, import, export, or stand-alone reference) is selected, either one of these keys cycles through the corners of the selected object. Follow this action with any one of the arrow keys to move the artifact. Use the Enter key to place the object in the new location, or use the Esc (Escape) key to cancel the move. If a wire is selected, the key cycles through the end-points of the wire. Follow this action with Alt+↑ and then the arrow keys to select a new target or source for the wire. |
| '|' or '/'                                                      | Cycles through the wires connected to the selected object. Use either of these keys for a selected partner reference, interface, or export. These keys also work on the collapsed references icon.                                                                                                                                                                                                                                                                                                                              |
| When selecting a reference: Ctrl + Home                         | Move the selected reference up                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| When selecting a reference: Ctrl + End                          | Move the selected reference down                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| When selecting the canvas: Ctrl + =                             | Zoom in                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| When selecting the canvas: Ctrl + -                             | Zoom out                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| When selecting the canvas: Shift + Insert                       | Paste                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| When selecting an artifact or multiple artifacts: Ctrl + Insert | Copy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| F2                                                              | Rename                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Esc (Escape) key                                                | Selects the background canvas. Also exits any action, such as moving a component. (From the background canvas, you can use any of the arrow keys to get back to navigating the diagram.)                                                                                                                                                                                                                                                                                                                                        |

Multiple selection can be done by using the Shift key
and one of the arrow keys.  This key combination will select the current
object and the one in direction of the arrow. If you want to select
two objects that are not next to each other, you use the spacebar
to select the current object and then press the Ctrl key together
with one of the arrow keys to keep the current selection and move
the cursor to the object in the direction of the arrow without selecting
it. This way, you can navigate to the object that you want to select
and press the spacebar to add the second object to the selection list.

## Adding an artifact to the assembly diagram

To
add an artifact to the canvas, use the Add pop-up
action from the canvas pop-up menu. For example, here are the instructions
to add a new component:

1. Move the focus to the canvas, the open area of the editor where
the components are assembled into a diagram. If a component is already
selected, press Esc to move to the canvas.
2. Press Shift+F10 to display the pop-up menu.
3. Press the down arrow (↓) until you select the Add menu
item. Press the right arrow to select Component (with no
implementation type) and press the spacebar. A component
is created on the canvas.
4. Press the dot (.) a number of times to select a corner of the
component so that you can drag it in the required direction. Then,
press one of the arrow keys to move the new component to the location
that you want.
5. Press Enter to fix the location of the new component.

## Wiring components

Use the Wire
(Advanced) action to launch the Advanced Wiring window
where you can select the reference that you want to wire and select
the target. When the window closes with your selections, the wiring
is completed in the assembly diagram.

This example demonstrates
how you can use the Advanced Wiring window to wire two components
in the assembly diagram. There are four unwired components in the
assembly diagram, as shown here:

Component2 has two references and we want to wire its
OneInterfacePartner reference to Component4, which has no interfaces.

1. In the assembly editor, use the right arrow key, →, to select
Component2.
2. Press Shift+F10 to open the pop-up menu.
3. Use the down arrow, ↓, to select Wire (Advanced) and
press the Enter key. The Advanced Wiring window opens.
4. The first option, Only show targets with matching interfaces check
box is selected. Press the spacebar to clear the check box. As a result,
the right container lists all the potential targets in the assembly
diagram.If the partner reference that you want to wire already
exists on Component2 and the target component has the matching interface,
then you can keep the Only show targets with matching interfaces option
enabled.  However, if you need to add a new reference or add the interface
on the target, you should disable this option.  Then, you can create
a wire from the source (or reference) to any potential target just
like the palette's wire tool or the wire handle.
5. The OneInterfacePartner reference on Component2 is already selected
so press the Tab key until you focus on the first component in the
right container.
6. Press the down arrow, ↓, till you focus on Component4 and press
the spacebar to select it. A message box appears to say that a matching
interface will be created on the target.
7. Press Enter to accept the OK and the message
box closes. The Component4 check box is selected.
8. Press Enter to accept the  OK in the Advanced
Wiring window. Component2 is wired to Component4 in the assembly diagram,
as shown here: