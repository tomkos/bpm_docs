<!-- image -->

# Checking the response message for business exceptions in JMS
client applications (deprecated)

## About this task

For example:

## Example

```
// receive response message
Message receivedMessage = ((JmsProxy) getToBeInvokedUponObject().receiveMessage();
String strResponse = ((TextMessage) receivedMessage).getText();
	
if (receivedMessage.getStringProperty("IsBusinessException") {
		// strResponse is a bussiness fault 
		// any api can end w/a processFaultMsg 
		// the call api also w/a businessFaultMsg
	}
else {
		// strResponse is the output message 
}
```