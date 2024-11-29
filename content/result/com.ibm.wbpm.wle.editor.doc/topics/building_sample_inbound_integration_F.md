# Creating an inbound web service

## Before you begin

To perform
this task, you must be in the IBM Process
Designer desktop
editor, which is deprecated.

## About this task

Now you need to provide a way for an external system
or application to call into IBM Business Automation Workflow. The
recommended method for accomplishing this is to create and publish
a web service endpoint so that external applications can initiate
a particular Business Automation Workflow service
or set of services by invoking an operation on the endpoint. By invoking
a SOAP call, external applications can call the web service.

All
operations that are exposed on an inbound web service are exposed
as request-response operations. Even an operation bound to a service
that has no outputs will be exposed as a request-response operation
with no output. One-way operations are not supported.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application in the Designer view.
3. Select the plus sign next to the Implementation category
and then select Web Service from the list.
4. In New Web Service, type KickTheBPD in
the Name field and then click the Finish button.
5. In the Operations section, click the Add button
and select the Inbound WS Handler Integration service
that you created in the preceding procedure from the list.
6. In the Operation Detail section, change Untitled in
the Operation Name field to doKick or something similar.
7 Notice the WSDLURI in the Behavior section. You can use thisURI to test the sample integration as instructed in Testing the integration . The Protected checkbox adds user name and password security to an operation in the webservice. For a web service client to invoke a protected operation,the user ID and password added to the user name and password elementsfor this operation must be registered at the server, assigned to theprocess application and have at least read authority. Note that thisis not authentication in the context of an HTTP transaction, so selecting Protected doesnot display a default user ID and password. The Targetnamespace scheme drop-down list provides options for settingthe target namespace: The following table shows the resulting target namespace dependingon the value you choose for the scheme, the namespace setting forthe process application, and where the web service is running. Combination Resulting URI http://xyz/web\_service\_name.tws http://xyz/snapshot/web\_service\_name.tws http://host:port/teamworks/webservices/proc\_app/web\_service\_name.tws http://host:port/teamworks/webservices/proc\_app/snapshot/web\_service\_name.tws http://custom\_namespace

The Protected check
box adds user name and password security to an operation in the web
service. For a web service client to invoke a protected operation,
the user ID and password added to the user name and password elements
for this operation must be registered at the server, assigned to the
process application and have at least read authority. Note that this
is not authentication in the context of an HTTP transaction, so selecting Protected does
not display a default user ID and password.

    - Per process app or toolkit settings (default):
Use the namespace from the XML Settings section
of the Process App Settings page and do not
include the snapshot name. This is the recommended setting because
the target namespace remains consistent across multiple snapshots.Important: If the process application namespace is not set,
the target namespace instead uses the per snapshot scheme. For more
information, see the table that follows this list of options.
    - Per snapshot name : Use the snapshot nameas well as the namespace from the XML Settings sectionof the Process App Settings page. This meansthat the namespace value in the web service client targets a specificsnapshot. Important: In the following situations,the namespace of the Web Services Description Language (WSDL) filechanges and you must obtain a new file to maintain consistency betweenthe namespace used by the client and the namespace on the server: Remember: Versions of Business Automation Workflow before8.0.1 use, in effect, the snapshot name scheme. Attention: In a web service that uses business objects thatare defined in a toolkit, after you update the toolkit namespace inthe advanced XML Settings and switch the snapshotdependencies to the updated namespace, the generated WSDL might notcontain the updated namespace. If you find that the namespace is notupdated in the generated WSDL, open the business objects definitionin the updated snapshot in the Process Designer andclick View XML Schema to update the namespace.
        - When the application namespace is not consistent with the namespace
on the server.
        - When the host name and port changes and the inbound web service
uses a business object defined in the System Data toolkit, which uses
a host name and port specification.
        - When you create a snapshot and switch a service to the inbound
web service in the new snapshot.
        - When you switch from a specific snapshot to the default snapshot
or from the default snapshot to a specific snapshot.
- Custom name: Use only the value specified
in the Target namespace field.

| Combination                                                                                                                                   | Resulting URI                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Process App namespace set to http://xyz value  Use process app or toolkit scheme                                                              | http://xyz/web\_service\_name.tws                                                |
| Process App namespace set to http://xyz value  Run on a snapshot that is not tip or default Use snapshot scheme                               | http://xyz/snapshot/web\_service\_name.tws                                       |
| Process App namespace set to no value  Run on a tip or default snapshot Use process app or toolkit scheme or Use snapshot scheme              | http://host:port/teamworks/webservices/ proc\_app/web\_service\_name.tws          |
| Process App namespace set to no value  Run on a snapshot that is not tip or default Use process app or toolkit  scheme or Use snapshot scheme | http://host:port/teamworks/webservices/ proc\_app/snapshot/web\_service\_name.tws |
| Use Custom scheme                                                                                                                             | http://custom\_namespace                                                        |

8. Select the SOAP version you want to use.
9 The Security and Policy sectionallows you to configure a policy set and a policy binding with yourweb service. The server must have been already configured by a systemadministrator. Note: SOAP header information is available in systemvariables. The tw.system.soap.header.request variableis automatically initialized to contain the list of SOAP header entriesfound in the incoming request message. You can include JavaScriptcode with your inbound web service which accesses these SOAP headerentries. You can also write JavaScript code which adds SOAP headerentries to the tw.system.soap.header.response systemvariable. The SOAP header entries contained in this variable are addedto the outbound response message.

- Policy Set: Specifies the name of the application
policy set. Click Select to choose the policy
set.  The list you will see depends on the policies available on the
server. Some default application policy sets include: WSHTTPS default,
WSAddressing default, and Username WSSecurity default. You can also
create additional application policy sets in the WebSphere Application
Server Administrative Console. Deselecting a policy set also removes
the policy binding. More information on policy sets can be found in
the IBM Redbook WebSphere Application Server Web Services Guide.
- Policy Binding: Specifies the name of the
general provider policy set binding, which contains system-specific
configuration parameters like username and password information. Click Select to
choose the policy binding. The list you will see depends on the general
provider policy set bindings available on the server. Default policy
set bindings include: Provider sample and Provider sample V2. You
can also create additional policy set bindings in the WebSphere Application
Server Administrative Console. Deselecting removes the policy binding.
10. Save your work. Limitation: Any variable
with a simple type containing a restriction element will not have
the restriction element on generation of the inbound web service.

## What to do next

If you do not specify a snapshot name in the URI, then
the default track is used to locate your web service. The tip in the
default track is assumed to contain the process application with your
web service. However, if you have your web service on a tip in a non-default
track, it cannot be found. Therefore, create a snapshot name or make
the track that you are working with the default track.