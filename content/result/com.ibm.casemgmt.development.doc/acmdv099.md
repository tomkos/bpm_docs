# Request modes

You must configure the external data service to respond
with the data that is required for that action. For example, if the
request is to create a case, the service needs to respond with the
initial property values that are defined for the case type.

The requestMode parameter
indicates the action that is being performed in Case Client. This action determines
the response that is returned by the external data service.

The input payload
does not contain the externalDataIdentifier parameter.
Instead, this parameter is set by the external data service and returned
in the response payload. Subsequent requests made during the creation
of the case include the externalDataIdentifier parameter
to indicate the current state of the data to the service.

The input payload also contains the objectId parameter
that specifies the GUID of the root folder for the case. The service
can use this GUID to refer to the case. However, remember that the
values stored in the repository for the case can change. Therefore,
the values that are provided in the input payload might not match
the values that are currently stored in the repository for the case.

The input payload does not contain the externalDataIdentifier parameter.
Instead, this parameter is set by the external data service and returned
in the response payload. Subsequent requests made during the update
of the case include the externalDataIdentifier parameter
to indicate the current state of the data to the service.

- The current working value for each property in the case.
- The externalDataIdentifier parameter, which
indicates to the service the previous state of any properties that
it updated.
- For an existing case, the objectId parameter,
which specifies the GUID of the root folder for the case.

The external data service responds to this request if the
attributes or working value of any property that it manages changed.
The service also responds to return a custom validation error.

For each property, the input payload that is
passed to the service contains the working values for all properties
that are defined by the case type.

For each property, the input payload that is passed
to the service contains the working values for all properties that
are defined by the case type.