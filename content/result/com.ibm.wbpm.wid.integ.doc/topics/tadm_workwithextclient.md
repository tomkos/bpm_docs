# Working with external clients

## About this task

Consider a very simple scenario in which an external client
wants to interact with an application on the
server. The figure depicts a typical simple scenario.

Figure 1. Simple use-case scenario: external client
interacts with server application

<!-- image -->

The SCA application includes an export with a JMS
binding; this makes the application available to external clients.

When you have an external client in a Java™ virtual machine (JVM) separate from your server, there are several
steps you must take in order to make a connection and interact with
a JMS export. The client obtains an InitialContext with the correct
values and then looks up the resources through JNDI. The client then
uses the JMS 1.1 specification client to access the destinations
and the send and receive messages on the destinations.

The default
JNDI names of the resources created automatically by the runtime are
listed in the configuration topic of this section. However, if you
have pre-created resources, use those JNDI names.

## Procedure

1. Configure JMS destinations and the connection factory to
send the message.
2. Make sure that the JNDI context, the port for the SIB resource
adapter, and the messaging bootstrapping port are correct. The server uses some default ports, but if there are more servers
installed on that system, alternate ports
are created at installation time to avoid conflicts with other server
instances. You can use the administrative console to determine which
ports your server is employing . Go to Servers > Application Servers > your\_server\_
name > Configuration and click Ports under Communication. You can then edit the port being used.
3. The client obtains an initial context with the correct
values and then looks up the resources through JNDI.
4. Using JMS 1.1 specifications, the client accesses the destinations
and the send and receive messages on the destinations.