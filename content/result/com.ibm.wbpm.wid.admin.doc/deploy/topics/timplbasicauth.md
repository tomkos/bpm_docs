<!-- image -->

# Implementing authentication

## About this task

- A library named Library that contains the WSDL files that
are shared by the modules.
- A module named ClientModule that contains a web service
import named sendWebServiceCallToServer, as shown in the following
figure:
- A module named ServerModule that contains a web service
export named receiveWebServiceCallFromClient, as shown in the
following figure:

As the import and export names imply, the import sendWebServiceCallToServer sends
a request message to the export receiveWebServiceCallFromClient at
run time.

In basic authentication, username tokens are inserted
in the request message of the import. There are typically no corresponding
username tokens in the response message from the export.

The
following topics describe how to implement basic authentication using
a username token.

- Creating a security token for the request message

The first step in implementing basic authentication is to create a security token for the request message to be sent by the import. The security token is sent to the server inside the header of the SOAP message.
- Creating a token generator for the request message

The second step in implementing basic authentication is to create a token generator for the request message to be sent by the import. The token generator reads the user name and password from the configuration file and generates the username token with the user name and password.
- Creating a required security token for the request message

The third step in implementing basic authentication is to create a required security token for the request message to be received by the export.
- Creating a caller part for the request message

The fourth step in implementing basic authentication is to create a caller part for the request message to be received by the export.
- Creating a token consumer for the request message

The fifth and final step in implementing basic authentication is to create a token consumer for the request message to be received by the export. The token consumer receives the security token in the request message and validates it.
- Testing authentication using the integration test client

If you want to test your authentication implementation, you can use the integration test client. The integration test client enables you to test your modules and components and report the results of your tests.