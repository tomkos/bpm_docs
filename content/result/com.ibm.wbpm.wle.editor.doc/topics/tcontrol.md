# Accessing a child view

## About this task

## Procedure

To use a control ID in your code:

1 Determine the control ID:
    1. Open the service that contains the page that you want to work with.
    2. In the design area, select the view that you want to access at run time.
    3. In the properties area, select General. 
The control ID field contains the unique ID for the control.
2 In the Behavior page of the view editor, add JavaScript code:

1. Get the control ID by using the this.context.getSubview(subViewId,
requiredOrder) method. The method returns an array of nested view instance objects. If
the result does not contain a set of repeatable objects, specify the first index of the returned
array list, for example this.context.getSubview("myCheckbox")[0]. If you need
the array in the same order as your document order, set the second optional parameter to true. By
default, it is set to false.

subViewID
The id parameter of the <div></div> tag of the
nested view instance object

requiredOrder
A Boolean value. If set to true, the method returns the array of view
instance objects in the same order as the document tree. The default is false.
2. Enter your code to interact with the nested view instance as appropriate. See
the following example for details.
3. Click Save or Finish Editing.

## Example

```
<div id="div\_2\_1" class="ContentBox" data-view-managed=false>
 <div id="div\_2\_1\_1" class="Checkbox CoachView" data-type="com.ibm.bpm.coach.Snapshot\_fc633c7d\_3b4f\_44db\_82c1\_cfc7ac8b5647.Checkbox" data-binding="" data-config="config2" data-viewid="myCheckbox" data-eventId="" >
```

```
if (this.context.getSubview("myCheckbox")[0].context.binding.get("value") == true) {
			 return true;
}else{
  			alert( "Check the checkbox");
  			return false;
}
```