<!-- image -->

# Mediation flow schema reference

## mediationFlow

This is the root
element of a mediation flow document.

```
<mediationFlow xmlns="http://www.ibm.com/xmlns/prod/websphere/2010/MediationFlow" 
               xmlns:HelloService="http://HelloService/HelloService" 
               xmlns:HelloWorld="http://HelloWorldLibrary/HelloWorld" 
               xmlns:XMLSchema="http://www.w3.org/2001/XMLSchema" 
               xmlns:mfcex="http://www.ibm.com/xmlns/prod/websphere/2010/MediationFlowExtension" name="HelloWorldMediation" 
                            targetNamespace="http://HelloWorldMediation/HelloWorldMediation">
```

| Attribute                                 | Required   | Description                                                                                                                                                 |
|-------------------------------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| xmlns                                     | Yes        | Default namespace "http://www.ibm.com/xmlns/prod/websphere/2010/MediationFlow"                                                                              |
| xmlns:xsi                                 | Yes        | XML schema instance namespace "http://www.w3.org/2001/XMLSchema-instance"                                                                                   |
| xsi:type                                  | Yes        | Mediation Flow element name "mediationFlow"                                                                                                                 |
| name                                      | Yes        | The name of the mediation flow document                                                                                                                     |
| targetNamespace                           | Yes        | The target namespace of the mediation flow document                                                                                                         |
| xmlns:XMLSchema                           | No         | If anyType is used in the document, declare the XML schema namespace.                                                                                       |
| xmln s:interfacePrefix=interfaceNamespace | No         | Declares the namespace of the interface used in this document (where interfacePrefix is the name of the interface and interfaceNamespace is the namespace). |

| Child elements   | Constraints                         | Description                                                                                                                                        |
|------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| import           | minOccurs="0" maxOccurs="unbounded" | Declares an import for an interface or business object to be used in this document.                                                                |
| promotedProperty | minOccurs="0" maxOccurs="unbounded" | Declares a promoted property.                                                                                                                      |
| reference        | minOccurs="0" maxOccurs="unbounded" | Adds a reference interface to use in this mediation flow.                                                                                          |
| interface        | minOccurs="0" maxOccurs="unbounded" | Adds an interface to use in this mediation flow.                                                                                                   |
| requestFlow      | minOccurs="0" maxOccurs="unbounded" | Only applicable when the mediation flow document is saved into multiple files.  References the operation flow: <requestFlow ref="tns:callHello"/>  |
| responseFlow     | minOccurs="0" maxOccurs="unbounded" | Only applicable when the mediation flow document is saved into multiple files.  References the operation flow: <responseFlow ref="tns:callHello"/> |
| subflow          | minOccurs="0" maxOccurs="1"         | Only applicable when the mediation flow document is saved as a mediation subflow (.mfcsubflow).                                                    |
| errorFlow        | minOccurs="0" maxOccurs="1"         | Only applicable when the mediation flow document is saved into multiple files.    References the operation flow: <errorFlow ref="tns:callHello"/>  |

## import

```
<import location="HelloWorld.wsdl" namespace="http://HelloWorldLibrary/HelloWorld"/>
```

| Attribute   | Required   | Description                                                                                                  |
|-------------|------------|--------------------------------------------------------------------------------------------------------------|
| location    | Yes        | Location of an external document to be imported. The supported document types are .mfcflow, .wsdl, and .xsd. |
| namespace   | No         | The namespace of the external document.                                                                      |

## reference

```
<reference name="HelloServicePartner" portType="HelloService:HelloService"/>
```

| Attribute   | Required   | Description                                 |
|-------------|------------|---------------------------------------------|
| name        | Yes        | The name of the partner reference.          |
| portType    | Yes        | The WSDL portType of the partner reference. |

## interface

```
<interface portType="HelloWorld:HelloWorld">
```

| Attribute   | Required   | Description                                          |
|-------------|------------|------------------------------------------------------|
| name        | Yes        | The name of the interface                            |
| portType    | Yes        | The WSDL portType that contains a set of operations. |

| Child Element   | Constraints                         | Description                                                  |
|-----------------|-------------------------------------|--------------------------------------------------------------|
| Operation       | minOccurs="0" maxOccurs="unbounded" | The operation for which the mediation flow is being defined. |

## operation

```
<operation name="callHello">
```

| Attribute   | Required   | Description               |
|-------------|------------|---------------------------|
| name        | Yes        | The name of the operation |

| Child Element   | Constraints                 | Description                        |
|-----------------|-----------------------------|------------------------------------|
| requestFlow     | minOccurs="1" maxOccurs="1" | The request flow of the operation. |
| responseFlow    | minOccurs="0" maxOccurs="1" | The response flow of the operation |
| errorFlow       | minOccurs="0" maxOccurs="1" | The error flow of the operation.   |

