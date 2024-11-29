# Accessibility in Heritage Process Portal (deprecated)

## Accessibility features

- Keyboard-only operation
- Interfaces that screen readers commonly use
- Information communicated independently of color
- Accessible documentation
- Interfaces that do not induce seizures from photosensitivity

## Keyboard navigation

| Action                                                                                   | Key                                   |
|------------------------------------------------------------------------------------------|---------------------------------------|
| Change the focus to the item that you want to move.                                      | Press Tab or Shift+Tab.               |
| Select an item in the list.                                                              | Press the space bar.                  |
| Move the item to a new location in the list.                                             | Use the up arrow and down arrow keys. |
| Set the item to its new location in the list.                                            | Press the space bar.                  |
| Set the item to its new location, select it, close the list, and show the item in a tab. | Press Enter.                          |
| Cancel the operation and leave the item where it was originally.                         | Press Esc or Tab.                     |

| Action                                                                                   | Key                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Go to the first swimlane.                                                                | Press Tab, and then press the down arrow key.                                                                                                                                                                                                                                                                                                                                                 |
| Toggle between the tree-style navigation and the graph-style navigation that uses links. | Press F8.                                                                                                                                                                                                                                                                                                                                                                                     |
| Clear the focus and all elements in the current selection.                               | Press Esc.                                                                                                                                                                                                                                                                                                                                                                                    |
| Traverse the diagram.                                                                    | Use the arrow keys to traverse the diagram in accordance with the selected navigation style. For more information about the use of the arrow keys, refer to the table for the corresponding navigation style in Changing current focus from the keyboard.                                                                                                                                     |
| Zoom in on the diagram.                                                                  | Press Tab until you get to the slider, and then use the Left Arrow and Right Arrow keys to zoom in and out.                                                                                                                                                                                                                                                                                   |
| Toggle between a subprocess activity and its parent process.                             | Press Enter to open the subprocess activity.To return to the parent process, press Esc. This action closes the diagram view, and then you can reopen it.                                                                                                                                                                                                                                      |
| Traverse the diagram for a subprocess activity.                                          | Press F8 twice to turn on tree-style navigation. Use the arrow keys to traverse the nodes in the diagram.Press F8 again, to switch to graph-style navigation. Use the arrow keys to traverse the nodes and links in the diagram. For more information about the use of the arrow keys, refer to the table for the corresponding navigation style in Changing current focus from the keyboard. |
| Leave the Diagram view.                                                                  | Press Esc.                                                                                                                                                                                                                                                                                                                                                                                    |
| Print the diagram.                                                                       | Press Tab until you get to the Print Diagram button, and then press Enter to open the Print window.                                                                                                                                                                                                                                                                                           |

| Action                                    | Key                                                               |
|-------------------------------------------|-------------------------------------------------------------------|
| Traverse between date cells.              | Press the left arrow, right arrow, up arrow, and down arrow keys. |
| Go to the same day in the next month.     | Press Page Down.                                                  |
| Go to the same day in the previous month. | Press Page Up.                                                    |
| Go to the same day in the next year.      | Press Ctrl+Page Down.                                             |
| Go to the same day in the previous year.  | Press Ctrl+Page Up.                                               |
| Go to the first day in the month.         | Press Home.                                                       |
| Go to the last day in the month.          | Press End.                                                        |
| Select the date.                          | Press Enter.                                                      |

1. Press Tab until your reach the Stream button.
2. Press the up arrow key to hear the timeline information.

<!-- image -->

<!-- image -->

- When the borders for a widget are hidden, the widget menu and minimize and maximize controls are
unavailable. To show the borders to access these controls, press
Tab until the widget has focus and then press
Enter. This action is the same as hovering over the widget with the mouse and then
clicking the Show title bar link.
- When you create or edit a space, you can skip to the Save button by using
an accelerator. In Mozilla Firefox, use Shift+Alt+X. For Microsoft Internet Explorer, use Alt+X.

## Interface information

- Customizing display attributes: Heritage Process Portal:
relies on cascading style sheets to render the user interface correctly. However, the application
provides equivalent facilitation if you have reduced vision by using your system display settings,
including high-contrast mode. You can also increase the size of Heritage Process Portal pages by using your browser zoom
feature.
- Browsing to the sidebar: A WAI-ARIA main landmark is provided to help you go directly to the
sidebar panel that contains the Launch, Following, and
Mentions tabs when you use a screen reader.
- Zooming activity details in a Diagram view in Mozilla Firefox: Go to the
activity. When the activity details appear, click the window, and then Ctrl+Plus
sign key (+) to zoom in and Ctrl+Minus sign key (-) to zoom out of the
diagram.
- Using JAWS with forms controls: Generally, JAWS automatically changes from the virtual PC cursor
mode to forms mode when it encounters forms controls, such as input tags. If a control does not
respond to the keyboard, press Insert+Z to turn off the virtual PC cursor
mode.
- Using dashboards: The dashboards provided with Heritage Process Portal have the following accessibility capabilitiesand limitations:
    - In Heritage Process Portal V8.5.0 and earlier releases,
the My Team Performance dashboard and the Process Performance dashboard, which were based on the
scoreboard technology from earlier releases, were not fully accessible. Those dashboards were
deprecated in V8.5.0 and replaced with the Team Performance dashboard and the new Process
Performance dashboard, which are fully accessible.
    - The SLA Overview dashboard and the My Performance dashboard have accessibility limitations. They
can be zoomed up to 200 percent, and they are visible in high-contrast mode. However, they have only
partial keyboard and minimum contrast support, and their graphical charts have no text
alternatives.

<!-- image -->

- If a widget has focus and JAWS does not say the widget name, press Insert+Z to
turn off the virtual PC cursor. JAWS then says the widget name. JAWS also says the controls on the
widget border when you use the Tab key to browse through them.
- To make JAWS read the contents of the in-focus widget, press Insert and the
down arrow (Say All).
- In the Create Space window, traverse between the radio buttons by pressing
the up arrow or down arrow keys twice. If you press the arrow key only once, the drop-down list that
is associated with the radio button item gets focus. This behavior differs from the standard Windows behavior where pressing the arrow key once puts the
focus on the other radio button. You can also put focus on the drop-down list by pressing
Tab.
- In the Create Space window, if you use F4 to open a
drop-down list, press Insert+Z to turn off the virtual PC cursor so that you can
select an item from the list.

## IBM and accessibility

For more information about the commitment that IBM® has to
accessibility, see the IBM Human Ability and Accessibility Center.