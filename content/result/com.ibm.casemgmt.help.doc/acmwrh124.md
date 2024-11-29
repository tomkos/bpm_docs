# Timeline Visualizer widget

The Timeline Visualizer widget is included on the Case Details page by
default. You can also include it on the Work Details page.

The widget uses a horizontal bar, the timeline to show the time duration of each
task and work item for the current case. The widget uses vertical bars to represent events, such as
filing a document into the current case or changing the properties of the current case. In addition,
the widget includes an event density histogram that provides an overview of when in time case events
occurred over the entire life of the current case.

By navigating through the events, tasks, and work items, you can use the extended history to
   determine the status of a specific case. By comparing the extended history for different cases,
   you can identify potential problems with the workflow that is defined for a case type. For
   example, you might notice that delays tend to occur during the review step in a particular task.
   You can then determine an approach to reduce this delay.

To use the Timeline Visualizer, a case history store must be enabled and configured. Use the
workflow Case administration client to
configure the extended history. When you configure the extended history, you create the Case History
table and select the properties to configure properties auditing. In addition, consider excluding
properties whose value is unlikely to change. Excluding such properties reduces clutter in the
widget, avoids wasting disk space, and helps performance. Users can still get the values of these
properties from the case objects themselves.

By default, the Timeline Visualizer widget initially displays only
a high-level timeline that shows the case events. The user can then
expand the widget to view an event histogram or the task list for
the case. The event histogram shows the density and distribution of
case events. The task details can be further expanded to show the
work items for each task. The widget switches to full-page mode when
it is expanded. You can configure this widget so that the histogram
and task list are expanded by default.

The widget initially displays a time range that is based on the
number of events that you specify in the widget settings. A user can
change the time range by using sliders in the timeline.

By default, the history events are collected every 2 minutes from
the server. Therefore, there is a slight delay before the events are
displayed in the Timeline Visualizer widget.

The following settings can be configured in case timeline visualizer widget to affect how events
are displayed. The settings are useful to control initial display of events in the widget, from a UI
perspective. The settings do not affect how events are retrieved from the case history store.

- Show only this number of tasks and workitems: The maximum number of tasks
and work items to be shown in the tasks list. Case visualizer displays all tasks and work items by
default. If this setting is configured, then widget size restricts the number of tasks and all
remaining tasks are shown inside scroll bar.
- Default time range to display (in number of events): Controls the time
range the widget initially displays based on the number of events that is specified. Users can
manually change the time range after the widget is loaded by using sliders in the timeline.

## Workflow pages that include this widget by default

The Timeline Visualizer
widget is included on the Case Details page by
default.

- Enabling the widget to display process activities

 Traditional: 
To view workflow process activity details in the Case History visualizer widget, the Case History event emitter needs to be installed and configured in the Business Automation Workflow on-premises environment.
- Timeline Visualizer widget events

The Timeline Visualizer widget publishes outgoing events to display the extended history for a case.