<!-- image -->

# Example of custom MQ data bindings

- The MQ data Application Programming
Interface (API)
- Description of this sample
- Order that methods are called in this sample
- MQBodyDataBinding interface
- MQHeaderDataBinding interface
- Implementation of an MQBodyDataBinding
- Implementation of an MQHeaderDataBinding
- Function selector
- Request message

## The MQ data Application Programming
Interface (API)

The MQ data API provides the classes and
methods you would use to create a custom data binding that interacts
with an application developed in IBM Integration
Designer that
uses the service component architecture. These classes and methods
are used in this sample.

The MQ data API is listed in the information
center under the references section.

## Description of this sample

In
this sample, we will send body and header data to our service component
architecture application. Sending body and header information is done
by some MQ users.

For the body data binding, the scenario involves
sending information on a credit to a bank. The information is passed
from a CreditRequest data structure to a CreditRequest business object.

The
CreditRequest fixed-length data structure contains the user's name
and account number, a bank sort code (which determines the branch
of the bank), the amount of money to credit and currency.

```
struct CreditRequest {
    MQCHAR[32] Surname;   // For validation, account holder's surname
    MQCHAR[8] AccountId;  // Destination account id, 8 numeric digits
    MQCHAR[6] SortCode;   // Bank's sort code, 6 numeric digits
    MQBYTE[2] Padding;    // For word-alignment; should be nulls
    MQLONG Amount;        // Amount to credit in major currency
    MQLONG SubAmount;     // Currency subdivision (for example, cents, pence)
    MQCHAR[4] Currency;   // Currency identifier
}
```

```
<complexType name="CreditRequest">
  <sequence>
    <element name="Surname" type="string"/>
    <element name="AccountId" type="tns:AccountIdType"/>
    <element name="SortCode" type="tns:SortCodeType"/>
    <element name="Amount" type="float"/>
    <element name="Currency" type="string"/>
  </sequence>
</complexType>

<!-- AccountId must be eight numeric digits -->
<xsd:simpleType name="AccountIdType">
  <xsd:restriction base="string">
    <xsd:pattern value="[0-9]{8}"/>
  </xsd:restriction>
</xsd:simpleType>

<!-- Sort code is of form 12-34-56 -->
<xsd:simpleType name="SortCodeType">
  <xsd:restriction base="string">
    <xsd:pattern value="[0-9]{2}-[0-9]{2}-[0-9]{2}"/>
  </xsd:restriction>
</xsd:simpleType>
```

In the business object editor,
the business object appears as follows:

<!-- image -->

Sometimes WebSphere® MQ cannot deliver a message to
a destination and sends the information to a dead letter queue. In
this sample, we create a custom header data binding to handle this
situation. The information is passed from a MQDLH data structure to
a DeadLetterHeader business object.

```
struct MQDLH {
    MQCHAR4  StrucId;
    MQLONG   Version;
    MQLONG   Reason;
    MQCHAR48 DestQName;
    MQCHAR48 DestQMgrName;
    MQLONG   Encoding;
    MQLONG   CodedCharSetId;
    MQCHAR8  Format;
    MQLONG   PutApplType;
    MQCHAR28 PutApplName;
    MQCHAR8  PutDate;
    MQCHAR8  PutTime;
}
```

```
<complexType name="DeadLetterHeader">
  <sequence>
    <element name="Reason" type="mq:MQLONG"/>
    <element name="DestQName" type="mq:MQCHAR48"/>
    <element name="DestQMgrName" type="mq:MQCHAR48"/>
    <element name="PutApplType" type="mq:MQLONG"/>
    <element name="PutApplName" type="mq:MQCHAR28"/>
    <element name="PutDate" type="mq:MQCHAR8"/>
    <element name="PutTime" type="mq:MQCHAR8"/>
  </sequence>
</complexType>
```

In the business object editor,
the business object appears as follows:

<!-- image -->

## Order that methods are called
in this sample

