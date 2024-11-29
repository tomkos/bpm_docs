<!-- image -->

# Creating custom maps using <any> elements

## About this task

- Mapping <any> elements to a target using condition on source

If a source and target schema contain the <any> element, the target business object <any> element is set dependent on a condition on the source. Before the custom code snippet is invoked, the source business object must be populated with input data.
- Mapping multiple <any> elements

In this map the business objects have more than one <any> element in the schema definition.
- Mapping a concrete type to <any> target element

You can map a concrete type to a target <any> element.
- Mapping xsd:any[]

A business object which has an xsd:any[] will have the maxOccurs = "unbounded"  in the type declaration for the <any> element. This would imply that the <any> element can hold multiple values within the same property that was used to define it.