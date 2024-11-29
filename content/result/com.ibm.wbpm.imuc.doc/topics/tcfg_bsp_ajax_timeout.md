# Changing the timeout settings for the Business Space Ajax proxy

## About this task

If the REST service connections
are timing out, update the following settings.

If you are using
the Business Space environment that is shipped with your business
process management product, the socket-timeout value is set to 30
seconds by default. Change it to an appropriate value for your situation.

If
you are using Business Space with WebSphere Portal, the socket-timeout
value is set to 10 seconds by default. Change it to an appropriate
value for your situation (30 seconds, if you are using IBM® Business Automation
Workflow administration
widgets).

## Procedure

1. Open the proxy-config.xml file.
 For information about where to find the Ajax proxy file, see Configuring the Business Space Ajax proxy.
2. Change the proxy:value for socket-timeout.
The time is specified in milliseconds. <proxy:meta-data>
	<proxy:name>socket-timeout</proxy:name>
	<proxy:value>30000</proxy:value>
</proxy:meta-data>
3. Complete the Ajax proxy configuration to suit your environment.
For information, see Configuring the Business Space Ajax proxy.