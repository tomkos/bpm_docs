<!-- image -->

# Creating custom XPath extension functions

- Creating an XPath function JAR file

Define your custom XPath extension functions by creating an XPath function Java™ archive (JAR) file that contains a Java service provider plug-in.
- Registering an XPath function JAR file with IBM Integration Designer

For IBM® Integration Designer to find your XPath extension function JAR file at run time, you must register the paths of your XPath extension function files with Integration Designer.
- Exposing an XPath function JAR file to the runtime environment

For the process servers in your configuration to find the Java service provider plug-in at run time, you must expose the class path of the plug-in in the XPath function Java archive (JAR) file. You expose the JAR file by setting a custom property for Business Flow Manager in the administrative console.