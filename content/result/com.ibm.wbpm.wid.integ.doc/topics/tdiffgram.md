<!-- image -->

# Working with Microsoft ADO.NET
services

## Understanding ADO.NET schema

<!-- image -->

Figure 1. Example response from ADO.NET

As the previous schema shows, the payload does not match
the embedded schema definition. There is an extra diffgram element,
and there are also extra attributes that are not defined in the schema.

In
order to handle this payload, it needs to be represented in a format
that IBM Integration
Designer can
handle. This is achieved by generating helper schemas that convert
the diffgram and extra attributes into xsd files. The next step is
to get the payload information, which you can get by calling the service,
or from the service provider as an xsd file. Once you have the xsd
files, you can use the capability to work with xsd:any to read and
write the data inside a diffgram.

## Generate helper schema

1. Import the original WSDL file from the Microsoft ADO.NET project into a mediation
module or library.
2 Add the line <s:element ref="s:schema" /> tothe WSDL message element so that IBM IntegrationDesigner cancorrectly handle the response from the ADO.NET service. For the exampleresponse shown in figure 1, the WSDL should be modified as follows:<?xml version="1.0" encoding="utf-8"?><wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/ xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/" .........xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"> <wsdl:types> <s:schema elementFormDefault="qualified" targetNamespace="http://ibm.com/WID/DataSetTests/"> 1 <s:import namespace="http://www.w3.org/2001/XMLSchema" /> <s:element name="getProducts"> <s:complexType /> </s:element> <s:element name="getProductsResponse"> <s:complexType> <s:sequence> <s:element minOccurs="0" maxOccurs="1" name="getProductsResult"> <s:complexType> <s:sequence> 2 <s:element ref="s:schema" /> <s:any /> </s:sequence> </s:complexType> </s:element> </s:sequence> </s:complexType> </s:element> ... (more elements) </wsdl:types></wsdl:definitions>

```
<?xml version="1.0" encoding="utf-8"?>
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/ 
xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/" 
...
...
...
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
 <wsdl:types>
   <s:schema elementFormDefault="qualified" targetNamespace="http://ibm.com/WID/DataSetTests/">
   1  <s:import namespace="http://www.w3.org/2001/XMLSchema" />
      <s:element name="getProducts">
        <s:complexType />
      </s:element>
      <s:element name="getProductsResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="getProductsResult">
              <s:complexType>
                <s:sequence>
                 2  <s:element ref="s:schema" />
                 <s:any />
                </s:sequence>
              </s:complexType>
            </s:element>
          </s:sequence>
        </s:complexType>
      </s:element>

  ... (more elements)
  </wsdl:types>

</wsdl:definitions>
```

    - 1  Add import
    - 2  Add <s:element ref="s:schema"
/>
3 Generate the helper schema, in one of the following ways:

- Go to the Problems view, and locate the error message for the
WSDL file. Right click the error message, and click Quick Fix to generate
the helper schema.
- Generate the helper schema from the Dependencies editor: Two helper schemas are created in your mediation moduleor library. You can view them in the Physical Resources view: The files created are diffgram.xsd ,which is the helper schema for diffgrams, and msdata.xsd ,which defines global attributes.
    1. Expand the module or library where the WSDL file is located, and
click the dependency editor icon
    2. In the dependency editor, expand Predefined Resources and
select Microsoft ADO .NET DataSet schema file.
Save the changes.

<!-- image -->

## Get the payload schema

- Your client or service provider may have given you the payload
schema as an xsd file. In this case, import the file that into your
library or mediation module.
- If you don't have the payload schema file, you can obtain it byusing the test client to save the results from the service invocationas an xsd file, as follows:
    1. Create a Web Service Import to call the web service using the
test client.
    2. In the test client, invoke the required operation
    3. When you get the response from the operation, display the results
in the SDO view by clicking the icon Display the SDO style
view in
the Response Parameters table.
    4. In the SDO style view, right click, and choose Export
