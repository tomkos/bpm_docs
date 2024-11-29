# Handling an IllegalDataException for invalid XML during serialization

## About this task

When you enter XML characters into a form,
coach, or a JavaScript API, the                     tw.system.serializer.toXml JavaScript
API takes the input as a                     TWObject,
parses it, and converts it into XML. If the                     TWObject contains
a string with invalid XML characters, such as                 control
characters 0x01 or 0x02, it raises
an                     IllegalDataException. To have IBM® Business Automation
Workflow automatically
correct                 the XML code, you can add a configuration
flag <autocorrect-xml>                 in the
appropriate 100Custom.xml file in your topology
that automatically removes invalid                 characters in a
string input and makes it XML-compliant.

## Procedure

1. Stop the server for IBM Workflow
Server or IBM Workflow
Center.
2. Locate each 100Custom.xml file in
your topology. For more information about the location
of the 100Custom.xml files that must be updated,
see the topic Location of 100Custom configuration files.
3. Add the following code to each 100Custom.xml file:
 <server>
    <autocorrect-xml merge="replace">true</autocorrect-xml>
</server>
4. Save your changes to each 100Custom.xml file.
5. Start the server for Workflow Server or Workflow Center.