<!-- image -->

# Details component: Tag definitions

The Details component consists of the JSF component
tags: bpe:details and bpe:property. The bpe:property tag
is a subelement of the bpe:details tag.

## Component class

## Example syntax

```
<bpe:details model="#{MyActivityDetails}">
    <bpe:property name="name"/>
    <bpe:property name="owner"/>
    <bpe:property name="activated"/>
</bpe:details>
```

```
<bpe:details model="#{MyActivityDetails}" style="style" styleClass="cssStyle">
             style="style"
             styleClass="cssStyle"
</bpe:details>
```

## Tag attributes

Use bpe:property tags
to specify both the subset of attributes that are shown and the order in which
these attributes are shown. If the details tag does not contain any attribute
tags, it renders all of the available attributes of the model object.

| Attribute     | Required   | Description                                                                                            |
|---------------|------------|--------------------------------------------------------------------------------------------------------|
| columnClasses | no         | A list of cascading style sheet style (CSS) style classes, separated by commas, for rendering columns. |
| id            | no         | The JavaServer Faces ID of the component.                                                              |
| model         | yes        | A value binding for a managed bean of the com.ibm.bpe.jsf.handler.BPCDetailsHandler class.             |
| rowClasses    | no         | A list of CSS style classes, separated by commas, for rendering rows.                                  |
| styleClass    | no         | The CSS class that is used for rendering the HTML element.                                             |

| Attribute    | Required   | Description                                                                                                                                 |
|--------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| converterID  | no         | The ID used to register the converter in the JavaServer Faces (JSF) configuration file.                                                     |
| label        | no         | The label for the property. If this attribute is not set, a default label is provided by the client model class.                            |
| name         | yes        | The name of the property to be displayed. This name must correspond to a named property as defined in the corresponding client model class. |