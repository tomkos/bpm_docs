<!-- image -->

# Creating a JMS client to receive messages from a JMS import

## Before you begin

1. In your CustomerModule module, create an interface called CustomerProcess.
It should have a request-response operation getCustomerAddress with
an input, customer, and an output, customerResult. Both input and
output have a business object type, Customer.
2. Create a business object, Customer, with two fields, name and
address, both with a string type.
3. Create an import with a JMS binding using the following settings:
JMS messaging domain set to Point-to-Point and
data format transformation to Serialized Java Object (JMS).

## Procedure

1. With the SCA artifacts created and the JMS import binding
created, create a JMS client like the one in the next step to receive
messages from the import.
2. The SCA application simply sends a business object with
a name value to the JMS client and expects the client to return the
address for that name. For the JMS client, here is an illustration
of Message-Driven Bean (MDB) code that can interact with the SCA application.
public void onMessage(javax.jms.Message msg) {
	try {
		// Get the value 'TargetFunctionName'
		String targetFunctionNameValue = msg.getStringProperty("TargetFunctionName");
		
		// Base off the 'TargetFunctionName', call the appropriate method to
		// process
		if (targetFunctionNameValue.equals("getCustomerAddress")) {
			getCustomerAddress(msg);
		}
	} catch (JMSException e) {
		// Todo - handle exception
		e.printStackTrace();
	}
}

private void getCustomerAddress(javax.jms.Message msg) {
	try {
		
		// Cast the incoming JMS Message to TextMessage since the SOA
		// application
		// is using 'Business Object XML using JMS TextMessage' as the
		// serialization format
		TextMessage message = (TextMessage)msg;
		
		// Get the context in the TextMessage. It would be the XML
		// of the BusinessObject 'Customer'. For example:
		//
		// <?xml version="1.0" encoding="UTF-8"?>
		// <module:Customer xmlns:module="http://CustomerModule">
		// <name>Name1</name>
		// <address></address>
		// </module:Customer>
		
		String customerXML = message.getText();
		
		// Have code to process the XML
		// We will do a rudimentary processing of this by doing a String
		// operations
		
		// Get the value of the name element
		int beginIndex = customerXML.indexOf("<name>");
		int endIndex = customerXML.indexOf("</name>");
		String name = customerXML.substring(beginIndex + 6, endIndex);
		
		String newCustomerXML = null;
		if (name == null)
			newCustomerXML = customerXML;
		else if (name.equals("Nathan"))
			newCustomerXML = customerXML.replaceFirst("<address></address>", "<address>123 AppleValley Drive</address>");
		else 
			newCustomerXML = customerXML.replaceFirst("<address></address>", "<address>No such address</address>");
		
		// **** Send the response message ***
		// Lookup the Connection Factory JNDI
		Context context = new InitialContext();
		ConnectionFactory factory = (ConnectionFactory)context.lookup("java:comp/env/jms/CF");
		
		if (factory != null) {
			Connection connection = factory.createConnection();
			Session session = connection.createSession(false, Session.AUTO\_ACKNOWLEDGE);
			
			// Create the Message Producer using the Destination
			// specified in the sent message 'JMSReplyTo'
			MessageProducer producer = session.createProducer(msg.getJMSReplyTo());
			TextMessage responseMessage = session.createTextMessage(newCustomerXML);
			
			// Need to correlate the response message by specifying the
			// 'JMSCorrelationID
			// to the sent message 'JMSMessageID'
			responseMessage.setJMSCorrelationID(msg.getJMSMessageID());
			
			// Send the response message
			connection.start();
			producer.send(responseMessage);
			connection.close();
		}			
	} catch (JMSException e) {
		// Todo - handle exception
		e.printStackTrace();
	} catch (NamingException e) {
		// Todo - handle exception
		e.printStackTrace();
	} 
	
}

## Related tasks

- Creating a JMS import to communicate with a JMS client
- Creating a JMS export to communicate with a JMS client
- Creating an import from an export using a JMS binding
- Creating a user-defined JMS data binding