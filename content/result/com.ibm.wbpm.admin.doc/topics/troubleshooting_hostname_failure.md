# SSL fails when host name configuration fails

```
javax.net.ssl.SSLException: hostname in certificate didn't match: requested\_URL\_or\_SSL\_connection != certificate\_common\_name
```

For more information about host names, see the related links at
the end of this topic.

## Certificate configuration using the common name (CN)

When a connection is established to a secure port, the initial
handshake involves verifying the certificates. When you connect to
a remote server over HTTPS, Business Automation Workflow expects
the common name in the SSL certificate of the remote server to match
the host name of the computer that it connected to. However, there
are several scenarios in which Business Automation Workflow connects
to itself using HTTPS. Therefore, Business Automation Workflow must
be set up with a certificate that has a common name that matches the
host name that Business Automation Workflow uses
when it connects to itself.

When a profile is created, IBM WebSphere® Application
Server by default
generates a self-signed root certificate that is valid for 15 years.
In a distributed environment, a certificate is generated for each
node and signed with the root certificate. The common name (CN) in
the certificate is the same as the host name that is specified during
profile creation.

SSL is a point-to-point connection. The common name in the certificate
must match the host name of the computer that is trying to connect.
When Business Automation Workflow is
configured to connect to itself through a web server, the web server
must be set up with a certificate that has a common name that must
match the host name that is used by Business Automation Workflow to connect
to this web server.

## Certificate configuration using Subject Alternative
Name (SAN) sets

In the X.509 certificate standard, the Subject Alternative Name
(SAN) extension enables a set of alternative values to be associated
with a single certificate. For example, a set of DNS names or IP addresses
can be specified as alternative values for a host name.

If you have configured Secure Sockets Layer (SSL) communication
and the name of a server certificate does not match the host name
of a server, an SSL connection failure may occur with the IOException
message HTTPS hostname wrong. To help
resolve this problem, you can add a Subject Alternative Name (SAN)
set to the server certificate.

When a client (like IBM Workflow
Server)
verifies a host name (such as for Workflow Center) during
an SSL handshake, it checks whether the server certificate has a SAN
set. If a SAN set is detected, only the names or IP addresses in the
SAN set are used. If no SAN set is detected, only the most significant
attribute of the subject distinguished name (DN) is used, which is
typically the subject common name (CN). This value is compared with
the host name to which the client is attempting to connect.

This is the expected behavior that is implemented in the IBM SDK
for Java and it is consistent with RFC
2818.

If you need the server side (such as Business Automation Workflow) to be
available over SSL on multiple host names, you must create certificates
with a SAN set. The set can contain multiple comma-separated lists
that are comprised of entities like DNS names or IP addresses.

In WebSphere Application Server, SSL certificates are created without
SAN sets by default. Also, the WebSphere administrative console does
not provide any fields for adding SAN sets to SSL certificates. However,
you can use a tool like the iKeyman utility, which is shipped with
the Java Runtime Environment of WebSphere Application Server, to add
SAN sets to SSL certificates.

## Problem scenarios and solutions

One problem
occurs if you install and test Business Automation Workflow using localhost as
your host name. Later, if you try to connect with an external name,
for example https://myname.mycompany.com:9443/bpm/rest,
or if you try to connect from another computer, the verification fails.
The failure of the connection generates an error in Process Inspector
and the Process Admin Console. To avoid this problem, the configuration
documentation warns against using localhost as
the host name. Particularly, the configuration documentation warns
against using localhost for environments that
are spread across multiple computers.

If you have a locally
installed Workflow Center that
you use for your own development purposes, set up your environment
with a host name such as bpm.company.com. On the
Windows operating system, set this environment in your Windows hosts
file. Always use that host name to access the Workflow Center server.

In
a production environment, always access clusters through the HTTP
server. The HTTP server must be accessible from Business Automation Workflow and must have a fully qualified host name with
a matching certificate.