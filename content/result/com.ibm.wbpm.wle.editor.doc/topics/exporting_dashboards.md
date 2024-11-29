# Generating portlets for heritage human services exposed as dashboards (deprecated)

## Before you begin

To perform
this task, you must be in the IBM Process
Designer desktop
editor, which is deprecated.

Make
sure that the heritage human service is exposed to the appropriate
group of process participants who work with the dashboard at run time,
and that the heritage human service is exposed as a dashboard. Make
sure that the heritage human service has at least one snapshot and
one coach.

The dashboard is available for the specified users
in Process Portal by
default. If you complete the following procedure, the dashboard also
is available for the specified users as a portlet deployed on a WebSphere Portal server.

- Work with the portal server administrator to understand how the
dashboard portlets are related to other portlets and services in the
portal server runtime environment.
- Make sure that the IBM WebSphere Portal server is
added to the trusted server list as described in Adding servers to the trusted server list.
- Typically, heritage human services that are exposed as dashboards
are not services that end. However, you are not prohibited from using
end events in the heritage human services that you expose as dashboards.
Remember that when a dashboard portlet is deployed, and it contains
an endpoint, the portlet ends, and it must be restarted. If your coach
is designed to end the service, the generated dashboard portlet includes
a Reload button for process participants to
start a new instance and refresh the dashboard.
- If a heritage human service contains two coaches with the same
name, make sure that all boundary events on the coaches have unique
control IDs. If the boundary event control IDs are not unique, process
participants who use the dashboard portlet might receive errors or
unexpected portlet interactions.
- You can generate portlets for dashboards that contain heritage
coaches, but you cannot map heritage coaches to boundary events for
dashboard portlets.
- If you use preprocessing and postprocessing for the heritage human
service, pay attention to where the processing occurs in relation
to the boundary event. Because portlets can be wired together and
wired to other services, you might need to move preprocessing and
postprocessing so that the boundary event triggers properly in the
dashboard portlet.
- If you are planning to update variables within a coach from an
inbound event, but you do not want trigger any of the boundary events
for the coach, add a new boundary event that loops back to the same
coach that is specified as part of an inbound event. Make sure to
select the new boundary event when you define the inbound event for
the generated dashboard portlet.
- If you are planning to designate a payload variable for inbound
or outbound events for the dashboard, make sure that the payload variable
is included on each coach that is part of the heritage human service.
The payload variable must be included on each coach that is part of
the heritage human service that is exposed as a dashboard and deployed
as a portlet. However, a coach can include a variable without displaying
it to process participants if you add a field for the variable to
the coach and set the visibility of the field as None (hide
or disable).
- For globalization support for the name and description of the
generated portlets, make sure to prepare an XML file that you designate
when you create the portlet from the dashboard. The XML must be ready
before you start the Export Dashboard wizard.
Ensure that the XML uses the same format as the following example:<?xml version='1.0' encoding='UTF-8' ?>
<portlet>
	<description xml:lang="en">English description</description>
	<description xml:lang="fr">French description</description>
	<description xml:lang="es">Spanish description</description>
	<display-name xml:lang="en">English display name</display-name>
	<display-name xml:lang="fr">French display name</display-name>
	<display-name xml:lang="es">Spanish display name</display-name>
</portlet>Ensure that the XML file has encoding
defined as UTF-8. The XML file can contain zero or more description or display-name elements.
The description and display-name elements
cannot have empty string values. The xml:lang attribute
must follow the RFC 1766 specification, which is available at http://www.ietf.org/rfc/rfc1766.txt.
- (Deprecated.) The collaboration feature is not available for dashboards
exposed as portlets. That is, users cannot interact in an activity
with other users or experts like they can in Heritage Process Portal (deprecated).
- (Deprecated.) Using the same security protocol for both the Business Automation Workflow server
and the IBM WebSphere Portal server prevents an issue
where the collaboration feature is not available for dashboards exposed
as portlets. That is, users cannot interact in an activity with other
users or experts like they can in Process Portal. users
see a blank task completion view in an IBM WebSphere Portal portlet.
For example, use HTTPS for both the Business Automation Workflow server
and the portlet running on the  IBM WebSphere Portal server, or
use HTTP for both the Business Automation Workflow server
and the portlet running on the  IBM WebSphere Portal server. When
you configure the portlet on the IBM WebSphere Portal server and
specify the Business Automation Workflow URL,
specify the same security protocol that is used by the Business Automation Workflow server.

