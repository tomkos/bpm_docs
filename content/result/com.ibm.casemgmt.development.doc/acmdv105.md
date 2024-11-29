# Persistence of case data

For the final call to the external data service, the requestMode parameter
is set to finalNewObject for a new case or finalExistingObject for
an updated case.

- A value that is explicitly passed to the protocol by Case Client is checked against any
property attributes that are returned by the external data service. If the value passes validation,
that value is saved for the case in Content Platform Engine. If the value does not pass
validation, the protocol returns an error.
- If a value is not explicitly passed by Case Client and the service passes a value
for the property, that value is saved for the case in Content Platform Engine.
- If a value is not explicitly passed by Case Client and the service does not pass
a value, the default value for a new case is saved for the case in Content Platform Engine. For an existing case, the
current value is unchanged. However, the REST protocol checks the default value or current value
against any property values returned by the service. If the value does not pass validation, the REST
protocol returns an error.

Typically, if the requestMode parameter is
set to finalNewObjector finalExistingObject,
the external data service overrides the current working value of a
property if that value is invalid. Typically, the service validates
property values in earlier requests, so this situation rarely occurs.
However, you can implement the service to override invalid property
values. In particular, the service can override a property value when
the display mode is set to read-only. The case worker cannot change
the property value in this situation.