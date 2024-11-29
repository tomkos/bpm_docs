<!-- image -->

# Understanding the SCA architecture to Java relationship

When you work in an SCA environment, you
create artifacts that make sense within the context of SCA. Understanding
several key SCA artifacts is the beginning of understanding the relationship
between the SCA architecture and the Java environment. A business
object is one of these important artifacts. A business object represents
in the SCA environment a message that is sent from a Java client.
A business object is in an XML format and it is similar in Java terms
to a data structure. An interface is another key artifact. An interface is
the means of getting input and output into the message sent between
the environments. Operations in an interface are similar to
methods in Java in that they perform actions. A createEmployeeRecord
operation could create an employee record if none existed and use
an employee business object as the means of adding information about
the new employee.

How is data transferred from a Java client
to an SCA artifact like a business object? An SCA application is found
within a module. Imports and exports are the means of sending and
receiving data from applications outside the module. Imports identify
services outside of a module such as a Java application that can be
called from within the module. Exports allow the SCA module
to listen for requests from external services such as Java clients. Bindings specify
the means of transforming the data between the environments. Many
bindings are available in IBM® Integration
Designer such
as JMS, MQ, HTTP bindings and bindings for EIS systems like SAP.

Mapping a message to an SCA interface will help you understand these key SCA artifacts and how they are
related to familiar Java constructs.

Creating
an import involves using a visual tool in IBM Integration
Designer to
create one. Once created, an import sends a request from the SCA application
to another application outside. There are many bindings available
for the import with the product. Creating a JMS import to communicate with a JMS client shows how to create an import with, in this case,
a JMS binding that sends requests to a Java client. It also provides
details on setting the binding properties necessary to work with the
application being called including using a JNDI lookup name.

Creating
an export is a similar process to creating an import. The export listens
for requests from another application. Like an import, many bindings
are available. Creating a JMS export to communicate with a JMS client shows how to create a JMS export to receive requests
from a Java client. You are shown how to select the right data transform,
often called serializing and deserializing, as the data is moved in
and out of an XML format. You are also shown the role of a function
selector, which determines what operation on the SCA application
to call when the SCA application is called.

Finally, let's
examine the flip side: setting up a Java client that can work with
the SCA imports and exports you have created. Suppose you created
an SCA interface for an SCA component and created a business object
to pass data to the SCA component with this interface. If your Java
client was using a TextMessage as the type for use in the message
it will pass from the Java client to the SCA application, then you
would choose a data format transformation like Serialized Java Object
(JMS) when you created the binding. These data transformations are
selectable from a list when you create your binding. Creating a JMS client to receive messages from a JMS import shows you the Java code you would need to
write on the client side. In this case, it is a Message Driven Bean
(MDB) that is listening for a request coming from the SCA import.