## About this task

Use the Export Dashboard wizard in Process Designer to
define portlet parameters and map events when exporting the dashboard.
After you generate a portlet for the dashboard, your portal server
administrator can deploy the portlet to IBM WebSphere Portal so that the
process participants interact with the dashboard in the runtime environment.

## Procedure

1. For heritage human services that are exposed as dashboards for a group of process participants,
click Create a Portlet from the Dashboard on the overview page in the desktop
Process Designer to open the Export Dashboard wizard.
2 When setting the parameters for the portlet, consider howthe portal server administrator and the process participants use thedeployed portlet:
    - Enter a name and a description that describe what the portlet
does.
    - If you created an XML file for globalization of the name and description
of the portlet, select Globalization and
browse to the file.
    - Select the snapshot that represents the version of the dashboard
that you want to be generated as a portlet for process participants
to use at run time. If you select an older snapshot, changes after
the snapshot was taken are not represented in the generated portlet.
3 Optional: Define inbound events for the dashboardportlet. At run time, other portlets interact with thedashboard portlet by sending events to it. When the dashboard portletreceives an event from another portlet, it fires a boundary event,moving the dashboard to another coach.

At run time, other portlets interact with the
dashboard portlet by sending events to it. When the dashboard portlet
receives an event from another portlet, it fires a boundary event,
moving the dashboard to another coach.

- For each inbound event that you want this dashboard portlet to
respond to, change the event name field to something meaningful to
your dashboard. The namespace default value makes the event unique
and prevents unintended interactions between portlets.
- Specify a payload variable if you expect the inbound event to
contain data that you want to use to update the dashboard data. If
the coach uses a payload variable, select the payload variable that
the dashboard portlet receives from other portlets at run time. You
can choose from variables that are part of the heritage human service.
As previously mentioned, ensure that the payload variable is included
on each coach that is part of the heritage human service.
- Select a coach and a boundary event that represents the user interface
element that you want the dashboard portlet to interact with when
it receives the event. The boundary event in a heritage human service
diagram is labeled as End State Binding. If
you selected a payload variable, make sure to select a coach that
has the same variable.
- Define multiple interface elements by clicking the plus sign and
designating another coach and boundary event.
- When the dashboard portlet receives the event, it interacts with
only the interface element on the currently displayed coach.
4 Optional: Define outbound events for the dashboardportlet. At run time, the dashboard portlet sends eventsto other portlets.

At run time, the dashboard portlet sends events
to other portlets.

- Select a boundary event to designate user interface elements that
cause the dashboard portlet to send the event.
- If you specify a payload variable, the dashboard portlet includes
data in the sent event for other portlets to use. As previously mentioned,
ensure that the payload variable is included on each coach that is
part of the heritage human service.
5 After you finish exporting the dashboard as a portlet,install the .war file on your Business Automation Workflow serverand tell the portal server administrator to point to the endpointfor the Web Services for Remote Portlets (WSRP) 2.0 protocol and importthe .war file. The Business Automation Workflow server comes with a WSRP 2.0 provideralready installed, which allows consumption of portlets generated from WebSphere Portal. The URL for accessing the WSPR 2.0 provider web serviceon an installed Business Automation Workflow server is:http://{BPM\_host\_name }:{BPM\_port }/producer/wsdl/wsrp\_service.wsdl . If you are not using WSRP, give the .war fileto the portal server administrator to deploy. Discuss the followingpoints with the portal server administrator:

The Business Automation Workflow server comes with a WSRP 2.0 provider
already installed, which allows consumption of portlets generated from WebSphere Portal. The URL for accessing the WSPR 2.0 provider web service
on an installed Business Automation Workflow server is:
http://{BPM\_host\_name}:{BPM\_port}/producer/wsdl/wsrp\_service.wsdl.

