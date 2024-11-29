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

## Class BPCListHandler

- java.lang.Object
    - com.ibm.bpe.jsf.handler.BPCListHandler

- All Implemented Interfaces:
ErrorHandler, ItemProvider

public class BPCListHandler
extends java.lang.Object
implements ItemProvider, ErrorHandler
This class can be used as a Faces Managed Bean that provides the data to be displayed
 in a List Component. In order to associate a Managed Bean of type
 BPCListHandler with a List Component on a page, the Value Binding Expression
 of the list tag must be targeted at the Managed Bean. For more information
 about the List Component, see ListTag.
 The BPCListHandler class generates Item Changed events whenever an item in the
 associated List Component is selected. The ItemListener can be registered
 on the BPCListHandler using the ItemListener property. For more information
 about using the ItemListener interface, see the example shown in
 ItemListener.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
ATTRIBUTE\_FOR\_SORTING
The name of the component attribute that determines which row
 is used when sorting the results.

static java.lang.String
COPYRIGHT
    - Constructor Summary

Constructors 

Constructor and Description

BPCListHandler()
    - Method Summary Methods Modifier and Type Method and Description void addItemListener (ItemListener listener) Adds a new ItemListener object to the list of ItemListener objects. void clearSelection () Resets the selection of the associated list to 'none'. java.lang.String executeQuery () Triggers execution of the associated query. java.util.Map getErrors () Returns the errors map for items in the list. java.lang.Object getItem () Returns the currently selected item. java.util.List getItemListener () Returns a list of all registered ItemListener objects. java.util.List getItems () Returns a list of all the items retrieved by running the associated query. java.lang.String getName () Returnes the list name. boolean getNotEmpty () com.ibm.bpe.jsf.handler.BPCListHandlerPagingHelper getPagingHelper () The returned class is not for public use. Query getQuery () Returns the registered query object. Message getQueryMessage () Returns message indication problems that occurred during execution of the query. java.util.List getSelectedItems () Returns all selected items in the list. com.ibm.bpe.jsf.handler.BPCListHandlerSelectionHelper getSelectionHelper () The returned class is not for public use. com.ibm.bpe.jsf.handler.BPCListHandlerSortHelper getSortHelper () The returned class is not for public use. java.lang.String getType () Returns the expected type of the query model. java.lang.String refreshList () Triggers a refresh of the list by executing the associated query. java.lang.String refreshList (boolean clearErrors) Triggers a refresh of the list by executing the associated query. void setErrors (java.util.Map errors) Sets the errors map for this instance. void setItemListener (java.util.List list) Sets the list of ItemListener objects. void setName (java.lang.String name) Sets the list name. void setQuery (Query newQuery) Sets the query used to retrieve the list of items. void setType (java.lang.String typeName) Sets the type of the BPCListHandler .

### Method Summary

| Modifier and Type                                     | Method and Description                                                                                     |
|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| void                                                  | addItemListener(ItemListener listener) Adds a new ItemListener object to the list of ItemListener objects. |
| void                                                  | clearSelection() Resets the selection of the associated list to 'none'.                                    |
| java.lang.String                                      | executeQuery() Triggers execution of the associated query.                                                 |
| java.util.Map                                         | getErrors() Returns the errors map for items in the list.                                                  |
| java.lang.Object                                      | getItem() Returns the currently selected item.                                                             |
| java.util.List                                        | getItemListener() Returns a list of all registered ItemListener objects.                                   |
| java.util.List                                        | getItems() Returns a list of all the items retrieved by running the associated query.                      |
| java.lang.String                                      | getName() Returnes the list name.                                                                          |
| boolean                                               | getNotEmpty()                                                                                              |
| com.ibm.bpe.jsf.handler.BPCListHandlerPagingHelper    | getPagingHelper() The returned class is not for public use.                                                |
| Query                                                 | getQuery() Returns the registered query object.                                                            |
| Message                                               | getQueryMessage() Returns message indication problems that occurred during execution of the query.         |
| java.util.List                                        | getSelectedItems() Returns all selected items in the list.                                                 |
| com.ibm.bpe.jsf.handler.BPCListHandlerSelectionHelper | getSelectionHelper() The returned class is not for public use.                                             |
| com.ibm.bpe.jsf.handler.BPCListHandlerSortHelper      | getSortHelper() The returned class is not for public use.                                                  |
| java.lang.String                                      | getType() Returns the expected type of the query model.                                                    |
| java.lang.String                                      | refreshList() Triggers a refresh of the list by executing the associated query.                            |
| java.lang.String                                      | refreshList(boolean clearErrors) Triggers a refresh of the list by executing the associated query.         |
| void                                                  | setErrors(java.util.Map errors) Sets the errors map for this instance.                                     |
| void                                                  | setItemListener(java.util.List list) Sets the list of ItemListener objects.                                |
| void                                                  | setName(java.lang.String name) Sets the list name.                                                         |
| void                                                  | setQuery(Query newQuery) Sets the query used to retrieve the list of items.                                |
| void                                                  | setType(java.lang.String typeName) Sets the type of the BPCListHandler.                                    |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait