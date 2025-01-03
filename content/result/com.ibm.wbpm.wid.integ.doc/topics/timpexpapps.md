<!-- image -->

# Accessing external services with adapters

- Pattern of accessing external services with adapters

Using the external service wizard to access external services follows a similar pattern regardless of the adapter you are using.
- Developing services with adapters

EIS imports and exports are the means of creating services that use resource adapters typically to access EIS systems.
- Simple adapter wizard

The simple adapter wizard provides a quick and easy way of creating a service with an adapter.
- Configuring and using adapters

The following adapters for Enterprise Information Systems (EIS) can be configured to work with IBM Integration Designer. In the documentation for each adapter, you will be shown how to use the external service wizard with the adapter as well as additional information that will be helpful such as field level reference information and runtime information. For example, the JDBC adapter information would be used if you needed to access a database.
- Migrating applications using previous adapter levels

Applications using a previous level of adapter can be quickly migrated to the current level with a utility.
- J2C data bindings

For J2C resource adapters, the data bindings are provided with the resource adapter, or they are generated by the tools.  There are two specialized interfaces for J2C data bindings that are shown in this section.
- Creating a business object from a source file

Using the external data wizard, you can create a business object from a C, COBOL or PL/I source file. You can also create a wrapper business object from an existing business object to be used with the EMail, Flat File and FTP adapters. A wrapper business object provides more fields for information related to the particular adapter you selected.
- A closer look at business objects from data structures

The business objects generated by the external service or external data wizards are similar to business objects created by the business object editor. This section shows you the business objects created with the wizards and why you might want to modify these business objects.
- J2C imports and exports at run time

The sequence of the methods used at run time is discussed.
- Trade-offs when developing adapter imports and exports

The external service wizard provides options for you. This section examines the meaning of choosing certain options and guidance in the use of the wizard.
- Considerations when using adapters

You should be aware of related information to adapters.
- Considerations when refactoring

The external service wizard and the assembly editor that simplify the development of applications through generating artifacts, also create references to the generated artifacts. When you refactor the artifacts, either through the refactoring user interface or manually moving, renaming and deleting objects yourself, these references sometimes will require revisions, which are listed in this section.
- Contributing your own external service or data wizard plug-in

You can contribute your own external service or data wizard plug-in customized to the needs of your organization. Integration developers can then use your plug-in in the same way the external service wizard or external data wizard is used.
- Limitations for adapter imports and exports

The limitations or restrictions when using the external service or external data wizards or the imports and exports they produce are listed here.