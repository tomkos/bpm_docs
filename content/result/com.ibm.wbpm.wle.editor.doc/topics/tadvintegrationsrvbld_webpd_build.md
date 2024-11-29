# Building an Advanced Integration Service in the Process Designer

Traditional: 
 Create an
Advanced Integration Service (AIS) to call a service that is implemented in IBM® Integration
Designer .

An
Advanced Integration Service is the result of a collaboration between
a process developer and an integration developer. To learn more about
implementing an Advanced Integration Service, see Authoring services in IBM Integration Designer.

For
example, your business process might need a list of computer parts
in your warehouses in Canada. Checking with an integration developer,
you realize that a service is being built in Integration Designer to query
the Canadian warehouses and return an inventory list of the computer
parts available. Typically, the integration developer provides an
interface to this service in a toolkit. By adding the toolkit to your
process application, you can use the Advanced Integration Service
in a process or service flow to invoke the query against the warehouses.

## Before you begin

To create
services, you must have access to a process application or toolkit
in the Workflow Center repository.
Access to process applications and toolkits is controlled by users
who have administrative rights to the repository. For more information,
see Managing access to the Workflow Center repository.

## About this task

To build an Advanced Integration Service in the Process Designer,
follow these steps.

## Procedure

1. Open a process application in the Designer view.
2. In Services library click the plus sign (+). Then select
Advanced Integration Service from the list of artifact types, enter a name
for the service and click Finish. Process Designer displays the default values for the
service.
3. The Parameters section is initially
empty and cannot be edited. When an integration designer adds an implementation
to this service using Integration Designer, the interface
for this service is also updated in this view.
4. The Details section contains fields
that are used in Integration Designer that are
initially empty, with the exception of the Can be used
with a service flow? field. The fields are displayed when
the service is implemented in Integration Designer.  At that
time, depending on the implementation in Integration Designer, you might
also be able to change the Can be used with a service flow? setting.
For more information about each field, see the following:
Module name
The name of the module in Integration Designer that contains
the service implementation. 
Module version
The version of the module in Integration Designer that contains
the service implementation. 
Export name
The name of the export of the module that exposes the service
implementation. An export is the endpoint to be used when invoking
the service.
Operation name
The name of the operation of the service to be invoked. 
Can be used with a service flow?
Not all implementations of Advanced Integration Services can be
used with a service flow. If the implementation cannot be used with
a service flow or human service, this field is set to No. You can
always use an Advanced Integration Service in a Process regardless
of whether the Can be used with a service flow? field
is set to Yes or No. The following table summarizes the meaning 
Table 1. Implications of the value of the Can be used with
a service flow? field 

Can be used with a service flow? field
value
Can be used in a service flow
Can be used in a human service
Can be used in a process

Yes
Yes
Yes
Yes

No
No
No
Yes

Important: Do not use an Advanced Integration
Service with a services flow or human service if this field is set
to No, otherwise these services might experience
unexpected behavior.

The Can be used with
a service flow? field value is determined by the preferred
interaction style and operation type that is used by the associated
export in Integration Designer.
Table 2. How the value of the Can be used with a service
flow? field depends on the combination of preferred interaction
style and operation type

Interaction style
One-way operation type
Request-response operation type

Asynchronous
Yes
No

Synchronous
Yes
Yes
5. Save your work. From the menu, select File > Save All

## Results

An Advanced Integration Service can be used as the implementation
of a linked service flow activity in a service flow, as the implementation
of a system task in a process, as the implementation of a called service
in a Client-side Human Service or as an implementation of a nested
service in an heritage human service. If it is used by a user task,
it is assigned as specified by the assignments of the user task.

- Instead of invoking the implementation of the service, the emulation
requires a user to manually enter values for the service output variables.
- If it is used by a user task, it is assigned as specified via
the Assignments of the user task.
- If it is used by a system task then it will use the All users
group.

When All users is shown in emulation, any user selected
will require authentication. Select the user you are currently authenticated
as and enter your credentials.

As discussed earlier, your service
is a collaborative arrangement. Should you move your Advanced Integration
Service to another toolkit, notify the integration developer who implemented
your service. Your service and its implementation by Integration Designer are decoupled,
which means that even though you may move a service in Process Designer there
will not be an automatic corresponding movement in the implementation
by Integration Designer.

The
integration developer should use the refresh function to identify
the implementation that she needs to move and recouple with the Advanced
Integration Service that you moved in Process Designer.

In
general, after moving or copying an Advanced Integration service,
all properties, such as module and export name, are cleared and the
service must be imported into Integration Designer and re-implemented.

## What to do next