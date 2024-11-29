# Retrieving and setting properties of a business object

```
var amount = tw.local.myVariable.amount;
tw.local.myVariable.amount = 123;
```

```
var metadata = tw.local.myVariable.getPropertyValue("metadata");
tw.local.myVariable.setPropertyValue("metadata", "The new metadata");
```

## Using predefined functions and properties

| Function or property name                    | Scope   | Description                                                                                                                                 |
|----------------------------------------------|---------|---------------------------------------------------------------------------------------------------------------------------------------------|
| getPropertyValue(propertyName)               | Objects | Returns the value of a property                                                                                                             |
| insertIntoList(index, value)                 | Lists   | Inserts an item into a list.                                                                                                                |
| isDirty()                                    | Both    | Checks if a shared business object has changes.                                                                                             |
| listAddSelected(index)                       | Lists   | Marks an item in a list as selected.                                                                                                        |
| listClearAllSelected()                       | Lists   | Marks all items in a list as not selected.                                                                                                  |
| listIsSelected(index)                        | Lists   | Checks if an item in a list is selected.                                                                                                    |
| listRemoveSelected(index)                    | Lists   | Marks an item in a list as not selected.                                                                                                    |
| listToNativeArray()                          | Lists   | Returns a JavaScript array with the items of the list.                                                                                      |
| load(key)                                    | Objects | Loads the latest version of a shared business object or, if a key is provided, loads the latest version of specific shared business object. |
| metadata(key)                                | Both    | Returns a metadata value of the object.                                                                                                     |
| propertyNames                                | Objects | Returns an array of the properties of the object.                                                                                           |
| propertyValues                               | Objects | Returns an array of the property values of the object.                                                                                      |
| removeIndex(index)                           | Lists   | Removes an item from a list.                                                                                                                |
| removeProperty(propertyName)                 | Objects | Removes a property from an object.                                                                                                          |
| save()                                       | Objects | Saves a shared business object.                                                                                                             |
| setPropertValue(propertyName, propertyValue) | Objects | Sets the value of a property.                                                                                                               |
| toJSONString(formatted)                      | Both    | Returns a JSON representation of the object or list                                                                                         |
| toXML()                                      | Both    | Returns a DOM representation of the object or list                                                                                          |
| toXMLString()                                | Both    | Returns an XML representation of the object or list                                                                                         |

The following properties are not persisted at the object level. When one of these properties is
used, a function runs in the background to obtain the requested value. For example, although
listLength is modeled as a property, it calls a function to obtain the value of listLength. Although
code snippets in the  JavaScript editor are scripted by using a JavaScript-like language, the real
Java™ objects are used at run time.

| Property name          | Scope   | Description                                                      |
|------------------------|---------|------------------------------------------------------------------|
| listAllSelected        | Lists   | Returns a list of all selected items of the list.                |
| listAllSelectedIndices | Lists   | Returns a list of the indices of all selected items of the list. |
| listLength             | Lists   | Returns the number of items in the list.                         |
| listSelected           | Lists   | Returns the first selected item of the list.                     |
| listSelectedIndices    | Lists   | Returns the index of the first selected item of the list.        |

## Parsing a JSON string

```
tw.local.myVariable = JSON.parse(aJsonString);
```

The property
names in the JSON string and their values must match the business
object type of myVariable.

```
<common merge="mergeChildren">
	<type-string-to-date merge="replace">true</type-string-to-date>
</common>
```

## Parsing an XML string

```
tw.local.myVariable = tw.system.serializer.fromXml(aXml);
```