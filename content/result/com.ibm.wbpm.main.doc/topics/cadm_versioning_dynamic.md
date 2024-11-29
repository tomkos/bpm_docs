<!-- image -->

# Version-aware dynamic invocation

If you use the IBM\_VRM style (<version>.<release>.<modification)
for the snapshot, you can export the process application EAR file
to WebSphere Service Registry and Repository (WSRR). When you create
the mediation module, you then configure the endpoint lookup to use
version-aware routing. For example, you select Return endpoint
matching latest compatible version of SCA module-based services from
the Match Policy field, and you select SCA for Binding
Type.

Future versions of the process application are deployed to the
server and published to WSRR, and the mediation module endpoint lookup
dynamically invokes the latest compatible version of the service endpoint.

Note that, as an alternative, you can set the target in the SMOHeader,
and the value can be carried by the request message.