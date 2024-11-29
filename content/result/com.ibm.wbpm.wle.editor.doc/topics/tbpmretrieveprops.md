# Reading from the IBM\_BPM\_Document\_Properties property

## About this task

```
// Initialize the variable that is used to store the BPM property values. A list of NameValuePair objects is used.
tw.local.bpmProperties = new tw.object.listOf.NameValuePair();

// Look for the BPM properties object
for (var i = 0; i < tw.local.document.properties.listLength; i++) {

    if(tw.local.document.properties[i].objectTypeId == "IBM\_BPM\_Document\_Properties"){
    
        // Found the BPM properties.  Save its value to a local variable
        var bpmProperties = tw.local.document.properties[i].value;

        // If there was only a single name-value pair stored in the BPM properties, then 
        // a string is returned.  Need to check here.
        if(typeof bpmProperties == 'string'){
        
            // There is a string in the format "name,value". Store it into the output variable.
            var nameValuePair = bpmProperties.split(",");
            
            tw.local.bpmProperties[0] = new tw.object.NameValuePair();
            tw.local.bpmProperties[0].name = nameValuePair[0];
            tw.local.bpmProperties[0].value = nameValuePair[1];
            
        }else{
            // Else, there is an instance ECMMultiValue. Introspect this object and store everything into the 
            // NameValuePair list.
            for (var j = 0; j < bpmProperties.value.listLength; j++) {
                
                var nameValuePair = bpmProperties.value[j].split(",");
                
                tw.local.bpmProperties[j] = new tw.object.NameValuePair();
                tw.local.bpmProperties[j].name = nameValuePair[0];
                tw.local.bpmProperties[j].value = nameValuePair[1];
            }
        }
        break; // The BPM document properties object has been processed.  Exit the loop.
    }
}
```