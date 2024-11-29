<!-- image -->

# Handling exceptions

A variety of problems can occur when a data handler or data binding
is called by your binding. For example, a data handler might
receive a message that has a corrupted payload, or it might try to
read a message that has an incorrect format.

The way your binding handles such an exception is determined by
how you implement the data handler or data binding. The recommended
behavior is that you design your data binding to throw a DataBindingException.

- If the mediation flow is configured to be transactional, the JMS
message , by default, is stored in the Failed Event Manager
for manual replay or deletion. Note: You can change the recovery
mode on the binding so that the message is rolled back instead of
being stored in the Failed Event Manager.
- If the mediation flow is not transactional, the exception is logged
and the message is lost.

The situation is similar for a data handler. Since the data handler
is invoked by the data binding, any data handler exception is wrapped
into a data binding exception. Therefore a DataHandlerException is
reported to you as a DataBindingException.