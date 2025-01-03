# icm.model

Case Client is
a plug-in to IBM® Content
Navigator.
The IBM Content
Navigator model provides
the capabilities for searching and retrieving Content Platform Engine objects on the server.
However, this model lacks the semantics for the case management context.
Therefore, the IBM Business Automation
Workflow model
provides the mechanism for adding the context that is needed for users
to search and retrieve case management objects.

The IBM Business Automation
Workflow model
classes are derived from the base classes in the IBM Content
Navigator
JavaScript model. In addition, some workflow model
classes use the functionality of IBM Content
Navigator classes. For
example, an WorkItem object is obtained by using an
ecm.model.WorkItem object.

A
model class also defines methods that enable the object to reference
related case management objects. For example, the Case.retrieveTasks() method
is used to fetch Task objects that are related
to a case. In many situations, a widget uses the model objects received
in an event payload to navigate the model API and retrieve needed
information. This ability simplifies the data that a widget must pass
in events because a widget can pass a model object instead of passing
all the information for that object. For example, an event to open
a work item can pass a WorkItem object or a WorkItemEditable object
in the payload. If this work item event is received by a milestones
widget, that widget can call the appropriate model API method to retrieve
the milestones. The originating widget does not need to collect and
pass the milestone information.

For certain objects, the model
defines two related classes. The persistent class represents the object
as it is saved in the object store. The other class represents an
editable version of the object. This editable class, sometimes called
a scratchpad, represents the object as it is being edited.

- The CaseEditable object is saved.
- A CaseEditable object that was obtained from
the same Case object is saved.

For editable properties, the onChange() methods,
such as onChoiceListChanged and onValueChanged,
notify the widgets when updates are made to the editable object. The
changes that are made to the editable object are saved to the corresponding
persistent object only when the user saves the page.

The editable
object is shared only by widgets that are on the same page. If multiple
pages related to the same object are open, each page has its own editable
object. However, the model is defined so that when a user saves changes
to the editable object on one page, the editable objects on the other
pages are refreshed. The widgets on these pages are notified of changes
by listening for the event that is triggered by the onRefresh() method
on the editable object.

| Persistent class      | Editable class         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Case                  | CaseEditable           | Represents a case.To obtain a CaseEditable object to create a case, call the createNewCaseEditable method on the Solution object. To obtain a CaseEditable object to edit an existing case, call the createEditable method on the Case object. The propertiesCollection attribute of the CaseEditable class provides a collection of PropertyEditable objects. Each PropertyEditable object represents a property value for a case.                                                                                                                                                                                                                   |
| CaseComment           |                        | Represents a comment that is entered for a case.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| CaseRelationship      |                        | Represents the relationship between two cases.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| CaseType              |                        | Represents a case type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DocumentType          |                        | Represents a document class.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| HistoryEvent          |                        | Represents the record of an event in a case history.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| InbasketDynamicFilter |                        | Represents a dynamic filter type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| InbasketFilter        |                        | Represents a inbasket filter type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| None                  | PropertyEditable       | Represents a property of a case or a parameter of a launch step or work item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ResultSet             |                        | Represents a set of search results or other items that are returned by a query to the content server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Solution              |                        | Represents a solution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Task                  | TaskEditableLaunchStep | Represents an activity.TaskEditable objects are primarily used to represent new discretionary activities. To obtain a TaskEditable object for a discretionary activity, call the createNewTaskEditable method on the Case object.  To obtain a TaskEditable object to edit an existing activity, call the createEditable method on the Task object. For discretionary activities, the model includes the LaunchStep class that represents the launch step of a workflow. The propertiesCollection attribute of this class provides a collection of PropertyEditable objects. Each PropertyEditable object represents a parameter for the launch step. |
| TaskType              |                        | Represents an activity type in a deployed case management solution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Timeline              |                        | Represents a timeline object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| TimelineEvent         |                        | Represents a timeline event of a given case.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| TimelineOverview      |                        | Represents a timeline overview of a given case.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TimelineTask          |                        | Represents a timeline activity of a given case.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TimelineWorkitem      |                        | Represents a timeline work item of a given activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| WorkItem              | WorkItemEditable       | Represents a work item.To obtain a WorkItemEditable object, call the createEditable method on the WorkItem object. The propertiesCollection attribute of this class provides a collection of PropertyEditable objects. Each PropertyEditable object represents a parameter for the work item.                                                                                                                                                                                                                                                                                                                                                         |

The following classes are included in the icm.model.properties.controller package:

## Related reference

- icm.action
- icm.base
- icm.dialog
- icm.pgwidget
- icm.util
- icm.widget.menu