# In-baskets widget outgoing events

## In-basket selected event

| Description   | The user opened the page that contains the In-baskets widget or has clicked a tab to display a different in-basket.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SelectInbasket                                                                                                    |
| Type          | Wired                                                                                                                 |
| Payload       | selectInbasket An ecm.model.ProcessInbasket object that represents the in-basket that is to be displayed.             |

## Open work detail page event

| Description   | The user selected a work item to open.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.OpenWorkItem                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Type          | Broadcast                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Payload       | workitem An icm.model.WorkItemEditable object that represents the selected work item. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. UIState A Dojo Stateful object that is used internally by the widgets in the same page. This object can contain the following properties: GetNext This property determines whether the next work item is to be opened automatically. workitemReadonly This property determines whether the work item is to be opened in view mode. GetNextCfg This property determines the configuration of the Open Next Work Item action. |

## Work item selected event

| Description   | The user clicked a row in the in-basket to select the work item.                      |
|---------------|---------------------------------------------------------------------------------------|
| Event ID      | icm.SelectWorkItem                                                                    |
| Type          | Wired                                                                                 |
| Payload       | workitem An icm.model.WorkItemEditable object that represents the selected work item. |

## Send selected work items event

| Description   | The In-basket widget received the          icm.RequestSelectedWorkItems event that requested information for         specified work items.                                                               |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendSelectWorkItems                                                                                                                                                                                  |
| Type          | Wired                                                                                                                                                                                                    |
| Payload       | result The payload that was passed by the handleRequestSelectedWorkItems function. selectWorkItems An array of icm.model.WorkItem objects that represent the work items in the specified in-basket rows. |