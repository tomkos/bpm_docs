# Retrieving SOAP headers from an inbound request message

## Before you begin

## About this task

IBM® Business Process
Manager provides a system variable that you can use to retrieve SOAP
headers. SOAP headers found in inbound request messages are automatically
copied to the tw.system.header.soap.request system
variable. You can write code to retrieve those SOAP headers.

## Procedure

In this example, the code example
is retrieving a header named subscriptionInfo of
type SOAPHeader from the system variable tw.system.header.soap.request.
If the request message contains SOAP headers, this variable will be
initialized to contain them. If the request message does not contain
SOAP headers, this variable will be null.

```
log.info(">>>>>> Checking to see if the subscriptionInfo SOAP header was received in the request message...")

var subscriptionInfoHeader = null

if (tw.system.header.soap.request != null) {
    for (var i = 0; i < tw.system.header.soap.request.headers.listLength; i++) {
        // search for the subscriptionInfo header
        if (tw.system.header.soap.request.headers[i].name == "subscriptionInfo") {
           subscriptionInfoHeader = tw.system.header.soap.request.headers[i]
       }
   }
}

if (subscriptionInfoHeader != null) {
    log.info("Found the subscriptionInfo SOAP header!")
}
else {
    log.info("The subscriptionInfo SOAP header was not present in the request message.")
}
```

```
<ns1:subscriptionInfo xmlns:ns1="http://acme.com">1234-56-7890-fc3a</ns1:subscriptionInfo>
```

```
Found the subscriptionInfo SOAP header!
```