# Search widget events

For example, the Search widget publishes an outgoing event
that contains the search criteria that a user specified.

- Search widget outgoing events

The Search widget provides an outgoing event that is broadcast to the other widgets on the page. The data that is included in the payload of this broadcast event is processed by any widget that has a corresponding handled event.
- Search widget incoming events

The Search widget provides an incoming event to handle the data that is received from other widgets.