# Enabling resumable services

## About this task

When an exposed heritage human service (deprecated) is invoked,
the service instance and associated data remains in the Process Portal user's session memory until one of the
following conditions occurs: the heritage human service ends, the Process Portal user logs out, or the session times out due
to inactivity.

If the Process Portal user
navigates away from a heritage human service Coach, the service instance
remains in the user's session.  Sessions are held in IBM® Business Automation Workflow server
memory, which might result in large memory allocations if many service
instances accumulate. Therefore, consider the various service types
and the service lifecycle when authoring and exposing a heritage human
service.

By default, services are not resumable.  A new service instance
is created each time the service is invoked.  If the service does
not flow to an end node, each instance remains in the Process Portal user's
session (until logout or session timeout), which can potentially utilize
a large amount of server memory per user. Therefore, services should
typically flow to an end node so that the service is removed from
the Process Portal user's
session immediately.

Startable services that are called from
the Process Portal Launch list
and administrative services that are called from the Process Admin
Console are not resumable.

Services can be called as resumable (called with zResumable=true).
When a service is resumable, a service instance is reused if a previously
created service instance is still available in the Process Portal user’s
session. The service state and any service variables set from the
prior instance invocation are still in session memory and are used.
 If the service does not flow to an end node, one instance remains
in the session and is available for reuse (until logout or session
timeout).  If the dashboard service flows to an end node, the service
instance is removed from the session, and the next time the service
is resumed, the Process Portal user
is prompted to restart the service. Resumable services are often authored
so that they do not end, which allows Process Portal users
to continue where they were when they logged out.

Dashboard
Services called from Process Portal can
be configured to be resumable (called with zResumable=true).

## Procedure

To enable resumable dashboards for a process application,
you must configure the com.ibm.bpm.social.zResumable property:

1. Open the administrative console and click Resources  > Resource Environment > Resource Environment Provider  > Mashups\_ConfigService > Custom properties.
2. Create a property named com.ibm.bpm.social.zResumable and
set its value to be a list of process application IDs, for example: TRD,RD,MAILCOM.
3. Save your changes
4. Restart the server.  Important: Do
not add the Process Portal (TWP) process application
to the com.ibm.bpm.social.zResumable list.  The dashboards
delivered in the Process Portal application
are not designed to be resumable.
5. Invoke resumable services by using the following URL: http://host\_name:port/contextRootPrefix/executeServiceByName?processApp=acronym&serviceName=MyService.
The default value for the contextRootPrefix is teamworks.
For more information about how to configure a custom context root,
see the section for the -update parameter in
the BPMConfig command-line utility topic.
6. In addition to the standard service URL parameters, you
can use the following resumable parameters: 
zResumable=true
This parameter causes the user's dashboard session to be resumed.
It is appended by default to all dashboard URLs. The resumable instances
are stored per user session, so different users have different instances.
When a user logs out, all resumable instances are cleared. The parameter
can be used with the optional zClientHandle={key} parameter.
If the process application for the dashboard is added to the com.ibm.bpm.social.zResumable list,
dashboard services called from Process Portal are
automatically called with zResumable=true.
zForceNew=true
If you use the URL to launch the dashboard as part of an application
that runs outside of Process Portal, you
can use this parameter to override the zResumable=true parameter
so that a new dashboard instance results. If you use this parameter,
you must ensure that services are terminated, for example, by modeling
an end event in the service, or by calling an API to complete or terminate
the service. 
[zClientHandle={key}]
If you use the URL to launch the dashboard as part of an application
that runs outside of Process Portal, you
can use this optional parameter with the zResumable=true parameter.
With these parameters, you can use a client-side key as a reference
to resume and reference multiple dashboard instances.

For information about HTTP session settings including session timeout intervals, see Session management settings in the IBM
WebSphere® Application Server documentation.