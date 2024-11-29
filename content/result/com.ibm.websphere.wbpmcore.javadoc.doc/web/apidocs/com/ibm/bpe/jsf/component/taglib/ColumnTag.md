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

## Class ColumnTag

- java.lang.Object
    - javax.servlet.jsp.tagext.TagSupport
        - com.ibm.bpe.jsf.component.taglib.ColumnTag

- All Implemented Interfaces:
java.io.Serializable, javax.servlet.jsp.tagext.IterationTag, javax.servlet.jsp.tagext.JspTag, javax.servlet.jsp.tagext.Tag

public class ColumnTag
extends javax.servlet.jsp.tagext.TagSupport
This class is used to configure a column of the List Component.
 The list itself is specified by the bpe:list ListTag tag. Each bpe:column tag must be enclosed within a bpe:list tag.
 If the model used provides metadata, the label and converter information are retrieved from the model,
 unless they are explicitly set on the tag.
 
 

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

ColumnTag()

- Method Summary Methods Modifier and Type Method and Description int doStartTag () java.lang.String getAction () Returns the action that is triggered by clicking on the link in this column. java.lang.String getConverterID () Returns the explicitly set converter ID. java.lang.String getEscape () Returns the escape attribute. java.lang.String getLabel () Returns the explicitly set label of the column header. java.lang.String getName () Returns the name of the property that is displayed in the column. java.lang.String getStyleClass () Returns the CSS style used to render the column content. void release () void setAction (java.lang.String action) Sets the action that is triggered by clicking on the link in this column. void setConverterID (java.lang.String converterId) Sets the converter ID for the column. void setEscape (java.lang.String escape) Sets the escape attribute. void setLabel (java.lang.String label) Sets the label of the column header. void setName (java.lang.String name) Sets the name of the property that is displayed in the column. void setStyleClass (java.lang.String cssStyle) Sets the CSS style used to render the column content.

### Method Summary

| Modifier and Type   | Method and Description                                                                                       |
|---------------------|--------------------------------------------------------------------------------------------------------------|
| int                 | doStartTag()                                                                                                 |
| java.lang.String    | getAction() Returns the action that is triggered by clicking on the link in this column.                     |
| java.lang.String    | getConverterID() Returns the explicitly set converter ID.                                                    |
| java.lang.String    | getEscape() Returns the escape attribute.                                                                    |
| java.lang.String    | getLabel() Returns the explicitly set label of the column header.                                            |
| java.lang.String    | getName() Returns the name of the property that is displayed in the column.                                  |
| java.lang.String    | getStyleClass() Returns the CSS style used to render the column content.                                     |
| void                | release()                                                                                                    |
| void                | setAction(java.lang.String action) Sets the action that is triggered by clicking on the link in this column. |
| void                | setConverterID(java.lang.String converterId) Sets the converter ID for the column.                           |
| void                | setEscape(java.lang.String escape) Sets the escape attribute.                                                |
| void                | setLabel(java.lang.String label) Sets the label of the column header.                                        |
| void                | setName(java.lang.String name) Sets the name of the property that is displayed in the column.                |
| void                | setStyleClass(java.lang.String cssStyle) Sets the CSS style used to render the column content.               |

    - Methods inherited from class javax.servlet.jsp.tagext.TagSupport
doAfterBody, doEndTag, findAncestorWithClass, getId, getParent, getValue, getValues, removeValue, setId, setPageContext, setParent, setValue
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait