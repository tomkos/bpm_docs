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

## Class PropertyTag

- java.lang.Object
    - javax.servlet.jsp.tagext.TagSupport
        - com.ibm.bpe.jsf.component.taglib.PropertyTag

- All Implemented Interfaces:
java.io.Serializable, javax.servlet.jsp.tagext.IterationTag, javax.servlet.jsp.tagext.JspTag, javax.servlet.jsp.tagext.Tag

public class PropertyTag
extends javax.servlet.jsp.tagext.TagSupport
This class is used to configure a property displayed by the Details Component.
 The details panel itself is specified by the bpe:details DetailsTag tag. A bpe:property tag must be enclosed within
 a bpe:details tag. If the model used provides meta data, the label and converter information is
 retrieved from the model, unless it is explicitly set on the tag.
 
 

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

PropertyTag()

- Method Summary Methods Modifier and Type Method and Description int doStartTag () java.lang.String getConverterID () Returns the explicitly set converter ID. java.lang.String getEscapeValue () java.lang.String getLabel () Returns the explicitly set label of the column header. java.lang.String getName () Returns the name of the property that is displayed in the column. java.lang.String getNotRenderedIfNoValue () java.lang.String getRendered () Returns the render information. void release () void setConverterID (java.lang.String converterID) Sets the converter ID for the column. void setEscapeValue (java.lang.String escapeValue) void setLabel (java.lang.String label) Sets the label of the column header. void setName (java.lang.String name) Sets the name of the property that is displayed in the column. void setNotRenderedIfNoValue (java.lang.String notRenderedIfNoValue) void setRendered (java.lang.String rendered) Sets the render information for the property.

### Method Summary

| Modifier and Type   | Method and Description                                                                        |
|---------------------|-----------------------------------------------------------------------------------------------|
| int                 | doStartTag()                                                                                  |
| java.lang.String    | getConverterID() Returns the explicitly set converter ID.                                     |
| java.lang.String    | getEscapeValue()                                                                              |
| java.lang.String    | getLabel() Returns the explicitly set label of the column header.                             |
| java.lang.String    | getName() Returns the name of the property that is displayed in the column.                   |
| java.lang.String    | getNotRenderedIfNoValue()                                                                     |
| java.lang.String    | getRendered() Returns the render information.                                                 |
| void                | release()                                                                                     |
| void                | setConverterID(java.lang.String converterID) Sets the converter ID for the column.            |
| void                | setEscapeValue(java.lang.String escapeValue)                                                  |
| void                | setLabel(java.lang.String label) Sets the label of the column header.                         |
| void                | setName(java.lang.String name) Sets the name of the property that is displayed in the column. |
| void                | setNotRenderedIfNoValue(java.lang.String notRenderedIfNoValue)                                |
| void                | setRendered(java.lang.String rendered) Sets the render information for the property.          |

    - Methods inherited from class javax.servlet.jsp.tagext.TagSupport
doAfterBody, doEndTag, findAncestorWithClass, getId, getParent, getValue, getValues, removeValue, setId, setPageContext, setParent, setValue
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait