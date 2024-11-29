<!-- image -->

# Viewing and updating Generic JMS bindings

## Before you begin

## About this task

## Procedure

1. Select the module
that contains the binding by navigating to Applications > SCA Modules and clicking the
module name.
2 Selectthe binding by performing the following steps:
    1. In the Module components section,
expand Imports or Exports.
    2. Expand the import or export,
and then expand Binding.
    3 Click the binding to be administered. The general properties of the binding are displayed: Note: You can also access a resource by typing the JNDI name in the text box. Doing so,however, allows you to enter the name of a resource that is not yet configured.
        - The Send Resources category contains the Connection Factory and the Send
Destination.
        - The Receive Resources category contains the Response Connection Factory,
the Listener Port, and the Activation Specification.
        - The Advanced Resources category contains Callback resources and other
available resources.
3 Administer the required resource:

1. Click Browse to open a window with a list of JNDI names; then, select
the required JNDI name.
The selected name will populate the appropriate text field.
2. Click Configure to open the corresponding page referred to by
the JNDI name.
While most resources can be configured at cluster scope, selecting the
Configure option at Listener Port displays a page showing all
listener ports with the cluster Listener Port names for all the members of the given cluster; you
can then select one listener port.When Configure has been selected, the
corresponding WebSphere® Application
Server
page will open.
4. Save your changes to the master configuration.

## Results

To ensure
that the changes you made remain with the module across deployments,
use IBM Integration Designer to make the changes in the source code
for the module.