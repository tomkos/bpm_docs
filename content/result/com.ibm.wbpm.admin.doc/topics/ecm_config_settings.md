# Enterprise Content Management configuration settings: technical
details

In case A, if the Enterprise Content Management service is called by a system task, the user
that is identified in the process application settings is used for authentication. In case B, if the
Enterprise Content Management service is called by a human task, by a coach, or by an integration
service within a user task, the task owner identity is propagated to the ECM system. In this latter
case, the user ID and password set on the process application are ignored.

The policy set is a collection of assertions about how services are defined, which is used to
simplify security configurations. The product uses different web service references and different
policy sets and bindings for the two methods. The service references beginning with a username token
(UNT) are used when attaching the user ID and password to the ECM service calls (case A). The
service references beginning with single sign-on (SSO) are used when the user identity is propagated
to the ECM service (case B).

## Calls using a username token (case A)

When you configure access to an Enterprise Content Management server in the designer, you set a
user ID and password. If you use the default setting, the ID and password do not need to have
validity on the workflow server, but they must be valid for the Enterprise Content Management
server. At the end of the settings is a check box labeled Always use connection
information specified here. When that check box is selected, which it is by default,
that user ID and password are attached to all calls made from that process application to the ECM
server. The advantage of this method is that the Enterprise Content Management server is immediately
available for use by the actions in the process application. Selecting this check box triggers what
we are referring to as case A.

In case A, a static user name and password are defined in the process application settings. The
UsernameToken authentication mechanism requires a Simple Object Access Protocol (SOAP) header that
conforms to the WS-Security UsernameToken Profile. The header, containing the user name and
text-based password, must be sent in the SOAP envelope. The workflow server has code to add the user
name and password to the outbound call before the policy set and binding are applied. Therefore this
addition may not be obvious from the policy set and binding information that you can see associated
with the call.

## Calls using single sign-on (case B)

Case
B works without customization under three conditions:

- You are using an IBM WebSphere-based content management system.
- The Enterprise Content Management server has been configured to
use WS-Security.
- An Enterprise Content Management server has been defined in the
Process App settings under the Servers tab.

To use single sign-on, you must clear the check box labeled Always use connection
information specified here on the page where you set or change server settings.

In case B, by default Business Automation Workflow attaches
a policy set and binding that sends an LTPA token as a binary security
token in the SOAP header. If the Enterprise Content Management system
runs on WebSphere Application Server, shares the same user repository,
and has a matching provider policy set and binding attached, it will
understand this call and run under the user who works with the Business Automation Workflow system.

If you are establishing single sign-on (SSO) between Business Automation Workflow and a system that does not meet the requirements
set out in the previous paragraph, a system administrator must exchange the policy set and binding
files for ones configured to meet your particular system requirements. If your administration system
has some other strategy for SSO (perhaps because the ECM server is a non-IBM server and understands
a different type of token), you can detach our default policy set and create and attach another one
in its place.