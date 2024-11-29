# Business objects, attributes, and variables that are renamed (deprecated)

Procedures for renaming business objects, their attributes, and variables in the desktop Process Designer (deprecated) are contained in the following
sections.

## Renaming business objects and attributes

To find business objects, select Data from the navigation. To rename a
business object, follow these steps in the desktop Process Designer:

1. Right-click the business object that you want to rename. Select Rename from the menu.
2. In the window that opens, change the business object name in the New name field. By default, when you click OK, you see the references to that business object in
the subsequent Refactor window. However, you
have the option of clearing Update references. In that case, none of the references to the business object are
updated.
3. In the Refactor window, the pane shows the
business processes and services that reference the business object.
Select the business processes and services that you want updated and
click OK. If there are no references, the pane
is blank; however, continue to click OK to
rename the business object. If you want to analyze the list later,
you can copy the names of the business processes and services to a
clipboard by clicking Copy To Clipboard.
4. Afterward, check all the artifacts that you expected to be updated,
particularly in JavaScript sections. The refactor function updates
all fully qualified references that are instantiated with the keyword new for the old business object and old business object
lists; for example, new tw.object.OldBusinessObject or new tw.object.listOf.OldBusinessObject.

Business objects are themselves composed of other variables, which are called attributes. You can
rename attributes of a business object and the rename function shows you the business processes and
services that are affected. To rename an attribute, follow these steps in the desktop Process Designer:

1. Click Data and double-click the business
object in the menu that contains an attribute that you want to rename.
2. Select the attribute in the Parameters list
that you want to rename. When you change the name in the Name field, a message says that to refactor the value
press Alt + Shift + R. Pressing this combination
starts the Rename window. Change the attribute
name in the New Name field. By default, when
you click OK, you see the references to the
attribute in the subsequent Refactor window.
However, you have the option of clearing Update references. In that case, none of the references to the attribute are updated.
3. In the Refactor window, the pane shows the
business processes and services that reference the business object.
Select the business processes and services that you want updated and
click OK. If there are no references, the pane
is blank; however, continue to click OK to
rename the attribute. You can copy the names of the business processes
and services to a clipboard if you want to analyze the list later
by clicking Copy To Clipboard.
4 Afterward, check all artifacts that you expected to be updated,particularly in JavaScript sections. The refactor function updatesattributes on objects in the following situations: In the first example, name would be updated.In the next two examples, id would be updated. var businessobject = new tw.object.BusinessObject();businessobject.name = "John"; tw.local.customerInfo.id = 1234; var customer = tw.local.customerInfo;customer.id = 5678;
    - The object is assigned to a fully qualified business object that
is instantiated with the keyword new or to any ancestral
attribute of the object. An example of an ancestral attribute that
would be refactored is GreatGrandparentBusObj.GrandparentBusObj.ParentBusObj.busobj.name.
    - The object is assigned to a local variable that does not have
an ANY type or to any ancestral attribute of the object.

In the first example, name would be updated.
In the next two examples, id would be updated.

```
var businessobject = new tw.object.BusinessObject();
businessobject.name = "John";
```

```
tw.local.customerInfo.id = 1234;
```

```
var customer = tw.local.customerInfo;
customer.id = 5678;
```

If you refactor a business object and one of its references
is being edited by another user, the reference is not selected to
be refactored. A message specifies the user who is editing the reference.

- JavaScript code in coaches is not updated.
- To be listed as selectable for refactoring, the business processes
or services must reference the business object with the variables
or variable fields that are found in the Variables tab.Attention: You cannot refactor the system-generated
private shared business object that is automatically created for a
case type definition. This business object tracks the case type definition
and its variables so it automatically reflects any changes that you
make to them. If you rename the case type definition, the private
shared business object is also renamed. For example, if you rename
the case type definition from My Case to My First Case, the name of
the private shared business object is automatically renamed from My\_Case\_Folder
to My\_First\_Case\_Folder.
- Property names are not updated when the square bracket notation
is used; for example, in the following code, firstname, would not be updated: customer['firstname'] = "John".
- Refactoring does not update the binding when the business object
parameter name is changed.

## Renaming a variable

Variables are found
within a business process or a service. In other words, renaming a
variable does not affect another business process or service. Renaming
a variable can affect a reference to it within the same business process
or service.

To rename a variable, follow these steps in the desktop Process Designer:

1. Click the Variables tab and select the
variable that you want to rename.
2. When you change the name in the Name field,
a message says that to refactor the value press Alt + Shift
+ R. Pressing this combination starts the Rename window. Change the variable name in the New Name field. By default, when you click OK, all
references to the variable are updated. However, you have the option
of clearing Update references. In that case,
none of the references to the variable are updated. Unlike renaming
a business object or attribute, you do not see a subsequent panel
where you select references or are shown no references.