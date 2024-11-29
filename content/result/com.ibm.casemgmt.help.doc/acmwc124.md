# Page Container widget outgoing events

## Open page event

| Description   | The user opened the page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.OpenPage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Type          | Broadcast                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Payload       | pageClassName A string that contains the name of the page class module. pageType A string that contains the one of the following values to indicate the type of page to be opened: CASE The page is a Case Details page. CASE\_NEW The page is an Add Case page. CASE\_SPLIT The page is a Split Case page. STATIC The page is a Solution page. STEP The page is a Work Details page. STEP\_LAUNCH' The page is an Add Activity page.   isLazy A Boolean value that is set to True to indicate that the page is to be lazy loaded. That is, the page is not selected immediately and is loaded only when it is selected manually. subject A model object or a simple string that represents the page subject. For example, you might use an icm.model.CaseEditable object for a Case Detail page or a string containing the Universally Unique Identifier (UUID) for a Work page. pageContext An object that represents the context that is to be added as a property of the page and each page widget. crossPageEventName A string that contains the name of the event that is to be broadcast in the page. crossPageEventPayload A object that represents the payload of the event that is to be broadcast in the page. |

## Page activated event

| Description   | The user selected the page.   |
|---------------|-------------------------------|
| Event ID      | icm.PageActivated             |
| Type          | Broadcast                     |
| Payload       | null                          |

## Page closed event

| Description   | The user closed the page.   |
|---------------|-----------------------------|
| Event ID      | icm.PageClosing             |
| Type          | Broadcast                   |
| Payload       | null                        |

## Page deactivated event

| Description   | The user selected a different page, which changed focus from the current page.   |
|---------------|----------------------------------------------------------------------------------|
| Event ID      | icm.PageDeactivated                                                              |
| Type          | Broadcast                                                                        |
| Payload       | null                                                                             |

## Page opened event

| Description   | The user opened the page.   |
|---------------|-----------------------------|
| Event ID      | icm.OpenPage                |
| Type          | Broadcast                   |
| Payload       | null                        |

## Send case information event

| Description   | The user opened a case.                                                                                                                                                                              |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendCaseInfo                                                                                                                                                                                     |
| Type          | Broadcast                                                                                                                                                                                            |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case that is to be displayed coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |

## Send new case information event

| Description   | The user clicked the Add Case button.                                                                                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendNewCaseInfo                                                                                                                                                                                |
| Type          | Broadcast                                                                                                                                                                                          |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case that is to be created coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |

## Send new task information event

| Description   | The user clicked the Add Activity button.                                                                                                                                                               |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendNewTaskInfo                                                                                                                                                                                     |
| Type          | Broadcast                                                                                                                                                                                               |
| Payload       | taskEditable An icm.model.TaskEditable object that represents the activity that is to be created. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |

## Send split case information event

| Description   | The user clicked the Split Case button.                                                                                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendSplitCaseInfo                                                                                                                                                                              |
| Type          | Broadcast                                                                                                                                                                                          |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case that is to be created coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |

## Send work item event

| Description   | Send the work item.                                                                                                                                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendWorkItem                                                                                                                                                                                                               |
| Type          | Broadcast                                                                                                                                                                                                                      |
| Payload       | workItemEditable An icm.model.WorkItemEditable object that represents the work item that is to be displayed and updated. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |

## Widgets loaded event

| Description   | Widgets in the page are loaded and ready to work.                                                              |
|---------------|----------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.WidgetLoaded                                                                                               |
| Type          | Broadcast                                                                                                      |
| Payload       | widgetLoadTime An icm.context.widgetLoadTime object that represents the time it takes for the widgets to load. |