<!-- image -->

# How lists are processed

This list handler tracks the selected items in the associated list
and it provides a notification mechanism to associate the list entries
with the details pages for the different kinds of items. The list
handler is bound to the List component through
the model attribute of the bpe:list tag.

The notification mechanism of the list handler is implemented using
the com.ibm.bpe.jsf.handler.ItemListener interface.
You can register implementations of this interface in the configuration
file of your JavaServer Faces (JSF) application.

The notification is triggered when a link in the list is clicked.
Links are rendered for all of the columns for which the action attribute
is set. The value of the action attribute is
either a JSF navigation target, or a JSF action method that returns
a JSF navigation target.

The BPCListHandler class also provides a refreshList method.
You can use this method in JSF method bindings to implement a user
interface control for running the query again.

## Query implementations

You can use the list
handler to display all kinds of objects and their properties. The
content of the list that is displayed depends on the list of objects
that is returned by the implementation of the com.ibm.bpc.clientcore.Query interface
that is configured for the list handler. You can set the query either
programmatically using the setQuery method of the BPCListHandler class,
or you can configure it in the JSF configuration files of the application.

You
can run queries not only against the Business Process Choreographer
APIs, but also against any other source of information that is accessible
from your application, for example, a content management system or
a database. The only requirement is that the result of the query is
returned as a java.util.List of objects by the execute method.

The
type of the objects returned must guarantee that the appropriate getter
methods are available for all of the properties that are displayed
in the columns of the list for which the query is defined. To ensure
that the type of the object that is returned fits the list definitions,
you can set the value of the type property on the BPCListHandler instance
that is defined in the faces configuration file to the fully qualified
class name of the returned objects. You can return this name in the getType call
of the query implementation. At run time, the list handler checks
that the object types conform to the definitions.

To
map error messages to specific entries in a list, the objects returned
by the query must implement a method with the signature public
Object getID().

## Default converters and labels

```
static public String getLabel(String property,Locale locale);
static public com.ibm.bpc.clientcore.converter.SimpleConverter 
       getConverter(String property);
```

If these methods are defined for the beans, the List component
uses the label as the default label for the list and the SimpleConverter
as the default converter for the property. You can overwrite these
settings with the label and converterID attributes
of the bpe:list tag. For more information, see the
Javadoc for the SimpleConverter interface and the ColumnTag
class.