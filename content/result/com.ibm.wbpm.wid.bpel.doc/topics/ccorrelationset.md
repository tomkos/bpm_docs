<!-- image -->

# Correlation sets

A correlation set is made up of one or more properties that are
defined in a WSDL file. A property alias is a rule that tells Business
Process Choreographer how to map data from a message into a correlation
property. You can use correlation sets in invoke, receive, pick, and
reply activities to indicate which correlation sets occur in the messages
that are sent and received. The values of each correlation set uniquely
identify the process instance. This is true even if the process  instance
has already reached an end state, such as the finished state.

A correlation set is required if a process consists of more than
one receive or pick activity. The receive or pick activity that initiates
a new process instance does not necessarily need a correlation set.
The remaining receive or pick activities, however, need a correlation
set to uniquely identify the process instance to route the message
to.