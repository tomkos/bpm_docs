<!-- image -->

# Creating an XML map in a Mapping transformation primitive

## About this task

- The part of the message that you want to map, by setting the rootproperty, which defines the part of the message that will be availablefor mapping in the XML map editor.
    - / to transform the complete message. To
map SOAP attachments, or to map anyType, use / as the root.
    - /body to transform the message body
    - /headers to transform the message headers
    - /context  to transform the message context
- The message type that is input to the map, and the message type
that is output from the map. You can choose a specific message type,
or a generic anyType, depending on your scenario. For example, if
you want to create a reusable subflow, use anyType as the input and
output.

1. Drop a Mapping transformation primitive on to the canvas of the
mediation flow editor.
2. Wire the input and output terminals of the primitive
3. Click the primitive to open the XML mapping wizard.
4. Click Finish to accept the defaults. Note: An
XML map created in this manner has a root of /body, and the input
and output message types of the map are the same as those of the primitive.
By default, a sample input file is created. You can use this file
to test the map you create. 
Note: If you do not need to change
the information in the headers or contexts sections of the service
message object, use /body as the mapping starting point. When you
select  /, /headers or /context as the root, you need to explicitly
map all of the service message object sections in the XML map editor
using the Match Mapping option. Otherwise, you might get errors at
run time.
5. The XML map editor opens, with the source message on the left
and the target on the right. Expand the message trees in the source
and target sections of the map editor, until you reach the elements
that you want to map. Click an element in the Source section drag
it to the matching element in the target section.

To quickly create an XML map with an input and output
type of anyType, follow these steps:

1. Drop a Mapping transformation primitive on to the canvas of the
mediation flow editor.
2. Optional: Wire the input and output terminals of the primitive.
3. Click the primitive to open the XML mapping wizard.
4. Click Next.
5 For both the input and output messages, identify the part of themessage that is available to the transformation by selecting an optionin the Message Root list:
    - / to transform the complete message. To
map SOAP attachments, use / as the root.
    - /body to transform the message body
    - /headers to transform the message headers
    - /context  to transform the message context
6. If your Mapping transformation primitive has both input and output
terminals wired, the wizard shows the input and output message types
that will be mapped. If you need to specify the message types, click Browse,
then Browse again and select an interface from
the list.
7. Select an operation, the message category and finally the message
type. Click OK to return to the New XML Mapping
wizard
8. Click Finish to launch the XML map editor.
9. In the editor, the source message is on the left and the target
on the right. Expand the message trees in the source and target sections
of the map editor, until you reach the elements that you want to map.
Click an element in the Source section drag it to the matching element
in the target section.

1. Right-click your Mapping transformation primitive and select Show
in Properties. The Properties view opens at the bottom
of the mediation flow editor.
2. In the Properties view, click the Details tab.
3. Beside the Mapping file field, click New.
The New XML Map wizard opens.
4. On the first page of the wizard, accept the default values and
click Next.
5 If a Manage the Existing Map page is displayed, an XML map alreadyexists for your Mapping transformation primitive and you should selectone of the following radio buttons to specify what you want to dowith the existing map:
    - Override the existing map Creates a new
map with the same name as the existing map and replaces the existing
map.
    - Create a new map and delete the existing map Creates
a new map with a different name than the existing map, but removes
the existing map.
    - Create a new map and keep the existing map Creates
a new map with a different name than the existing map, but retains
the existing map.
6. Click Next.
7. Either accept the default message types or modify them as described
in the previous section, then click Finish.