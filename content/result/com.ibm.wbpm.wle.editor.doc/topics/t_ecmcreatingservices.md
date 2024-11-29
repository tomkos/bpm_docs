# Creating attached services

## About this task

It is generally recommended that you create an attached
service at the same time as the other required components by following
the instructions in the topic Subscribing to document and folder events.
This is a simpler approach than creating each component on a stand-alone
basis and it automatically creates some resources that you would otherwise
need to create manually.

However, you can also create an attached
service on its own without any consideration for some of the other
components that are required to detect and respond to ECM events.
There are two kinds of attached service that you can create:

- If you want to create an attached service that will directly invoke
a content UCA without first querying the ECM server for additional
information, then you should create a general system service.
- If you want to create an attached service that will first query
the ECM server for additional information before determining whether
a UCA should be invoked, then you should create an integration
service.

Information about creating these two kinds of services is found in Building an Integration service and Building a General System service.