## requestFlow

```
<requestFlow mfcex:showInputResponse="false" mfcex:showInputFault="false">
```

| Attribute               | Required    | Description                                                           |
|-------------------------|-------------|-----------------------------------------------------------------------|
| mfcex:showInputResponse | No          | Show or hide the input response node in the mediation flow editor.    |
| mfcex:showInputFault    | No          | Show or hide the input fault node in the mediation flow editor.       |
| ref                     | No          | Only applicable when the mediation flow is saved into multiple files. |
| portType                | No          | Only applicable when the mediation flow is saved into multiple files. |
| operation               | No          | Only applicable when the mediation flow is saved into multiple files. |

| Child Element   | Constraints                         | Description                                        |
|-----------------|-------------------------------------|----------------------------------------------------|
| note            | minOccurs="0" maxOccurs="unbounded" | An annotation on the request flow.                 |
| node            | minOccurs="0" maxOccurs="unbounded" | A mediation node or primitive in the request flow. |

## responseFlow

| Attribute   | Required    | Description                                                           |
|-------------|-------------|-----------------------------------------------------------------------|
| ref         | No          | Only applicable when the mediation flow is saved into multiple files. |
| portType    | No          | Only applicable when the mediation flow is saved into multiple files. |
| operation   | No          | Only applicable when the mediation flow is saved into multiple files. |

| Child Element   | Constraints                         | Description                                        |
|-----------------|-------------------------------------|----------------------------------------------------|
| note            | minOccurs="0" maxOccurs="unbounded" | An annotation on the request flow.                 |
| node            | minOccurs="0" maxOccurs="unbounded" | A mediation node or primitive in the request flow. |

## errorFlow

```
<errorFlow mfcex:showInputResponse="false">
```

| Attribute               | Required   | Description                                                                                                                                        |
|-------------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| name                    | No         | The name that identifies the error flow to the main mediation flow. Only applicable when the mediation flow document is saved into multiple files. |
| description             | No         | A description of the error flow. Only applicable when the mediation flow document is saved into multiple files.                                    |
| mfcex:showInputResponse | No         | Show or hide the input response node in the mediation flow editor.                                                                                 |
| ref                     | No         | Only applicable when the mediation flow document is saved into multiple files.                                                                     |

| Child element   | Constraints                         | Description                                      |
|-----------------|-------------------------------------|--------------------------------------------------|
| note            | minOccurs="0" maxOccurs="unbounded" | An annotation on the error flow.                 |
| node            | minOccurs="0" maxOccurs="unbounded" | A mediation node or primitive in the error flow. |

## subflow

```
<subflow>
    <node name="in" type="In">
      <outputTerminal type="XMLSchema:anyType">
        <wire targetNode="Fail1"/>
      </outputTerminal>
    </node>
    <node name="Fail1" type="Fail">
      <inputTerminal/>
    </node>
  </subflow>
```

| Attribute   | Required   | Description                   |
|-------------|------------|-------------------------------|
| name        | No         | The name of the subflow.      |
| description | No         | A description of the subflow. |

| Child element   | Constraints                         | Description                                   |
|-----------------|-------------------------------------|-----------------------------------------------|
| note            | minOccurs="0" maxOccurs="unbounded" | An annotation on the subflow.                 |
| node            | minOccurs="0" maxOccurs="unbounded" | A mediation node or primitive in the subflow. |

## note

```
<note mfcex:x="64" mfcex:y="113">This is an annotation.</note>
```

| Attribute   | Required   | Description                                                                                    |
|-------------|------------|------------------------------------------------------------------------------------------------|
| mfcex:x     | No         | Optional x-coordinate of the note. Automatic layout is used if the attribute is not specified. |
| mfcex:y     | No         | Optional y-coordinate of the note. Automatic layout is used if the attribute is not specified. |

## property

```
<property name="root" promotedPropertyGroup="HelloWorldMediation.HelloWorldMediation" promotedPropertyName="input\_map.root" value="/body"/>
<property name="XSLTransform" value="xslt/input\_map\_req\_1.xsl"/>
<property name="XMXMap" value="xslt/input\_map\_req\_1.map"/>
<property name="validateInput" promotedPropertyGroup="HelloWorldMediation.HelloWorldMediation" promotedPropertyName="input\_map.validateInput"/>
<property name="SMOVersion" value="SMO61"/>
```

| Attribute             | Required   | Description                                                                                             |
|-----------------------|------------|---------------------------------------------------------------------------------------------------------|
| name                  | Yes        | The name of the property.                                                                               |
| description           | No         | The description of the property.                                                                        |
| value                 | No         | The value of the property.                                                                              |
| promotedPropertyName  | No         | Promotes this property to the parent, and use the specified value as the name of the promoted property. |
| promotedPropertyGroup | No         | Optional attribute to help identify the promoted property name.                                         |

