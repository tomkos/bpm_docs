<!-- image -->

# Creating a service for Cognos reports in Integration Designer

IBM
Cognos Analytics reports provide insight into the management
and performance of your enterprise. Using data from across an organization,
these reports can be useful in decision making situations. You can
view, import, and create services accessing these reports with the
editors in Integration Designer.

You must access a server with Cognos 8.4.1 or higher to use these functions. You can then have
your processes dynamically react to values in reports against those processes; for example, it could
offer a discount if the monthly sales report against your Sales process returns a value that is too
low.

- Setting up the preferences page for Cognos reports

The preferences page for Cognos reports specifies the default Cognos Universal Resource Identifier (URI) address and manages credentials saved from connecting to a Cognos server using the External service wizard.
- Viewing and importing a Cognos report as a web service

You can browse a Cognos report on a server, view it and import the report as a web service.
- Working with Cognos reports

Developing services that use Cognos reports requires you to use SOAP headers, be aware of security requirements and keep track of the state of the report being retrieved. Cognos reports use the SOAP header to pass state between invocations, such as security between logon and report retrieval, or the state when looping on report retrieval. Cognos reports support single sign-on and logging on providing security credentials. Examples of how to work with Cognos reports are provided below.