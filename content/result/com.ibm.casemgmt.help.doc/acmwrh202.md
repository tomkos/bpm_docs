# Process History widget

The Process History widget displays the milestones that the workflow
author defines to represent key points in the workflow. The user can
track the progress of the workflow by viewing the milestones. For
a pending milestone, the widget displays only the milestone name.
For a reached milestone, the widget displays the milestone name, an
icon, the milestone message, and the date on which the milestone was
reached.

- Add Activity page
- Add Activity Form page
- Cases page
- Form Attachment Work Details page
- Work Details page
- Work Details Form page

You can also add the Process History widget to the Work page.
On this page, you must manually wire the icm.SelectWorkItem event
that is published by the In-baskets widget to the icm.sendWorkItem
event that is handled by the Process History widget.

You can edit the settings for the Process History widget to specify
the highest milestone level that is to be visible to users. The Process
History widget displays milestones at the specified level and any
lower levels. For example, if you enter 5, the Process History widget
displays milestones at levels 1, 2, 3, 4, and 5. By default, users
see only milestones with level 1.

- Process History widget events

The Process History widget handles incoming events to display the history for tasks and work items.