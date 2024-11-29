<!-- image -->

# Viewing and updating web service import bindings

## Before you begin

## About this task

The steps for administering web service bindings depend on the type of binding:

- For JAX-RPC bindings, you can view attributes of the binding and edit the target endpoint.
- For JAX-WS bindings, you can view attributes of the binding, edit the target endpoint, and
configure policy sets.

A policy set is a collection of policy types, each of which provides a quality of
service. These types have been configured and can be associated with a web service provider or
consumer.

## Procedure

1. Select the module
that contains the binding by navigating to Applications > SCA Modules and clicking the
module name.
2 Selectthe binding by performing the following steps:
    1. In the Module components section,
expand Imports.
    2. Expand the import, and then
expand Binding.
    3. Click the binding to view
information about its properties.
3. Change the value of Target endpoint address, which is the location of
the web service, and then click Apply or OK.
4 For JAX-WS bindings only, configure policy sets for import bindings by performing the followingtasks:

1. Optional: 
Expand Preferences, indicate the maximum number of rows and whether you
want to retain the filter criteria, and click Apply.
2. Optional: 
Select the filter icon if you want to use a filter to search the table.
3. Select the import binding, and click Attach to attach a policy set to
the binding, or click Detach to remove the policy set.
4. To assign a policy set binding, select the import binding, click
Assign Binding, and provide a name for the policy set binding.
5. Repeat steps 4.c and 4.d for each binding you want to configure.
5. Save your changes to the master configuration.

## Results

To ensure
that the changes you made remain with the module across deployments,
use IBM Integration Designer to make the changes in the source code
for the module.