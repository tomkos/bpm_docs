# Original Case Properties widget incoming events

## Clear content event

| Description   | Clear the content in the Case List widget.   |
|---------------|----------------------------------------------|
| Event ID      | icm.ClearContent                             |
| Payload       | null                                         |

## Original case event

| Description   | Display the properties of an existing case from which property values are to be reused in a new case.                                                                                                                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.SendSplitCaseInfo                                                                                                                                                                                                                                                                              |
| Payload       | caseEditable An icm.model.CaseEditable object that represents the case that is to be created. This object provides the properties of the original case by using the getSplitSource() method. coordination An icm.util.Coordination object that is used internally by the widgets in the same page. |