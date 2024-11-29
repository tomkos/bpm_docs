<!-- image -->

# Viewing and updating web service export bindings

## Before you begin

## About this task

The steps for administering web service bindings depend on the type of binding:

- For JAX-RPC bindings, you can view attributes of the binding.
- For JAX-WS bindings, you can view attributes of the binding and configure policy sets.

A policy set is a collection of policy types, each of which provides a quality of
service. These types have been configured and can be associated with a web service provider or
consumer.

Policy sets work in pairs. You must have the same policy set on the service requester as on the
service provider. Therefore, you should have the same policy set on the export binding as on the
client.

## Procedure

1. Select the module
that contains the binding by navigating to Applications > SCA Modules and clicking the
module name.
2 Selectthe binding by performing the following steps:
    1. In the Module components section,
expand Exports.
    2. Expand the export, and then
expand Binding.
    3 Click the binding to view information about its properties.
        - In the General Properties section, view the name, port, and location
(endpoint address) of the web service.
        - From the Related Properties list, click the interface to view the Web
Services Description Language (WSDL) file that is associated with the web service.
3 To change properties that are associated with the web module, click one of the followingproperties in the Web Module Properties list:

- Click Manage Export Binding Web Module to view or edit
deployment-specific information for a web module. For example, you can edit the Starting
weight, which specifies the priority of this module during server startup.
- Click Context Root to view the web module name and Uniform Resource
Identifier (URI) and edit the context root.
- Click Virtual Hosts to specify the virtual host for the web module.
Virtual hosts let you associate a unique port with a module or application.
- Click JSP reload options for Web modules to specify information about the
reloading of JavaServer Pages (JSP) files (such as the number of seconds to scan a file system for
updated JSP files).
- Click Session management to specify information about HTTP session
support. For example, you can set the number of minutes before a session times out.
4 For JAX-WS bindings only, configure policy sets for export bindings by performing the followingtasks:

1. Optional: 
Expand Preferences, indicate the maximum number of rows and whether you
want to retain the filter criteria, and click Apply.
2. Optional: 
Select the filter icon if you want to use a filter to search the table.
3. Select the export binding, and click Attach to attach a policy set to
the binding, or click Detach to remove the policy set.
4. To assign a policy set binding, select the export binding, click Assign
Binding, and provide a name for the policy set binding.
5. Repeat steps 4.c and 4.d for each binding you want to configure.
6. Save the changes to the master configuration.

## Results

To ensure
that the changes you made remain with the module across deployments,
use IBM Integration Designer to make the changes in the source code
for the module.