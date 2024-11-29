<!-- image -->

# Viewing and updating SCA import bindings

## Before you begin

## About this task

To view information about an SCA import binding or to change the target of the associated module,
use the administrative console to complete the following steps.

## Procedure

1. Select the module
that contains the binding by navigating to Applications > SCA Modules and clicking the
module name.
2 Selectthe binding by performing the following steps:
    1. In the Module components section,
expand Imports.
    2. Expand the import, and then
expand Binding.
    3 Click the binding to view information about its properties.
        - Module identifies the module that contains the import with this import
binding.
        - Version displays the SCA module version, if the module is versioned.
        - Cell ID identifies the SCA module instance in the cell.
        - Import identifies the import that contains the selected import
binding.
        - Import interfaces contains the list of interfaces for the import of this
module.
3 To select a new target SCA module, perform the following steps:

1. Select a module from the Target list.

Selecting another SCA module changes the exports and export interfaces that are displayed.
2. Select an export from the Export list.
4. Save your changes to the master configuration.

## Results

To ensure
that the changes you made remain with the module across deployments,
use IBM Integration Designer to make the changes in the source code
for the module.