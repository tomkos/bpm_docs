# Creating custom inline messages and prompts

```
var propertyController = controller.getPropertyController("F\_CaseFolder", "ABC\_Property1");
propertyController.set('promptMessage", "Enter your favorite color");
propertyController.set("invalidMessage", "The value that you entered is not valid.");
propertyController.set("rangeMessage", "Enter a value between {0} and {1}");
```