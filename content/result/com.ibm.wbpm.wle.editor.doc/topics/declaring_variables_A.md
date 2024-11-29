# How variables are passed between process components at run
time

Variables capture business data. If the business data is a simple
type (for example, a String) then the variable contains a value of
the business data. If the business data is a complex type, then the
variable is a reference to an object that contains multiple values.

| Call                      | Call                      | Pass-by     | Pass-by                                                                           |
|---------------------------|---------------------------|-------------|-----------------------------------------------------------------------------------|
| From                      | To                        | Simple type | Case property, complex business object, or shared business object                 |
| Activity                  | Linked process            | Value       | Reference (complex business object, shared business object)                       |
| Activity                  | Client-side human service | Value       | Value (complex business object, shared business object)                           |
| Activity                  | Other service             | Value       | Value (complex business object, shared business object)                           |
| Client-side human service | Nested service            | Value       | Value (case property, complex business object, shared business object)            |
| Other service             | Nested service            | Value       | Value (case property) Reference (complex business object, shared business object) |

Processes and services have references to their variables. When complex variables are passed from
a process to a service, a deep copy of the variable is transferred from the process space to the
service space, and the service gets a reference to the copy. Similarly, when a complex variable is
passed from the service to a process, a deep copy of the variable is transferred from the service
space to the process, and the process gets a reference to the copy.

When the service changes the values of the existing complex variable, the changed values are
passed back to the process by replacing the entire complex variable with a deep copy from the
service. If the replaced variable was originally passed by value from an outer process, the inner
and outer processes no longer access the same variable. Therefore, changes made to the inner process
are not reflected in the outer process.

Changes that you make to a shared business
object are saved and propagated to other instances that work with the same data. The setting
Automatically sync shared business objects must be enabled in the process or
service to enable the automatic save and data synchronization.

For example, a shared business
object is shared between a process and two different services. The process and services each contain
a separate copy of the business object. When the first service completes, the shared object values
are automatically persisted to the data store. When the second service starts, the shared object
values are automatically loaded from the data store. So even though the process and the two services
reference separate objects, the values of these objects are updated by the data store and the
services operate on current data.

For information about shared business objects, see Creating business objects.

```
Outer process -> NVP1
Inner process -> NVP1
```

```
Outer process -> NVP1
Inner process -> NVP1
Service -> NVP2
```

```
Outer process -> NVP1
Inner process -> NVP3
```

If you want a service to modify a top-level variable
in a process, use either an embedded server script to store the service
result in a temporary variable and copy its members to the original
variable, or a shared business object. The parent process is not updated
until the child process has finished.

## Guidelines for passing variables

Because
of how variables are handled at run time, follow these guidelines:

- If the variable is a simple type, declare the variable as an input and an output in linked
processes, services, and nested services.
- If an input variable is a complex
type and you are passing it from a process to a service, it will be
passed as a value. If you want the updated value to be returned, also
declare it as an output variable. If the complex type is a shared
business object, you do not need to return it as an output because
the updates that are made in a service will become visible to everyone
who uses the shared business object.
- Always use an identical name and data type for a set of input and output variables for data that
is passed in, processed, and then passed back.