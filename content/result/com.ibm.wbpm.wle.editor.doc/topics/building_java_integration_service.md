# Calling a Java method in an Integration service (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

Before
creating the Integration service, add the JAR file that contains the
classes that you need. After you add the JAR file as a server file,
you can select the class and method that you want to use for your
service. If the JAR files that you need are included in an IBM Business Automation Workflow toolkit,
you can add a dependency to that toolkit to access those files. See
"Creating a toolkit dependency in the Designer view" for instructions.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Create an integration service.
3. Drag a Java Integration step from the palette to the service
diagram and then use sequence lines to connect the step to the Start
and End Events.
4. Click the Java Integration step in the diagram and then
click the Definition option in the properties.
5. Click the Select button next to
the Java Class field to choose the JAR file and the class on the JAR
file that you want to call. The JAR files listed are
the ones added as managed server files as described in topic "Managing
external files". By default, the classes in the Business Automation Workflow Java
package are available in the integration.jar file,
which is included in the System Data toolkit. If your current project
has dependencies on other toolkits that include JAR files, those files
are also available.
6. From the Discovery section (under
the Properties and Definition tabs),
click the Method field. From the drop-down
list, choose the method that you want to call on the class that you
selected in the preceding step.
7. Enable the Translate JavaBeans check box if you want the
result of the Java method that is invoked to be serialized and returned
to the Integration service as an XML element. The content of the element
is based on the properties of the object's class.   For
example, if you choose the teamworks.Users class
from the integration.jar file (Business Automation Workflow Java
packages) and then select the getUser method with
the Translate JavaBeans check box enabled. The result looks like the
following example:
<userino type="com.lombardisoftware.core.UserInfo" description="UserInfo">
   <calendarId type="com.lombardisoftware.client.persistence.common.ID" description="calendarId" />
   <fullname type="java.lang.String" description="String">tw\_author</fullname>
   <qualifiedName type="java.lang.String" description="String">tw\_author</qualifiedName>
   <sendToAddress type="com.lombardisoftware.core.routing.Address" description="Address">
     <name type="java.lang.String" description="String">tw\_author</name>
     <toGroup type="java.lang.Boolean" description="Boolean">false</toGroup>
     <toUser type="java.lang.Boolean" description="Boolean">true</toUser>
   </sendToAddress>
   <userData type="java.util.HashMap" description="HashMap">
     <entry key="Full Name" description="Map Entry">
    	  <key type="java.lang.String" description="String">Full Name</key>
    	  <value type="java.lang.String" description="String">tw\_author</value>
     </entry>
   <userData>
   <userId type="com.lombardisoftware.client.persistence.common.ID$NumericID" description="ID$NumericID">
     <id type="java.math.BigDecimal" description="BigDecimal">2</id>
     <type type="com.lombardisoftware.client.persistence.common.POType$User" description="POType$User">
 	      <deleted type="java.lang.Boolean" description="Boolean">false</deleted>
 	      <exportable type="java.lang.Boolean" description="Boolean">false</exportable>
 	      <factoryName type="java.lang.String" description="String">com.lombardisoftware.client.persistence.UserFactory</factoryName>
 	      <id type="java.lang.Integer" description="Integer">2048</id>
 	      <libraryItem type="java.lang.Boolean" description="Boolean">false</libraryItem>
 	      <name type="java.lang.String" description="String">User</name>
 	      <tableName type="java.lang.String" description="String">LSW\_USR\_XREF</tableName>
     </type>
   </userId>
   <username type="java.lang.String" description="String">tw\_author</username>
</userinfo>Note: When you enable the Translate
JavaBeans check box, the variable type that you select
in the Integration service for the value returned from the Java method
should be XMLElement or ANY.
If you do not enable the Translate
JavaBeans check box, the Java method can only return objects
of the types shown in Table 1.
Table 1. Types
of objects returned by the Java method if Translate JavaBeans is not
enabled

Object types

java.lang.String
java.lang.Double
java.lang.ArrayList

java.lang.Long
java.lang.Float
java.lang.HashMap

java.lang.Integer
java.lang.Boolean
org.jdom.Document

java.lang.Short
java.lang.Character
org.jdom.Element

java.lang.Byte
java.lang.Calendar
com.lombardisoftware.core.XMLNodeList and com.lombardisoftware.core.TWObject
8. Click the Variables tab for the
Integration service to add any input variables that the service needs
to receive and any output variables that the service needs to make
available for subsequent steps in the service or BPD. Restriction: Arrays are not supported as input parameters.
9. Click the Java Integration step
in the service diagram and then click the Data Mapping option
in the properties to configure the input and output mappings for the
step.
10. Nest the Integration service in another service or select
it as the implementation for an activity, depending on the requirements
of the overall process.

## Related information

- Using the TWObjectFactory, TWObject and TWList classes