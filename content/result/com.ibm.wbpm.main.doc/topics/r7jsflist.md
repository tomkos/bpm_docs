<!-- image -->

# List component: Tag definitions

The List component consists of the JSF component
tags: bpe:list and bpe:column. The bpe:column tag
is a subelement of the bpe:list tag.

## Component class

## Example syntax

```
<bpe:list model="#{ProcessTemplateList}">
          rows="20"
          styleClass="list"
          headerStyleClass="listHeader"
          rowClasses="normal"> 

    <bpe:column name="name" action="processTemplateDetails"/>
    <bpe:column name="validFromTime"/>
    <bpe:column name="executionMode" label="Execution mode"/>
    <bpe:column name="state" converterID="my.state.converter"/>
    <bpe:column name="autoDelete"/>
    <bpe:column name="description"/>

</bpe:list>
```

## Tag attributes

The body of the bpe:list tag
can contain only bpe:column tags. When the table is rendered,
the List component iterates over the list of application
objects and renders all of the columns for each of the objects.

| Attribute        | Required   | Description                                                                                                                                                                                                   |
|------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| buttonStyleClass | no         | The cascading style sheet (CSS) style class for rendering the buttons in the footer area.                                                                                                                     |
| cellStyleClass   | no         | The CSS style class for rendering individual table cells.                                                                                                                                                     |
| checkbox         | no         | Determines whether the check box for selecting multiple items is rendered. The attribute has a value of either true or false. If the value is set to true, the check box column is rendered.                  |
| headerStyleClass | no         | The CSS style class for rendering the table header.                                                                                                                                                           |
| model            | yes        | A value binding for a managed bean of the com.ibm.bpe.jsf.handler.BPCListHandler class.                                                                                                                       |
| rows             | no         | The number of rows that are shown on a page. If the number of items exceeds the number of rows, paging buttons are displayed at the end of the table. Value expressions are not supported for this attribute. |
| rowClasses       | no         | The CSS style class for rendering the rows in the table.                                                                                                                                                      |
| selectAll        | no         | If this attribute is set to true, all of the items in the list are selected by default.                                                                                                                       |
| styleClass       | no         | The CSS style class for rendering the overall table containing titles, rows, and paging buttons.                                                                                                              |

| Attribute    | Required   | Description                                                                                                                                                                                                                                                     |
|--------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| action       | no         | If this attribute is specified, a link is rendered in the column. Either a JavaServer Faces action method or the Faces navigation target is triggered when this link is clicked. A JavaServer Faces action method has the following signature: String method(). |
| converterID  | no         | The Faces converter ID that is used for converting the property value. If this attribute is not set, any Faces converter ID that is provided by the model for this property is used.                                                                            |
| label        | no         | A literal or value binding expression that is used as a label for the header of the column or the cell of the table header row. If this attribute is not set, any label that is provided by the model for this property is used.                                |
| name         | yes        | The name of the property that is displayed in this column.                                                                                                                                                                                                      |