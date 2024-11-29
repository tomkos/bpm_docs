<!-- image -->

# J2C imports and exports at run time

## J2C import

The sequence
of the methods used at run time is shown in the following diagram.
First the data object for the request data binding is set unless the
input is a record. The next set of methods is determined by whether
there are three or two arguments in the InteractionSpec.execute method.
If three, then a set data object method is performed for the response
data binding. The other methods are the same for either the three
or two arguments. The record is retrieved from the request and response
data binding and the data object is retrieved from the response data
binding.

In the case of an exception, some fault handling is
provided. the isFault method will be called for a ResourceException
or DataBindingException. Note that isFault is not called for a fault
exception. Then the fault name is generated, the fault data set and
the data object retrieved.

<!-- image -->

## J2C export

The sequence
of the methods used at run time is shown in the following diagram.
The function name is first generated. Then, for the request, the record
is set and the data object retrieved for the input data binding.

For the response, the data object is set on the output
data binding and the record retrieved.

<!-- image -->

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
- Trade-offs when developing adapter imports and exports
- Considerations when using adapters
- Considerations when refactoring
- Contributing your own external service or data wizard plug-in
- Limitations for adapter imports and exports