# Visualize BPD tag groups (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a business process definition (BPD) in the Designer
view.
3. Click the Data Visualization button
in the upper right corner. Alternatively, click Playback > Visualize Process to view the
data visualization diagram. The data visualization
diagram opens in a new web browser window.
4. Select Tag Groups from the drop-down
list in the selection area on the left side in the browser window.
Under Tag Group Value, select the tag group
and its values that you want to visualize in the diagram on the right
side. Tag groups are represented by labels on
top of the activities in the diagram. The activities in the selected
business process definition (BPD) that have the same tag groups display
labels that have the same color. Where an activity is mapped to more
than one tag group, the labels that contain the tag groups are displayed
stacked on top of each other in a tab.
Note: A script activity
can call a service synchronously from a BPD using the tw.system.executeServiceByName() JavaScript
function. To visualize the tag groups defined for such a service,
an annotation that includes the service name must be added to the
script activity. Add the //@ServiceName annotation
followed by the exact name of the service, to the first line of the
script activity. For example, //@ServiceName "myService",
where myService is the exact name of the service.
5. Click the tab of stacked labels in the diagram to display
all the labels on top of the activity.
6. Click a subprocess within a process in the diagram to visualize
that subprocess. Tag groups are specific to the services
within a process. If the process and its subprocesses use the tagged
service, the tag groups are displayed for both.
7. Click the Minimize button on the left side to hide the
tag groups list and view only the data visualization diagram. Use
the zoom in or zoom out bar in the upper right corner to enlarge or
reduce the diagram size in the browser window.