# Third-party authentication in federated
process environments

The topic Planning the topology of your federated
environment describes topologies that include Process Federation Server and a dedicated
server for hosting Workplace and  Process Portal, such as the default
production topology shown in the following graphic:

In these topologies, connections from Process Federation Server to
federated systems run on behalf of the end user. These requests can
fetch the list of items that can be started and ensure that Process Federation Server has
up-to-date group membership and team membership information in order
to apply authorization for task list queries.

To augment your topologies with third-party authentication, you
need a firm understanding of the following concepts:

- Customized
authentication
- Cookie propagation

These concepts provide options for avoiding the use of Lightweight Third Party Authentication
(LTPA). One reason for wanting to avoid LTPA is the lack of horizontal propagation in WebSphere
Liberty Profile that underlies Process Federation Server. It is impossible to transmit additional attributes about the user between Liberty Profile and
WebSphere® Application
Server Network Deployment using LTPA. As a result, you may have
a Trust Association Interceptor (discussed later), which asserts additional group memberships when
authenticating a request into Process Federation Server. Forwarding LTPA to a federated system would not carry these custom group memberships. This could
possibly lead to unexpected results when working with BPEL tasks in Human Task Manager that are
configured with group work items.

The concepts of customized authentication and cookie propagation
are described in the following two sections.

## Customized authentication

In the default topology shown in the previous graphic, the authentication mechanism assumes that
all relevant servers have the following characteristics:

- Share a common network domain
- Share LTPA keys and cookie name
- Have the same user registry configuration (such as a connection
to the same LDAP server), including matching realm-name configuration

There are several reasons why you might want to customize
this default behavior. The most common reason is to implement corporate
intranet-wide SSO using third-party authentication systems, such as IBM® Security Access
Manager or
CA Single Sign-On (formerly CA SiteMinder). These products not only
allow seamless access to many intranet applications (without prompting
end users for credentials for every single application they access),
they also come with additional features. For example:

- Session management (which allows a maximum number of active sessions
for each user and re-authentication based on idleness)
- Audit capability
- Access control or even request content filtering
- Multi-factor authentication

In WebSphere Application
Server, there is a plug point named Trust
Association Interceptor (TAI) that allows third-party authentication software vendors and customers
to plug custom code into the authentication process for inbound web requests. (For detailed
information about TAI, see the documentation topics Developing a custom trust association interceptor and Configuring TAI in Liberty.)

When
an unauthenticated request for a protected resource reaches the web
container of WebSphere Application
Server,
the security run time iterates through the list of registered TAIs
and allows each of them to determine if it can handle the current
request. The first TAI that responds true receives
full control over the HTTP request and response. It can inspect all
aspects of the request (such as cookies, HTTP headers, etc.), contact
remote servers, respond in order to implement a challenge response
scheme, or simply forward it to a login form.

Many third-party
authentication products are implemented as reverse proxy components
in front of the actual applications. Typically, their TAI inspects
cookies and headers (assuming that they were injected by the intermediary
server) and then either callback, decrypt or validate a signature
to establish trust.

Ultimately, if the TAI successfully validates
information provided in the inbound request, it can either assert
just a user name or a full JAAS subject to WebSphere Application
Server.

Adding
an authenticating reverse proxy to the topology simplifies interactions
from the browser. It connects to a single server component and maintains
a single authentication cookie. The authenticating reverse proxy performs
any required validation and forwards requests to the various connected
back-end systems, as shown in the following graphic:

As mentioned, each
WebSphere-based back-end system can be configured with a vendor-supplied
TAI that authenticates requests based on information that might have
been injected by the reverse proxy component, which avoids the use
of default login forms.

For SSO from the browser into the various applications in the SSO domain, the sharing of LTPA
keys is not technically required because authentication is handled by the third-party authentication
components. Authentication using LTPA might even be disabled in order to enforce the route through
the third-party authentication component, which ensures consistent audit logging and centralized
access control and session management. As a result, connections between Process Federation Server and the federated systems can be
complicated. In the previous diagram, the red connections between Process Federation Server and the two HTTP servers might not be
possible. Instead, Process Federation Server can be
required to connect to the federated systems through the third-party authentication component, which
is shown in the previous diagram as a green connection that directly connects Process Federation Server to the authenticating reverse
proxy.

These third-party authentication
systems can enforce complex challenges for authentication (such as
text messages sent to a mobile device as a second authentication factor),
which means that it is impossible to support all third-party authentication
products from the perspective of the out-of-the-box Process Federation Server.
Instead, generic support is provided by cookie propagation, which
solves most (if not all) customer scenarios that have been encountered
up to this point in time.

## Cookie propagation

When a
user’s browser requests the federated task list from Process Federation Server for
the first time using a REST request, Process Federation Server connects
to each of the federated systems to query the user’s group and
team membership information. This enables the appropriate filtering
to be applied on the task list query. The membership information is
temporarily cached in Process Federation Server,
which means that later task list queries may or may not trigger the
same set of interactions.

By default, in order to connect to
a federated system as the end user, Process Federation Server injects
the LTPA token cookie into outbound requests. As mentioned earlier,
there are third-party authentication scenarios in which these requests
are forced through a third-party authentication system that will probably
not accept LTPA tokens for authentication. Instead, the third-party
authentication system expects a set of cookies that identify the authenticated
user session. For this reason, Process Federation Server has
been extended to allow propagation of cookies from inbound to outbound
requests, as shown in the following configuration properties:

```
<ibmPfs\_bpdRetriever   
    internalRestUrlPrefix="https://bpmHost.mycompany.com:9443/rest/bpm/wle"
    federatedSystemRef="bpm1"
    connectTimeout="10s"   
    readTimeout="10s"
    propagateCookieNames="PD-S-SESSION-ID"   
    cacheCookieNames="JSESSIONID,PD-S-SESSION-ID"
/>
```

The configuration property propagateCookieNames allows
you to specify a comma-separated list of cookie names that are extracted
from an inbound request and propagated with an outbound request. The
configuration property cacheCookieNames allows
you to specify a comma-separated list of cookie names that are extracted
from a response of a federated system and are cached for each user.
These two properties allow Process Federation Server to
appear as the end user to a third-party authentication system in case
a direct connection to a federated system is impossible.

If you are using a third-party authentication system, you do not necessarily need to set up
cookie forwarding or ensure that requests from Process Federation Server to federated systems pass through the
third-party authentication system. It is very possible that you set up the third-party
authentication system for initial authentication only. In this scenario, there is no login form used
to access any of the Business Automation Workflow or IBM BPM applications in case the user is already signed
into any other application on your intranet. However, the various systems in the previous diagram
still share LTPA keys and have matching realm names and user registry configurations, which enables
the default forwarding of LTPA token cookies to work.