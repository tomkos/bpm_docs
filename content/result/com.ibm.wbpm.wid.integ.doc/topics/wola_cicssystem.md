<!-- image -->

# Transactions, security, and connection properties for a CICS
system

## CICS outbound calling

You can achieve access to CICS by using the WOLA proxy adapter connected to a remote WebSphere Application Server for z/OS with a CICS Link server configured. You can
make outbound calls to applications in CICS in either of the following ways:

- By using the WebSphere Application Server for z/OS-supplied link
server - You can start the WOLA CICS link server in the CICS region using a WebSphere Application Server for z/OS-supplied CICS control transaction (BBOC).
The link server accepts program LINK requests from WebSphere Application Server for z/OS through WOLA and calls the target CICS
program using the EXEC CICS LINK API. The link server invocation task can pass a set of parameters
to the CICS program in either a COMMAREA or a CHANNEL/CONTAINER. Then the link server invocation
task receives the response back and returns the response to the calling program in WebSphere Application Server for z/OS.
- Using the native WOLA APIs - You can use the native APIs Host Service or
Receive Request instead of the supplied WOLA link server. These APIs provide
enhanced control and performance.

## CICS security propagation

In WebSphere Application Server for z/OS, you might choose to use the
security credentials that are already set on the thread, which by default is the user ID that is
running the server, or you can set the credentials using a JAAS alias.

## CICS connection properties

When creating the WOLA import and service, you must define the connection properties for the
target CICS system.

In the New External Service wizard, on the Security and
Configuration Properties page, specify the JNDI name of the connection factory defined on
WebSphere Application Server for z/OS or specify the connection
properties for the CICS server that you want to connect to. If you choose to specify the connection
properties, then the managed connection factory is created during deployment with the specified
properties. In both the cases, a connection property that must be specified for CICS is the target
register name.

If the target program on the CICS system uses CICS containers and can be accessed using WOLA,
then in the Security and Configuration Properties page under the CICS
connection properties area, you must select CICS connection properties and
select Use CICS containers to use CICS containers to communicate with the
CICS link server. CICS programs that use containers can pass data that is larger than 32 KB.

To communicate with a COBOL, PL/I, C, or C++ program on a CICS system when using CICS containers,
you must set the following properties:

- Request container ID - Specifies the name of the container that is used to
pass the request message to a CICS program.
- Request container type - Specifies the CICS link request container type. If
you select CHAR, the WOLA CICS Link task copies the message into the request
container and converts it from code page UTF-8 to IBM-037
(EBCDIC).Note: If you set the Request container type property to
CHAR, then the Code page in the Select Data
Structures page must be set to UTF-8 while specifying the target program
for the WOLA import.
- Response container ID - Specifies the name of the container that receives
the response message from a CICS program.
- Response container type - Specifies the CICS link response container type.
If you select CHAR, the WOLA CICS Link task converts the response message to code
page UTF-8 before it returns message to the application server.

Link invocation task transaction ID - Specifies the CICS transaction ID that
is used to run the program link invocation task. The default transaction ID is
BBO#. If the default transaction ID is changed, the CICS system programmer must
ensure that the transaction ID is defined properly in the target CICS regions. The transaction ID
must be defined with the name of the WOLA CICS link invocation program, which is
BBOACLNK.

- For CICS programs, you must specify the name of the CICS program to invoke in the
InteractionSpec Service name property for the selected operation in the
New External Service wizard.
- If a specific user ID and password are required to run under CICS on the remote server, ensure
these additional properties are available on the optimized local adapters RAR connection factory so
the request can specify the user ID to use for an interaction. For more information, see Configuring optimized local adapters in development mode on the local
node.