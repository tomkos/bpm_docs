# The change event handler

## Usage

## The event object

| Property     | Type    | Description                                                                                            |
|--------------|---------|--------------------------------------------------------------------------------------------------------|
| type         | String  | Valid values are "binding" , "config", undefined, or null. An undefined or null value means "binding". |
| property     | String  | The property that was changed                                                                          |
| oldVal       |         | For simple types, the previous value                                                                   |
| newVal       |         | new value                                                                                              |
| insertedInto | Integer | For arrays, the index where the object was added to the list                                           |
| removedFrom  | Integer | For arrays, the index where the object was removed from the list                                       |

## Sample change event

The
following change event code is from the Output Text
stock control. The code checks if a configuration property has changed,
and updates the view with the new value. At the end, it calls the
view() change event.

```
1 if (event.type == "config") {
 2 	if (event.property == "\_metadata.label") {
 3 		var label = this.context.element.querySelector(".outputTextLabel > label");
 4 		label.innerHTML = this.context.htmlEscape(event.newVal);
 5 	} else if (event.property == "\_metadata.helpText") {
		var label = this.context.element.querySelector(".outputTextLabel > label");
		label.title = event.newVal;
	}
} else {
	var newData;
	if (event.newVal != undefined) {
		newData = event.newVal;
	} else {
		newData = "";
	}
 6 	this.context.element.getElementsByTagName("span")[0].innerHTML = this.context.htmlEscape(newData);
}

 7 this.view();
```

- 1  If the change event type is "config",
run the code. Note that if the type is not "config", the event type
is "binding".
- 2  Checks if the label property has
changed.
- 3  Using css query selector, finds
the element with class .outputTextLabel, and its child element label
(outputTextLabel is the class name on the html element).
- 4  Set the label to the new text.
- 5  Run the same code as steps 1 to
5 for the helpText property.
- 6  Set the contents of the html span
element to the new value.
- 7  Call the view() event
handler to reuse code used during initial load/creation and when changes
occur.