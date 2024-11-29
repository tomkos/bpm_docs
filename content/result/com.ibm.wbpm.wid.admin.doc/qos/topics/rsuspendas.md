<!-- image -->

# Suspend activity session qualifier

By default, activity session context is always propagated to a
target component when it is invoked using the synchronous programming model.
If the client does not want a target component to federate with the client's
activity session, further qualification of the reference is required using
the suspend activity session qualifier.

Location: The suspend
activity session qualifier is set on a reference.

- False (default) - The target component's methods
that are invoked using this reference will run as a part of any client activity
session, but only if the target component also joins any client activity session.
- True - The target component's methods that are
invoked using this reference will not run as part of any client activity session.

## Programming notes

The suspend activity session qualifier
is ignored if the invocation occurs using any of the asynchronous interaction
styles. The client activity session is not propagated if the client uses any
asynchronous interaction styles. This reference qualifier is also ignored
if the invocation occurs outside the scope of an activity session.

This
qualifier does not affect the activity session environment of the target component.
That is, the target component's hosting container is still entirely responsible
for providing the activity session environment that is required by the implementation.