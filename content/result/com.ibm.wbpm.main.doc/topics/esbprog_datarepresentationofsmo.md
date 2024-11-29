<!-- image -->

# Data representation of SMO

You can use the SMO with business object utilities such as BOCopy and BOXMLSerializer. In
addition if you need to examine the SMO, you can access and manipulate it using the BO API (SDO
API). This provides extensive capabilities including the ability to get and set individual fields.
The SMO also has its own Java™ interface which is a convenience
method for accessing the top level structure of the SMO.

Many mediation primitives have properties that contain XPath expressions. You can use this XPath
expression to specify which subset of the message for the mediation primitive, should be processed.
Depending on the mediation primitive, you can specify: /,
/body, /headers, /context,
/attachment, or your own XPath expression.
/ refers to the complete SMO, /body refers to the body
section of the SMO, /headers refers to the headers of the SMO. If you specify
your own XPath expression, the part of the SMO you specify is processed.

Integration Designer shows the structure of a message and allows you to select locations within the
message. In this way you can navigate the structure of a message and create XPath expressions.

Business objects provide a platform wide data representation. The structure of a business object
is defined in an XML schema which is either imported or created in Integration Designer using
the business object editor. Business objects are used to represent the data that is passed through
an SCA module.