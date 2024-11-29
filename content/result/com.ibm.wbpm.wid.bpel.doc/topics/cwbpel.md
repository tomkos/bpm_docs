<!-- image -->

# BPEL process editor

The BPEL process editor has been designed to simplify the construction
of BPEL processes. The main white space is called the canvas and
it is where you create your process from the objects that you pull
from the palette to the left and with reference
to the objects in the tray on the right. Below
all of this is an interactive properties area
that changes to display pertinent details about whatever object you
currently have selected on the canvas or in the tray.

The BPEL process editor is divided into several distinct areas,
each with its own individual use.

<!-- image -->

1 The navigation bar
    - The navigation bar shows you where you are in your BPEL process.
The first breadcrumb on the left corresponds to the assembly diagram
and the second to the BPEL process itself. Subsequent breadcrumbs
correspond to activities nested within the BPEL process. You can navigate
through the levels using the bread crumbs in the navigation bar.
    - When you open certain activities in the canvas of your BPEL process
editor, the editor drills down to that activity. You will see a new
breadcrumb added to the navigation bar and the canvas displays only
the content of the selected activity. To move back up to the previous
level you can either double-click in the canvas area or click the
previous breadcrumb. In the previous screen capture, you can navigate
back to the BPEL process bp1 by clicking on
the bp1 breadcrumb in the navigation bar. If
there are multiple entries at a particular navigation level, a list
of the valid choices is presented when you click the navigation bar.
    - You can also use the navigation bar to jump to other levels of
the BPEL process directly by clicking the entry you want to display
and chosing the specific item from the list.
2 The palette Table 1. Basic palette tools Name Icon Description Selection tool Use this tool to select individual elementson the canvas. Hold the CTRL key while makingselections to select more than one. Marquee tool Use this tool to select multiple elements onthe canvas. Choose the tool, and then draw a box around the elementsthat you want to work with. Zoom in Use this tool to magnify portions of the canvas. Zoom out Use this tool to shrink the elements, and therebyincrease the size of the canvas. Create a note Use this tool to place a note anywhere on thecanvas. You can then enter text into the body of the note to labelspecific parts of your BPEL process. You can connect the note to oneor more activities in the BPEL process by creating associations.

