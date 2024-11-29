# Re-creating heritage human services as client-side human services in the Process Designer

- If the server script only requires simple access to or simple manipulation of local variables,
create a client-side script in the client-side human service and enter the same logic into it. You
can copy and paste the server script content into the client-side script. If your script includes
instantiation logic, it might require adjustments, as specified in the following note.
- If the server script includes complex server-side operations, create a service flow that
contains a server script that has the script logic. In your client-side human service, use a service
activity to call the service flow that you created.

```
// To instantiate and populate a complex variable
tw.local.customer= {};
tw.local.customer.firstName = "Jane";
tw.local.customer.lastName = "Doe";

// To instantiate and populate an array
tw.local.addresses = [];
tw.local.addresses[0] = {};
tw.local.addresses[0].city = "Boston";

// To instantiate a String variable
tw.local.customerID = "12345";

// To create a Date variable
tw.local.dueDate = new Date();
```

- If the server script logic includes complex operations or requires access to private or
confidential data, create a service flow that contains a server script that has the validation logic
and use it as described earlier.
- If your server script logic requires simple access to local variables and does not require
access to private or confidential data, select the page node in the client-side human service
diagram, and then use the Data Change properties of the page to implement the
validation logic. For more information, see JavaScript API for client-side human service development.