The order that the methods are called in
this sample will help you understand the actions at run time. With
respect to these data bindings, the pattern of the called methods
is as follows:

- When reading, the headers are parsed first (using header data
bindings). Then the function selector is executed and finally the
the body data binding.
- In the MQHeaderDataBinding, the four getter methods will be called
after the call to read. They return information discovered from data
passed to the most recent call to read.
- Similarly, in an MQHeaderDataBinding, the four setter methods
will be called before any call to write. The format/ccsid/encoding
information should normally be embedded in the serialization of the
header.
- In an MQBodyDataBinding, setFormat() will be called before the
call to read and provides the format identifier used for the body.
- Similarly, in an MQBodyDataBinding, getFormat() is called after
write() is called. The body data binding must return a format identifier
which will be used in the outbound MQ message. setFormat() may be
called before write() with a suggested format identifier. This may
for example have been set from an incoming MQ message or using a mediation
flow module.

## MQBodyDataBinding interface

The
purpose of the body data binding is to convert the payload of an MQ
message to the body business object and vice versa when the data flows
from the service component architecture application to the Java application. If your MQ messages
do not have payload that is in a format we support with our supplied
data bindings then you will need to write your own data binding.

Specifically,
you need to implement the read and write methods and specify the MQ
message format. Read() reads the WebSphere MQ
message into a DataObject type and then retrieves the DataObject.
Write() writes to the WebSphere MQ
message. Read() takes an MQMD (MQ message descriptor) header, a header
list (an ordered list of headers) and an MQDataInputStream (a stream
of bytes) as arguments. Write() uses the same arguments though output
is an MQDataOutputStream. It is assumed that the structure of the
message in the stream is known.Implementation of an MQHeaderDataBinding provides
an example of how you might implement the read and write methods in
the MQBodyDataBinding interface.

The MQBodyDataBinding interface
also sets and gets metadata related to the service-oriented architecture
environment and identifies the WebSphere MQ
message format. The BusinessException accessor, used with respect
to the service-oriented environment, may need to update the MQMD header
and header list depending on the structure of the message. The setFormat()
accessor, called before a read, determines the MQ format string described
in the service-component architecture header. The getFormat() accessor,
called after a write, determines the MQ format string that gets written
into the message identifying the body structure.

```
public interface MQBodyDataBinding extends DataBinding {
	// from DataBinding
	public DataObject getDataObject() throws DataBindingException;

	public void setDataObject(DataObject dObj) throws DataBindingException;

	// Control methods. Both read and write may alter the contents 
	// of the MQMD and the List of MQHeader objects - if read alters 
	// these, then it changes how the message is represented in SCA; 
	// if write alters these, then it changes how the message gets 
	// written to WMQ. The headers parameter is a List of
	// MQHeader DataObjects
	public void read(MQMD md, List headers, MQDataInputStream input)
			throws IOException;

	public void write(MQMD md, List headers, MQDataOutputStream output)
			throws IOException;

	// setter is called before a write; getter after a read. 
	// Marks whether this is an exception for response messages.
	public void setBusinessException(boolean isBusinessException);

	public boolean isBusinessException();

	// setFormat() is called before a read, and contains the MQ format 
	// string identifying the body format. It is also called before a write, 
	// and contains the MQ format string described in the SCA header. 
	// getFormat() is called after a write, and determines the format 
	// string that actually gets written into the message to identify 
	// the body structure.
	public void setFormat(String format);

	public String getFormat();
}
```

## MQHeaderDataBinding interface

You
must implement the MQHeaderDataBinding interface if you intend to
use MQ header types not supported by the MQ bindings in IBM Integration
Designer.
Implementing the MQHeaderDataBinding interface means you will extend
an import or export with MQ bindings. getDataObject(), setDataObject(),
read() and write() methods are identical to the MQBodyDataBinding
interface. isSupportedFormat() must be implemented, returning true
if the header data binding implementation is prepared to handle the WebSphere MQ format identifier.

