<!-- image -->

# Emulating an Advanced Integration service

Emulation is automatically turned on for Advanced Integration services
that are not yet implemented. To emulate an Advanced Integration service
that has been implemented, you must explicitly turn on emulation.
To emulate an implemented Advanced Integration service, follow these
steps:

1. Open the Advanced Integration service in Process Designer and
select the Emulate Service check box.
2. When you playback the business process, an emulation coach will
be displayed when the service is encountered.
3. Enter the outputs of the service in the coach and click OK.

When emulation is turned on for an Advanced Integration service,
the service will always be emulated during playback in the Process
Center. If the service is deployed to the Process Center, you will
see the emulation coach if the service and implementation are not
synchronized.

The emulation coach is also launched if deployment of your process
application to the Process Center is in progress. In that case, you
will see a Postpone button in the emulate coach.
You can then select postpone if you do not want to emulate the service,
but want to wait until the actual service has been executed so that
you can rerun the Advanced Integration service. Postpone is only available
if the service would have been executed if it was deployed to the
Process Center.

If you use complex output parameters, the generated form may exceed
the maximum length of characters allowed. The generated HTML code
needed to emulate the Advanced Integration Service may not be created.
If you experience this problem, simplify your existing Advanced Integration
Service or disable the emulation. Alternatively, if you have not implemented
your service, implement it as emulation will automatically be invoked
each time the service is used with no implementation.

If you are emulating a bottom-up service that is backed by a Web
Services Description Language (WSDL) binding with inline types, it
causes the Advanced Integration service to be out-of-sync, and you
must synchronize the IBM Integration Designer implementation again.
Avoid emulating bottom-up services for WSDL bindings with inline types.