<!-- image -->

# Administering EIS bindings

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
    3. To view the WSDL, expand Interfaces and select the interface you want to
view. 
The WSDL of the interface is displayed. The WSDL cannot be edited through the
administrative console but can be altered with text editors.
    4. To view the binding, expand Bindings and click the import or export
binding that you want to view. You can change the port or the name of the imported or exported
service.
3. Optional: 
Change the port or the name of the imported or exported service.
4. Save your changes to the master configuration.

## Results

To ensure
that the changes you made remain with the module across deployments,
use IBM Integration Designer to make the changes in the source code
for the module.