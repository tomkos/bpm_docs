<!-- image -->

# Deploying a stand-alone adapter

## Before you begin

1. Set this value in the configuration properties window to enable a stand-alone adapter. In the
Deploy connector project properties list, select On server for use
by multiple applications.
2. When you export the application, review the dependencies settings in IBM® Integration
Designer for the module. Deploy with
module under Java EE must be unchecked for the dependent RAR file
modules associated with a stand-alone adapter.
3. Ask an administrator to set up the RAR file on the application server.

## About this task

At deployment time, an administrator installs the adapter RAR file on each node of the
application server cluster and configures some properties.

## Procedure

To deploy a stand-alone adapter, complete the following steps:

1. Locate the RAR file for the adapter you want to use and that it is accessible by the
administration console. Look for the adapter RAR files in your Integration Designer installation at the following path, which is
where they are typically located:
install\_root/ResourceAdapters/adapter\_name/adapter.rar
2. In the Integrated Solutions console, go to the resource adapters section
and click Resources > Resource Adapters.
3. Select Install RAR.
4. Select a node that contains an application cluster member and browse for the RAR file
identified in the first step.

Note: The RAR file must be installed on each node that contains a cluster member.
5. Click OK and save your changes.
6. Repeat steps 3-5 until the RAR file is installed on every node that contains an application
cluster member.
7. Change the scope of the Resource Adapters page to that of the application
cluster and select New.
8. Add a name. For Archive Path, choose the RAR file you installed.
9. Set the custom properties that you want under Additional Properties. See
specific adapter documentation for more details about individual configuration properties.

Note: If you run multiple instances of the same adapter, ensure that the first seven characters of
the adapter ID property are unique for each instance. Then, you can correlate the log and trace
information to a particular adapter instance.

## Results

A stand-alone resource adapter is deployed to the application cluster scope for use with your
application's adapter bindings.