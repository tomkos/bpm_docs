<!-- image -->

# Create the mediation flow

## About this task

To create a mediation flow, follow these steps:

## Procedure

1. Open the assembly editor, if it is not open. Double-click Assembly
Diagram under SeparateCustomers.
2. From the Palette, select Mediation
Flow, release the mouse button and then click with the
mouse button again when you want the mediation flow to be placed onto
the canvas. Place it between CustomersIn and SeparateCustomerOut.
Rename the mediation flow to InboundToOutbound.
Save your work. From the menu, click File > Save.

The entries you will see in the Problems view
will disappear at the end of this section.
3. Double-click InboundToOutbound.
A message asks if you would like to implement the component now. Click Yes.
A Generate Implementation window opens. Accept
the defaults and click OK. The mediation flow
editor opens.
4. Near the top of the editor, select Add Interface.

In the Add
Interface window, select CustomersIn and
click OK.
5. Near the top of the editor, select Add Reference.

In the Add
Reference window, select SeparateCustomerOut and
click OK.
6. In the mediation flow editor, click the emit link
and from the Select a Mediation Flow Template window
click the Operation Map link. In the Select
Reference Operation window, select SeparateCustomerOutPartner and
click OK. Save your work. From the menu, click File
> Save.
7. In the Request tab of the mediation
flow editor, double-click the input\_map node
to implement the input map.  
The New XML Map window
opens. Accept the defaults and click Finish.
The map editor opens.
8. In the map editor, expand the emit element
to reveal the emitInput element. Expand the create element
to reveal the createInput element. Click the Add
Connection handle beside the emitInput element.
Drag the handle to the createInput element
to create a Move transformation. 
Save your work. Close the map editor.
In the mediation flow editor, save your work. Close the mediation
flow editor. In the assembly editor, save your work.
Since emit is
a one-way operation and the application is splitting the content into
separate files and creating output files from the split content, the
application is complete at that point. Therefore, there is no need
to map the response.
9. Connect the components. In the assembly editor, select
the handle on the right end of CustomersIn and
drag it to the left end of InboundToOutbound.
A message tells you that the service interface from the export will
be added to the target. Click OK. Select the
handle on the right end of InboundToOutbound and
drag it to the left end of SeparateCustomerOut.
A message tells you that a matching reference will be created on the
source. Click OK. Save your work.