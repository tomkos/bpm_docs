<!-- image -->

# Considerations when using adapters

- Changes to EIS systems
- IMS
- JDBC
- Third party libraries

## Changes to EIS systems

When
the EIS system you access through the discovery wizard and an adapter
changes, it will have an effect on the application you created in IBM® Integration
Designer.
Typically, this EIS change will alter a business object in some way.
For example, if you add a column on a table in an EIS system and then
rediscover the EIS system or edit a service, you will find a new element
in the business object (for the column). This in turn could appear
as an unmapped field in a map. Since most EIS systems will change,
you should expect these differences when using the tools at different
points in time.

## IMS

Since
you work with a host based system with IMS,
you should change the default settings for the COBOL importer. They
can be changed when using the external service wizard or on the operating
system. For example, in Windows from
the menu, select Window > Preferences. The Preferences window
opens. Expand Workbench and select Capabilities.
Expand Advanced J2EE and select Enterprise
Java in the Capabilities pane. Click OK.
Again, select Window > Preferences. The Preferences window
opens. Expand Importer. Select COBOL.
In the Platform field, select z/OS. Click OK.

## JDBC

The JAR for the JDBC
driver of the database system that is being used needs to be added
to the classpath. When using the external service wizard, you will
be prompted for this JAR.

## Third party libraries

- Third party library: You will need to add the library to the classpath
of the connector project by importing the library into the connector
project. You will then need to update the classpath of the project
to include the library and export it.
- Third party native library: You will need to check exactly where
the native library should be placed. It is sometimes placed on the
PATH variable of your machine. It might also be in the bin folder
of the workbench. In the case of SAP, the third party library will
be added to the lib folder of the application server.

When using the external service wizard for the IBM shipped adapters, you will be
prompted for these libraries if they are required.

## Related concepts

- Pattern of accessing external services with adapters
- Developing services with adapters
- Simple adapter wizard
- Migrating applications using previous adapter levels

## Related tasks

- Configuring and using adapters
- Creating a business object from a source file

## Related reference

- J2C data bindings
- A closer look at business objects from data structures
- J2C imports and exports at run time
- Trade-offs when developing adapter imports and exports
- Considerations when refactoring
- Contributing your own external service or data wizard plug-in
- Limitations for adapter imports and exports