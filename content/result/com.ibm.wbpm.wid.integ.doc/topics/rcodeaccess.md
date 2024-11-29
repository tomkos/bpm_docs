<!-- image -->

# Code to access binding-specific headers

## Accessing SMO headers in data handlers

The following
programming examples show how the header information can be accessed by the
data handlers.

## Accessing the properties section of an SMO header

Consider
the case where there is a property called businessObjectName in the properties
section of the SMO header.

```
1	DataObject header = (DataObject) ContextService.INSTANCE.getHeaders();
2	List<DataObject> userPropertiesList = header.getList("properties");
3	for (DataObject userProperty : userPropertiesList) {
4	    String name = userProperty.getString("name");
5	     if (name.equals("businessObjectName")) {
6	           String businessObjectName = userProperty.getString("value");
7	     }
8	 }
```

## Accessing a JMS header from an SMO header

To access
the JMS header from the SMO header, you would use the following code:

```
9	DataObject header = (DataObject) ContextService.INSTANCE.getHeaders();
10	DataObject jmsHeader = header.getDataObject("JMSHeader");
11	String jmsMessageID = jmsHeader.get("JMSMessageID");
```

## Accessing an MQ header from an SMO header

To access
the MQ header from the SMO header, you would use the following code:

```
12	DataObject header = (DataObject) ContextService.INSTANCE.getHeaders();
13	DataObject mqHeader = header.getDataObject("MQHeader");
14	DataObject mqmd = mqHeader.get("md");
```

## Accessing an HTTP header from an SMO header

To access
the HTTP header from the SMO header, you would use the following code:

```
15	DataObject header = (DataObject) ContextService.INSTANCE.getHeaders();
16	DataObject httpHeader = header.getDataObject("HTTPHeader");
17	DataObject httpControl = mqHeader.get("HTTPControl");
```

## Accessing an EIS Flat File header from an SMO header

To
access the EIS Flat File header from the SMO header, you would use the following
code:

```
18	DataObject header = (DataObject) ContextService.INSTANCE.getHeaders();
19	DataObject eisHeader = header.getDataObject("EISHeader");
20	DataObject eisIneractionSpec = mqHeader.get("EISInteractionSpec");
```