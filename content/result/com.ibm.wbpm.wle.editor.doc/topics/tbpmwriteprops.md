# Writing to the IBM\_BPM\_Document\_Properties property

## About this task

```
// Initialize the properties input variable to be passed to the Content Integration node
   tw.local.properties = new tw.object.listOf.ECMProperty();

   // Initialize the  ECMMultiValue variable that will carry the name value pairs for the BPM properties
   var props = new tw.object.ECMMultiValue();
   props.value = new tw.object.listOf.ANY();

   // Set the property name value pairs
   props.value[0] = "Property 1,value 1";
   props.value[1] = "Property 2,value 2";
   props.value[2] = "Property 3,value 3";

   // Create the IBM\_BPM\_Document\_Properties property entry
   tw.local.properties[0] = new tw.object.ECMProperty();
   tw.local.properties[0].objectTypeId = "IBM\_BPM\_Document\_Properties";
   tw.local.properties[0].value = props.value;
```

For an example of how to update the value of
the IBM\_BPM\_Document\_Properties property, see the topic "Updating
the IBM\_BPM\_Document\_Properties property."