- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class CommandTag

- java.lang.Object
    - javax.servlet.jsp.tagext.TagSupport
        - com.ibm.bpe.jsf.component.taglib.CommandTag

- All Implemented Interfaces:
java.io.Serializable, javax.servlet.jsp.tagext.IterationTag, javax.servlet.jsp.tagext.JspTag, javax.servlet.jsp.tagext.Tag

public class CommandTag
extends javax.servlet.jsp.tagext.TagSupport
This class is used to configure the commands displayed by the Command Bar component. The Command Bar
 itself is specified by the bpe:commandbar CommandBarTag tag. A bpe:command tag must be
 enclosed within a bpe:commandbar tag. Each command is represented as a button on the view.

  

See Also:Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String COPYRIGHT

### Field Summary

| Modifier and Type       | Field and Description   |
|-------------------------|-------------------------|
| static java.lang.String | COPYRIGHT               |

    - Fields inherited from class javax.servlet.jsp.tagext.TagSupport
id, pageContext
    - Fields inherited from interface javax.servlet.jsp.tagext.IterationTag
EVAL\_BODY\_AGAIN
    - Fields inherited from interface javax.servlet.jsp.tagext.Tag
EVAL\_BODY\_INCLUDE, EVAL\_PAGE, SKIP\_BODY, SKIP\_PAGE

- Constructor Summary

Constructors 

Constructor and Description

CommandTag()

- Method Summary Methods Modifier and Type Method and Description int doStartTag () java.lang.String getAction () Returns the Action being specified. java.lang.String getActionListener () Returns the Action Listener being specified. java.lang.String getCommandClass () Returns the class name of the command. java.lang.String getCommandID () Returns the command ID that has been specified. java.lang.String getContext () Returns the Value Binding pointing to a Context Object, if specified. java.lang.String getErrorTarget () Returns the navigation target that is used for error conditions. java.lang.String getImmediate () Returns a boolean value that defines if this component is activated by the user, notifications should be delivered to interested listeners and actions immediately (that is, during Apply Request Values phase) rather than waiting until Invoke Application phase. java.lang.String getLabel () Returns the button's label. java.lang.String getRendered () Returns a boolean value or value expression that defines whether or not the command button is to be rendered. java.lang.String getStyleClass () Returns the CSS style used to render the h:commandButton tag. void release () void setAction (java.lang.String facesAction) Sets a Faces Action for the command button. void setActionListener (java.lang.String facesActionListener) Sets a Faces Action Listener for the command button. void setCommandClass (java.lang.String commandClassName) Sets the class name of the command that is triggered by the rendered button. void setCommandID (java.lang.String commandID) Sets the command ID of the command. void setContext (java.lang.String contextObject) Sets the Value Binding Expression that points to a Context object. void setErrorTarget (java.lang.String errorTarget) Sets the navigation target that is used for error conditions. void setImmediate (java.lang.String immediate) Specifies a boolean value that defines if this component is activated by the user, notifications should be delivered to interested listeners and actions immediately (that is, during Apply Request Values phase) rather than waiting until Invoke Application phase. void setLabel (java.lang.String label) Sets the label of the command button. void setRendered (java.lang.String rendered) Specifies a boolean value or value expression that defines whether or not the command button is to be rendered. void setStyleClass (java.lang.String cssStyle) Sets the CSS style used to render the h:commandButton tag.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                                                                                                                                                                               |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int                 | doStartTag()                                                                                                                                                                                                                                                                                                         |
| java.lang.String    | getAction() Returns the Action being specified.                                                                                                                                                                                                                                                                      |
| java.lang.String    | getActionListener() Returns the Action Listener being specified.                                                                                                                                                                                                                                                     |
| java.lang.String    | getCommandClass() Returns the class name of the command.                                                                                                                                                                                                                                                             |
| java.lang.String    | getCommandID() Returns the command ID that has been specified.                                                                                                                                                                                                                                                       |
| java.lang.String    | getContext() Returns the Value Binding pointing to a Context Object, if specified.                                                                                                                                                                                                                                   |
| java.lang.String    | getErrorTarget() Returns the navigation target that is used for error conditions.                                                                                                                                                                                                                                    |
| java.lang.String    | getImmediate() Returns a boolean value that defines  if this component is activated by the user,  notifications should be delivered to   interested listeners  and actions immediately (that is, during Apply Request Values phase)  rather than waiting until Invoke Application phase.                             |
| java.lang.String    | getLabel() Returns the button's label.                                                                                                                                                                                                                                                                               |
| java.lang.String    | getRendered() Returns a boolean value or value expression that defines whether or not the  command button is to be rendered.                                                                                                                                                                                         |
| java.lang.String    | getStyleClass() Returns the CSS style used to render the h:commandButton tag.                                                                                                                                                                                                                                        |
| void                | release()                                                                                                                                                                                                                                                                                                            |
| void                | setAction(java.lang.String facesAction) Sets a Faces Action for the command button.                                                                                                                                                                                                                                  |
| void                | setActionListener(java.lang.String facesActionListener) Sets a Faces Action Listener for the command button.                                                                                                                                                                                                         |
| void                | setCommandClass(java.lang.String commandClassName) Sets the class name of the command that is triggered by the rendered button.                                                                                                                                                                                      |
| void                | setCommandID(java.lang.String commandID) Sets the command ID of the command.                                                                                                                                                                                                                                         |
| void                | setContext(java.lang.String contextObject) Sets the Value Binding Expression that points to a Context object.                                                                                                                                                                                                        |
| void                | setErrorTarget(java.lang.String errorTarget) Sets the navigation target that is used for error conditions.                                                                                                                                                                                                           |
| void                | setImmediate(java.lang.String immediate) Specifies a boolean value that defines  if this component is activated by the user,  notifications should be delivered to   interested listeners  and actions immediately (that is, during Apply Request Values phase)  rather than waiting until Invoke Application phase. |
| void                | setLabel(java.lang.String label) Sets the label of the command button.                                                                                                                                                                                                                                               |
| void                | setRendered(java.lang.String rendered) Specifies a boolean value or value expression that defines whether or not the  command button is to be rendered.                                                                                                                                                              |
| void                | setStyleClass(java.lang.String cssStyle) Sets the CSS style used to render the h:commandButton tag.                                                                                                                                                                                                                  |

    - Methods inherited from class javax.servlet.jsp.tagext.TagSupport
doAfterBody, doEndTag, findAncestorWithClass, getId, getParent, getValue, getValues, removeValue, setId, setPageContext, setParent, setValue
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait