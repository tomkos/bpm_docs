# Passing and retrieving variables (deprecated)

## Passing simple variable types

You can pass
simple variables types to the web API. In general, the web API uses
the same simple types as the XML schema.

For example, if you
pass in an XSD simple string, the web API will use the same data type.
For more information, consult the web service documentation for the
toolkit that you are using.

## Passing complex variable types

You can pass
external complex variable types to the web API after converting them
to XML and wrapping them in a ComplexValue object.

You
can use tools to convert your data structures to and from XML. For
example, for Java classes, you can use a JAXB implementation, Apache
XMLBeans, or Castor. In Microsoft .NET, you can use the XML serialization
APIs provided in the platform libraries.

```
protected String toCustomerXml(String id, String firstName, String lastName)
{
  return "<customer xmlns=\"urn:testcases.webapi.common\">" +
  "<id>" + id + "</id>" +
  "<firstName>" + firstName + "</firstName>" +
  "<lastName>" + lastName + "</lastName>" +
  "</customer>";
}
```

## The ComplexValue object

The ComplexValue object
is part of the Business Automation Workflow web
API. You can use the ComplexValue object to wrap
complex type values to pass to and from web API operations. The ComplexValue object
can contain a single element from any namespace.

When passing
an external complex type value, ensure that there is a corresponding
complex type in Business Automation Workflow that
has its advanced XML properties configured to match the schema of
the complex type you would like to pass.

- Simple variable types (deprecated)

Business Automation Workflow simple variable types are automatically mapped to XML and vice versa.
- Editing advanced properties for complex variable types (deprecated)

To pass a variable to the web API, you have to serialize it to XML. You can customize the serialization of a variable to match the specifications of your external web service.