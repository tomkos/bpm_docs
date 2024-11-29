# Page Container widget incoming events

## Add case event

| Description   | Open an Add Case page so the user can add a case.                                                                                                                                                                                                                                     |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.AddCase                                                                                                                                                                                                                                                                           |
| Payload       | caseType An icm.model.CaseType object that represents the type of case to be added. caseEditable An icm.model.CaseEditable object that represents the case that is to be added. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |

## Add activity event

| Description   | Open an Add Activity page so that the user can add an activity.                                                                                                                                                                                                                                                    |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.AddTask                                                                                                                                                                                                                                                                                                        |
| Payload       | taskEditable An icm.model.TaskEditable object that represents the activity that is to be added. caseEditable An icm.model.CaseEditable object that represents the case to which the activity is to be added. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |

## Close page event

| Description   | Close the current page.   |
|---------------|---------------------------|
| Event ID      | icm.ClosePage             |
| Payload       | Empty                     |

## Collapse region event

| Description   | Collapse a region in the page.                                                                                                                                                                                    |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.CollapseRegion                                                                                                                                                                                                |
| Payload       | region A string that identifies the region of the page to be collapsed. The valid values are leading， trailing， top， and bottom. You can specify center as the region, but the center region cannot be collapsed. |

## Mark or clear page as changed event

| Description   | Set or clear the flag that indicates whether the page contains unsaved changes.   |
|---------------|-----------------------------------------------------------------------------------|
| Event ID      | icm.SetDirtyState                                                                 |
| Payload       | reference A reference that identifies the entity that invoked this event.         |

## Open case event

| Description   | Open the specified case in a Case Details page.                                                                                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.OpenCase                                                                                                                                                                                       |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case that is to be opened. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |

## Open page event

| Description   | Open the page that is specified in the event payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.OpenPage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Payload       | pageClassName A string that contains the name of the page class module. pageType A string that contains the one of the following values to indicate the type of page to be opened: casePage The page is a Case Details page. caseNewPage The page is an Add Case page. caseSplitPage The page is a Split Case page. staticPage The page is a Solution page. stepPage  The page is a Work Details page. stepLaunchPage The page is an Add Activity page.   isLazy A Boolean value that is set to True to indicate that the page is to be lazy loaded. When used incorrectly, the new page doesn't render the case toolbar correctly. subject A model object or a simple string that represents the case or work item that is to be opened in the page. For example, you might use an icm.model.CaseEditable object for a Case Detail page or a string containing the Universally Unique Identifier (UUID) for a Work page. pageContext An object that represents the context that is to be added as a property of the page and each page widget. crossPageEventName A string that contains the name of the event that is to be broadcast in the page. crossPageEventPayload A object that represents the payload of the event that is to be broadcast in the page. |

## Open work item event

| Description   | Open the specified work item in a Work Details page.                                                                                                                                                                                                                                        |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.OpenWorkItem                                                                                                                                                                                                                                                                            |
| Payload       | workItem An icm.model.WorkItemEditable object that represents the work item that is to be opened. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. UIState A dojo.Stateful object that represents the state of the selected work item. |

## Restore region event

| Description   | Restore a region in the page to its original size.                                                                              |
|---------------|---------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.RestoreRegion                                                                                                               |
| Payload       | region A string that identifies the region of the page to be restored. The valid values are leading， trailing， top， and bottom. |

## Split case event

| Description   | Open a Split Case page so that the user can create a case from an existing case.                                                                                                                                                                                                                               |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SplitCase                                                                                                                                                                                                                                                                                                  |
| Payload       | caseType An icm.model.CaseType object that represents the type of case to be created from the existing case. caseEditable An icm.model.CaseEditable object that represents the case that is to be split. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |