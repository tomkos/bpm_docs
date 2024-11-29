<!-- image -->

# Changing an external service without interruption

One advantage of using an intermediary module is that you can then
change the external service or application that your application is
invoking without interruption. This example uses a web service import
to illustrate the concept.

The first figure below shows module A with an import that invokes
a remote service through a direct connection. If you wanted module
A to invoke a different remote service, you would need to update the
logic. You would then need to stop the old version of the module and
uninstall it from the server. The new version of the module can then
be installed and started. During this process, there is an interruption
of service for module A.

<!-- image -->

If you use an intermediary module in your application and connect
it to module A with an SCA binding, you have more flexibility. The
figure below shows that configuration. Module A has an import that
is wired to the export of an intermediary module or mediation module,
module B. The modules must have matching interfaces. In the scenario
described in this topic, they must have an SCA binding. Module B invokes
the service. Module B is a facade; module A contains the real business
logic.

The figure also shows another service, remote web service 2. In
preparation for using that service, module C and its web service import
have been built and tested using the WebSphere® Test Environment.

<!-- image -->

When that new module is ready to be deployed, you can use the IBM® Workflow
Server administrative console to point the SCA import in module A from
the old target module (module B) to the SCA export in the new one
(module C), creating a seamless transition to the updated service.
The figure below shows the new deployment. You can use this method
to update an application without causing any interruption in service.

<!-- image -->

This pattern can also be used for external exports. For example,
a module can expose a service through a web service export. Typically,
if the logic of the module needs to be updated, there would be an
interruption in service. However, if a facade module is used for the
web service export, the business logic can be updated without a break
in service.

This design principle is more fully explained in documentation
for IBM Workflow
Server; see the instructions for isolating modules and targets
and for changing targets.