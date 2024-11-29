# Symbolic names

Typically, the symbolic name is generated from the display
name that you enter for an object. The symbolic name begins with a
letter and consists of uppercase and lowercase ASCII letters, decimal
digits, and underscores. It can contain a maximum of 64 characters.
The Content Platform Engine enforces
that symbolic names are unique within an object store.

- Certain URI elements, including class names and object store names
- Values for query parameters that reference metadata objects
- The JSON payload for the names of object stores, case types, and activity types

Content Platform Engine requires
symbolic names that are unique within the object store for metadata
objects such as document classes and property templates. Instance
objects, such as documents and folders, do not have symbolic names.
For these objects, you use the GUID that is assigned to the object
in the target object store.

In addition, solutions
do not have symbolic names. To reference a solution, you use the solution
name that is defined in Case Builder.