# Content List widget outgoing events

## Document opened event

| Description   | The user opened a document                                                         |
|---------------|------------------------------------------------------------------------------------|
| Event ID      | icm.OpenDocument                                                                   |
| Type          | Broadcast                                                                          |
| Payload       | contentItem An ecm.model.ContentItem that represents the document that was opened. |

## Document selected event

| Description   | The user selected a document                                                |
|---------------|-----------------------------------------------------------------------------|
| Event ID      | icm.SelectDocument                                                          |
| Type          | Wired                                                                       |
| Payload       | contentItem An ecm.model.ContentItem that represents the selected document. |