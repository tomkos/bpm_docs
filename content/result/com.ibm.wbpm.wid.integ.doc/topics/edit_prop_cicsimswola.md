<!-- image -->

# Examining and editing the properties of a CICS, IMS, or WOLA
import

To examine the relationship of the business object to others, select
the business object under Data under Assembly
Diagram. The relationship of this business object with
others appears in the References view. If the References view
is not open, then right click the business object and select Show
References in References view.

To examine the business object using the Business Object Editor,
right click the business object and select Open
With > Business Object Editor. The object opens in the editor. Selecting an item
from the business object results in seeing lower level information
in the Properties view.

To examine the interface, right click your interface under Interfaces and
select Open With > Interface
Editor. The relationship between the interface
and the service is shown in the References view.

- Select Details to view the interface name,
preferred interaction style, operations, and qualifiers.
- Select Binding to view the adapter typeand the data binding configuration. You can add a binding description.Under Binding :
    - Select End-point Configuration and select Connection toview or modify the connection properties that you set while creatingthe import.
        - Expand Managed Connection Factory Properties to
view the managed connection factory class available for the adapter.
Select Advanced to view or modify the connection
and security properties and the interaction specification (InteractionSpec)
class name.Note: If a JNDI name was specified previously, then the
connection section is empty since it is defined at the server.
        - Expand Connection Spec Properties to view
or modify the connection specification (ConnectionSpec) class.
        - Expand Admin Connection Properties to view
or modify the properties for connection pool values and configuration
values if you would like custom names and values for you application. Note: If
you had specified a JNDI name earlier, the administration connection
properties are empty since the server is determining connection pooling
values.
- Under End-point configuration, select Resource
Adapter to view or modify the resource adapter name, class
name and the properties of the resource adapter. The name of the resource
adapter needs to match the name of the resource adapter as it is deployed.
If the resource adapter is embedded in the module, then the name must
be the application name (that is, the module name)+'App'+'.'+'<display
name of the resource adapter>'. For example, InventoryApp.ECIResourceAdapter.
If the resource adapter is not embedded in the module, then it must
match the name of the resource adapter as it is installed on the server.
- Select Method Bindings to view or modify
the interaction information at the method level. Specifically, the
interaction specification (InteractionSpec) class and its properties
are displayed.
- Select Security Attributes and expand Authentication
Properties to view or modify the authentication properties.
The J2C authentication data entry name is displayed (if it had been
specified when the component was developed). If you expand Advanced,
the authentication properties are displayed such as the level of the
authentication; for example, at the container level.

To add, update or remove operations in the import, under Assembly
Diagram, right click the created CICS, IMS, or WOLA import
and select Edit binding. Alternatively, you
could select the import component from the Assembly editor canvas,
right click and select Edit binding. The Operations page
from the New External Service wizard opens. You
can add new operations for the import, or edit or remove existing
operations.