to XML file.
    5. Save the payload to an xsd file (for example, payload.xsd).

## Modify the payload schema

If
you want to create diffgrams that perform insert, update and delete
operations to a database on the .NET server, you need to modify the
payload schema.

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema id="NewDataSet" xmlns:xsd="http://www.w3.org/2001/XMLSchema" targetNamespace="http://InventoryLib">
  <xsd:element name="NewDataSet">
  	<xsd:complexType>
  		<xsd:choice maxOccurs="unbounded" minOccurs="0">
  			<xsd:element name="Product\_x0020\_Table">  				<xsd:complexType>
  					<xsd:sequence>
  						<xsd:element minOccurs="0" name="Product" type="xsd:string" />
  						<xsd:element minOccurs="0" name="Quantity" type="xsd:int" />
  					</xsd:sequence>
  					<xsd:anyAttribute namespace="##any" processContents="lax" />
  				</xsd:complexType>
  			</xsd:element>
  		</xsd:choice>
  		</xsd:complexType>
  </xsd:element>
</xsd:schema>
```

## Access the payload schema in a mediation flow

To
access and manipulate the payload in a mediation flow, first generate
the helper schema and obtain the payload schema. Then, in the mediation
flow, drop a Set Message Type primitive to assert the actual type
for the diffgram and the payload content. Now, you have full access
to the structure of the diffgram message, for mapping or XPath access.

- Cast dynamic data content using the Set Message Type primitive.
- Read and write data in the diffgram block using the Message Element
Setter, when used in conjunction with the Set Message Type primitive.
- Provide mapping for the diffgram payload in the Mapping primitive
or the Business Object Map primitive, when used in conjunction with
the Set Message Type primitive.

## Example: Log the message and pass through

1. Import the original wsdl file from the Microsoft ADO.NET project into a mediation
module or library.
2. Generate helper schema.
3 Implement the mediation flow component.
    - Connect the source and target operations
    - In the request flow, wire the input node to the callout node
    - In the response flow, wire a message logger primitive between
the callout and input response nodes. In the logger's properties view,
set the root property to specify the part of the message that you
want to log.

## Example: Update diffgram content using XPath

In
this example, you want to update an element in a diffgram block in
the response message from a .NET service. In this situation, you don't
have the payload schema, but you know the structure of the data. You
can access the element by  manually entering the XPath to the diffgram
content,  assuming that you know this location path.

1. Import the original wsdl file from the Microsoft ADO.NET project into a mediation
module or library.
2. Generate helper schema.
3 Implement the mediation flow component.
    - Connect the source and target operations
    - In the request flow, wire the input node to the callout node
    - In the response flow, wire a Message Element Setter primitive
between the callout and input response nodes.
    - In the properties view of Message Element Setter, add a message
element. In the target field, specify the XPath expression for the
location of the element that you want to update, and enter a type
and value.

## Example: Update diffgram content using payload schema

In
this example, you want to update an element in a diffgram block in
the response message from a .NET service. In this situation, you have
the payload schema, so you can use Set Message Type together with
Message Element Setter to update the element.

1. Import the original wsdl file from the Microsoft ADO.NET project into a mediation
module or library.
2. Generate helper schema.
3. Get the payload schema
4 Implement the mediation flow component.
    - Connect the source and target operations
    - In the request flow, wire the input node to the callout node
    - In the response flow, wire a Set Message Type primitive and a
Message Element Setter primitive between the callout and input response
nodes. We will use the Set Message Type primitive to cast the diffgram
any type to the business object that we need. We can then use Message
Element Setter to update the required element.
    - In the properties view of SetMessageType1 set the following: If you hover over the input andoutput terminals of the Set Message Type primitive, you will see thechange in input and output message types. The input message type shownbelow does not show the message body. The output message type shownbelow has the business object that contains the element that we wantto access.
        - First, set the <xsd:any> to the diffgram business object.
        - Then, set the <xsd:any> in the diffgram to the actual payload
business object

<!-- image -->

<!-- image -->

<!-- image -->

- In the properties view of Message Element Setter, click Add, and
then Edit to launch the XPath Expression Builder. You can now drill
down the message to choose the target message element that you want
to update.

## Example: Transform a response from a .Net service

In
this example, you want to consume a response from a .NET service,
and transform the response to the format expected by the service provider.
Proceed as follows:

1. Import the original wsdl file from the Microsoft ADO.NET project into a mediation
module or library.
2. Generate helper schema.
3. Get the payload schema
4 In the assembly editor, create the following:
    - An export, with web service binding. When you import the service
requester's wsdl file, an interface is created for each port type
defined in the wsdl file. Give the export the appropriate interface
    - A mediation flow component
    - An import, with the interface of the service provider. Use a web
service binding, with the address from the original wsdl file.
    - Wire together the export, mediation flow component, and the import.
5 Implement the mediation flow component.

- Connect the source and target operations
- In the request flow, wire the Mapping primitive between the input
and callout.
- The response from the service is in the anyType format. In order
to transform the message, you need to convert the anyType field into
the elements you want. In the response flow, wire a Set Message Type
primitive and a Mapping primitive between the callout and input response
nodes. We will use the Set Message Type primitive to cast the diffgram
any type to the business object that we need. We can then use XSLT
Transformation primitive to perform the required mapping. Note: You
can use the Business Object Map instead of the Mapping primitive.
- In the properties view of SetDiffgramAndPayloadType set the followingproperties in the message field refinements table. If you hover over the input and output terminals of the Set MessageType primitive, you will see the change in input and output messagetypes. The input message type shown below does not show the messagebody. The output message typeshown below has the business object that contains the element thatwe want to access.
    1. First, set the <xsd:any> to the diffgram business object: 
Weakly typed field
/body/getProductsResponse/getProductsResult/xsd:any
Actual field type
{urn: schemas-microsoft-com:xml-diffgram-v1}diffgram
    2. Then, set the <xsd:any> in the diffgram to the actual payload
business object: 
Weakly typed field
/body/getProductsResponse/getProductsResult/diffgram/xsd:any
Actual field type
{null}NewDataSet

<!-- image -->

<!-- image -->

- In the properties view of MapPayload, create the mapping file.
First, map the NewDataSet to the corresponding element in the target,
using an inline map transform.
- Next, map the elements within the inline map, using the move transform.

## Example: Create a diffgram message

In this
example, you want to create a diffgram message. For example, you may
want to persist the data on a .NET server. Proceed as follows:

1. Import the original wsdl file from the Microsoft ADO.NET project into a mediation
module or library.
2. Generate helper schema
3. Get the payload schema
4. Modify the payload schema.
5 Implement the mediation flow component.
    - Connect the source and target operations
    - In the request flow, wire a Custom Mediation primitive between
the input and callout nodes to create the diffgram.
6 Implement Java™ code as eithera Java snippet or a Visual snippetin the custom mediation to create a diffgram and set payload informationand attributes:

- Java snippet implementation
In
the Java Imports page in the properties view,
add these import statements: import commonj.sdo.DataObject;
import com.ibm.websphere.sibx.smobo.ServiceMessageObjectFactory;
import com.ibm.websphere.bo.BOFactory;
import com.ibm.websphere.sca.ServiceManager;
import com.ibm.websphere.bo.BOXSDHelper;
import commonj.sdo.Property;
import com.ibm.websphere.bo.BOXMLSerializer;
import java.io.InputStream;
import java.math.BigInteger;
- In the Details properties page, add your Java code. See the example code
below; details are provided in the comments in the code. /**
 * GENERATED COMMENT - DO NOT MODIFY
 * Variables:  for output terminals - out (com.ibm.wsspi.sibx.mediation.OutputTerminal)
 *             for user properties - <No user properties defined>
 * Inputs:     inputTerminal (com.ibm.wsspi.sibx.mediation.InputTerminal), smo (com.ibm.websphere.sibx.smobo.ServiceMessageObject)
 * Exceptions: com.ibm.wsspi.sibx.mediation.MediationConfigurationException, com.ibm.wsspi.sibx.mediation.MediationBusinessException
 */
// Step 1a: Create an SMO body

DataObject newBody = (DataObject) ServiceMessageObjectFactory.eINSTANCE.createServiceMessageObject(new javax.xml.namespace.QName("http://ibm.com/WID/DataSetTests/", "addProductsSoapIn")).getBody();

// Step 1b: Create wrappers addProducts and products

DataObject addProductsElement = newBody.createDataObject("addProducts");
DataObject productsElement = addProductsElement.createDataObject("products");

// Step 1c: Set the SMO body

smo.set("body", newBody);

// Step 2a: Create a BO from payload schema NewDataSet.xsd

DataObject schemaBO = null;
try {
	BOXMLSerializer boXMLSerializer = (BOXMLSerializer) ServiceManager.INSTANCE.locateService("com/ibm/websphere/bo/BOXMLSerializer");
	InputStream inputStream = this.getClass().getClassLoader().getResourceAsStream("NewDataSet.xsd");
	schemaBO = (DataObject) boXMLSerializer.readXMLDocument(inputStream).getDataObject();
}
catch(java.io.FileNotFoundException ex){
}
catch(java.io.IOException ex2){
}

// Step 2b: Add schema BO to SMO body wrapper

DataObject dummy = productsElement.createDataObject("schema");
productsElement.setDataObject("schema", schemaBO);

// Step 3a: Create diffgram
BOFactory boFactory = (BOFactory) ServiceManager.INSTANCE.locateService("com/ibm/websphere/bo/BOFactory");
DataObject diffgram = boFactory.createByElement("urn:schemas-microsoft-com:xml-diffgram-v1","diffgram");

// Step 3b: Add diffgram to SMO body wrapper
BOXSDHelper boXSDHelper = (BOXSDHelper) ServiceManager.INSTANCE.locateService("com/ibm/websphere/bo/BOXSDHelper");

// Get global property for diffgram

Property diffgramProperty = boXSDHelper.getGlobalProperty("urn:schemas-microsoft-com:xml-diffgram-v1", "diffgram", true);

// Set wildcard xsd:any with global element diffgram

productsElement.getSequence().add(diffgramProperty, diffgram);

// Step 4a: Create payload

DataObject payload = boFactory.createByElement(null,"NewDataSet");

// Step 4b: Set payload

DataObject Product\_x0020\_TableBO = payload.createDataObject("Product\_x0020\_Table");
Product\_x0020\_TableBO.set("Product", "chair");
Product\_x0020\_TableBO.set("Quantity", "40");

// Step 4c: Add payload to diffgram

Property payloadProperty = boXSDHelper.getGlobalProperty(null, "NewDataSet", true);
diffgram.getSequence().add(payloadProperty, payload);

// Step 5: Set diffgram attributes "rowOrder" and "hasChanges"

Property rowOrderProperty = boXSDHelper.getGlobalProperty("urn:schemas-microsoft-com:xml-msdata", "rowOrder", false);
Product\_x0020\_TableBO.set(rowOrderProperty, new BigInteger("0"));
Property hasChangesProperty = boXSDHelper.getGlobalProperty("urn:schemas-microsoft-com:xml-diffgram-v1", "hasChanges", false);
Product\_x0020\_TableBO.set(hasChangesProperty, "inserted");

// propagate the service message object to the primitive that is wired to the 'out' terminal
out.fire(smo);
- Visual snippet implementation
In the Details properties
page, add a visual snippet, as shown below: