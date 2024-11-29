# Content List widget events

For example, the Content List widget publishes an outgoing
event when a user selects a document in the list. The Content List
widget handles an incoming event to run a stored search for documents.

- Content List widget outgoing events

The Content List widget  provides outgoing events that are wired to the other widgets on the page. The data that is included in the payload of a wired event is processed by the handled event in the target widget to which the published widget is wired.
- Content List widget incoming events

The Content List widget provides incoming events to handle the data that is received from other widgets.