# Attachments widget outgoing events

## Document opened event

| Description   | The user opened a document or an initiating document was opened when the widget loaded.                                                                                           |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.OpenDocument                                                                                                                                                                  |
| Type          | BroadcastNote: This event is only broadcast when there is a Viewer widget on the page and when the Open documents in a separate browser window setting on the widget is disabled. |
| Payload       | contentItem An ecm.model.ContentItem object that represents the document that was opened. action An ecm.model.Action object that represents the Open action.                      |

## Document selected event

| Description   | The user selected a document.                                                            |
|---------------|------------------------------------------------------------------------------------------|
| Event ID      | icm.SelectDocument                                                                       |
| Type          | Wired                                                                                    |
| Payload       | document An ecm.model.ContentItem object that represents the document that was selected. |