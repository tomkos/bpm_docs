<!-- image -->

# Calling data handlers from bindings

The following sections show how the delimited data handler created
previously is invoked from these data bindings.

- JMS, MQ JMS and Generic JMS data bindings
- MQ data binding
- HTTP data binding
- Configuring a data binding to call a data handler
- Using data handler instances from multiple threads

## JMS, MQ JMS and Generic JMS
data bindings

The code snippets that follow show how the
delimited data handler whose configuration was created previously
is invoked from the JMS data bindings. The JMS data binding implementation
uses the configuration QName of the data handler to obtain and create
the data handler instance from the binding registry.

```
1	public void read(Message jmsMessage)
2	        throws JMSException
3	{
4	    QName configurationName = new QName("http://ProcessCustomerWPS", "DelimitedDataHandlerConfiguration");
5	    DataHandler dataHandler = (DataHandler)bindingRegistry.locateBinding(configurationName, bindingContext);
6	
7	    if (jmsMessage instanceof TextMessage) {
8	        String textMessage = ((TextMessage) jmsMessage).getText();
9	        Reader reader = new StringReader(textMessage);
10	        this.dataObject = (DataObject)datahandler.transform(reader,DataObject.class, null);                
11	        return;
12	    }
13	
14	    if (jmsMessage instanceof BytesMessage) {
15	        BytesMessage bytesMessage = (BytesMessage) jmsMessage;
16	        byte[] sourceBytes = new byte[(int) bytesMessage.getBodyLength()];
17	        bytesMessage.readBytes(sourceBytes);
18	        ByteArrayInputStream InputStream = new ByteArrayInputStream(sourceBytes);
19	        this.dataObject = (DataObject)datahandler.transform(inputStream, DataObject.class, null);
20	        return;
21	    }
22	}
```

```
24	public void write(Message jmsMessage)
25	        throws JMSException
26	{
27	    QName configurationName = new QName("http://ProcessCustomerWPS", "DelimitedDataHandlerConfiguration");
28	    BindingRegistry bindingRegistry = BindingRegistryFactory.getInstance();
29	    DataHandler dataHandler = (DataHandler)bindingRegistry.locateBinding(configurationName, bindingContext);

30	    if((jmsMessage instanceof TextMessage){
31	         Writer writer = new StringWriter();    
32	     datahandler.transformInto(dataObject, Writer, null);                
33	     String messageString = writer.toString();
34	    ((TextMessage) message).setText(messageString);
35	    return;
36	}
       if((jmsMessage instanceof BytesMessage)
37	    ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
38	    datahandler.transformInto(dataObject, outputStream, null);                
39	    byte[] messageBytes = outputStream.toByteArray();
40	    ((BytesMessage) message).setBytes(messageBytes);
41	    return;
42	}
```

## MQ data binding

The following
code snippet shows how the delimited data handler is invoked from
the MQ data binding. The MQ data binding implementation uses the configuration
QName of the data handler to obtain and create the data handler instance
from the binding registry.

```
1	public void read(MQMD md,
2	                 List headers,
3	                 MQDataInputStream inputStream)
4	        throws IOException
5	        // Create the configuration information for the child DataHandler
6	        QName configurationName = new QName("http://ProcessCustomerWPS", "DelimitedDataHandlerConfiguration");
7	        BindingRegistry registry = BindingRegistryFactory.getInstance();
8	        DataHandler dataHandler = (DataHandler) bindingRegistry.locateBinding(configurationName, context);
9	        
10	        if(format != null && (format.equals("MQSTR") || format.equals(""))
11	        {
12	            String textMessage = inputStream.readMQChar(InputStream.available());
13	            Reader reader = new StringReader(textMessage);
14	            this.dataObject = (DataObject)datahandler.transform(reader,DataObject.class, null);                
15	
16	        }
17	        else
18	        {
19	             this.dataObject = (DataObject)dataHandler.transform(inputStream, DataObject.class, null);
20	        }
21	        //deal with business exception
22	   }
```

```
1	    public void write(MQMD md,
2	                      List headers,
3	                      MQDataOutputStream output)
4	        throws IOException
5	    {
6	        // Create the configuration information for the child DataHandler
7	        QName configurationName = new QName("http://ProcessCustomerWPS", "DelimitedDataHandlerConfiguration");
8	
9	        BindingRegistry registry = BindingRegistryFactory.getInstance();
10	        DataHandler dataHandler = (DataHandler) bindingRegistry.locateBinding(configurationName, context);
11	
12	        if(format != null && (format.equals("MQSTR") || format.equals(""))
13	        {
14	            Writer writer = new StringWriter();
15	            datahandler.transformInto(dataObject, writer, null);                
16	            String messageString = writer.toString();
17	             output.writeMQChar(messageString);
18	        }
19	        else
20	        {
21	
22	            dataHandler.transformInto(dataObject, output, null);
23	        }
24	    }
```

## HTTP data binding

The following
code snippet shows how the delimited data handler is invoked from
the HTTP data binding. The HTTP data binding implementation uses the
configuration QName of the data handler to obtain and create the data
handler instance from the binding registry.

```
25	public void convertFromNativeData(HTTPInputStream inputStream)
26	        throws DataBindingException, IOException
27	{
28	    // Create the configuration information for the child DataHandler
1	    QName configurationName = new QName("http://ProcessCustomerWPS", "DelimitedDataHandlerConfiguration");
2	    BindingRegistry registry = BindingRegistryFactory.getInstance();
3	    DataHandler dataHandler = (DataHandler) registry.locateBinding(configurationName, context);
4	    byte[] bytes = httpInputStream.getBytes();
5	    ByteArrayInputStream InputStream = new ByteArrayInputStream(bytes);
6	
7	    this.dataObject = dataHandler.transform(inputStream, DataObject.class, null);
8	    //...
9	}
```

```
10	public void write(HTTPOutputStream output)
11	        throws IOException
12	{
13	    // Create the configuration information for the child DataHandler
14	    QName configurationName = new QName("http://ProcessCustomerWPS", "DelimitedDataHandlerConfiguration");
15	    BindingRegistry registry = BindingRegistryFactory.getInstance();
16	    DataHandler dataHandler = (DataHandler) registry.locateBinding(configurationName, context);
17	    
18	    ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
19	    dataHandler.transformInto(dataObject, outputStream, null);
20	    byte[] messageBytes = outputStream.toByteArray();
21	
22	    httpControl.setContentLength(bytes.length);
23	    output.write(messageBytes);
24	    
25	    // ...
26	}
```

## Configuring a data binding to
call a data handler

We have shown how to call a data handler
from a data binding with example code. You can also configure a data
binding to call a data handler using the binding resource configuration
wizard, where the data handler is configured as a property (see Creating a data format transformation resource configuration).

## Using data handler instances from multiple
threads

The data handler instance created as described is
not thread safe so a data handler instance should not be called from
more than one thread.  Create a new instance each time you need to
apply the data handler.