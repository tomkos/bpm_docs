# Invoking a Java service

## Before you begin

Before creating the external service, add the JAR file that contains the classes that you need,
as described in Adding managed files. For information about the scope of
uploaded JAR files, see Managing external files.

If the JAR files that you need are included in a toolkit, you can add a dependency to that
toolkit to access those files. See Managing toolkit dependencies.

## About this task

To use a Java service in the designer, you first discover the Java class and then generate an
external service from it. The external service contains operations with inputs and outputs based on
the methods in the discovered Java class. When you discover a service, if a corresponding external
service already exists in the designer, you can either overwrite the existing service or create a
new one.

Complete the following steps to discover a Java class and generate an external service.

1 Create an external service in one of the following ways:
    - Beside Services in the library navigation, click the plus sign (+).
Select External Service. In the New External Service 
page, choose Java, REST or Web service.
    - In the Service Flow editor, select a Service task.
In the Implementation tab for the service, click New.
In the New External Service  page, choose Discover an existing
service.
2. Select Java service from Server File as the method to discover a
service.
3. Beside Managed file, click Select and select the
file that you want.
4. Beside Java class, select the class that you want from the drop-down
list. Click Finish.
5 An external service is created with a Java binding. The operations and their inputs and outputsare based on the methods in the discovered Java class. In the Details section, the service name is shown. You can also add a documentation. The discovered namespace isshown. Selecting Binding shows the Java binding type.Click a parameter and select Binding to see the native type of theparameter.Note: Whether an operation can be successfully invoked from a service flow depends on thelinkage of the class, the method, the parameter types and result type of the method:

- The Java class must be 'public'.
- The method must be 'public'.
- Either the method must be 'static', or the Java class must have a public no-arguments
constructor.
- Each of the parameter types, as well as the result type (if not 'void'), must be one of:

Java type
Operation parameter type

byte, Byte
Integer

short, Short
Integer

int, Integer
Integer

long, Long
Decimal

float, Float
Decimal

double, Double
Decimal

boolean, Boolean
Boolean

char, Character
String

String
String

java.util.Calendar
Date

org.jdom.Element
XMLElement

org.jdom.Document
XMLDocument

java.util.Map
Map

## Results

After your external service is created, you can select it as an implementation of a service in a
service flow. Select the operation that
you want to use from the operation drop-down list and map the inputs and outputs in the
Data Mapping tab. See Creating a service flow.

If the operation has a parameter type that is Map, XMLElement,
or XMLDocument, use the JavaScript API to construct the argument or to decompose
the return value. For more information, see JavaScript API in processes and service flows.

- Invoking SQL Integration service flows

To integrate with an external database, you can use the SQL Integration service flows that are available in the System Data Toolkit by using the designer.