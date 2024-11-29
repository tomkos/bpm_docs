<!-- image -->

# Developing interfaces: bottom-up

## Before you begin

## About this task

## Procedure

1. Create a new module. In the navigation, go to another module
with an interface already created, select the interface and from the
pop-up menu select Copy. Return to the new module, select it,
and from the pop-up menu select Paste. The interface is copied
to the new module. In our case, we copied the interface CreditReport
created in the top-down development of an interface section from a
module FinancialInformation to the module FinancialCreditInformation.
2. Open the assembly editor in the new module. From the palette,
select Component (with no implementation type).
As its name suggests, this is a component that has not been implemented.
Drag it onto the canvas. Rename it Credit Report Summary.
Right-click the component and from the pop-up menu, select Add >
Interface.
3. In the Add Interface window, select
the interface you added. In our case, it was CreditReport.
4. The interface is added to the component. Select the interface
and it is displayed in the properties view.
5. Right-click the interface and from the pop-up menu select Open
With > Interface Editor. The interface opens in the
interface editor. Looking at the properties view, the interface details
are the same as those in the original module. However, you can change
them if you want. Typically, in the bottom-up development of an interface
you would make a few changes, since your new component might have
a slight difference such as less inputs or outputs or a few different
data types.

## What to do next