# Creating a web service

## About this task

To provide a way for an external system or application
to call your services, create and publish a web service endpoint.
The web service endpoint invokes an operation that calls a particular
service or set of services.

All operations that you expose
in a web service are request-response operations. Even an operation
that is bound to a service that has no outputs is still a request-response
operation that has no output. One-way operations are not supported.

```
https://host\_name:port/[custom\_prefix/]teamworks/webservices/process\_app\_name/[snapshot\_name/]web\_service\_name.tws
```

If
you do not specify the snapshot\_name in the endpoint URL, it points to the tip
snapshot of the default branch for the playback server or to the default snapshot for a workflow
server.

## Procedure

To create the web service:

1. Open the designer.
2. Select the plus sign next to Exposed Automation Services and then
select Web Service from the list.
3 Name the new web service. Note: Only ASCII characters are allowed in the following: Rationale: From the web service definition, a valid WSDL is generatedthat adheres to the respective specifications. The web service editor opens.
    - The name of the web service
    - The target namespace of the web service (see step 4)
    - The target namespace of the process application, or toolkit settings (see step 4)
    - The name of an operation (see step 5)
    - The names of the input or output of the service flow (see step 5)
    - The names of the business objects referenced by the inputs or outputs of the service flow (see
step 5)
    - The properties of the business objects referenced by the inputs or outputs of the service flow
(see step 5)
    - The namespace in the advanced properties of the business objects referenced by the inputs or
outputs of the service flow (see step
5)
4 In the Behavior section: Note: SOAP header information is available in system variables. Thetw.system.soap.header.request variable is automatically initialized to contain thelist of SOAP header entries found in the incoming request message. You can include JavaScript codewith your inbound web service which accesses these SOAP header entries. You can also writeJavaScript code which adds SOAP header entries to thetw.system.soap.header.response system variable. The SOAP header entries containedin this variable are added to the outbound response message.

- Traditional:  If you want to add
user name and password security to the operations, enable Protected. The user
name and password must be registered at the server and the user name must have at least read access
to the process application. Note that the protection is not authentication in the context of an HTTP
transaction, so selecting Protected does not display a default user ID and
password.
- Containers:  Users are authenticated using HTTP basic authentication.
- Notice the WSDL URI in the Behavior section. You can use this URI to test the exposed web
service.
- Set the scheme used to create the target namespace for the web service in Targetnamespace scheme . The target namespace depends on the scheme that you pick, thenamespace setting in the process app or toolkit settings, and the snapshot. See the table below thescheme options for more information.. The following table shows the resulting target namespace depending on the value you choosefor the scheme, the namespace setting for the process application, and where the web service is running. Combination Resulting URI http://xyz/web\_service\_name.tws http://xyz/snapshot/web\_service\_name.tws http://host:port/teamworks/webservices/proc\_app/web\_service\_name.tws http://host:port/teamworks/webservices/proc\_app/snapshot/web\_service\_name.tws http://custom\_namespace
    - Use process app or toolkit settings (default): Use the namespace from the
XML Settings section of the Process App Settings page
and do not include the snapshot name. This is the recommended setting because the target namespace
remains consistent across multiple snapshots. Important: If the process application
namespace is not set, the scheme instead uses the host and port of the local machine and, if it
exists, the snapshot name.
    - Use snapshot name : Use the snapshot name as well as the namespace fromthe XML Settings section of the Process App Settings page. This means that the target namespace value in the web service client targets a specificsnapshot. Important: In the following situations, the namespace of the Web Services DescriptionLanguage (WSDL) file changes and you must obtain a new file to maintain consistency between thenamespace used by the client and the namespace on the server:
        - When the application namespace is not consistent with the namespace on the server.
        - When the host name and port changes and the exposed web service uses a business object defined
in the System Data toolkit, which uses a host name and port specification.
        - When you create a snapshot and switch a service to the exposed web service in the new
snapshot.
        - When you switch from a specific snapshot to the default snapshot or from the default snapshot to
a specific snapshot.
- Custom: Use only the value specified in the Target
namespace field.

| Combination                                                                                                                                   | Resulting URI                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Process App namespace set to http://xyz value  Use process app or toolkit scheme                                                              | http://xyz/web\_service\_name.tws                                                |
| Process App namespace set to http://xyz value  Run on a snapshot that is not tip or default Use snapshot scheme                               | http://xyz/snapshot/web\_service\_name.tws                                       |
| Process App namespace set to no value  Run on a tip or default snapshot Use process app or toolkit scheme or Use snapshot scheme              | http://host:port/teamworks/webservices/ proc\_app/web\_service\_name.tws          |
| Process App namespace set to no value  Run on a snapshot that is not tip or default Use process app or toolkit  scheme or Use snapshot scheme | http://host:port/teamworks/webservices/ proc\_app/snapshot/web\_service\_name.tws |
| Use Custom scheme                                                                                                                             | http://custom\_namespace                                                        |

- Select the SOAP version you want to use.
5. For each function that you want your web service to support, add an
operation. In the Operation Detail section, name the operation. If the
service flow that provides the functionality is already defined, you can attach it to the
operation. If this service flow does not yet exist, click New  to
create it now and attach it to the operation. For information about service flows and how to create
them, see Creating a service flow. Tip:  Traditional:  By default, the list
of services that you can attach contains only service flows. If you want to attach a service created
in Business Automation Workflow V8.5.7.0 or
earlier and it has not been converted into a service flow, select the Show heritage
services checkbox at the bottom of the list of services. The list of attachable services
now includes these services. They are categorized according to their type. These services are not
editable in the web Process Designer. If you want to edit
them, you must open them in the desktop Process Designer.
6 Traditional: In thePolicy section, specify the application policy set and then specify thepolicy binding for the web service.

- Policy set: Select the application policy set from the list available
on the server. Selecting no policy set removes any existing policy binding.The policy set
contains configuration and security settings. For additional information about policy sets, see the
IBM Redbook WebSphere Application Server Web Services Guide. Some default application
policy sets include WSHTTPS default, WSAddressing default, and
Username WSSecurity default. You can also create custom application policy sets in
the WebSphere Application Server Administrative Console.
- Policy binding: After you have selected the policy set, select the
policy binding from the list of general provider policy set bindings available on the server. The
policy binding is not available until you select the policy set that the binding applies to.The
policy binding contains the system-specific configuration parameters like username and password
information. Default policy set bindings include Provider sample and
Provider sample V2. You can also create custom policy set bindings in the WebSphere
Application Server Administrative Console.
7. Click Save or Finish
Editing.