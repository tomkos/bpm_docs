<!-- image -->

# Keyboard shortcuts for the mediation flow editor

This topic describes the shortcut keys that apply when
working with the mediation flow editor and the XPath expression builder
that is launched from the mediation flow editor.

## Mediation flow editor shortcuts

After you
open the mediation flow with the mediation flow editor, you can use
keys to add and select elements. All the actions that you need to
perform on a selected element are available from the element's pop-up
menu, which you can invoke with the Shift+F10 key.

These
are the shortcut keys for the mediation flow editor:

| Key combination                     | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| →                                   | Move to select the next element to the right of the current element.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Alt + ↓                             | Move one level down into the node.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Alt + ↑                             | Move one level up.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ←                                   | Move to select the previous element to the left of the current element.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ↓                                   | Move to select the element below the current element.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ↑                                   | Move to select the element above the current element.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| '.' or '>'                          | If a node (input, input response, input fault, mediation primitive, callout, callout response, callout fault) is selected, either one of these keys cycles through the corners of the selected object.  Follow this action with any one of the arrow keys to move the node around.  Use the Enter key to place the object in the new location, or use the Esc (Escape) key to cancel the move.  If a wire is selected, the key cycles through the end-points of the wire. Follow this action with Alt+↑ and then the arrow keys to select a new target or source for the wire. |
| '|' or '/'                          | Cycles through the wires connected to the selected object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| When selecting the canvas: Ctrl + = | Zoom in                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| When selecting the canvas: Ctrl + - | Zoom out                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| F2                                  | Rename                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Esc (Escape) key                    | Selects the background canvas. Also exits any action like moving a mediation primitive or multiple selection.  (From the background canvas, you can use any of the arrow keys to get back to navigating the flow.)                                                                                                                                                                                                                                                                                                                                                             |

Multiple selection can be done by using the Shift key
and one of the arrow keys.  This key combination will select the current
object and the one in direction of the arrow. If you want to select
two objects that are not next to each other, you use the spacebar
to select the current object and then press the Ctrl key together
with one of the arrow keys to keep the current selection and move
the cursor to the object in the direction of the arrow without selecting
it. This way, you can navigate to the object that you want to select
and press the spacebar to add the second object to the selection list.

## XPath expression builder shortcuts

After
you launch the XPath expression builder, you can use keys to move
the cursor within the editor. These are the shortcut keys for the
XPath expression builder:

| Key combination                                   | Function                                                                                                                                                 |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ctrl + Tab                                        | Move between the different areas of the XPath expression builder; Schema viewer, XPath Construction, Full XPath expression, Override and action buttons. |
| Space bar                                         | Toggle Override check box.                                                                                                                               |
| Key combination                                   | Function in the Schema Viewer                                                                                                                            |
| ↑                                                 | Move one level up                                                                                                                                        |
| ↓                                                 | Move one level down                                                                                                                                      |
| →                                                 | Expand tree view                                                                                                                                         |
| ←                                                 | Collapse tree view                                                                                                                                       |
| Key combination                                   | Function in the XPath construction area (XPath location, Condition, Value)                                                                               |
| "↑" , "↓" , "→" , or "←"                          | Use the up, down, right or left arrow keys to move between the fields in this area                                                                       |
| Ctrl + Space Bar                                  | Displays the assistant window in the Condition and Value fields                                                                                          |
| Ctrl + Esc (Escape) key                           | Close the assistant window in the Condition and Value fields                                                                                             |
| arrow keys ("↑" , "↓" , "→" , or "←") + Enter key | Use the arrow key to highlight from the assistant in the Condition and Value fields, and hit enter to make a selection                                   |