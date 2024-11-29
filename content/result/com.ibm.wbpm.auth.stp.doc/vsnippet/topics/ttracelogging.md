<!-- image -->

# Setting trace logging

## Procedure

To set and turn on trace logging, complete the following
steps:

1. See the Selecting a standard visual snippet topic for
information on the print to logger visual snippet.
2. On the server set the following: java.util.logging.Logger l = java.util.logging.Logger.getLogger("com.ibm.bpe.generated");
if(l.isLoggable(java.util.logging.Level.FINE))
{
	l.log(java.util.logging.Level.FINE, "This is a message");
}