- The palette is the shaded area to the left of the canvas that
houses the objects that you click and drag onto the canvas to build
your process.
- Hover over items in the palette to see a brief description of
that item.
- The icons are organized under several different headings that
act as toggles. Click the heading once, and the icons will remain
hidden until you click that heading again. This allows you to reduce
the complexity of the palette and keep those icons that you rarely
use out of sight.
- If you work with the same icons continually, you can gather them
into a Favorites folder. To put an icon in this folder, right-click
the icon and select Add to Favorites (If the
Favorites folder doesn't already exist, it will be created with the
first icon added to it.
- To hide the text labels once you are familiar with the
icons, right-click the palette, and toggle the Show Tool
Names setting.
- To increase the size of the icons, right-click the palette,
and toggle the Use Large Icons setting.

| Name           | Icon   | Description                                                                                                                                                                                                                                            |
|----------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Selection tool |        | Use this tool to select individual elements on the canvas. Hold the CTRL key while making selections to select more than one.                                                                                                                          |
| Marquee tool   |        | Use this tool to select multiple elements on the canvas. Choose the tool, and then draw a box around the elements that you want to work with.                                                                                                          |
| Zoom in        |        | Use this tool to magnify portions of the canvas.                                                                                                                                                                                                       |
| Zoom out       |        | Use this tool to shrink the elements, and thereby increase the size of the canvas.                                                                                                                                                                     |
| Create a note  |        | Use this tool to place a note anywhere on the canvas. You can then enter text into the body of the note to label specific parts of your BPEL process. You can connect the note to one or more activities in the BPEL process by creating associations. |

3 The canvas

- The canvas is the white empty area in the middle of the editor
that you use to assemble the activities to compose your BPEL process.
- When you click and drag an activity from the palette onto the
canvas, the icon beside your cursor has a plus symbol and you can
decide where you want to drop the activity. When the cursor becomes
a crossed out circle, continue moving the cursor until it becomes
a plus sign again.
- Structured activities (that contain other activities) appearing
on the canvas can be expanded or collapsed either by clicking the
plus () or minus () icons.
- If your process contains structured activities you can drill
down into these activities by double-clicking on them in the canvas.
The navigation bar at the top of the canvas can be used to return
to the enclosing activity or process.
4 The action bar

- The action bar is a miniature dialogue that displays beside certain
activities when you've selected them, and it contains a series of
one or more icons that are relevant to that activity.
5 The tray Table 2. Tray icons Name Icon Description Add tool Click this to create a new partner, global variable,correlation set or correlation property. Remove tool Click this to remove an existing partner, variable,correlation set or correlation property. Sort variables tool Use this tool to arrange the variables alphabetically.Once you turn this setting on , then all newly added variablesare automatically sorted alphabetically against existing ones. Youcan also reorder variables by right-clicking on individual variablesand then choosing Move Up or MoveDown . Add a local variable Use this tool create a new local variable. Localvariables are created within individual scopes, and are availableonly to the objects within the scope for which the variable was created.This button is only enabled when you have a scope or collaborationscope selected.

- The tray displays the Partners, Variables, Correlation
sets and Correlation properties that are associated with
your process.
- Partners and Correlation sets can be dragged and dropped directly
onto the canvas. You can drop a partner on to the canvas to create
a fully configured invoke activity that when executed, will call (or
invoke) the partner. You can drop correlation sets within existing
activities and further configure them in the Properties view.
- To see the interfaces and operations associated with the partners,
click the small gray arrow beside the name of the partner.
- Click the dark horizontal arrow to collapse or expand the tray.
Click the individual headings to collapse or expand that section allowing
you to put those icons that you rarely use out of sight.

| Name                 | Icon   | Description                                                                                                                                                                                                                                                                                          |
|----------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Add tool             |        | Click this to create a new partner, global variable, correlation set or correlation property.                                                                                                                                                                                                        |
| Remove tool          |        | Click this to remove an existing partner, variable, correlation set or correlation property.                                                                                                                                                                                                         |
| Sort variables tool  |        | Use this tool to arrange the variables alphabetically. Once you turn this setting on, then all newly added variables are automatically sorted alphabetically against existing ones. You can also reorder variables by right-clicking on individual variables and then choosing Move Up or Move Down. |
| Add a local variable |        | Use this tool create a new local variable. Local variables are created within individual scopes, and are available only to the objects within the scope for which the variable was created. This button is only enabled when you have a scope or collaboration scope selected.                       |

6 The properties view

- This area displays properties that are relevant to the object
that is currently selected on the canvas or the tray. click the tabs
to the left of this view to toggle through the pages. Some pages display
properties in tabular format, and you can add or modify these properties
by clicking the appropriate cell and then interacting with the graphical
interface that appears. Properties marked with an * are
mandatory.
- The contents of the page will differ on the activity or object
chosen. In all cases, you can press F1 (or Ctrl+F1 on
a Linux® system) to launch
a help window and click the link to be taken directly to the product
documentation for more details.

- Administration tab: BPEL process editor

This topic includes a description of each of the fields on the Administration tab of the Properties view.
- Authorization tab: BPEL process editor

This topic includes a description of each of the fields on the Authorization tab of the Properties view.
- Compensation tab: BPEL process editor

This topic includes a description of each of the fields on the Compensation tab of the Properties view.
- Choosing the appropriate compensation for your process

There are two ways in which you can compensate a business processes. Here are some suggestions on how to choose the one that is best for you.
- Correlation tab: BPEL process editor

This topic includes a description of each of the fields on the Correlation tab of the Properties view.
- Correlating BPEL processes

Correlations are used in runtime environments where there are multiple instances of the same process running. The sets allow two partners to initialize a BPEL process transaction, temporarily suspend activity, and then recognize each other again when that transaction resumes.
- Defaults tab: BPEL process editor

This topic includes a description of each of the fields on the Defaults tab of the Properties view. The values you supply on this tab become the default values for appropriate activities, but the values can be overridden when you configure the individual activities.
- Description tab: business state machine editor

This topic includes a description of each of the fields on the Description tab of the Properties view.
- Customizing behavior with visual snippets
- Details tab: BPEL process editor

This topic includes a description of each of the fields on the Details tab of the Properties view.
- Versioning business state machines

You can create new versions of your business state machine, so that multiple versions of those same business state machines can coexist in a runtime environment.
- Adding a variable to a business state machine

Variables store the data that are used by a business state machine.
- Defaults tab: BPEL process editor

You use the Defaults tab shows in the Properties view when you are working on a BPEL process. You use the Defaults tab to set default values .
- Environment tab: Human Task editor

This topic includes a description of each of the fields on the Environment tab of the Properties view. This tab is available when you select the task itself.
- Using custom properties for human tasks

Custom properties are used to categorize a task, and can be useful for querying, sorting, and filtering tasks.
- Exit tab: business state machine editor

This topic includes a description of each of the fields on the Exit tab of the Properties view.
- Expiration tab: BPEL process editor

This topic includes a description of each of the fields on the Expiration tab of the Properties view.
- Import tab: BPEL process editor

This topic includes a description of each of the fields on the Import tab of the Properties view.
- Java Imports tab: BPEL process editor

This topic includes a description of the Java Imports tab of the Properties view.
- Join Behavior tab: BPEL process editor

This topic includes a description of each of the fields on the Join Behavior tab of the Properties view.
- Link Evaluation Order tab: BPEL process editor

Outgoing gateways have multiple outgoing links, you can prioritize links of a split gateway using the Link Evaluation Order tab of the Properties view.
- Working with generalized flow activities

The generalized flow activity is very similar to a parallel activity in that you can nest other process activities within it, and then control the execution order of those activities through links. The generalized flow activity differs however in its ability to use conditional links to loop back to previous activities in the sequence.
- Query properties tab: BPEL process editor

This topic includes a description of each of the fields on the Query properties tab of the Properties view.
- Repeat tab: BPEL process editor

This topic includes a description of each of the fields on the Repeat tab of the Properties view.
- Server tab: BPEL process editor

This topic includes a description of each of the fields on the Server tab of the Properties view.