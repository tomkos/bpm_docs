# Binding a complex data structure to a Table control in a heritage coach (deprecated)

## Before you begin

## About this task

If you have created a complex data structure and you want to bind it to a Table control in a
heritage coach, you do not have to create the table and then bind each element of the table to the
appropriate variable parameter. You can create the table and the bindings automatically by dragging
the data structure to the heritage coach.

A complex data structure is a private variable
in an HR process used to submit requests to open new positions. You
can see this process and its variables in the Hiring Sample process
application. (For more information see the IBM Business Process Management
documentation.

At one point in the process, a General Manager must approve a submitted request. The heritage
coach displays the information submitted in the requisition to enable the General Manager to make a
decision. The GM Approval service (in the Hiring Sample process application) includes the
requisition variable as both input and output. This enables the heritage coach to display the
requisition parameters to the General Manager and then the service passes the values of the
parameters in the requisition variable back to the BPD for processing by subsequent steps in the
process.

## Procedure

1. To display the values of the parameters in the requisition variable in a
heritage coach, click the Coaches tab.
2. Drag the input requisition variable from
the palette to the design area.
3. Right-click and select Delete for
the parameters that should not be displayed as output text; select
all remaining fields and change the Control Type to Output
Text.
4. Click the Section option in the
properties and increase the number of columns to 2.
5. Click the Preview tab to see how the table will look when the service
runs. 
When you run the tutorial BPD, the heritage coach displays the table with the appropriate data
for the manager to act upon.