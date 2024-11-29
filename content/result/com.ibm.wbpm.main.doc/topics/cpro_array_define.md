<!-- image -->

# Arrays in business objects

```
<xsd:element name="telephone" type="xsd:string" maxOccurs="3"/>
```

- the contents of the array
- the array itself.

```
<?xml version="1.0" encoding="UTF-8"?>
 	<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
 	 	  <xsd:element name="Customer">
 	    <xsd:complexType>
 	      <xsd:sequence>
 	        <xsd:element name="name" type="xsd:string"/>
 	        <xsd:element name="ArrayOfTelephone" type="ArrayOfTelephone"/>
 	      </xsd:sequence>
 	    </xsd:complexType>
 	  </xsd:element>

 	  <xsd:complexType name="ArrayOfTelephone">
 	    <xsd:sequence maxOccurs="3">
 	      <xsd:element name="telephone" type="xsd:string" nillable="true"/>
 	    </xsd:sequence>
 	  </xsd:complexType> 
	</xsd:schema>
```

The telephone element now appears as a child of the
ArrayOfTelephone wrapper object.

```
<Customer>
	  <name>Bob</name>
	  <ArrayOfTelephone>
	    <telephone>111-1111</telephone>
	    <telephone xsi:nil="true"/>
	    <telephone>333-3333</telephone>
	  </ArrayOfTelephone>
	</Customer>
```

```
DataObject customer = ...
	customer.setString("name", "Bob");
	 
	DataObject tele\_array = customer.createDataObject("ArrayOfTelephone");
	Sequence seq = tele\_array.getSequence();  // The array is sequenced
	seq.add("telephone", "111-1111");
	seq.add("telephone", null);
	seq.add("telephone", "333-3333");
```

```
String tele3 = tele\_array.get("telephone[3]");  // tele3 = "333-3333"
```

You can enter the data items for the array in the list index by using fixed width or delimited
data placed in a JMS or MQ message queue. You can also accomplish this task by using a flat text
file that contains the properly formatted data