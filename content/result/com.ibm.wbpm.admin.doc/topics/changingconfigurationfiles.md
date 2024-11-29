# Creating a 100Custom.xml configuration file

## About this task

The settings that comprise the TeamWorksConfiguration.running.xml file
originate from the system XML files that contain the default values as well as from the
100Custom.xml configuration files. All XML files are read from the
configuration scope, but it is recommended that you only use files that are prefixed with
100Custom.xml for custom changes to the settings. You should not modify the
system XML files directly. The XML files are first loaded in alphabetic order and then in numeric
order, although it is best to avoid any conflicting changes in your custom settings to prevent the
order of the files being loaded from impacting the final settings.

The following XML snippet shows the high-level structure of a 100Custom.xml
change file. At most, only one occurrence of these XML tags should exist in a particular
100Custom.xml file:

```
<properties>
   <authoring-environment>
   <!-- Settings related to Process Designer -->
   </authoring-environment>
   <common>
   <!-- General IBM Business Automation Workflow settings -->
   </common>
   <server>
   <!-- Settings related to the run-time server -->
   </server>
   <web-pd>
   <!-- Settings related to the web Process Designer -->
   </web-pd>
   <event-manager>
   <!-- Settings related to Event Manager -->
   </event-manager>
   <performance-server>
  <!-- Settings related to Performance Data Warehouse -->
   </performance-server>
</properties>
```

In the previous XML snippet, some sections are only useful in certain configuration scopes. For
example, the performance-server section is only useful in the
performance-data-warehouse configuration scope.

The way that elements are nested is important. For example,
if you nest the <timeout> element under an
inappropriate parent element like <server>,
the value will not change. The property must be in the correct location
in the XML document for Workflow Server to
read and update the values during run time.

Business Automation Workflow merges
the changes that you make in the 100Custom.xml file
with the original configuration based on the value of the merge attribute.
All attribute values must be specified in quotation marks. For example,
the merge attribute and its default value mergeChildren are
specified as merge="mergeChildren". Depending on
how you want to merge updated elements between the 100Custom.xml file
and the original configuration, use one of the values in the following
table.

| Value for merge attribute   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| append                      | Appends the new element to any existing elements, which is useful when you are adding an additional element to an existing list that contains multiple copies of the same element.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| mergeChildren               | Merges the new element with the first of the existing elements, which is useful when you are specifying the parent XML tags of child elements that need to be changed. The mergeChildren value is the default value for the merge attribute, which means that the attribute value merge="mergeChildren" is implied and does not actually need to be specified on an element.                                                                                                                                                                                                                                                                                                                                          |
| replace                     | Replaces all existing elements and their child elements with the new element, which is useful when you are changing the value of child elements or when you want to modify a parent element and all its child elements. Note: When you set the merge="replace" attribute for an element that has nested child elements, any existing child elements from the product's default configuration will be deleted and only the child elements that are specified in your customization will be set. As a result, it is recommend that you only use merge="replace" on leaf nodes where the element does not have any children. Otherwise, ensure that you are including all required child elements in your customization. |

## Procedure

To configure a 100Custom.xml file:

1. To contain your change, use the existing 100Custom.xml file
or create a new file based on the existing one. If you are creating
multiple files to contain your changes, you should prefix each file
with 100Custom.   You should
avoid having multiple files with conflicting changes. When you modify
your 100Custom.xml configuration files, you should
first make a backup of the original file content using a .bak extension.
Be careful not to leave old .xml files in the
config directories as all *.xml files will be
loaded into the server configuration.
2. Fill out the 100Custom XML file with the desired parent/child XML
structure leading to the element you wish to modify. All elements are contained within the topmost
properties tag as shown in the previous example. Consult the documentation for a particular setting
for more information or review the TeamWorksConfiguration.running.xml file. 

Some settings contained in the TeamWorksConfiguration.running.xml file do
not support customization by the customer. As a result, you should avoid changing undocumented
settings.
3 Fill in the merge="attribute\_value " attributeof the XML elements based on the following guidelines:
    - For parent XML elements only including updates to child elements,
omit the attribute (implying the mergeChildren value).Note: For
new child elements to correctly append, merge, or replace existing
elements, the names of the parent XML elements must match the names
of the existing elements. Additionally, all attributes and their values
for the parent elements must match up exactly. (This does not include
the merge and match attributes, which are not considered.)
    - For new or existing XML elements for which you are updating
the value or attributes, use merge="replace". Any
preexisting child elements will also be removed and replaced with
the contents of this element. You can review the TeamWorksConfiguration.running.xml file
to see the preexisting content of a particular element.
    - For XML elements that you want to add to an existing list
of similar elements, use merge="append".
4. Test out the new file changes by deploying them to your environment
and reviewing the updated TeamWorksConfiguration.running.xml file. For more
information, see Deploying a 100Custom.xml file to a deployment environment.  
 Traditional: Alternatively, you can use the updateBPMConfig command to write your changes to
the 100Custom.xml file after you have determined the changes that are
needed.