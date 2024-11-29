<!-- image -->

# Join activity session qualifier

- For all of its interfaces
- For an individual interface
- For an individual operation of an interface

- True - The hosting container will join any activity
session propagated by a client.
- False (default) - The hosting container will not join
any activity session propagated by a client.

## Programming notes

Asynchronous component implementations
should not expose join activity session set to "true" on any of its asynchronous
interfaces.