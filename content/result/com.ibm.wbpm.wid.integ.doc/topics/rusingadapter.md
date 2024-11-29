<!-- image -->

# Considerations when working with IBM Business Automation
Workflow tasks

The following sections describe areas for your attention
when working with BPEL processes and case management tasks:

- Handling faults
- Working with generated code
- Long-running processes
- Managing configuration changes
- Boundary cases

## Handling faults

A common
way of handling exceptions in BPEL processes is to use business faults.
However, you will find that the interface editor in  Integration Designer  will
not let you add faults to the generated interface. IBM Business Automation
Workflow tasks
do not support business faults. Given this circumstance, what could
you do to handle an exception in another way?

There are several
techniques which avoid the use of business faults on the interface:

- Design the business interface such that it returns normal and
error values through the normal interface outputs.
- Use a human task to handle the error within the BPEL process such
that a normal return value can subsequently be passed back to the
case management task through the normal interface output.

## Working with generated code

The external service wizard produces Web Services Description
Language (WSDL) code and business objects (XSDs). Exports, imports
and stubs for the BPEL process are also among the generated artifacts.
These artifacts also contain the module name containing the artifacts.
The FileNet repository is highly dependent on the content of these
generated files. As a rule, you should not modify them as the implementation
on the FileNet repository and the web service will become out-of-sync.
 If you do make a change like renaming the generated export or import,
you will need to use the edit binding function to synchronize the
implementations as discussed in Editing and validating exports used with IBM Case Manager tasks.

A seeming inconsistency
may appear in the name of a case property because in Case Manager
a user could change the display name though not the symbolic name.
 When a web service is created, Integration Designer will show
the display name but use the symbolic name in the generated code.
 In the business object, you will see the symbolic name.

## Long-running processes

Use the generated long-running process stub for developing your
long-running process. In other words, do not try to connect to an
existing long-running process rather than using the generated stub.
Inside the generated long-running process stub are elements needed
for a BPEL process that is in-sync with the particular case management
task associated with the web service.

## Managing configuration changes

Changes to the original configuration created in Integration Designer will likely
occur. Input and output parameters for a task can change as case management
applications change. Configuration changes can occur because services
have been moved to another server, which you may or may not know about.
To manage expected and unexpected changes, use the edit binding and
validate functions as discussed in Editing and validating exports used with IBM Case Manager tasks.

## Boundary cases

Boundary
cases are situations that are not common but could occur. The boundary
cases that follow are situations where there is only a request, that
is, a one-way input; only a response, that is, only an output, and
lastly the case where there is no input or output. In these situations,
follow the steps provided.

Microflow

1. Generate a correct input business object and an empty output business
object.
2. Generate a two-way interface; that is, an interface with a request-response
operation.
3. Generate receive and reply activities in your BPEL process. At
run time, receive a correct input business object from the FileNet
repository and reply with an empty output business object to the FileNet
repository.

1. Generate an empty input business object and a correct output business
object.
2. Generate a two-way interface; that is, an interface with a request-response
operation.
3. Generate receive and reply activities in your BPEL process. At
run time, receive an empty input business object from the FileNet
repository and reply with a correct output business object to the
FileNet repository.

1. Generate an empty input business object and output business object.
2. Generate a two-way interface; that is, an interface with a request-response
operation.
3. Generate receive and reply activities in your BPEL process. At
run time, receive an empty input business object from the FileNet
repository and reply with an empty output business object to the FileNet
repository.

Long-running process (macroflow)

1. Generate a correct input and output business object. For the output
business object, the only property should be the correlation ID.
2. Generate a two-way interface; that is, an interface with a request-response
operation.
3. Generate receive, assign and invoke activities in your BPEL process.
At run time, receive a correct input business object from the FileNet
repository, assign the correlation ID from the input business object
to the output business object, and reply with the output business
object with the correlation ID to the FileNet repository.

1. Generate a correct input and output business object. For the input
business object, the only property should be the correlation ID.
2. Generate two one-way interfaces; that is, interfaces with a request
operation.
3. Generate receive, assign and invoke activities in your BPEL process.
At run time, receive the input business object with the correlation
ID from the FileNet repository, assign the correlation ID from the
input business object to the output business object, and reply with
the output business object to the FileNet repository.

1. Generate a correct input and output business object. For the input
and output business objects, the only property should be the correlation
ID.
2. Generate two one-way interfaces; that is, interfaces with a request
operation.
3. Generate receive, assign and invoke activities in your BPEL process.
At run time, receive the input business object with the correlation
ID from the FileNet repository, assign the correlation ID from the
input business object to the output business object, and reply with
the output business object with the correlation ID to the FileNet
repository.

No process

1. Generate a correct input business object and an empty output business
object.
2. Generate a two-way interface; that is, an interface with a request-response
operation.

1. Generate an empty input business object and correct output business
object.
2. Generate a two-way interface.

1. Generate an empty input business object and an output business
object.
2. Generate a two-way interface.