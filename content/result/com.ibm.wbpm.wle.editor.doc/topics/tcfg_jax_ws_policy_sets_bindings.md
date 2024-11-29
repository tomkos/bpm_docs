# Attaching different policy sets or bindings to service references

## About this task

- SSO
- UNT
- ContentStore
- Embedded

- SSODiscoveryServiceRef
- UNTDiscoveryServiceRef
- ContentStoreDiscoveryServiceRef
- EmbeddedDiscoveryServiceRef

SSO-prefixed service references are configured to send a LTPA binary security
token so that user identities can be propagated to content management systems, such as IBM FileNet
Content Manager or IBM Content Manager when LTPA keys are shared.

Note that a
UNT-prefixed service reference does not have a WS-Security policy set and binding
assigned to set the actual user ID and password. These credentials are retrieved dynamically from
the process app settings so that the same service references are used to call out to all content
management systems that might expect different user IDs and passwords in a username token.

## Procedure

To attach a different policy set or binding to a service
reference, complete the following steps:

1. From the administrative console, click Services > Service Clients.
2. From the Service Clients page, select
the name of the service reference. For example, SSODiscoveryServiceRef.
3. Click Attach Client Policy Set and
select the name of policy set to attach.
4. Click Assign Binding to change the
name of the binding.
5. Save your changes.