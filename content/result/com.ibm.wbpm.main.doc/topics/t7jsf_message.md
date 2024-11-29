<!-- image -->

# Adding the Message component to a JSF application

## About this task

If the message type is a primitive type, a label and an
input field are rendered. If the message type is a data object, the
component traverses the object and renders the elements within the
object.

## Procedure

1. Add the Message component to the JavaServer
Pages (JSP) file. Add the bpe:form tag
to the <h:form> tag. The bpe:form tag
must include a model attribute.
The
following example shows how to add a Message component.

<h:form>

   <h:outputText value="Input Message" /> 
   <bpe:form model="#{MyHandler.inputMessage}" readOnly="true" />

   <h:outputText value="Output Message" />  
   <bpe:form model="#{MyHandler.outputMessage}" /> 

</h:form>The model attribute
of the Message component refers to a com.ibm.bpc.clientcore.MessageWrapper
object. This wrapper object wraps either a Service Data Object (SDO)
object or a Java™ primitive type, for example, int or boolean.
In the example, the message is provided by a property of the MyHandler
managed bean.
2. Configure the managed bean referred to in the bpe:form tag.
The following example shows how to add the MyHandler managed
bean to the configuration file.
<managed-bean>
<managed-bean-name>MyHandler</managed-bean-name>
<managed-bean-class>com.ibm.bpe.sample.jsf.MyHandler</managed-bean-class>
<managed-bean-scope>session</managed-bean-scope>

   <managed-property>
      <property-name>type</property-name>
      <value>com.ibm.task.clientmodel.bean.TaskInstanceBean</value>
   </managed-property>

</managed-bean>
3. Add the custom code to the JSF application. The
following example shows how to implement input and output messages.
public class MyHandler implements ItemListener {

  private TaskInstanceBean taskBean;
  private MessageWrapper inputMessage, outputMessage 

  /* Listener method, for example, when a task instance was selected in a list handler.
   * Ensure that the handler is registered in the faces-config.xml or manually. 
   */ 
  public void itemChanged(Object item) {
    if( item instanceof TaskInstanceBean ) {
        taskBean = (TaskInstanceBean) item ;
    }
  }

  /* Get the input message wrapper
   */
  public MessageWrapper getInputMessage() {
    try{
        inputMessage = taskBean.getInputMessageWrapper() ;
    }
    catch( Exception e ) {
        ;       //...ignore errors for simplicity
    }
    return inputMessage;
  }

  /* Get the output message wrapper
   */
  public MessageWrapper getOutputMessage() {
    // Retrieve the message from the bean. If there is no message, create
    // one if the task has been claimed by the user. Ensure that only 
    // potential owners or owners can manipulate the output message.
    try{
        outputMessage = taskBean.getOutputMessageWrapper();
        if( outputMessage == null 
         && taskBean.getState() == TaskInstanceBean.STATE\_CLAIMED ) { 
            HumanTaskManagerService htm = getHumanTaskManagerService();
            outputMessage = new MessageWrapperImpl();
            outputMessage.setMessage(   
               htm.createOutputMessage( taskBean.getID() ).getObject() 
            );
         }
    }
    catch( Exception e ) { 
        ;       //...ignore errors for simplicity
    }
    return outputMessage
  }
}

     The MyHandler managed bean implements
the com.ibm.jsf.handler.ItemListener interface
so that it can register itself as an item listener to list handlers.
When the user clicks an item in the list, the MyHandler bean is notified
in its itemChanged( Object item ) method about
the selected item. The handler checks the item type and then stores
a reference to the associated TaskInstanceBean object. To use
this interface, add an entry to the itemListener list in the appropriate
list handler in the faces-config.xml file.
The
MyHandler bean provides the getInputMessage and getOutputMessage methods.
Both of these methods return a MessageWrapper object. The methods
delegate the calls to the referenced task instance bean. If the task
instance bean returns null, for example, because a message is not
set, the handler creates and stores a new, empty message. The Message component
displays the messages provided by the MyHandler bean.

## Results

- Message component: Tag definitions

The Business Process Choreographer Explorer Message component renders commonj.sdo.DataObject objects and primitive types, such as integers and strings, in a JavaServer Faces (JSF) application.