If you are not using WSRP, give the .war file
to the portal server administrator to deploy.

- The administrator should install dashboard portlets on the same
cluster as Process Portal.
- Notify the administrator that the IBMBPM keyword
is added to the generated dashboard portlet. The keyword makes it
easier for administrators to find and manage the dashboard portlets.
- Make sure that the administrator knows that portlet preferences
can be edited in WebSphere Portal
using the edit page for the portlet. The administrator can edit the
following information for the dashboard portlet that is generated:
host name, port number, width, and height.
- Give the administrator information about the following Business Automation Workflow portlet preferences that can be edited in thedashboard portlet. All other Business Automation Workflow portletpreferences should not be changed. Tip: The WSRP Producer for WebSphere ApplicationServer is a stateless producer and does not manage anyportlet preferences on the server. If you are using the WSRP Producer, you must update theportlet.xml file that is contained in the exported .war file with any portlet preference changes before the administrator installs the.war file.
    - bpmHost (default: localhost) - The host name or IP address for the
server
    - bpmPort (default: 9080) - The port number for the server
    - bpmUseSSL (default: false) - The indication that https should be used
instead of http
    - bpmWidth - The width (in pixels) to be used for the portlet iframe that
displays the dashboard
    - bpmHeight (default: 400) - The height (in pixels) to be used for the
portlet iframe that displays the dashboard
    - bpmUseDojo (default: true) - A boolean value to indicate if Dojo should be
used when available for client-side events. If the value is true, the portlet tests if Dojo is
loaded and uses the Dojo publish-subscribe methods to send and receive events. If the value is
false, the portlet uses server side-events as specified in JSR286.
- Tell the administrator the following requirements for using single-sign-on(SSO) and Secure Sockets Layer (SSL) protocol in WebSphere Portal with the dashboard portletsfrom Business Automation Workflow .

- To prevent the Process Portal login panel from
appearing in the dashboard portlet, administrators should enable and configure single-sign-on for
the WebSphere Portal and Business Automation Workflow servers. See Single sign-on for authentication in the IBM
Documentation for WebSphere Application
Server.
- To avoid browser messages about secure connects for process participants who connect to WebSphere Portal and use the dashboard portlets,
administrators should replace personal, self-signed certificates with those provided by a trusted
external certificate authority (CA). See Creating a certificate authority request in the IBM
Documentation for WebSphere Application
Server.
- If using personal certificates for testing or in a pre-production
environment, the administrator can import the certificates from each
system into the browser before testing.
- In a production environment, administrators should avoid using
self-signed certificates.
- If using HTTPS to connect to WebSphere Portal,
the administrator should also use HTTPS in the dashboard portlets.
If a part of a page is loaded using HTTPS, and other parts are loaded
using HTTP, process participants who connect to WebSphere Portal and use the dashboard
portlets might receive a warning that some content on the page is
not secure.
- The portal server administrator should determine whether to use
client-side events or server-side events. Both client-side events
and server-side events use the boundary events that are modeled as
part of the heritage human service definition. The difference between
client-side events and server-side events is the channel for communication.When
using client-side events, the portlets created with Process Designer
use the Dojo Toolkit to send messages between portlets that are on
the same page in the portal server. Using client-side events is faster,
because it does not require events to be sent to the server for processing
and does not require page reloads when an event is sent or received.
If client-side events are used, the Dojo Toolkit must be loaded as
part of the theme for the portal page, and the generated dashboard
portlets send events using only the Dojo Toolkit. The generated dashboard
portlets receive server-side events from other portlets on the page
that are not using client-side events.
Server-side events do
not require the Dojo Toolkit to be loaded and are the standard event
mechanism defined in the JSR286 specification. Server-side events
take longer to process because the events must be sent to the server
for processing and the page must be reloaded to display the results.
Server-side events can be used across portal server pages with the
correct portal configuration and wiring.
- If the administrator decides to use client-side events, the Dojo Toolkit must be loaded as part
of the theme for the portal page.