# Configuring multiple deployment environments

See Considerations for multiple deployment environments in the same cell for things to
consider prior to making changes to your deployment environment.

You must create unique HTTP endpoints for each deployment environment.
Optionally, you can specify different security settings for each deployment
environment by creating multiple security domains and attaching one
security domain to each deployment environment.

Only users that are assigned to the administrator role can configure multiple security domains.
For more information on multiple security domains, see Multiple security domains in the WebSphere® Application
Server documentation.

To isolate administrative access, you can specify administrative authorization groups to grant
administrative access only to the resources of a single deployment environment. Administrative
authorization groups are described in the WebSphere Application
Server
documentation at Fine-grained administrative security.

The following sections provide instructions
for three different configuration scenarios that isolate multiple
deployment environments within a single cell. Notice that each of
these sections includes instructions for configuring dedicated virtual
host aliases, which is a mandatory task. Choose the section that best
describes your intended configuration scenario.

- Isolating deployment environments

To isolate multiple deployment environments within a single cell, complete the following steps.
- Configuring security domains

To configure multiple deployment environments and security domains, complete the following steps.
- Configuring security domains and third-party authentication

To configure multiple deployment environments, security domains, and third-party authentication, complete the following steps.