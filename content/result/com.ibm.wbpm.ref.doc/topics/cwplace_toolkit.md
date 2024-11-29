# Workplace
toolkit

- Views in the Workplace toolkit
- Customizing the views

- A JavaScript file that provides the behavior of the
view
- Image files to represent the view on the palette and on the canvas
- A preview JavaScript file that shows a preliminary image of the view

<!-- image -->

## Views in the Workplace toolkit

| View name       | Description                                                                                                                                                                                                                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Instance List   | Adds an instance list widget to your dashboard, which lists all the workflow instances that you are authorized to see and participate in. You can sort, filter by app, and reload the instances in the list.For the methods and event handlers that are available for the view, see Instance List.                                           |
| Instance Viewer | Adds an instance viewer widget to your dashboard, which displays data that is relevant to the workflow instance.For the methods and event handlers that are available for the view, see Instance Viewer.                                                                                                                                     |
| Task List       | Adds a task list widget to your dashboard, which lists all the tasks that you claimed or you've been assigned, as well as the unclaimed tasks that are assigned to your team. You can search, sort, filter by app, reload, and open the tasks in the list.For the methods and event handlers that are available for the view, see Task List. |
| Task Viewer     | Adds a task viewer widget to your dashboard, which displays data that is relevant to the task. For the methods and event handlers that are available for the view, see Task Viewer.                                                                                                                                                          |

## Customizing the views

- Name: PFS
- Value: PFSEndpoint

- Name: WORKFLOW
- Type: Registry Lookup
- Category: IBM\_WORKFLOW
- Key: WORKFLOW\_SYSTEM
- Authentication: OpenID Connect

- Add the Task Viewer to the coach to display the task and instance details.
- Select the Enable instance launch configuration option in the Instance
List view to enable instances to open when you click their name.
- Select the Enable task launch configuration option in the Task List view
to enable tasks to open when you click their name.

- For Task List, select Open task in new window to open all the tasks in a
new window or tab.
- For Instance List, select Open instance in new window to open all the
instances in a new window or tab.

1. Clear the Open task in new window or Open instance in new
window option.
2. Add all the existing views in a Vertical layout container, except
for the Task Viewer and Instance Viewer.
3 Add the following line of code to the specified events in the corresponding views, asfollows:this.ui.getSibling("Vertical\_Layout1").setVisible(false,true); whereVertical\_Layout1 is the control ID of the vertical layout container.

```
this.ui.getSibling("Vertical\_Layout1").setVisible(false,true);
```

    - In the Task List view, add the code to the "On task launched" event.
    - In the Instance List view, add the code to the "On instance launched"
event.
    - In the Task Viewer view, add the code to the "On task opened" and "On
service opened" events.
    - In the Instance Viewer view, add the code to the "On instance UI launched"
event.
4 Add the following line of code to the specified events in the corresponding views, asfollows:this.ui.getSibling("Vertical\_Layout1").setVisible(true,true); where Vertical\_Layout1 is the control ID of the vertical layout container.

```
this.ui.getSibling("Vertical\_Layout1").setVisible(true,true);
```

- In the Task Viewer view, add the code to the "On task closed" and "On
service closed" events.
- In the Instance Viewer view, add the code to the "On instance closed"
event.