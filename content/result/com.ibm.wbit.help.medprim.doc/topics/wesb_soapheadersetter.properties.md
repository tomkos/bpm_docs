# SOAP Header Setter mediation primitive properties

## SOAP Header Elements headerElements

A table of actions that you want to
perform on SOAP header elements, in the SMO. You can add to this table by clicking
Add. Then follow the instructions of the wizard.

- If you want to create a new SOAP header, set the property to Create. This
is the default action.
- If you want to search for SOAP headers and then either set the values in any headers that are
found or create a new header if none are found, set the property to Find and
Set.
- If you want to search for SOAP headers and then copy the first header that is found to another
location in the SMO, set the property to Find and Copy.
- If you want to search for SOAP headers and then delete any headers that are found, set the
property to Find and Delete.

Used only
when the Action is Find and Set, Find and
Copy or Find and Delete.

Used only
when the Mode property (or Action) is
Create or Find and Set.

If the
Mode property (or Action) is set to Find and
Set, the wizard lets you use Search Values to define the search
criteria, and then use Values to specify the values you want to set (when the
search is satisfied).

## Validate input validateInput

If true, causes the input message to be
validated before the mediation is performed.

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
<node name="addHeader" type="SOAPHeaderSetter">
  <table name="headerElements">
    <row>
      <property name="mode" value="Create"/>
      <property name="searchValues" value=""/>
      <property name="values" value="header\_\_name=&quot;SecurityID&quot; 
      header\_\_namespace=&quot;http://TestMod&quot; 
      @xsi:type=&quot;{http://TestMod}SecurityHeader&quot; 
      SecurityHeader/id=&quot;id123&quot; SecurityHeader/password=&quot;pwd123&quot;"/>
      <property name="targetDestination" value=""/>
      <property name="headerType" value="{http://TestMod}SecurityHeader"/>
      <property name="searchValues.reconstruction" value=""/>
      <property name="values.reconstruction" value="<?xml version=&quot;1.0&quot; 
      encoding=&quot;UTF-8&quot;?>&#xD;&#xA;<com.ibm.ccl.soa.test.common.
      models.parm:ParameterList xmi:version=&quot;2.0&quot; xmlns:xmi=&quot;
      http://www.omg.org/XMI&quot; xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot; 
      xmlns:com.ibm.ccl.soa.test.common.models.parm=&quot;http:///com/ibm/ccl/
      soa/test/common/models/parm.ecore&quot; xmlns:com.ibm.ccl.soa.test.
      common.models.value=&quot;http:///com/ibm/ccl/soa/test/common/models/value.ecore&quot; 
      id=&quot;1291224679937\_3&quot;>&#xD;&#xA;  <parameters xsi:type=&quot;com.ibm.ccl.soa.
      test.common.models.value:ValueStructure&quot; name=&quot;
      SecurityHeader&quot; id=&quot;1291224680343\_4&quot; value=&quot;&quot; 
      defaultValue=&quot;&quot; typeURI=&quot;xsd:/http://TestMod#SecurityHeader&quot; 
      baseTypeURI=&quot;xsd:/http://TestMod#SecurityHeader&quot; 
      hasChildren=&quot;true&quot;>&#xD;&#xA;    
      <context>&#xD;&#xA;      <properties name=&quot;project\_context&quot; 
      value=&quot;TestMod&quot;/>&#xD;&#xA;    </context>&#xD;&#xA;    
      <properties name=&quot;elementNS&quot; value=&quot;http://TestMod&quot;
      />&#xD;&#xA;    <elements xsi:type=&quot;com.ibm.ccl.soa.test.common.models.
      value:ValueField&quot; name=&quot;id&quot; id=&quot;1291224680421\_5&quot; 
      value=&quot;&amp;quot;id123&amp;quot;&quot; defaultValue=&quot;&quot; 
      typeURI=&quot;xsd:/http://www.w3.org/2001/XMLSchema#string&quot; 
      baseTypeURI=&quot;xsd:/http://www.w3.org/2001/XMLSchema#string&quot;/>&#xD;&#xA;    
      <elements xsi:type=&quot;com.ibm.ccl.soa.test.common.models.
      value:ValueField&quot; name=&quot;password&quot; id=&quot;1291224680484\_9&quot; 
      value=&quot;&amp;quot;pwd123&amp;quot;&quot; defaultValue=&quot;&quot; 
      typeURI=&quot;xsd:/http://www.w3.org/2001/XMLSchema#string&quot; 
      baseTypeURI=&quot;xsd:/http://www.w3.org/2001/XMLSchema#
      string&quot;/>&#xD;&#xA;  </parameters>&#xD;&#xA;</com.ibm.ccl.soa.
      test.common.models.parm:ParameterList>&#xD;&#xA;"/>
    </row>
  </table>
  <inputTerminal/>
  <outputTerminal>
    <wire targetNode="nextNode"/>
  </outputTerminal>
  <failTerminal/>
</node>
```