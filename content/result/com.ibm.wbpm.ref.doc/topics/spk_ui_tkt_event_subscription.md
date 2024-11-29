# Event subscription

Events can be published through the following two methods:

- view.ui.publishEvent(eventName, payloadData)
- bpmext.ui.publishEvent(eventName, payload, persistence)

If the persistence is set to true for the
bpmext.ui.PublishEvent method, event listeners will fire, even if they load
after the event actually fires. This capability is only available through bpmext.

## Configuration properties

Under Configuration, set or modify the configuration
properties for the view.

The configuration properties for Event subscription are shown in the following table:

| Configuration property   | Description                                                                                                                   | Data type   |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------|
| Event name               | Specifies the name of the subscribed-to event. By default, no event name is specified.                                        | String      |
| On published event       | Specifies the logic that occurs when the specified subscribed-to event has been published. By default, no logic is specified. | String      |

## Example

Assume that you have two Masked Text views where users can type in their credit card number. The
second Masked Text view is inside a Tooltip view and the Tooltip view is inside an Input Group view.
You can use the Event subscription view to verify whether the two typed numbers match. For the Event
subscription view, you could specify the event name CCN\_Match in the
Event name field. And you could specify the following logic in the
On published event field (where the bold text indicates the control IDs for
the Masked Text, Tooltip, and Input Group views):

```
if(${CCN}.getText() == ${VerifyCCN}.getText() && (${CCN}.getText() != "" && ${VerifyCCN}.getText() != "")){${Input\_Group1}.setIcon("check");
${Tooltip1}.setText("Numbers Match");
${Tooltip1}.setColorStyle("S");
${Input\_Group1}.setColorStyle("S") } else {${Tooltip1}.setText("Numbers Don't Match");
${Tooltip1}.setColorStyle("E"); ${Input\_Group1}.setIcon("close");
${Input\_Group1}.setColorStyle("G") }
```

In the above code fragment, the control ID for the first Masked Text view is
CCN and the view has the following logic specified for the On change
event:

${CCN}.ui.publishEvent("CCN\_Match");

The control ID for the second Masked Text view is VerifyCCN and the view
has the following logic specified for the On change event:

${VerifyCCN}.ui.publishEvent("CCN\_Match");

If the two specified credit card numbers match, the first instance of the credit card number is
flagged with the text Numbers Match and the second instance is flagged
with a check mark symbol. If the two specified credit card numbers do not match, the first instance
of the credit card number is flagged with the text Numbers Don't Match
and the second instance is flagged with an X symbol.

bpmext.ui.publishEvent(${Name}.getText(), ${Data}.getText())

## Events

Set
or modify the event handlers for the view in the Events properties. You can set
events to be triggered programmatically or when a user interacts with the view. For information about how to define and code events, see User-defined events.

Event subscription has the following type of event handler:

- On published event: Activated when an event is published. For example:
${SubResult}.setText(me.getEventData())

Depending on the specific event, you can use JavaScript logic to modify the effects of the
view. More information on using events with views is found in the topic
User-defined events.

## Methods

For detailed information on the available methods for Event subscription, see the Event subscription JavaScript
API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.