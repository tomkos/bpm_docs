# Particular object type resource

You do not use this resource directly in your case management application. Instead, the workflow
REST protocol calls the POST method for resource automatically when a case is
being added or modified to communicate with the external data service. The service then returns the
required information in the response to this method call.

- POST method for the particular object type resource

The POST method provides the means for obtaining data from an external data source for a case of a specific case type. You do not call this method directly. Instead, the workflow REST protocol calls this method automatically when a case is being added or modified.
- Request modes

When a case is created or modified in Case Client, the workflow REST protocol calls the POST method for the particular object type resource to submit a request to the external data service. This request contains a request mode that indicates the action that is being performed.
- Client context for work items

The clientContext parameter provides contextual information about a work item that a case worker opened. An external data service can use this information to determine the appropriate response. For example, an account identifier might typically be read-only. However, if the work item is to open an account, the external data service can set the account identifier to be writable.
- Response to a request for case data

The external data service responds to a POST method that was submitted by the workflow REST API. The response payload contains values for the properties that are managed by the service.
- Error responses for an external data service

If the POST method call fails, the response code that the workflow REST protocol returns indicates the type of error that occurred.