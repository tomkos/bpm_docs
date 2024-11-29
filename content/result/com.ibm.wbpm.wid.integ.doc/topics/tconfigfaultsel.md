<!-- image -->

# Creating a fault selector resource configuration

## Before you begin

## About this task

## Procedure

1. Right-click the module and from the menu select New
> Configure Binding Resource. The Binding Resource
Configuration window opens. Select Fault Selector and
click Next.
2. In the Select fault selector page,
select an existing fault selector or choose a custom fault selector
from your workspace.  The Fault selector
class name field lets you select a class from an existing
list of fault selectors. The list is contextual; that is, depending
on how you create your configuration, you may find a list of fault
selectors that is supplied with the product or you may not find a
list at all. For example, if you had created an import with a JMS
binding and then in the Faults Configuration section
of the Properties view launched the Select button,
you would find some existing fault selectors provided by the product
because the product can determine the context for the fault selector.
To
create your own fault selectors, you would read Developing a custom fault selector.
Once you had created one or more fault selectors, you would add them
to the product's fault selectors by adding them through the Binding
Registry section of the Preferences page
as discussed in Binding registry preferences page. 
Note that only classes on the class
path with a name following this pattern <class name>Properties are
selectable. 
Click Next.
3. In the Fault Selector Properties page,
add the properties. Since we selected the header-based fault selector,
the names for the headers were required. Click Next.
4. In the New Binding Resource Configuration page,
enter a name for your fault and, optionally, a folder. Click Finish.
5. The fault selector resource configuration is completed
and shown in the editor. The fault selector is listed in the navigation
under Binding Resources. In the editor, you
can choose to expose this fault selector resource configuration to
other bindings besides the bindings chosen by the wizard by selecting
the binding in the Select bindings table.