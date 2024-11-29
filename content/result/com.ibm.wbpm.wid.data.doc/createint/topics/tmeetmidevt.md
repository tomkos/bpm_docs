<!-- image -->

# Developing interfaces: meet-in-the-middle

## Before you begin

## About this task

## Procedure

1. Open the module with the component that is already implemented
in the assembly editor. In our case, we have a Java™ component with the following methods:

Table 1. Java implementation
of component

Method
Input Arguments
Returned Data

loginAccount
Business object containing userid and password
String (login success or failure)

selectAccount
String accountName
Void

updateAccount
Boolean performCredit, Integer amount
Integer (balance after update)

Our component has no interface, which is shown when it is
selected in the assembly editor.
2. Find an interface in another module that exactly fits your
implementation or closely fits it. In our case, we found an interface
that would fit with the component previously described. Specifically,
we looked for an interface with operations and inputs and outputs
that could closely match those of the methods in the Java implementation. The interface we found
and slightly modified was as follows:
3. Copy the interface to the module with the implementation
with no interface. Select the interface in the navigation and from
the pop-up menu, select Copy. Select the module
with the implementation with no interface and from the pop-up menu
select Paste. We copied our Account interface
shown previously.
4. Right-click your component in the assembly editor and select Add
> Interface.
5. In the Add Interface window, select
the interface you added. In our case, it was Account. The interface
is added to the component. Select the component and in the properties
view the new interface has been added.

## What to do next