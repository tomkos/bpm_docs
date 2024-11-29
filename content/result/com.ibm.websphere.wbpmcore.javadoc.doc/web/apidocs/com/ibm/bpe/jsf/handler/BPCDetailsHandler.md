- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class BPCDetailsHandler

- java.lang.Object
    - com.ibm.bpe.jsf.handler.BPCDetailsHandler

- All Implemented Interfaces:
ItemListener, ItemProvider

public class BPCDetailsHandler
extends java.lang.Object
implements ItemListener, ItemProvider
This class can be used as a Faces Managed Bean that provides the data displayed in a Details Component.
 In order to associate a Managed Bean of type BPCDetailsHandler with a Details Component on a page, the 
 Value Binding Expression of the list tag must be targeted at the Managed Bean. For more information about
 the Details Component, see DetailsTag.
 In order to be notified of selection changes, the DetailsHandler must be set as ItemListener on the 
 BPCListHandler. For more information about using the ItemListener interface, see the example in ItemListener.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Constructor Summary

Constructors 

Constructor and Description

BPCDetailsHandler()
    - Method Summary Methods Modifier and Type Method and Description java.lang.Object getModel () Returns the model managed by this instance. java.util.List getPropertyList () Returns a list of the objects that represent the properties of the model class. java.util.List getSelectedItems () Returns the list of selected items. java.lang.String getType () Returns the model type that this instance is to be associated with. void itemChanged (java.lang.Object item) Triggered whenever a new element is selected in the ItemListener event provider. void setType (java.lang.String modelType) Sets the model type that this instance is to be associated with.

### Method Summary

| Modifier and Type   | Method and Description                                                                                              |
|---------------------|---------------------------------------------------------------------------------------------------------------------|
| java.lang.Object    | getModel() Returns the model managed by this instance.                                                              |
| java.util.List      | getPropertyList() Returns a list of the objects that represent the properties of the model class.                   |
| java.util.List      | getSelectedItems() Returns the list of selected items.                                                              |
| java.lang.String    | getType() Returns the model type that this instance is to be associated with.                                       |
| void                | itemChanged(java.lang.Object item) Triggered whenever a new element is selected in the ItemListener event provider. |
| void                | setType(java.lang.String modelType) Sets the model type that this instance is to be associated with.                |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait