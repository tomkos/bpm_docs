# Case List widget events

For example, the Case List widget publishes an outgoing
event to open a case that a user double-clicks. The Case List widget
handles an incoming event to display the list of cases that were returned
by a search.

- Case List widget outgoing events

The Case List widget provides outgoing events that are broadcast to the other widgets on the page. The data that is included in the payload of a broadcast event is processed by any widget that has a corresponding handled event.
- Case List widget incoming events

The Case List widget provides incoming events to handle the data that is received from other widgets.