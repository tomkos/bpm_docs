# In-baskets widget events

For example, the In-baskets widget publishes an outgoing
event when the user selects a work item in an in-basket to open. The
In-baskets widget handles an incoming event to apply user-specified
filters to the list of work items.

- In-baskets widget outgoing events

The In-baskets widget provides outgoing events that are broadcast and wired to the other widgets on the page. The data that is included in the payload of a broadcast event is processed by any widget that has a corresponding handled event. The data that is included in the payload of a wired event is processed by the handled event in the target widget to which the published widget is wired.
- In-baskets widget incoming events

The In-baskets widget provides incoming events to handle the data that is received from other widgets.