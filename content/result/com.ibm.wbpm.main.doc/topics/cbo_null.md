<!-- image -->

# Support for null business objects

Here is an example which illustrates an XML message with a nillible element.

```
<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2001/12/soap-envelope">
	<soap:Body>
		<p:Employee xmlns:p="http://www.mycompany.com" xmlns:xsi="http://www.w3.org" 
			xsi:nil="true"/>
	</soap:Body>
</soap:Envelope>
```

```
<element name="Employee" nillable="true">
...
</element>
```