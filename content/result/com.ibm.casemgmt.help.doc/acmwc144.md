# Markup widget incoming events

## Clear Content event

| Description   | Clear the content from the Markup widget.   |
|---------------|---------------------------------------------|
| Event ID      | icm.ClearContent                            |
| Payload       | null                                        |

## Receive Markup event

| Description   | Display the content is contained in the event payload.                                         |
|---------------|------------------------------------------------------------------------------------------------|
| Event ID      | icm.ReceiveMarkup                                                                              |
| Payload       | markupText The HTML tags and text that is used to construct the contents of the Markup widget. |