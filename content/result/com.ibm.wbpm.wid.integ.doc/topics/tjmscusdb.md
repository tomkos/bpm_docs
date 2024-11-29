<!-- image -->

# Creating a user-defined JMS data binding

## Before you begin

## About this task

The BookObject.java code is shown below:

```
public class BookObject implements java.io.Serializable {

	private String ISDN;

	private String author;

	private String title;

	private float price;

	public String getAuthor() {
		return author;
	}

	public void setAuthor(String author) {
		this.author = author;
	}

	public String getISDN() {
		return ISDN;
	}

	public void setISDN(String isdn) {
		ISDN = isdn;
	}

	public float getPrice() {
		return price;
	}

	public void setPrice(int price) {
		this.price = price;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}
}
```

## Procedure

1. You will need to represent the BookObject class
as a business object. If you do not already have a business object
to represent BookObject, the easiest way to accomplish
this would be to create a business object with four fields to represent
the four fields of the BookObject class. Right click Data in
your module, and select New > Business Object from
the contextual menu.  Specify an appropriate name such as BookObjectBO for
your business object, and select Finish.  Add
the appropriate fields to your business object to fully describe it,
and save.
2. You will now need to create a JMS data binding that would
map the BookObject class to the business object BookObjectBO created
in step 1. The data binding implementation must implement com.ibm.websphere.sca.jms.data.JMSDataBinding.
The skeleton of such a class is shown as follows: import javax.jms.JMSException;
import javax.jms.Message;

import com.ibm.websphere.sca.jms.data.JMSDataBinding;
import commonj.connector.runtime.DataBindingException;
import commonj.sdo.DataObject;

public class BookObjectDataBinding implements JMSDataBinding {

public int getMessageType() {return 0;}
public void read(Message arg0) throws JMSException {}
public void write(Message arg0) throws JMSException {}
public boolean isBusinessException() {return false;}
public void setBusinessException(boolean arg0) {}
public DataObject getDataObject() throws DataBindingException {return null;}
public void setDataObject(DataObject arg0) throws DataBindingException {}
}
3. You will now need to provide the implementation. For a
detailed description of the methods, see Overview of JMS, MQ JMS and generic JMS bindings. The following implementation
of the getMessageType(), read(Message arg0) and write(Message arg0)
could be used to map between the BookObjectBO business
object and the BookObject class. 	public void read(Message message) throws JMSException {
		//		 Get the payload of the JMS Object message
		BookObject bookObj = (BookObject) ((ObjectMessage) message).getObject();

		//		 Create the SDO
		com.ibm.websphere.sca.ServiceManager serviceManager = new com.ibm.websphere.sca.ServiceManager();
		com.ibm.websphere.bo.BOFactory factory = (com.ibm.websphere.bo.BOFactory) serviceManager
				.locateService("com/ibm/websphere/bo/BOFactory");
		DataObject bookBO = factory.create("http://BB\_Books\_SCA",
				"BookObjectBO");

		bookBO.setString("ISDN", bookObj.getISDN());
		bookBO.setString("Author", bookObj.getAuthor());
		bookBO.setString("Title", bookObj.getTitle());
		bookBO.setFloat("Price", bookObj.getPrice());

		try {
			//		 Set the data object
			setDataObject(bookBO);
		} catch (DataBindingException e) {
			throw new JMSException(e.getLocalizedMessage());
		}
	}

	public void write(Message message) throws JMSException {
		try {
			//		 Get the data object
			DataObject bookBO = getDataObject();

			//		 Create the Book Object
			BookObject bookObj = new BookObject();
			bookObj.setISDN(bookBO.getString("ISDN"));
			bookObj.setAuthor(bookBO.getString("Author"));
			bookObj.setTitle(bookBO.getString("Title"));
			bookObj.setPrice(bookBO.getFloat("Price"));

			//		 Set the payload of the JMS Object Message
			((ObjectMessage) message).setObject(bookObj);

		} catch (DataBindingException e) {
			throw new JMSException(e.getLocalizedMessage());
		}
	}

## Related tasks

- Creating a JMS import to communicate with a JMS client
- Creating a JMS export to communicate with a JMS client
- Creating a JMS client to receive messages from a JMS import
- Creating an import from an export using a JMS binding