<!-- image -->

# Synchronizing the interfaces and references between components
and implementations

After a component in the assembly diagram has been associated
with an implementation, the interfaces and partner references must
be kept synchronized. The assembly editor in IBM® Integration
Designer provides
a mechanism that allows you to maintain this synchronization.

If you have developed a component using a top-down development
style, the component's interfaces and references will be synchronized
with the implementation when you generate the implementation. If you
develop the component further by adding a new reference or interface
or by modifying an existing interface or reference, the implementation
is no longer synchronized with its component. When the component and
its implementation are not synchronized, errors appear for the component
in the assembly diagram. An error is flagged as a small red x on the
component, on the interface, or on a reference.

In the same way, after you have generated an implementation, you
might further develop it. In doing so, you might add, modify, or delete
the features in the implementation that correspond to the component's
interfaces or references. Such changes leave the implementation and
component no longer synchronized.

If you have developed the implementation first and then created
the component for it using the bottom-up development style, the component's
interfaces and references are also initially synchronized with the
implementation. However, further changes to the component's interfaces
or references or further changes to the implementation's features
that correspond to those interfaces and references can result in them
no longer being synchronized. The assembly editor will display an
error on the component for each mismatch.

To remove the errors by synchronizing a component with its implementation,
you must first decide which has the most up-to-date information. If
you edited the implementation, synchronize the interfaces and references from the
implementation to the component. If you made changes to the component
in the assembly editor, synchronize the interfaces and references to the
implementation from the component.

## Synchronize interfaces and references from the implementation

1. In the assembly editor, right-click the component.
2. In the pop-up menu, select Synchronize
interfaces and references > from implementation.
3. You will be warned that this action cannot be undone. Click OK to
continue.
4. If a message prompts you to save all editors, click OK to
continue.

When the operation completes, the interfaces and references
on the component and implementation should be synchronized and related
errors will have been removed from the component.

If the interfaces and references on the component are the most
current ones, follow these steps to synchronize to the implementation:

1. In the assembly editor, right-click the component.
2. In the pop-up menu, select Synchronize
interfaces and references > to implementation.
3. You will be warned that this action cannot be undone. Click OK to
continue.
4. If a message prompts you to save all editors, click OK to
continue.

When the operation completes, the interfaces and references on
the component and implementation should be synchronized and related
errors will have been removed from the component.

## Related tasks

- Creating an implementation for a component
- Opening an implementation
- Replacing an implementation
- Changing the implementation type of a component