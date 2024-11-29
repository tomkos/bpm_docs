<!-- image -->

# Accessing the Business Process Choreographer JMS API (deprecated)

## About this task

The following example
assumes that the JMS client is executed in a managed environment (EJB,
application client, or web client container).

## Procedure

1. Create a connection to the BPC.cellname.Bus.
No preconfigured connection factory exists for a client application's
requests: a client application can either use the JMS API's ReplyConnectionFactory
or create its own connection factory, in which case it can use Java
Naming and Directory Interface (JNDI) lookup to retrieve the connection
factory. The JNDI-lookup name must be the same as the name specified
when configuring the Business Process Choreographer's external request
queue. The following example assumes the client application creates
its own connection factory named "jms/clientCF". //Obtain the default initial JNDI context.
Context initialContext = new InitialContext();
    
// Look up the connection factory.
// Create a connection factory that connects to the BPC bus.
// Call it, for example, "jms/clientCF". 
// Also configure an appropriate authentication alias.
ConnectionFactory connectionFactory = 
            (ConnectionFactory)initialcontext.lookup("jms/clientCF");
            
// Create the connection.
Connection connection = connectionFactory.createConnection();
2. Create a session so that message producers and consumers
can be created. // Create a transaction session using auto-acknowledgment.
Session session = connection.createSession(true, Session.AUTO\_ACKNOWLEDGE);
3. Create a message producer to send messages. The
JNDI-lookup name must be the same as the name that was specified when
the external request queue for Business Process Choreographer was
configured.// Look up the destination of the Business Process Choreographer input queue to 
// send messages to.
Queue sendQueue = (Queue) initialcontext.lookup("jms/BFMJMSAPIQueue");
      
// Create a message producer.
MessageProducer producer = session.createProducer(sendQueue);
4. Create a message consumer to receive replies. The
JNDI-lookup name of the reply destination can specify a user-defined
destination, but it can also specify the default (Business Process
Choreographer-defined) reply destination jms/BFMJMSReplyQueue.
In both cases, the reply destination must lie on the BPC.<cellname>.Bus.// Look up the destination of the reply queue.
Queue  replyQueue = (Queue) initialcontext.lookup("jms/BFMJMSReplyQueue");

// Create a message consumer.
MessageConsumer consumer = session.createConsumer(replyQueue);
5. Send a message. // Start the connection. 
connection.start();
     
// Create a message - see the task descriptions for examples - and send it.
// This method is defined elsewhere ...
String payload = createXMLDocumentForRequest();    
TextMessage requestMessage = session.createTextMessage(payload);
     
// Set mandatory JMS header.
// targetFunctionName is the operation name of JMS API 
// (for example, getProcessTemplate, sendMessage)
requestMessage.setStringProperty("TargetFunctionName", targetFunctionName);

// Set the reply queue; this is mandatory if the replyQueue 
// is not the default queue (as it is in this example).
requestMessage.setJMSReplyTo(replyQueue); 

// Send the message.
producer.send(requestMessage);
     
// Get the message ID.
String jmsMessageID = requestMessage.getJMSMessageID();
     
session.commit();
6. Receive the reply. // Receive the reply message and analyse the reply.
TextMessage  replyMessage = (TextMessage) consumer.receive();
          
// Get the payload.
String payload = replyMessage.getText();

session.commit();
7. Close the connection and free the resources.  // Final housekeeping; free the resources.
session.close();
connection.close();Note:  It is not necessary to close
the connection after each transaction. Once a connection has been
started, any number of request and response messages can be exchanged
before the connection is closed. The example shows a simple case with
a single call within a single business method.

- (Deprecated) Structure of a Business Process Choreographer JMS message (deprecated)

The header and body of each JMS message must have a predefined structure.