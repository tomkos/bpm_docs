<!-- image -->

# How commands are processed

These buttons trigger functions that act on the objects that are returned
by a com.ibm.bpe.jsf.handler.ItemProvider interface, such
as the BPCListHandler class, or the BPCDetailsHandler class.
The CommandBar component uses the item provider that is
defined by the value of the model attribute in the bpe:commandbar tag.

1. The CommandBar component identifies the implementation
of the com.ibm.bpc.clientcore.Command interface that is
specified for the button that generated the event.
2. If the model associated with the CommandBar component
implements the com.ibm.bpe.jsf.handler.ErrorHandler interface,
the clearErrorMap method is invoked to remove error messages
from previous events.
3. The getSelectedItems method of the ItemProvider interface
is called. The list of items that is returned is passed to the execute method
of the command, and the command is invoked.
4. The CommandBar component determines the JavaServer
Faces (JSF) navigation target. If an action attribute
is not specified in the bpe:commandbar tag, the return value
of the execute method specifies the navigation target.
If the action attribute is set to a JSF method binding,
the string returned by the method is interpreted as the navigation target.
The action attribute can also specify an explicit navigation
target.