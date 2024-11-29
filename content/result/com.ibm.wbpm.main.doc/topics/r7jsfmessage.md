<!-- image -->

# Message component: Tag definitions

The Message component consists of the JSF component
tag: bpe:form.

## Component class

## Example syntax

```
<bpe:form model="#{TaskInstanceDetailsBean.inputMessageWrapper}"
          simplification="true" readOnly="true"
          styleClass4table="messageData"
          styleClass4output="messageDataOutput">
</bpe:form>
```

## Tag attributes

| Attribute               | Required   | Description                                                                                                                                                        |
|-------------------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                      | no         | The JavaServer Faces ID of the component.                                                                                                                          |
| model                   | yes        | A value binding expression that refers to either a commonj.sdo.DataObject object or a com.ibm.bpc.clientcore.MessageWrapper object.                                |
| readOnly                | no         | If this attribute is set to true, a read-only form is rendered. By default, this attribute is set to false.                                                        |
| simplification          | no         | If this attribute is set to true, properties that contain simple types and have a cardinality of zero or one are shown. By default, this attribute is set to true. |
| style4validinput        | no         | The cascading style sheet (CSS) style for rendering input that is valid.                                                                                           |
| style4invalidinput      | no         | The CSS style for rendering input that is not valid.                                                                                                               |
| styleClass4invalidInput | no         | The CSS style class name for rendering input that is not valid.                                                                                                    |
| styleClass4output       | no         | The CSS style class name for rendering the output elements.                                                                                                        |
| styleClass4table        | no         | The class name of the CSS table style for rendering the tables rendered by the message component.                                                                  |
| styleClass4validInput   | no         | The CSS style class name for rendering input that is valid.                                                                                                        |