During
a read method, the MQHeaderDataBinding must also retrieve information
from the WebSphere MQ
message related to character encoding such as the Coded Character
Set Identifier (CCSID) and then return the same information in a write
method using get and set accessors.

Implementation of an MQHeaderDataBinding provides an example of you how
you might implement the methods in the MQHeaderDataBinding interface.

```
public interface MQHeaderDataBinding extends DataBinding
{
  // which formats this binding supports
  public boolean isSupportedFormat(String format);
  
  // from DataBinding
  public DataObject getDataObject() throws DataBindingException;
  public void setDataObject(DataObject dObj) throws DataBindingException;
  
  // Control methods. Format on read is the format identifying 
  // the header structure; on write it is the format string 
  // associated with the DataObject.
  public void read(String format, MQDataInputStream input) throws IOException;
  public void write(String format, MQDataOutputStream output) throws IOException;
  
  // setters are called before a write; getters after a read
  public void setNextFormat(String format);
  public String getNextFormat();
  public void setNextCCSID(int ccsid);
  public int getNextCCSID();
  public void setNextEncoding(int encoding);
  public int getNextEncoding();
}
```

## Implementation of an MQBodyDataBinding

The
following sample shows how an MQ body data binding passes data from
a fixed-length data structure, commonly used in C or COBOL applications,
to a business object (XML Schema Definition (XSD)). The fixed-length
data structure and the business object in XML format are shown. The
scenario is a request for a credit to a bank account from the service-component
architecture application.

The body data binding converting between
the WMQ message and the Business Object has a number of concerns.
As well as dealing with the problems of converting those fields with
slightly different representations, it must deal with the WMQ format
identifier. The customer's WMQ usage standards dictate that the format
identifier should be "FCREDRQ".

```
public class CreditRequestDataBinding implements WMQBodyDataBinding {
	private DataObject dObj;

	public DataObject getDataObject() throws DataBindingException {
		return dObj;
	}

	public void setDataObject(DataObject dObj) throws DataBindingException {
		this.dObj = dObj;
	}

	public void read(MQMD md, List headers, MQDataInputStream input) throws IOException
    {
        // Create the output DataObject
        BOFactory bof=(BOFactory)ServiceManager.INSTANCE
                                       .locateService("com/ibm/websphere/bo/BOFactory");
        DataObject dObj=bof.create("urn://sample", "CreditRequest");

        // Read data from the input message
        dObj.setString("Surname", input.readMQCHAR32().trim());
        dObj.setString("AccountId", input.readMQCHAR8());

        // Read and format the sort code
        String sortCode=input.readMQCHAR(6);
        StringBuffer scbuf=new StringBuffer();
        scbuf.append(sortCode.substring(0,2);
        scbuf.append('-');
        scbuf.append(sortCode.substring(2,4);
        scbuf.append('-');
        scbuf.append(sortCode.substring(4,6);
        dObj.setString("SortCode", scbuf.toString());

        // Skip the two byte pad field
        input.skipBytes(2);

        // Read the amount
        int amount=input.readMQLONG();
        int subamount=input.readMQLONG();
        dObj.setFloat("Amount", amount+(subamount/100.0f));
	
        // Finally the currency
        dObj.setString("Currency", input.readMQCHAR4().trim());

        this.dObj=dObj;
    }

	public void write(MQMD md, List headers, MQDataOutputStream output)
			throws IOException {
		// Write data to the output message
		output.writeMQCHAR32(dObj.getString("Surname"));
		output.writeMQCHAR8(dObj.getString("AccountId"));

		// Sort code
		String[] sortCode = dObj.getString("SortCode").split("-");
		for (int i = 0; i < sortCode.length; i++)
			output.writeMQCHAR(2, sortCode[i]);

		// Write two zero bytes of padding
		output.writeMQSHORT(0);

		// Amount
		float amount = dObj.getFloat("Amount");
		output.writeMQLONG((int) amount);
		output.writeMQLONG(((int) (amount * 100)) % 100);

		// Currency
		output.writeMQCHAR4("Currency");
	}

	// A CreditRequest message can never represent a business 
	// exception, as it is a request and not a response.
	public void setBusinessException(boolean isBusinessException) {
	}

	public boolean isBusinessException() {
		return false;
	}

	// The format value has a number of uses. Before a read, 
	// we get told 	the format identifier and can use that 
	// to determine how to parse the message
	// (and also the function name). After a write(), getFormat 
	// is called to determine the format identifier to write into 
	// the outbound message. We usually return the format identifier 
	// appropriate for the structure; but some data bindings will 
	// return the format identifier set with setFormat immediately
	// before the write.
	public void setFormat(String format) {
	}

	public String getFormat() {return "FCREDRQ"};
}
```

