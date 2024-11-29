<!-- image -->

# Policy sets and binding considerations for IBM Business Automation
Workflow tasks

A policy set is a collection of policy types that
are configured and associated with a given web service provider or
requester. Policy sets do not include environment or platform-specific
information, such as the key for signing, keystore information, or
persistent store information. These types of information are defined
in the binding.

## Default policy set and bindings

- BPM FileNet® Web Services
policy set
- BPM FileNet Web Services
- Provider binding
- BPM FileNet Web Services
- Client binding

The default provider binding is set on the web service
export. If a web service import was generated, the default client
binding is set on it as well. These policy set bindings act as starting
points for your configuration.

## Considerations for modifying policy set bindings

In
some cases, the default policy set binding might not be appropriate
for your particular use. You can create a new policy set binding to
add or remove the capabilities of the default binding and associate
it with a policy set.

To associate an application-specific binding
with a policy set, you copy the default binding and modify it. For
example, the BPM FileNet web
services policy set includes the WSAddressing policy and the WSSecurity
policy. The WSSecurity policy defines, among other things, the parts
of a message that are encrypted and signed, but not how they are encrypted
and signed.

If you create an application-specific binding for
that policy on an application, you can specify the particular certificates
used to encrypt and sign those parts of the message.

For instructions
on performing these tasks, see  Securing Web services using policy sets.