## node

```
<node displayName="callHello : HelloWorld" name="HelloWorld\_callHello\_InputResponse" type="InputResponse">
```

| Attribute   | Required   | Description                                                                                                 |
|-------------|------------|-------------------------------------------------------------------------------------------------------------|
| name        | Required   | The name of the mediation node.                                                                             |
| type        | Required   | The mediation type.                                                                                         |
| displayName | No         | The name that will be displayed in the user interface.                                                      |
| description | No         | The description of the mediation node.                                                                      |
| mfcex:x     | No         | Optional x-coordinate of the node or primitive. Automatic layout is used if the attribute is not specified. |
| mfcex:y     | No         | Optional y-coordinate of the node or primitive. Automatic layout is used if the attribute is not specified. |

| Child Element   | Constraints                         | Description                                        |
|-----------------|-------------------------------------|----------------------------------------------------|
| note            | minOccurs="0" maxOccurs="unbounded" | An annotation that attaches to the mediation node. |
| property        | minOccurs="0" maxOccurs="unbounded" | A property of the mediation node.                  |
| inputTerminal   | minOccurs="0" maxOccurs="unbounded" | An input terminal of the mediation node.           |
| outputTerminal  | minOccurs="0" maxOccurs="unbounded" | An output terminal of the mediation node.          |
| failTerminal    | minOccurs="0" maxOccurs="1"         | A fail terminal of the mediation node.             |

## inputTerminal

```
<inputTerminal type="HelloWorld:callHelloResponseMsg"/>
```

| Attribute   | Required   | Description                                                                                               |
|-------------|------------|-----------------------------------------------------------------------------------------------------------|
| name        | No         | The identifier of the input terminal.                                                                     |
| displayName | No         | The name that will be displayed in the user interface.                                                    |
| description | No         | The description of the terminal.                                                                          |
| type        | No         | The message type of the input terminal. If not specified, the message type will be automatically deduced. |

| Child element   | Constraints                         | Description                                               |
|-----------------|-------------------------------------|-----------------------------------------------------------|
| refinement      | minOccurs="0" maxOccurs="unbounded" | A refinement of a weakly-typed field in the message type. |

## outputTerminal

```
<outputTerminal type="HelloService:getHelloRequestMsg">
            <wire targetNode="HelloServicePartner\_getHello\_Callout"/>
          </outputTerminal>
```

| Attribute   | Required   | Description                                                                                                |
|-------------|------------|------------------------------------------------------------------------------------------------------------|
| name        | No         | The identifier of the output terminal.                                                                     |
| displayName | No         | The name that will be displayed in the user interface.                                                     |
| description | No         | The description of the terminal.                                                                           |
| type        | No         | The message type of the output terminal. If not specified, the message type will be automatically deduced. |

| Child element   | Constraints                         | Description                                               |
|-----------------|-------------------------------------|-----------------------------------------------------------|
| refinement      | minOccurs="0" maxOccurs="unbounded" | A refinement of a weakly-typed field in the message type. |
| wire            | minOccurs="0" maxOccurs="unbounded" | An outgoing connection to a mediation node or primitive.  |

## failTerminal

| Attribute   | Required   | Description                                                                                              |
|-------------|------------|----------------------------------------------------------------------------------------------------------|
| name        | No         | The identifier of the fail terminal.                                                                     |
| displayName | No         | The name that will be displayed in the user interface.                                                   |
| description | No         | The description of the terminal.                                                                         |
| type        | No         | The message type of the fail terminal. If not specified, the message type will be automatically deduced. |

| Child element   | Constraints                         | Description                                               |
|-----------------|-------------------------------------|-----------------------------------------------------------|
| refinement      | minOccurs="0" maxOccurs="unbounded" | A refinement of a weakly-typed field in the message type. |
| wire            | minOccurs="0" maxOccurs="unbounded" | An outgoing connection to a mediation node or primitive.  |

## refinement

| Attribute   | Required   | Description                                  |
|-------------|------------|----------------------------------------------|
| path        | Yes        | An XPath expression to a weakly-typed field. |
| type        | Yes        | The data type to use for the refinement.     |

## wire

```
<wire targetNode="HelloServicePartner\_getHello\_Callout"/>
```

| Attribute      | Required   | Description                                                                                 |
|----------------|------------|---------------------------------------------------------------------------------------------|
| targetNode     | Yes        | The name of the mediation node or primitive that this wire is connecting to.                |
| targetTerminal | No         | The input terminal name of the mediation node or primitive that this wire is connecting to. |