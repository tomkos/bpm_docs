# MQ Header Setter mediation primitive properties

## MQ Header Elements headerElements

A table of actions that you want to perform
on MQ header elements, in the SMO. You can add to this table by clicking Add
(follow any instructions to add a dependency, from the module to the MQ schemas). Then follow the
instructions of the wizard.

| Field detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Value and notes   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Mode mode  In IBM Integration Designer, the available values for this property are shown within a field titled Header Action. Use this property to specify the action that you want to perform on MQ headers. If you want to create a new MQ header, set the property to Create. This is the default action. If you want to search for MQ headers and then either set the values in any headers that are found or create a new header if no headers are found, set the property to Find and Set. If you want to search for MQ headers and then copy the first header that is found to another location in the SMO, set the property to Find and Copy. If you want to search for MQ headers and then delete any headers that are found, set the property to Find and Delete.    Values values In IBM Integration Designer, you can specify a value for this property by using the Set Values table. If the Mode property (or Header Action) is set to Create or Find and Set, you can set the Values property.The Values property is a list of MQ header field names and their values. When a new MQ header is created, or MQ headers are found, the new values are set in the specified fields. Each value can be either a literal value or an XPath expression that is resolved at run time to provide the value. The value provided must be compatible with the field where it is to be set. For example, if the field is of type int, the value could validly be 14, but not GoldAccount. The MQRFH2 header is structurally complex; therefore, you might need to refine the schema. You can do this by adding elements to the MQRFH2Group[] element.  Target Destination targetDestination If the Mode property (or Header Action) is set to Find and Copy, the Values property should be an XPath 1.0 expression that identifies the target destination. The first MQ header to be found is copied to the target destination. MQ Header Type type The type of MQ header to create or search for. If the Mode property (or Header Action) is Create or Find and Delete, the Header Type can be any of the following types: MQRFH2, MQCIH (MQ-CICS bridge) or MQIIH (MQ-IMS bridge). If the Mode property (or Header Action) is Find and Set or Find and Copy, the Header Type can be any of the following types: MQRFH2, MQCIH (MQ-CICS bridge), MQIIH (MQ-IMS bridge) or MQMD. The default is MQRFH2. Note: You cannot create or delete the MQMD header.  Value Reconstruction values.reconstruction This property is used in IBM Integration Designer to store data that controls the display characteristics of the primitive; it has no effect on the runtime environment. |                   |

## Validate input validateInput

If true, causes the input message to be
validated before the mediation is performed.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | false             |

## Considerations

- If the Header Action is Find and Set and
a header cannot be found, a new header is created.
- If you attempt to set a header field to a value of incompatible
type, a runtime exception occurs.
- If the Target Destination resolves to more than
one element in the SMO, a runtime exception occurs.
- If the Validate input property is true and
the input message is invalid, a runtime exception occurs.

## Sample XML code

```
<node name="MQHeaderSetter1" type="MQHeaderSetter">
   <table name="headerElements">
    <row>
      <property name="mode" value="Create"/>
      <property name="values" value="MQRFH2\_TYPE/@xsi:type=&quot;MQRFH2\_TYPE&quot; 
      MQRFH2\_TYPE/Flags=&quot;1&quot; MQRFH2\_TYPE/NameValueCCSID=&quot;2&quot;"/>
      <property name="targetDestination" value=""/>
      <property name="type" value="MQRFH2"/>
      <property name="values.reconstruction" value="<?xml version=&quot;
      1.0&quot; encoding=&quot;UTF-8&quot;?>&#xD;&#xA;<com.ibm.ccl.soa.test.common.
      models.parm:ParameterList xmi:version=&quot;2.0&quot; xmlns:xmi=&quot;
      http://www.omg.org/XMI&quot; xmlns:xsi=&quot;
      http://www.w3.org/2001/XMLSchema-instance&quot; xmlns:com.ibm.ccl.soa.
      test.common.models.parm=&quot;http:///com/ibm/ccl/soa/test/common/models/parm.
      ecore&quot; xmlns:com.ibm.ccl.soa.test.common.models.value=&quot;
      http:///com/ibm/ccl/soa/test/common/models/value.ecore&quot; 
      id=&quot;1290898834640\_2&quot;>&#xD;&#xA;  <parameters xsi:type=&quot;
      com.ibm.ccl.soa.test.common.models.value:ValueStructure&quot; 
      name=&quot;MQRFH2\_TYPE&quot; id=&quot;1290898835281\_3&quot; value=&quot;&quot; 
      defaultValue=&quot;&quot; typeURI=&quot;xsd:/#MQRFH2\_TYPE&quot; 
      baseTypeURI=&quot;xsd:/#MQRFH2\_TYPE&quot; hasChildren=&quot;
      true&quot;>&#xD;&#xA;    <context>&#xD;&#xA;      
      <properties name=&quot;project\_context&quot; value=&quot;
      TestMod&quot;/>&#xD;&#xA;    </context>&#xD;&#xA;    
      <elements xsi:type=&quot;com.ibm.ccl.soa.test.common.models.value:ValueField&quot; 
      name=&quot;Flags&quot; id=&quot;1290898835312\_4&quot; 
      value=&quot;&amp;quot;1&amp;quot;&quot; defaultValue=&quot;
      0&quot; typeURI=&quot;xsd:/http://www.w3.org/2001/XMLSchema#int&quot; 
      baseTypeURI=&quot;xsd:/http://www.w3.org/2001/XMLSchema#int&quot; 
      required=&quot;true&quot;/>&#xD;&#xA;    
      <elements xsi:type=&quot;com.ibm.ccl.soa.test.common.models.
      value:ValueField&quot; name=&quot;NameValueCCSID&quot; id=&quot;
      1290898835640\_8&quot; value=&quot;&amp;quot;2&amp;quot;&quot; defaultValue=&quot;
      0&quot; typeURI=&quot;xsd:/http://www.w3.org/2001/XMLSchema#int&quot; 
      baseTypeURI=&quot;xsd:/http://www.w3.org/2001/XMLSchema#int&quot; 
      required=&quot;true&quot;/>&#xD;&#xA;    
      <elements xsi:type=&quot;com.ibm.ccl.soa.test.common.models.
      value:ValueArray&quot; name=&quot;folder&quot; id=&quot;1290898835656\_11&quot; 
      writeable=&quot;false&quot; value=&quot;&quot; defaultValue=&quot;&quot; 
      typeURI=&quot;xsd:/#MQRFH2Group[]&quot; baseTypeURI=&quot;xsd:/
      #MQRFH2Group[]&quot; elementTypeURI=&quot;xsd:/#MQRFH2Group&quot; 
      elementBaseTypeURI=&quot;xsd:/#MQRFH2Group&quot;/>&#xD;&#xA;  
      </parameters>&#xD;&#xA;</com.ibm.ccl.soa.test.common.
      models.parm:ParameterList>&#xD;&#xA;"/>
    </row>
  </table>
  <inputTerminal/>
  <outputTerminal>
    <wire targetNode="XSLTransformation1"/>
  </outputTerminal>
  <failTerminal/>
</node>
```