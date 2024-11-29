<!-- image -->

# Viewing and changing qualifier settings

## About this task

- Where have qualifiers been set in my module, and what settings
have been used?
- Will current settings propagate a transaction from one component
to the next?
- When a transaction commits, what will be committed?

- If an element is not highlighted at all, it does not join or propagate
a transaction.
- A thickened solid green line around an element and along a wire
shows that the element joins a transaction and the wire propagates
a transaction. In the diagram below, Component1 and Import3 participate
in a transaction.
- A broken green line indicates that a transaction might be joined
or propagated but the system cannot confirm that will happen. The
line around Import2 in the diagram is broken, because the tools cannot
guarantee that the target web service can actually join the transaction.
A Java component reference might have a broken line leading to the
target service because the system cannot determine if the Java component
makes synchronous or asynchronous outbound calls
- A dotted line around a component indicates that the component
participates in at least one transaction, but it might participate
in more than one transaction.  In a long-running BPEL process or
a business state machine implementation, a component might call separate
services at different times. It might make a call to one service in
one transaction and a different service in another transaction. The
dotted line indicates that possibility.

When you add an interface or reference or create
an implementation, the assembly editor automatically adds appropriate
quality of service qualifiers and sets values that ensure reliability
and data integrity. See the "Preset values for quality of service"
table in Transactions in IBM Integration Designer.

To
see and edit the qualifiers that are used in a module, follow these
steps:

## Procedure

1. In the assembly editor, right-click an empty portion of
the canvas and select Show In > Properties View.
The Properties view is displayed.
2. In the Properties view, click the All Qualifiers tab.
All of the qualifiers defined in the module are displayed in
a table. White cells can be edited.
3. To instantly expand the rows for a particular component,
click the component in the assembly diagram canvas. You can also right-click
any row to adjust the display for that row.
4 To filter the contents of the qualifiers table, completeone of the following steps:
    - Click All Qualifiers to display all
qualifier categories, such as reliability, activity, and security.
This is the default selection.
    - Click Reliability Qualifiers to display
only reliability qualifiers.
    - Click Activity Session Qualifiers to
display only activity session qualifiers.
    - Click Security Qualifiers to display
only security qualifiers.
    - Click Options to open the Options window,
which enables you to select one or more qualifier categories and specific
qualifiers. Using the Options window, you can also choose other properties
that determine the contents or display of the table, such as the sorting
of rows and the ordering of columns.
5. To change the setting on a qualifier, click a qualifier
setting and select from the displayed list.