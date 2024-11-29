# Security for web service integration

- Add a web service server
- Creating an inbound web service

In the context of web service integration with BPDs, security can
be required at design time and at run time.

## Design time authentication

## Run time authentication

If you are manually
creating your own security, authentication options for SOAP calls
at run time are available in the security properties for the Web Service
Integration step. The following table describes the information that
you must provide for each supported option:

| Option                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HTTP basic authentication                  | Requires a user name and password. Business Automation Workflow never stores the password in plain text in its database or export files, and no plain text passwords are required in Business Automation Workflow configuration files. Attention: The user name and password are sent as base64-encoded text strings in the HTTP basic authentication header. To prevent eavesdropping, use only SSL secured connections by ensuring that the URL starts with https://.                                                                                                                                                                                                                                                                                                                                          |
| Traditional: Username token authentication | When using username token authentication in Business Automation Workflow, a user name and password are passed to a web service in the SOAP header of the SOAP request. Username token authentication allows for different algorithms and formats for passing the password.       Business Automation Workflow supports passwords in plain text and digest format. The specification for username token authentication describes two optional elements that can be supplied:  wsse:Nonce wsu:Created   The Business Automation Workflow implementation of this standard always provides wsse:Nonce and wsu:Created. This is compatible with the behavior of Microsoft WSE 2.0 Toolkit when using username token digest authentication. For more information, see Web Services Security UsernameToken Profile 1.0. |