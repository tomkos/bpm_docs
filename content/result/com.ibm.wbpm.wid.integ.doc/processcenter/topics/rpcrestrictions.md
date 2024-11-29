<!-- image -->

# Limitations when working with process applications and toolkits

The following sections group the limitations
as follows:

- Limitations when deploying IBM Integration Designer V8.5.7 applications
- Limitations for the definition of an Advanced Integration Service in IBM Process Designer and its implementation in IBM Integration Designer
- Limitations on the configuration of process applications and toolkits
- Limitations when creating a business process definition or an Advanced Integration Service
- Limitations for SCA service interfaces that are based on the receiving message events of a BPD

## Limitations when deploying IBM Integration
Designer V8.5.7 applications

- You can deploy Integration Designer V8.5.7
applications to IBM® Business Automation
Workflow V18.0.0.0. However,
you can't deploy Integration Designer applications to
IBM Business Automation
Workflow V18.0.0.1 unless you install the fix
at JR59572: YOU CAN'T DEPLOY IBM INTEGRATION DEVELOPER APPLICATIONS TO IBM BUSINESS
AUTOMATION WORKFLOW.

## Limitations for the definition of an
Advanced Integration Service in IBM Process
Designer and
its implementation in IBM Integration
Designer

- It is recommended that only one request-response operation be
defined in the Web Services Description Language (WSDL) file associated
with an Advanced Integration Service. Using one request-response operation
per interface reduces the risk of generating multiple WSDL files in Process Designer when
changes occur.
- A binding style specifies how a service is bound to a messaging
protocol. Binding style is sometimes called the WSDL style or encoding
style. An interface for an Advanced Integration Service must be of
the document literal wrapped binding style.
- An SCA export should have only one interface. As discussed in
other limitations, using one interface and one operation reduces the
risk of generating multiple WSDL files in Process Designer when
changes occur.
- An operation parameter must be a valid Java name.
- The following types are not supported: anySimpleType, QName.
- The runtime validation is not enforced for XSD enumeration, duration,
hexBinary, base64binary types, or ID or IDREF references in any part
of the system.
- A list of XSD / WSDL restrictions as defined in XML constructs not supported.
- If you import a process application and later refresh it with
updates from the Workflow Center,
you may see attributes marked deleted and added instead of an expected
delta change such as a renamed attribute. These changes are from the Workflow Center and
are caused by the differences between the Process Designer and Integration Designer programming
models.
- You cannot use full-length Latin and half-width Katakana characters
in SCA component names (eg BPEL or mediation flow component) in Integration Designer even
though these characters are permitted in IBM Process
Designer and
the Workflow Center.
This restriction is an XML standard restriction on XML names.
- If you want to use a WebSphere adapter in a stand-alone resource
adapter configuration, you will need to restart the Workflow Center or Workflow Server after
installation of the adapter before you can deploy an application from
the Workflow Center that
uses the adapter.
- You can make a service in Integration Designer available
to Process Designer.
This approach of starting an Advanced Integration Service in Integration Designer is
known as a bottom-up approach. Should you create an interface with
multiple operations and a business programmer makes changes to any
of them in Process Designer then
multiple files will be generated.To prevent this error, place the
interfaces and data types in a toolkit with read-only access for the
business programmer. This recommendation is discussed in Best practices when using IBM Integration Designer
and IBM Process Designer together. Alternately, use only one
operation for each interface.
- In a bottom-up approach as described previously, an Advanced Integration
Service parameter that is typed to a wrapped array created in Integration Designer will
be represented in Process Designer as
a list type if the following conditions are true: the wrapped array
has only one child element; the maxOccurs indicator element has a
value of unbounded; there are no attributes; and the element has an
ArrayOf type name.
- If a Process Designer user
modifies a business object (or XSD) the business object inProcess Designer will
get regenerated based on the business object model definition. The
result is that the business object you published may not be the business
object you receive.
- If you use an element reference, be aware that once the Process Designer user
modifies the element reference, the global element will become a global
type and the references will be broken since the global element is
no longer present.

## Limitations on the configuration of
process applications and toolkits

- Modules and library names must be unique in a process application.
- When you disassociate a default project (for example, the default
module: PA\_Implementation or the default library: PA\_Library), you
cannot then reassociate the same default project that you have disassociated.
To associate the disassociated default project back to the Process
Center, you must rename the project before you can associate it to
the same process application or toolkit in the Process Center. If
a process application does not have a default project associated to
it (for example, the default module: PA\_Implementation or the default
library: PA\_Library), when you open that process application in your
workspace, a default project is automatically created.
- When a toolkit is shared with another Workflow Center,
you can open the tip of the toolkit and the tip of the process application
in the same workspace. Before using the refresh and publish action,
however, you must right-click the toolkit and change the snapshot
version to the snapshot version that the process application depends
upon.
- Testing process applications on the Workflow Center server
using the integration test client requires that an HTTP connection
be available. When only an HTTPS connection is available, the deployment
manager connection information cannot be obtained and testing a process
application will fail.

## Limitations when creating a business
process definition or an Advanced Integration Service

- When you create a business process definition (BPD) or an Advanced
Integration Service (AIS) for the same process application or toolkit,
you need to make sure that the BPD and the AIS both have a unique
name so that the WSDL they each generate will also have a unique name.
This makes sure that both WSDLs are integrated in your project. This
applies to an Advanced
deployment environment only.

## Limitations for
SCA service interfaces that are based on the receiving message events
of a BPD

- You cannot
refactor the interface name because it is generated by Process Designer
based on the BPD name and the service identifier specified for the
receiving message event.
- You cannot
refactor the binding style or operation name for any service interface
because they are generated by Process Designer.