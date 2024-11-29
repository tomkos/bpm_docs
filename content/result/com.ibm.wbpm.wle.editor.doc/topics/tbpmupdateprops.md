# Updating the IBM\_BPM\_Document\_Properties property

## About this task

```
// Find the ECMProperty object for the BPM document properties.  Assume that the tw.local.document 
// contains the document instance retrieved previously (by a get document operation, for example).
var bpmPropertiesEntry;
for (var j = 0; j < tw.local.document.properties.listLength; j++) { 
    if(tw.local.document.properties[j].objectTypeId == "IBM\_BPM\_Document\_Properties"){
        bpmPropertiesEntry = tw.local.document.properties[j];
        break;
    }
}

// If there is a single BPM document property, the ECMProperty value will be a string.
// This is made an instance of ECMMultiValue, which enables the update to be
// handled generically even if the number of properties eventually changes.
if(typeof bpmPropertiesEntry.value == 'string') {
    var value = bpmPropertiesEntry.value;
    bpmPropertiesEntry.value = new tw.object.ECMMultiValue();
    bpmPropertiesEntry.value.value = new tw.object.listOf.ANY();
    bpmPropertiesEntry.value.value[0] = value;
    
}
    
// Cycle through the properties and update them with new values.
var bpmPropValues = bpmPropertiesEntry.value;    
for (var j = 0; j < tw.local.bpmProperties.listLength; j++) { 
    
    var updateValue = tw.local.bpmProperties[j];
    
    var found = false;
    for (var i = 0; i < bpmPropValues.value.length; i++) {
        
        var nameValuePair = bpmPropValues.value[i].split(",");

        if(updateValue.name == nameValuePair[0]){
            // Found the property, set the new value.
            bpmPropValues.value[i] = updateValue.name + "," + updateValue.value;
            found = true; // No need to add the property
            break; // Property found, break out of the loop.
        }
    }

    // If the property is not found in the existing list, add it
    // to the set.
    if(!found){
        bpmPropValues.value[bpmPropValues.value.length] = updateValue.name + "," + updateValue.value;
    }
}

// Now that the properties have been updated, populate the update operation with the input

tw.local.properties = new tw.object.listOf.ECMProperty();

tw.local.properties[0] = new tw.object.ECMProperty();
tw.local.properties[0].objectTypeId = "IBM\_BPM\_Document\_Properties";
tw.local.properties[0].value = bpmPropValues.value;
```