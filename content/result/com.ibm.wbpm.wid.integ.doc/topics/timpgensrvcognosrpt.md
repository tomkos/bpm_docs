<!-- image -->

# Viewing and importing a Cognos report as a web service

## About this task

To work with the Cognos reports on a Cognos server, follow
these steps:

## Procedure

1. Right-click a module you have created and select New
> External Service. In the New External Service window,
expand Web and click From Cognos
Reports. Click Next. The Select
a Cognos Report page opens.
2. The address in the Cognos gateway URI field
will be the one you entered on the Preferences page.
You can enter a different URI. Click Retrieve.
3 At this point, you are accessing a Cognos server and securityis required. However, how you interact with the security on the Cognosserver is determined by how the security for the server was configured.
    1. Single sign-on: A single sign-on configuration is a
way of letting users access one or more systems by logging on once.
Single sign-on security is only available if Cognos is running on
WebSphere Application Server. Single sign-on security is discussed
for both the JAX-WS and JAX-RPC web bindings in the Working with Cognos reports section.
    2. Credentials: In this case, you are prompted for these
security credentials: a namespace, a user ID and a password. Selecting Save
credentials stores the security credentials locally so
you do not need to enter them again when you access the server the
next time.
    3. No security: In this case, the server has been set up
to let you log on without any security credentials. You are not prompted
for any security.
4. A list of Cognos reports from the server appear in the
panel on the page. Select the report you want to work with. To see
a report, click Preview Report.
5 To import the report and create a service, click Next .The SCA Module or Library Name page opens. The Targetmodule or library field is filled with the module nameyou chose earlier. You can also browse for another module or libraryname or create a new one. The following options are available:

- Extract inline elements (interfaces and business objects) lets
you separate interfaces and business objects from the WSDL file you
are importing, which is useful in Integration Designer if you
need to reuse the business objects within your application.
- Generate Web service for Cognos authentication lets
you generate the business objects, interface and web service binding
for a Cognos authentication service.
6. Click Finish and the report is imported
into the module, where it can be used as a web service in your application.

## Related concepts

- Working with Cognos reports

## Related tasks

- Setting up the preferences page for Cognos reports