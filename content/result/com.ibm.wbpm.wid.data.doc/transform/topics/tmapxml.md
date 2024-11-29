<!-- image -->

# Transforming data using XML maps

## About this task

- Creating a new XML map

An XML map defines mappings between input and output business objects or service message objects. XSL style sheets generated from the XML maps are used at run time to transform the data. XML maps are used with Mapping primitives in mediation flows.
- Editing an XML map

After you create an XML map, you can edit it using the XML map editor.
- Functions and transforms

In the XML map editor, you map elements and attributes between source and target business objects or messages, and then you apply transform logic that specifies the action to be performed on the source data. The result of the transform is stored in the target element. The XML map editor provides ready-made transforms that you can use to process input data. You can also use XSLT or XPath functions.
- XML Map: Using user-defined variables

You can define your own variables and use them within transformations in an XML map.
- Choosing a transform for an XML map

The XML map editor provides many types of transforms that perform different actions on input data and move the result to the output element. Choose the appropriate transform depending on the result you want to achieve.
- Automatically mapping elements

The XML map editor provides an auto map function to facilitate mapping of inputs and outputs.
- Mapping substitutable elements using an XML map

A substitution group is a construct in XML Schema (XSD) that allows a set of elements to be substituted for a head element. An XML instance can contain only one of the elements in the substitution group. You can map the elements of substitution groups in an XML map.
- Mapping array elements using an XML map

The XML map editor provides transforms that allow you to iterate over an array of elements, choose the indexes of the elements in the array that you want to transform, and place the result in an output array or single element.
- Creating a custom lookup

In the XML map editor, you can look up a value from a file by using a key from the input element and populate the target element with the retrieved value. In addition to the lookups provided by the map editor, you can contribute lookup engines for your own custom file types.
- XML mapping tutorial

Learn how to quickly create robust and well-organized XML maps, and how to test and debug maps to make problem determination easier. Also learn advanced techniques for creating XML maps, including mapping arrays and other complex structures, and performing custom transforms.
- XML mapping examples

By looking at XML mapping examples, learn how to create XML-to-XML maps.
- Testing XML Maps

You can quickly test an XML map while you are creating it in the XML map editor. Alternatively you can test already completed maps in the unit test environment; however they are not run on a server.
- XML map: Troubleshooting and limitations

Limitations and troubleshooting tips for XML maps and the XML map editor.