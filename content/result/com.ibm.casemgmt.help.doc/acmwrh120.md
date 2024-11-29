# Script Adapter widget

When wiring widgets, if the widgets have the same event and the
format for the event data is the same, you can simply wire one widget
to another. However, if the format for the event data is not the same,
you will need to transform the data in the source event into a format
expected by the target widget. The Script Adapter widget is the way
you achieve this transformation. When the Script Adapter widget receives
an event from a widget it is wired to, it displays the event details
in the Received Event section. The Script Adapter then runs a script
that transforms the data as a function with a "payload" parameter,
which is the payload of the incoming event. The script is how you
manipulate the payload using any type of logic that you feel is necessary.
The value that your custom code returns is the payload of the outbound
event of this widget. The Sent Event section displays this information.

```
alert("The value of the payload is: " + payload);
return "Event Payload: " + payload + "!";
```

The Sent Event section displays "Event Payload: test data!" as
the payload for the outbound event.

## IBM® Business Automation
Workflow pages
that include this widget by default

The Script Adapter widget
is included on the Cases page by default.

- Inserting logic to transform or validate event data

You use the Script Adapter widget to insert logic that either transforms or validates event data that is sent by a widget. You use JavaScript code to implement the logic in the Script Adapter widget. The resulting value is contained in the payload of the event that is published by the Script Adapter widget.
- Debugging events by using the Script Adapter widget

You can use a Script Adapter to view event data to debug problems with wires between two widgets.
- Script Adapter widget events

The Script Adapter widget uses events to insert logic to transform or validate event data between the widgets on a page.