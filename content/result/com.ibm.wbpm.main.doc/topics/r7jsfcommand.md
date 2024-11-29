<!-- image -->

# CommandBar component: Tag definitions

The CommandBar component consists of the JSF
component tags: bpe:commandbar and bpe:command.
The bpe:command tag is a subelement of the bpe:commandbar tag.

## Component class

## Example syntax

```
<bpe:commandbar model="#{TaskInstanceList}">

    <bpe:command
       commandID="Work on"
       label="Work on..."
       commandClass="com.ibm.bpc.explorer.command.WorkOnTaskCommand"
       context="#{TaskInstanceDetailsBean}"/>

    <bpe:command
       commandID="Cancel"
       label="Cancel"
       commandClass="com.ibm.task.clientmodel.command.CancelClaimTaskCommand"
       context="#{TaskInstanceList}"/>

</bpe:commandbar>
```

## Tag attributes

| Attribute        | Required   | Description                                                                                                                                                                                                                                                                                                                                                |
|------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| buttonStyleClass | no         | The cascading style sheet (CSS) style class that is used for rendering the buttons in the command bar.                                                                                                                                                                                                                                                     |
| id               | no         | The JavaServer Faces ID of the component.                                                                                                                                                                                                                                                                                                                  |
| model            | yes        | A value binding expression to a managed bean that implements the ItemProvider interface. This managed bean is usually the com.ibm.bpe.jsf.handler.BPCListHandler class or the com.ibm.bpe.jsf.handler.BPCDetailsHandler class that is used by the List component or Details component in the same JavaServer Pages (JSP) file as the CommandBar component. |
| styleClass       | no         | The CSS style class that is used for rendering the command bar.                                                                                                                                                                                                                                                                                            |

| Attribute    | Required   | Description                                                                                                                                                                                                                                                                                                                               |
|--------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| action       | no         | A JavaServer Faces action method or the Faces navigation target that is to be triggered by the command button. The navigation target that is returned by the action overwrites all other navigation rules. The action is called when either an exception is not thrown or an ErrorsInCommandException exception is thrown by the command. |
| commandClass | no         | The name of the command class. An instance of the class is created by the CommandBar component and run if the command button is selected.                                                                                                                                                                                                 |
| commandID    | yes        | The ID of the command.                                                                                                                                                                                                                                                                                                                    |
| context      | no         | An object that provides context for commands that are specified using the commandClass attribute. The context object is retrieved when the command bar is first accessed.                                                                                                                                                                 |
| immediate    | no         | Specifies when the command is triggered. If the value of this attribute is true, the command is triggered before the input of the page is processed. The default is false.                                                                                                                                                                |
| label        | yes        | The label of the button that is rendered in the command bar.                                                                                                                                                                                                                                                                              |
| rendered     | no         | Determines whether a button is rendered. The value of the attribute can be either a Boolean value or a value expression.                                                                                                                                                                                                                  |
| styleClass   | no         | The CSS style class that is used for rendering the button. This style overrides the button style defined for the command bar.                                                                                                                                                                                                             |