## Implementation of an MQHeaderDataBinding

The
following sample shows how an MQ header data binding passes data from
a fixed-length data structure, commonly used in C or COBOL applications,
to a business object (XML Schema Definition (XSD)). The fixed-length
data structure and the business object in XML format are shown. The
scenario is a dead letter situation where WebSphere MQ cannot deliver a message to
a destination and so has added it to the Dead Letter queue. A user
has created a module that reads from the dead letter queue and performs
an action based on the content (that is, the error information) that
is found. A custom header data binding is needed because there is
no support for dead letter headers.

The application checks that
the MQDEAD format is supported then it proceeds to read in the data
and convert it to data objects. Once all data is read and processed,
the information written out specifies the reason for the failure to
deliver the message and provides some application-specific details
on the queue, date and time, and other relevant data.

```
public class DLHDataBinding implements MQHeaderDataBinding {
	private DataObject dObj;

	private String nextFormat;

	private int nextCCSID;

	private int nextEncoding;

	// DLHDataBinding only understands "MQDEAD" format
	public boolean isSupportedFormat(String format) {
		return format.equals("MQDEAD");
	}

	public DataObject getDataObject() {
		return dObj;
	}

	public void setDataObject(DataObject dObj) {
		this.dObj = dObj;
	}

	public void read(String format, MQDataInputStream input) throws IOException {
		String strucId = input.readMQCHAR4();
		if (!strucId.equals("DLH "))
			throw new IOException("Malformed dead-letter header");
		int version = input.readMQLONG();
		if (version != 1)
			throw new IOException("Unsupported DLH version");

		// Create the output DataObject
		BOFactory bof = (BOFactory) ServiceManager.INSTANCE
				.locateService("com/ibm/websphere/bo/BOFactory");
		DataObject dObj = bof.create("urn://sample", "DeadLetterHeader");
		dObj.setInt("Reason", input.readMQLONG());
		dObj.setString("DestQName", input.readMQCHAR48());
		dObj.setString("DestQMgrName", input.readMQCHAR48());
		nextEncoding = input.readMQLONG();
		nextCCSID = input.readMQLONG();
		nextFormat = input.readMQCHAR8();
		dObj.setInt("PutApplType", input.readMQLONG());
		dObj.setString("PutApplName", input.readMQCHAR28());
		dObj.setString("PutDate", input.readMQCHAR8());
		dObj.setString("PutTime", input.readMQCHAR8());

		this.dObj = dObj;
	}

	public void write(String format, MQDataOutputStream output)
			throws IOException {
		output.writeMQCHAR4("DLH"); // StrucId
		output.writeMQLONG(1); // Version
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

	public void setNextFormat(String format) {
		nextFormat = format;
	}

	public String getNextFormat() {
		return nextFormat;
	}

	public void setNextCCSID(int ccsid) {
		nextCCSID = ccsid;
	}

	public int getNextCCSID() {
		return nextCCSID;
	}

	public void setNextEncoding(int encoding) {
		nextEncoding = encoding;
	}

	public int getNextEncoding() {
		return nextEncoding;
	}
}
```

## Function selector

