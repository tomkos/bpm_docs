<!-- image -->

# Viewing and updating MQ JMS bindings

## Before you begin

You must have permission to make and save changes to the profile on the administrative console.

The queue and queue manager are not automatically generated; they must be created in WebSphere® MQ by your
WebSphere MQ
administrator.

## About this task

## Procedure

1. Select the module
that contains the binding by navigating to Applications > SCA Modules and clicking the
module name.
2 Select the binding by performingthe following steps:
    1. In the Module components section,
expand Imports or Exports.
    2. Expand the import or export,
and then expand Binding.
    3 Click the binding to view informationabout its properties. The general properties of the bindingare displayed: Note: You can also access a resource by typing the JNDI namein the text box. Doing so, however, allows you to enter the name ofa resource that is not yet configured.
        - The Send Resources category contains the
Connection Factory and the Send Destination.
        - The Receive Resources category contains
the Response Connection Factory and the Activation Specification.
        - The Advanced Resources category contains
Callback resources and other available resources.
3 Make any required changes to the resources:

1. Click Browse to open a window with a list of JNDI names; then, select
the required JNDI name.
The selected name will populate the appropriate text field.
2. Click Configure to open the corresponding page referred to by
the JNDI name.

Note: Most resources can be configured at the cluster scope. However, when you select the
Configure option for the activation specification, a page is displayed
that shows all activation specifications for all members of the given cluster; you can then
select one activation specification.
4. Save your changes to the master configuration.

## Results

To ensure
that the changes you made remain with the module across deployments,
use IBM Integration Designer to make the changes in the source code
for the module.