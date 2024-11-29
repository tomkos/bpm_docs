<!-- image -->

# Using Java to access the WebSphere MQ header

For outbound messages, the WebSphere MQ binding automatically adds an MQ Message Descriptor
(MQMD) to all messages. You cannot modify the MQMD. If the message already contains an MQMD, then it
is used, and a new one is not created. If you create an MQMD before the message reaches the
WebSphere MQ binding, you are can control the content of the header. The WebSphere MQ binding
provides an API that you use to add an MQMD and custom header to a message. You can use this API in
a custom mediation, to modify the SMO to include the WebSphere MQ headers.

- MQMD describes the MQMD that is added to the message.
- MQControl describes the formatting used for the message body.

Figure 1. MQHeader SMO structure

<!-- image -->

## Parsing a WebSphere MQ header using a custom header data binding

IBM® Business Automation
Workflow provides data bindings that enable various
WebSphere MQ headers to be parsed. Some native WebSphere MQ applications use user-defined headers.
Business Automation Workflow provides an API to create custom header data bindings, which parse
these headers so they can be changed using a mediation flow.

Before creating the data binding, the user-defined header must be modelled as a business object
using the IBM Integration Designer business object editor. An example of a MQ Dead Letter Header
(MQDLH) is shown in Figure 2.

Figure 2. An example MQ Dead Letter Header (MQDLH)

<!-- image -->

The control information; Encoding, CodedCharSetId,
and Format fields, of the header are not modeled here. They are mapped to the
supplied MQControl Business Object.

- In the SMO the control information that describes each header is placed within the header
structure in the SMO.
- On the wire, each header carries the control information of the next header or payload in the
sequence.

Figure 3. WebSphere MQ header structure

<!-- image -->

- isSupportedFormat receives a format and checks if the data binding is
supported. It only returns true if the format matches the MQDLH format MQDEAD.
- getDataObject returns the DataObject that the read method of the data
binding creates.
- setDataObject sets the DataObject in the data binding.
- read reads the message header from incoming messages, and creates the
required DataObject.
- write creates the message header for outgoing messages.
- setNextFormat sets the formatting of either the next header, or if this
is the last header in the chain, the body of the message.
- getNextFormat creates the formatting of either; the next header, or the
body of the message (if it is the last header in the chain).
- setNextCCSID sets the Coded Character Set ID of either the next header,
or if this is the last header in the chain, the body of the message.
- getNextCCSID gets the Coded Character Set ID of either the next header,
or if this is the last header in the chain, the body of the message.
- setNextEncoding sets the encoding of either the next header, or if this
is the last header in the chain, the body of the message.
- getNextEncoding gets the encoding of either the next header, or if this
is the last header in the chain, the body of the message.