On an export,
the function selector determines which operation to call on the export
interface. For the MQ data bindings and other data bindings, IBM Integration
Designer provides
several function selectors. You can find more information on the function
selector at these links:

- Overview of the MQ function selectors
- Overview of JMS function selectors

WebSphere MQ only
allows one dead-letter queue on a queue manager. Messages other than
the CreditRequest message can be sent to the dead-letter queue. By
using a function selector when reading the dead letter queue, you
can filter out the messages not needed. The function selector generates
a native function name based on the format identifier of the inbound
message and on the contents of any Dead Letter Header. The result
would be deployed along with a set of method bindings that map from
the set of supported format identifiers (plus functions named "cancel"
followed by the format identifier and a special function "ReportNoAuthority")
to the set of operations known to the module.

```
public class DLHFunctionSelector extends MQFunctionSelector {
	public String generateEISFunctionName(MQMD md, String bodyFormat,
			List headers, MQDataInputStream input) throws IOException,
			SelectorException {
		// Find any DLH
		int reason = -1;
		Iterator iter = headers.iterator();
		while (iter.hasNext()) {
			MQHeader header = (MQHeader) iter.next();
			// Is it a DLH?
			if (header.getFormat().equals("MQDEAD")) {
				DataObject dlh = header.getValue();
				reason = dlh.getInt("Reason");
			}
		}

		switch (reason) {
		case -1:
			// No DLH found. The native function is just the format
			return bodyFormat;
		case 2035:
			// MQRC\_NOT\_AUTHORIZED
			return "ReportNoAuthority";
		default:
			// Some other error.
			return "cancel" + bodyFormat;
		}
	}
}
```

## Request message

The following
content is an example of a message received from WebSphere MQ that would be handled by the
previous MQ data bindings.

| MQMD header      | Value                                                       | Message body   | Value    |
|------------------|-------------------------------------------------------------|----------------|----------|
| StrucId          | MQMD                                                        | Surname        | Smith    |
| Version          | 2                                                           | AccountId      | 01731972 |
| Report           | 0 (MQRO\_NONE)                                               | SortCode       | 767216   |
| MsgType          | 1 (MQMT\_REQUEST)                                            | Padding        | (zeros)  |
| Expiry           | -1 (MQEI\_UNLIMITED)                                         | Amount         | 418      |
| Feedback         | 0 (MQFB\_NONE)                                               | SubAmount      | 28       |
| Encoding         | 546 (reversed)                                              | Currency       | GBP      |
| CodedCharSetId   | 437                                                         |                |          |
| Format           | FCREDRQ                                                     |                |          |
| Priority         | 4                                                           |                |          |
| Persistence      | 1 (MQPER\_PERSISTENT)                                        |                |          |
| MsgId            | 0x414d5120 54455354   20202020 20202020   D1C94344 20000205 |                |          |
| CorrellId        | (zeros)                                                     |                |          |
| BackoutCount     | 0                                                           |                |          |
| ReplyToQ         | F.REP                                                       |                |          |
| ReplyToQMgr      | BRANCH.QMGR.2416                                            |                |          |
| UserIdentifier   | CLERK237                                                    |                |          |
| AccountingToken  | (omitted)                                                   |                |          |
| ApplIdentityData | (none)                                                      |                |          |
| PutApplType      | 11 (MQAT\_WINDOWS\_NT)                                        |                |          |
| PutApplName      | actmng.exe                                                  |                |          |
| PutDate          | 20060417                                                    |                |          |
| PutTime          | 18104245                                                    |                |          |
| ApplOriginData   | (none)                                                      |                |          |
| GroupId          | (zeros)                                                     |                |          |
| MsgSeqNumber     | 1                                                           |                |          |
| Offset           | 0                                                           |                |          |
| MsgFlags         | 0 (MQMF\_NONE)                                               |                |          |
| OriginalLength   | -1 (MQOL\_UNDEFINED)                                         |                |          |