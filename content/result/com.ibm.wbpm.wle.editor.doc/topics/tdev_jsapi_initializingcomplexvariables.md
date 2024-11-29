# Using complex variables and lists in JavaScript

## About this task

Before you can set the properties of a business object and before you can add items to a
list, you need to initialize your variable.

## Procedure

1. In the Variables tab of your process or service flow, declare a
variable that is a complex business object or a list. For example, a variable named
myVariable of type Requisition or a variable named
myList that is a list of string variables.
2. In the diagram, drag a script task from the palette onto the canvas.
3 In the Implementation tab, initialize your variableby using a JavaScript text area: Remember: If your complex business object or list includes elements that are complexvariables, they must also be initialized. Important: The server script syntax in a heritage human service or service flow is different from the client-side script syntax in aclient-side human service. For client-side human services, ensure that you use the standardJavaScript syntax to instantiate objects in the client-side script, insteadof the server script syntax that is used in a heritage human service . Forexample:// To instantiate and populate a complex variabletw.local.customer= {};tw.local.customer.firstName = "Jane";tw.local.customer.lastName = "Doe";// To instantiate and populate an arraytw.local.addresses = [];tw.local.addresses[0] = {};tw.local.addresses[0].city = "Boston";// To instantiate a String variabletw.local.customerID = "12345";// To create a Date variabletw.local.dueDate = new Date(); Note: If the name of your complex business object conflicts with an existing JavaScript namespace,such as tw.object.property , tw.object.contentObject , ortw.object.toolkit , use the tw.object.baw namespace to instantiate thebusiness object. Forexample:tw.local.myVariable = new tw.object.baw.property(); tw.local.myListVariable = new tw.object.listOf.baw.toolkit();
    - If the variable is a complex object, use:
tw.local.<variableName> = new tw.object.<businessObject>();For
example: tw.local.myVariable=new tw.object.Requisition();
    - If the variable is a list, use:
tw.local.<listName>=new tw.object.listOf.<businessObject>();For
example: tw.local.myList=new tw.object.listOf.String();

```
// To instantiate and populate a complex variable
tw.local.customer= {};
tw.local.customer.firstName = "Jane";
tw.local.customer.lastName = "Doe";

// To instantiate and populate an array
tw.local.addresses = [];
tw.local.addresses[0] = {};
tw.local.addresses[0].city = "Boston";

// To instantiate a String variable
tw.local.customerID = "12345";

// To create a Date variable
tw.local.dueDate = new Date();
```

```
tw.local.myVariable = new tw.object.baw.property(); 
tw.local.myListVariable = new tw.object.listOf.baw.toolkit();
```

## What to do next

- Retrieving and setting properties of a business object

After you initialize a business object, you can access its properties by using various functions.