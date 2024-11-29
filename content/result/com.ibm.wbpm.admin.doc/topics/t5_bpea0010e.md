<!-- image -->

# Unexpected exception during execution (Message: CWWBA0010E)

## Resolution

1. If the systemout.log file contains javax.jms.JMSException: MQJMS2005: failed to create MQQueueManager, start the queue
manager.
2. Make sure that the database administrator password stored in the
Business Process Choreographer configuration matches the one set in
the database.