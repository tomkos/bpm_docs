<!-- image -->

# Adding the CommandBar component to a JSF application

## About this task

## Procedure

1. Add the CommandBar component to the JavaServer
Pages (JSP) file. Add the bpe:commandbar tag
to the <h:form> tag. The bpe:commandbar tag
must contain a model attribute.
The following example
shows how to add a CommandBar component that provides refresh
and claim commands for a task instance list.
<h:form>

   <bpe:commandbar model="#{TaskInstanceList}">
      <bpe:command commandID="Refresh" >
                   action="#{TaskInstanceList.refreshList}"
                   label="Refresh"/>

      <bpe:command commandID="MyClaimCommand" >
                   label="Claim" >
                   commandClass="<customcode>"/> 
   </bpe:commandbar>

</h:form>The model attribute refers
to a managed bean. This bean must implement the ItemProvider interface
and provide the selected Java™ objects. The CommandBar component
is usually used with either the List component or the Details component
in the same JSP file. Generally, the model that is specified in the tag is
the same as the model that is specified in the List component
or Details component on the same page. So for the List component,
for example, the command acts on the selected items in the list. 
In
this example, the model attribute refers to the TaskInstanceList
managed bean. This bean provides the selected objects in the task instance
list. The bean must implement the ItemProvider interface.
This interface is implemented by the BPCListHandler class
and the BPCDetailsHandler class.
2. Optional: Configure the managed bean that is referred
to in the bpe:commandbar tag. If the CommandBar model attribute
refers to a managed bean that is already configured, for example, for a list
or details handler, no further configuration is required. If you use neither
the BPCListHandler class nor the BPCDetailsHandler class
for the model, you must refer to another object that has a class that implements
the ItemProvider interface.
3 Add the code that implements the custom commands to the JSF application. The following code snippet shows how to write a commandclass that implements the Command interface. This commandclass (MyClaimCommand) is referred to by the bpe:command tagin the JSP file. public class MyClaimCommand implements Command { public String execute(List selectedObjects) throws ClientException { if( selectedObjects != null && selectedObjects.size() > 0 ) { try { // Determine HumanTaskManagerService from an HTMConnection bean. // Configure the bean in the faces-config.xml for easy access // in the JSF application. FacesContext ctx = FacesContext.getCurrentInstance(); ValueBinding vb = ctx.getApplication().createValueBinding("{htmConnection}"); HTMConnection htmConnection = (HTMConnection) htmVB.getValue(ctx); HumanTaskManagerService htm = htmConnection.getHumanTaskManagerService(); Iterator iter = selectedObjects.iterator() ; while( iter.hasNext() ) { try { TaskInstanceBean task = (TaskInstanceBean) iter.next() ; TKIID tiid = task.getID() ; htm.claim( tiid ) ; task.setState( new Integer(TaskInstanceBean.STATE\_CLAIMED ) ) ; } catch( Exception e ) { ; // Error while iterating or claiming task instance. // Ignore for better understanding of the sample. } } } catch( Exception e ) { ; // Configuration or communication error. // Ignore for better understanding of the sample } } return null; } // Default implementations public boolean isMultiSelectEnabled() { return false; } public boolean[] isApplicable(List itemsOnList) {return null; } public void setContext(Object targetModel) {; // Not used here }} The command is processed in the following way:

The following code snippet shows how to write a command
class that implements the Command interface. This command
class (MyClaimCommand) is referred to by the bpe:command tag
in the JSP file.

```
public class MyClaimCommand implements Command {

  public String execute(List selectedObjects) throws ClientException {
	    if( selectedObjects != null && selectedObjects.size() > 0 ) {
  	     try {
         // Determine HumanTaskManagerService from an HTMConnection bean. 
         // Configure the bean in the faces-config.xml for easy access 
         // in the JSF application.
		       FacesContext ctx = FacesContext.getCurrentInstance();
         ValueBinding vb = 
           ctx.getApplication().createValueBinding("{htmConnection}");
         HTMConnection htmConnection = (HTMConnection) htmVB.getValue(ctx);
         HumanTaskManagerService htm = 
            htmConnection.getHumanTaskManagerService();

         Iterator iter = selectedObjects.iterator() ;			
         while( iter.hasNext() ) {
           try {
                TaskInstanceBean task = (TaskInstanceBean) iter.next() ;
                TKIID tiid = task.getID() ; 
						
                htm.claim( tiid ) ;
                task.setState( new Integer(TaskInstanceBean.STATE\_CLAIMED ) ) ;
						
           }
           catch( Exception e ) {
             ;			// Error while iterating or claiming task instance.
                  // Ignore for better understanding of the sample.
           }
         }
       }
       catch( Exception e ) {
         ; 	// Configuration or communication error.
           // Ignore for better understanding of the sample
       }
     }
     return null;
  }

 // Default implementations
 public boolean isMultiSelectEnabled() { return false; }
 public boolean[] isApplicable(List itemsOnList) {return null; }
 public void setContext(Object targetModel) {; // Not used here }
}
```

    1. A command is invoked when a user clicks the corresponding button in the
command bar. The CommandBar component retrieves the selected
items from the item provider that is specified in the model attribute
and passes the list of selected objects to the execute method
of the commandClass instance.
    2. The commandClass attribute
refers to a custom command implementation that implements the Command interface.
This means that the command must implement the public String execute(List
selectedObjects) throws ClientException method. The command returns
a result that is used to determine the next navigation rule for the JSF application.
    3. After the command completes, the CommandBar component
evaluates the action attribute. The action attribute
can be a static string or a method binding to a JSF action method with the public
String Method() signature. Use the action attribute
to override the outcome of a command class or to explicitly specify an outcome
for the navigation rules. The action attribute is not
processed if the command generates an exception other than an ErrorsInCommandException exception.
    4. If the commandClass attribute does not have a command
class specified, the action is immediately called. For example, for the refresh
command in the example, the JSF value expression #{TaskInstanceList.refreshList} is
called instead of a command.

## Results

- How commands are processed

Use the CommandBar component to add action buttons to your application. The component creates the buttons for the actions in the user interface and handles the events that are created when a button is clicked.
- CommandBar component: Tag definitions

The Business Process Choreographer Explorer CommandBar component displays a bar with buttons. These buttons operate on the object in a details view or the selected objects in a list.