```
package com.ibm.custom.data.binding;

import java.io.IOException;
import com.ibm.mq.data.MQDataInputStream;
import com.ibm.mq.data.MQDataOutputStream;
import com.ibm.websphere.bo.BOFactory;
import com.ibm.websphere.sca.ServiceManager;
import com.ibm.websphere.sca.mq.data.MQHeaderDataBinding;
import commonj.sdo.DataObject;

public class MQDLHDataBindingImpl implements MQHeaderDataBinding {

	private DataObject dObj;
	private String nextFormat;
	private int nextCCSID;
	private int nextEncoding;
	    
	//MQDLHDataBinding only understands "MQDEAD" format
	public boolean isSupportedFormat(String format)
	{
		return format.trim().equals("MQDEAD");
	}
	  
	public DataObject getDataObject()
	{
		return dObj;
	}

	public void setDataObject(DataObject dObj)
	{
		this.dObj=dObj;
	}
	  
	public void read(String format, MQDataInputStream input) throws IOException
	{
		//Check the Structure Id is the expected DLH
		String strucId=input.readMQCHAR4();
		if (!strucId.equals("DLH ")) throw new IOException
			("Malformed dead-letter header");
		//Check this is a version 1 header
		int version=input.readMQLONG();
		if (version!=1) throw new IOException("Unsupported DLH version");

		//Create the output DataObject
		BOFactory bof=(BOFactory)ServiceManager.INSTANCE.
			locateService("com/ibm/websphere/bo/BOFactory");
		DataObject dObj=bof.create("http://MQCustomHeaderLibrary", "MQDLH");
		dObj.setString("StrucId", strucId);
		dObj.setInt("Version", version);
		dObj.setInt("Reason", input.readMQLONG());
		dObj.setString("DestQName", input.readMQCHAR48());
		dObj.setString("DestQMgrName", input.readMQCHAR48());
		nextEncoding=input.readMQLONG();
		nextCCSID=input.readMQLONG();
		nextFormat=input.readMQCHAR8();
		dObj.setInt("PutApplType", input.readMQLONG());
		dObj.setString("PutApplName", input.readMQCHAR28());
		dObj.setString("PutDate", input.readMQCHAR8());
		dObj.setString("PutTime", input.readMQCHAR8());

		this.dObj=dObj;
	}

	public void write(String format, MQDataOutputStream output) throws IOException
	{
		output.writeMQCHAR4("DLH ");     // StrucId
		output.writeMQLONG(1);           // Version
		output.writeMQLONG(dObj.getInt("Reason"));
		output.writeMQCHAR48(dObj.getString("DestQName"));
		output.writeMQCHAR48(dObj.getString("DestQMgrName"));
		output.writeMQLONG(nextEncoding);
		output.writeMQLONG(nextCCSID);
		output.writeMQCHAR8(nextFormat);
		output.writeMQLONG(dObj.getInt("PutApplType"));
		output.writeMQCHAR28(dObj.getString("PutApplName"));
		output.writeMQCHAR8(dObj.getString("PutDate"));
		output.writeMQCHAR8(dObj.getString("PutTime"));
	}
	  
	public void setNextFormat(String format)   {nextFormat=format;}
	public String getNextFormat()              {return nextFormat;}
	public void setNextCCSID(int ccsid)        {nextCCSID=ccsid;}
	public int getNextCCSID()                  {return nextCCSID;}
	public void setNextEncoding(int encoding)  {nextEncoding=encoding;}
	public int getNextEncoding()               {return nextEncoding;}
}
```

The API provides access to the MQDataInputStream, and the
MQDataOutputStream, for reading and writing to a WebSphere MQ message. The methods
allow you to access various WebSphere MQ types. For text types, you must know the length of the
field in the custom WebSphere MQ header. This is always a multiple of 4, and is accessed using the
readMQCHARXX and
writeMQCHARXX methods, where XX is the number
of characters to read or write.

In your binding configuration, you can add the custom header data binding to a list where
multiple custom header data bindings are defined for handling sequences of headers. Any messages
that contain the supported header, have the header parsed into the MQChainedHeader
list provided in the SMO. You can access it using Java code or mediation primitives.

## Using Java to access and change a WebSphere MQ header

```
//Retrieve the MQMD from the MQHeader
MQMD mqmd = smo.getHeaders().getMQHeader().getMd();

MQControl mqControl = smo.getHeaders().getMQHeader().getControl();
```

```
//Retrieve the headers from the context service
HeadersType headers = ContextService.INSTANCE.getHeaders();

MQMD mqmd = headers.getMQHeader().getMd();

MQControl mqControl = headers.getMQHeader().getControl();
```

```
//Create a new MQMD structure
MQMD mqmd = WMQStructuresFactory.eINSTANCE.createMQMD();
//Set it in the MQHeader
smo.getHeaders().getMQHeader().setMd(mqmd);

//Create the MQControl structure.  This describes the format of the message body
mqControl = WMQStructuresFactory.eINSTANCE.createMQControl();
//Set it in the MQHeader
smo.getHeaders().getMQHeader().setControl(mqControl);
```