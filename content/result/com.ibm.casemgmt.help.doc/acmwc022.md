# Properties widget events

For example, the Properties widget handles an incoming
event to display the properties for a case type so that the user can
create a case of that type.

- Properties widget outgoing events

The Properties widget provides outgoing events that are broadcast and wired to the other widgets on the page. The data that is included in the payload of a broadcast event is processed by any widget that has a corresponding handled event. The data that is included in the payload of a wired event is processed by the handled event in the target widget to which the published widget is wired.
- Properties widget incoming events

The Properties widget provides the following incoming events to handle the data that is received from other widgets.