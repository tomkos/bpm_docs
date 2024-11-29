<!-- image -->

# Query properties tab: BPEL process editor

Use the fields on this page to declare one or more query
properties for the selected process variable. These query properties
determine which parts of a variable can be queried in the runtime
environment. At run time use the query API function to include a query
property in a query. You can also use query tables to expose the query
properties to the business user in Business Space. The query property
may be either a built-in XML schema simple type, or a user-defined
simple type based on a built-in XML schema type using restrictions.
Complex types, list, and union types (neither built-in nor user-defined)
are not supported for query properties.

1. A local query property is created by selecting From query and
can be used for getting and filtering data from a single process.
2. A global query property is created by selecting From property and
can be used when you would like to filter data from multiple processes.
This option is only available when you have an interface typed variable,
and a correlation property is defined for the underlying WSDL message.
Since this correlation property can be shared between multiple processes,
you must then define a query property From property in the
corresponding interface typed variable for each process.

For data typed variables you can only define local query
properties.

When you declare a query property a new entry is
added to the table in the Query Properties tab. In general the fields
of this table cannot be edited directly, to modify a query property
click the Edit button. However, for certain
query properties you can enter an XPath expression in the Query field
directly, click the  icon in the right side
of the Query field, to load an XPath expression editor.

For
more information, see Declaring a query property for a variable. Also see the
runtime example in Example: Including query properties in a query if
you have IBM® Workflow
Server installed.