# Planning security for your federated environment

## User authentication

A common user registry is required for Workplace, Process Portal, Process Federation Server, and the
IBM BPM, Business Automation Workflow or Case Manager systems, so that
authenticated users can access the entire environment. Supported user registries include LDAP and
custom user registry. In development and test environments, you can also use a file-based basic
registry.

To provide Workplace
and Process Portal users
access to all the systems across the federated environment, configure single sign-on (SSO). SSO
ensures that users can access Process Federation Server and federated
systems through their browsers. It also ensures that requests that are forwarded from Process Federation Server to federated
systems are authorized. A typical SSO solution uses cookies that are saved in the user's browser
after the initial login. For the cookies to be accepted by all the systems, the domain names across
the federated environment must be the same. For example, in your federated environment, Process Portal is available at
portal.mycompany.com, Process Federation Server at
pfs.mycompany.com, and the federated systems at bpm1.mycompany.com
and bpm2.mycompany.com. In both quick-start and production environments, browser
clients must use the full domain name to access any system in the federated environment. For
example, to access Process Portal browser clients must
use portal.mycompany.com.

## Secured communications

Communications are secured with Secure Sockets Layer (SSL) protocol. The SSL protocol provides
transport-layer security that includes authenticity, data signing, and data encryption to ensure
secure communication between a client and server. In a federated environment, a component can act as
a server to one component, and as a client to another component.

If the remote federated data repository service (Elasticsearch or
Opensearch cluster) uses SSL to secure communications, you must import the certificate exposed by
the remote federated data repository service into the Process Federation Server truststore.

Figure 1. Quick-start environment

<!-- image -->

Of the servers that are shown in Figure 1,
only Process Federation Server
has a configured truststore for the communication with the IBM BPM, Business Automation Workflow or Case Manager systems through
their REST services. Because SSL is optional for REST services, you can therefore eliminate all
server-side SSL for development environments that do not require security. To simplify security
configuration in a quick start development environment, configure Process Federation Server to connect to
the REST services through the HTTP port on the IBM BPM, Business Automation Workflow or Case Manager system instead
of the secured HTTPS port.

Figure 2. Production environment

<!-- image -->

For secure server-to-server
communication, configure SSL between each component. Each component that acts as a client to another
component must have a signer certificate in a truststore. You therefore need to have an overall plan
for signer certificates. For example, configure all the servers to use certificates that are signed
by a certificate authority (CA). The CA can be a third-party CA, or a CA that is internal to your
organization. You then have a single common signer certificate that you can import into each
truststore.

- If the browser connects directly to the federated environment, a signer certificate for each of
the process federation servers and federated systems that it communicates with.
- If the browser connects to the federated environment through IBM HTTP Server, a signer
certificate for each of the IBM HTTP Servers.

If CA-signed certificates are not used, for example, in a development or test environment, users
must import signer certificates into their browsers before they use Workplace or  Process Portal in the federated
environment. The signer certificate can be manually imported into the browser. Alternatively, the
user can go to the URL for each component in the federated environment that Workplace or Process Portal communicate with, and
accept the certificate when prompted.

## Cross-origin resource sharing (CORS)

The browser that displays Workplace, Process Portal or the custom client
application makes requests to Process Federation Server and federated
systems. Because the requested services are not on the system that originated Workplace, Process Portal or the custom client
application, the federated components use CORS to enable the browser to trust the cross-origin
requests. You must therefore configure a list of allowed origins for Process Federation Server and the
federated systems. The allowed origin is the web server that hosts Workplace, Process Portal or the custom client.
For more information, see Configuring allowed origins for Process Portal .