<!-- image -->

# Accessing the JMS header

## Using Java to access the JMS header

The SCA module can access the JMS message header and JMS message properties. An example where
this can be used is to determine the format of the message body. A custom data handler determines
the message format by accessing the JMS header. The custom data handler decides how the message body
is handled. For example, if you access the JMSType field in the JMS header, a
data handler can determine how the message body is formatted. As a result, you can use a single data
handler for multiple JMS message formats. This removes the need for multiple exports, imports and
JMS destinations.

```
HeadersType headers = ContextService.INSTANCE.getHeaders();
 JMSHeaderType jmsHeader = headers.getJMSHeader();
 String jmsType = jmsHeader.getJMSType();
 
 if (jmsType.equals("Company1Quote")) {
 	/* parse XML using Company1 schema to create business object*/
 } else if (jmsType.equals("Company2Quote")) {
 	/* parse XML using Company2 schema to create business object*/
 } else if (jmsType.equals("Company3Quote")) {
 	/* parse XML using Company3 schema to create business object*/
 } else {
 	/* parse XML using standard schema to create business object*/
 }
```

```
HeadersType headers = ContextService.INSTANCE.getHeaders();
 List<PropertyType> properties = headers.getProperties();

 for (PropertyType property : properties) {  	
	String propName = property.getName();  	
	String propValue = property.getValue();  	
	/* Check for required JMS property */  
 }
```

## Using a mediation flow component to access the JMS header

Figure 1. The structure of the JMS header in the SMO

<!-- image -->