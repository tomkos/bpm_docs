<!-- image -->

# Interface editor

- Parts of an interface
- Ways of starting to build an interface
- Interface development
- Restrictions

## Parts of an interface

An interface
consists of one or more operations and a binding style.

An
operation is a description of an action implemented by the component.
An operation may be a request-response type, meaning a request
is sent and a response returned to the interface, or a one-way type,
meaning only an input is sent and there is no response needed. Each
operation in the interface defines the data that can be passed in
the form of inputs to and outputs from the component
when the operation is invoked. Each operation may have one or more
faults to handle error conditions. A one way operation only has an
input. The binding style specifies the protocol and data format of
the operation.

In the screen capture that follows, an interface
has been created called CreditReport. CreditReport is the interface
to a component that will send a balance of a customer's account and
get the approval for a transaction, get the history of the customer's
account, and then update the customer's credit rating. Sending the
balance, getting the approval and the getting the history are request-response
operations. Updating the customer's credit rating is a one-way operation.

The
following parts of CreditReport are shown in the interface editor:

- Request response operation - getBalance when invoked sends thebalance of customer account and gets the approval for a transaction.getBalance contains the following inputs, outputs, and faults:
    - Input - getBalance sends as input the variable balance.
The variable balance must have a double data type.
    - Output - getBalance returns as output a variable named approval.
The variable approval contains a string recommending approval (if
funds are sufficient to justify granting credit) or rejection (if
funds are not sufficient to extend credit to the applicant).
    - Faults - getBalance may return one of two faults, both of which
are strings describing an error condition: timeout is returned
if the service waits for an excessive amount of time to determine
approval; systemFailure is returned if there is communication
or power failure.
- Request response operation - getHistory when invoked sends thename of a customer account and gets the history of the customer'stransactions. getHistory contains the following inputs, outputs, andfaults:

- Input - getHistory sends as input the variable customerName.
The variable customerName must have a string data type.
- Output - getHistory returns as output a variable named customerPastHistory.
The variable customerPastHistory contains a string with a record of
past transactions.
- Faults - getHistory may return one of two faults, both of which
are strings describing an error condition: timeout is returned
if the service waits for an excessive amount of time to determine
approval; systemFailure is returned if there is communication
or power failure.
- One way operation - updateCreditRating when invoked sends thecurrent credit rating of the customer. updateCreditRating has thefollowing input:

- Input - updateCreditRating sends as input the variable currentRating.
The variable currentRating must have a string data type.

<!-- image -->

By default, all added
inputs and outputs of any simple type are mandatory fields. If the
interface is used in a human task and you generate a client user interface
for the human task, the input and output fields in the client user
interface will be flagged with an asterisk to indicate that the fields
are mandatory and values must be specified.

Selecting an input,
output, or fault from the table opens further details about them in
the properties view of the interface editor. For example, selecting
customerPastHistory results in the following information in the properties
view. You are shown the properties and can change the name and data
type. Were customerPastHistory a business object, you could open it
in the business object editor.

<!-- image -->

Should
you click outside the table with the operations, inputs, outputs,
and faults, you can see the properties for the interface; specifically,
its name, namespace, folder and documentation.

<!-- image -->

Selecting an operation and then selecting the Details tab
in the properties view shows the binding style and operation type
of the operation. The binding style is viewable, though not editable.
Should you build an interface with the interface editor, the editor
will use document literal wrapped style as the default binding
style. See binding style for
more information.

## Ways of starting to build an interface

IBM® Integration
Designer is
a flexible development environment that lets you determine the best
approach for application development. You can build interfaces either
before or after component implementation with the same results. Choose
your interface build process to complement your particular development
process.

Should you decide to build your interfaces first and
implement them later, you would start the interface editor from the
menu bar or by selecting a module and launching a context menu. You
are presented with a menu of the business perspective editors and
wizards, which includes the interface editor.

The other approach
is to build your component first in the assembly editor and then add
an interface to it. In this case, after building your component, you
select it can add an interface to it.

<!-- image -->

## Interface development

The
following approaches can be taken in developing an interface; which
approach you choose depends on your circumstance. All three approaches
are shown in the documentation.

- Top-down development - Use this methodology when there is no existing
interface to work with. You launch the interface editor, provide a
name for the interface, and add one or more operations to it. Inputs,
outputs, and faults are added to each operation.
- Bottom-up development - Use this approach when you already have
an interface created as a Web Services Description Language (WSDL)
file. In this case, you import it into a module and then start the
interface editor. The editor will display the interface as operations,
inputs, outputs, and faults. You can then use the interface editor
to modify operations, inputs, outputs, and faults.
- Meet-in-the-middle development - Use this approach when you have
an interface that either exactly matches the interface needs for a
component or is close to what you need. Drag the interface onto the
component and it will either be a perfect fit, or you may need to
make a few modifications to it with the interface editor to make the
interface work. Meet-in-the-middle development saves you development
time.

## Restrictions

A single
component cannot have multiple operations with the same name, since
at run time the correct operation cannot be determined. The interface
editor, therefore, does not allow you to have two or more operations
with the same name.

Avoid
duplicate business objects and duplicate WSDL interfaces. You might
not notice the duplicates if they are in another library or module
that you are interacting with. See Duplicate business objects.