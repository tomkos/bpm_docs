<!-- image -->

# Pattern of accessing external services with adapters

You would follow the steps described below with the external service wizard
to get the service metadata artifacts from a system you are searching and
generate a service.

1. Connect to a host system. A host system could be a server name or a URL
address. Connecting to a system may involve security details, depending on
the security setup in your organization.
2. Once the external service wizard connects to the system, it searches the
metadata repository for the artifacts available to import and presents them
as a list.
3. You make selections from the list. Depending on the adapter, you may be
able to configure each selection, and configure the entire selection. Your
selections create a query.
4. You generate the service description artifacts, which means
interfaces, business objects, and other XML structures are created in your
module.

<!-- image -->

## Related concepts

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
- Considerations when using adapters
- Considerations when refactoring
- Contributing your own external service or data wizard plug-in
- Limitations for adapter imports and exports