<!-- image -->

# Referenced and swaRef-type attachments

The following types of attachments are discussed in this
section:

- Referenced attachments
- swaRef-type attachments

## Referenced attachments

Referenced
attachments allow you to model an attachment in a WSDL file. For example,
you might want to send a resume of an employee to a web service from
an application created in IBM® Integration
Designer.
In that resume, you might want to include an attachment for a picture
of the employee.

To support SOAP messages with referenced attachments
for exports, the interface operations must use the document literal
non-wrapped binding style or the RPC literal binding style (see Binding style) and the input
or output in the operation containing the reference must be binary.
Furthermore, the WSDL binding must contain a MIME transport binding.
A MIME transport binding is handled for you when you use the editors
in IBM Integration
Designer.
Since referenced attachments involve multi-part messages, you should
read Using document binding style with multipart messages for an understanding of how the Web Services Interoperability
(WS-I) standard and binding style are related.

Referenced
attachments can be modeled by using the interface editor. The following
steps show you how to model the attachment.

These steps assume
that you have a module with an interface that contains one or more
input operations. The instructions also assume that you have an export
and the interface has been added to it.

1. Open your interface in the interface editor.
2. In the interface editor, select the operation or that will contain
a referenced attachment. If the binding style is not Document/literal
non-wrapped, click Change binding style to
document/literal non-wrapped and change the binding style.
3. In the Type column, select a binary type,
for example, hexBinary, for those inputs and
outputs that will be passing an attachment.
4. Click the Properties tab and select an
input or output with the binary type.
5. Beside the Binary content type box, click Add.
The Select Binary Content window opens.
6. In the Binary content type field, select
the type category, for example, image/jpg,
or type it in the field.
7. Click OK.
8. In the assembly editor, right-click your export and select Generate
Binding > Web Service Binding. The Transport
Protocol Selection wizard opens.
9 Depending on the SOAP release that you want to use, select oneof the following: Both of these options support the Java API for XML WebServices (JAX-WS).
    - SOAP1.2/HTTP
    - SOAP1.1/HTTP

Both of these options support the Java API for XML Web
Services (JAX-WS).

10. Click Finish. If you have selected at least
one binary type to use as an attachment, the new WSDL binding file
will be generated with a MIME transport binding.
11. Deploy your application and run it.

## swaRef-type attachments

Using
the Web Services Interoperability Organization (WS-I) Attachments
Profile, you can pass a SOAP with attachment  (swaRef) type attachment.

To
pass an attachment as a swaRef type using the WS-I Attachments Profile,
follow these steps:

1. Add the WS-I attachment profile to your module. Open Dependencies in
the Business Integration view and in the Predefined
Resources section select WS-I attachment profile
1.0 swaRef schema file. Save your work.
2. To add an attachment in a business object, create a business object
and for the type select swaRef, which will
be available since you added the schema previously.
3. To add an attachment as a type for an input or output to an operation,
create the operation in the interface. Add an input or output to the
operation. If using the business object created previously then select
the business object as the type to your input or output. If you are
not using the business object created earlier, add another input or
output and select swaRef as the type.
4. Generate the binding, deploy the your application and run it.