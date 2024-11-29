<!-- image -->

# WS-Security specification

A web service is a self-contained, self-describing modular application
that can be published, discovered, and invoked over a network using
standard network protocols. Typically, XML is used to tag the data,
SOAP is used to transfer the data, WSDL is used for describing the
services available, and UDDI is used for listing the services that
are available.

The WS-Security specification is one of several security standards
that can be used to secure a web service. It provides message-level
security, which means it is independent of the transport protocol
and can be used for any web service binding, such as HTTP, SOAP, and
RMI. It also provides a general-purpose mechanism for associating
security tokens with message content.

## Security mechanisms

The WS-Security specification
provides the following three mechanisms for securing web services
at the message level:

| Web resource                                                                                                         | Location                                                 |
|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| OASIS WS-Security specification                                                                                      | http://www.oasis-open.org/specs/index.php#wssv1.0        |
| Chapters 9 and 21 in the IBM redbook SG246461 WebSphere Version 6 Web Services Handbook - Development and Deployment | http://www.redbooks.ibm.com/abstracts/sg246461.html?Open |

Although the redbook that is mentioned in the table
shows how the web services and EJB deployment descriptor editors of Rational® Application
Developer are
used to edit the WS-Security properties, there is a direct mapping
between these editors and the IBM Integration
Designer module deployment editor.

## Authentication

In authentication, a security
token is inserted in the request message of an import. Depending on
the type of security token that is being used, the security token
can also be inserted in the response message of an export.

Several
types of security tokens are used in authentication, including:

- Username tokens
- Binary tokens, such as X.509 tokens and Lightweight Third Party
Authentication (LTPA) tokens.
- Custom tokens, such as XML tokens and custom binary tokens.

Username tokens are used to simply validate user names and
passwords. They are the sole means of security in basic authentication
(and for this reason, basic authentication should only be used in
secure networks like HTTPS sites or corporate intranets). When a username
token is received by a web service server, the user name and password
are extracted and passed to a people directory for verification. If
the user name and password combination is valid, the result is returned
to the server and the message is accepted and processed. When used
in basic authentication, username tokens are typically only passed
in the request message of an import and they are not passed in the
response message of an export.

In this release of IBM Integration
Designer, username tokens (as used in basic authentication) are the only
form of security token that is thoroughly documented. If you want
detailed information on other types of security tokens, such as binary
tokens or custom tokens, you should consult the web resources listed
in the table.

## Message security architecture

<!-- image -->

These components are described individually
in the following table.

|     | Component          |  Description                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1  | Request generator  | On the client (import) side, the request generator defines the security constraints on the outgoing SOAP request message with one or more security mechanisms, such as digital signing, encryption, or security tokens.                                                                                                                                                                                                                                            |
|   2 | Request consumer   | On the server (export) side, the request consumer defines the security constraints on the incoming SOAP request message, such as ensuring that: The required integrity parts are signed and the signature is verified. The required confidential parts are encrypted and subsequently decrypted. The security tokens are validated.  The WS-Security properties defined for the request consumer must match those that were defined for the request generator.     |
|   3 | Response generator | On the server (export) side, the response generator defines the security constraints on the outgoing SOAP response message with one or more security mechanisms, such as digital signing, encryption, or security tokens.                                                                                                                                                                                                                                          |
|  4  | Response consumer  | On the client (import) side, the response consumer defines the security constraints on the incoming SOAP response message, such as ensuring that: The required integrity parts are signed and the signature is verified. The required confidential parts are encrypted and subsequently decrypted. The security tokens are validated.  The WS-Security properties defined for the response consumer must match those that were defined for the response generator. |

## Advantages of WS-Security

There are numerous
advantages to using WS-Security, such as:

- Different parts of a message can be secured in a variety of ways.
For example, you can use integrity on the security token (user ID
and password) and confidentiality on the SOAP message body.
- Intermediaries can be used and end-to-end message-level security
can be provided through any number of intermediaries.
- WS-Security works across multiple transports and is independent
of the underlying transport protocol.
- Authentication of both individual users and multiple party identities
is possible.