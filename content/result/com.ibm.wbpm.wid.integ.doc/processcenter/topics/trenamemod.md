<!-- image -->

# Renaming a module or library associated with a process application
or toolkit

## About this task

A module or library that has been associated with a process
application has a relationship with both the Process Center and the
workspace. If, during iterative development, you change (refactor)
its name and then publish the updated module or library, you might
experience deployment failures or unexpected behavior in the process
application or toolkit.

To avoid problems, follow these steps
when renaming a module or library that is already associated with
a process application or toolkit.

## Procedure

1. Ensure you are logged in to IBM Integration Designer with
the necessary permission.
2. (Library only) Remove any dependencies on the library.
3. Disassociate the library or module from the process application
or toolkit.
4. Rename the library or module, using the refactoring function.
5. Associate the renamed library or module with the process
application or toolkit.
6. (Library only) Reinstate any dependencies you removed.