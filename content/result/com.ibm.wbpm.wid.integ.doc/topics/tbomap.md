<!-- image -->

# Using the Business Object Map primitive

## About this task

To use an
existing map:

## Procedure

1. Right-click the Business Object Map primitive and then
click Show in properties.
2. Click Details and then click Browse
3. Select a map from the list and click OK.

## Example

To create a new map follow these steps:

1. Select the Business Object Map primitive, right click it and then
click Show in properties.
2. Click Details, and then click New. In the
New BO Map wizard, name the map and, optionally, select a folder location
by clicking Browse. If you do not select a folder location, the map
will be placed in the default location. Click Next.
3 On the Specify Message Types page of the wizard, first selectthe root which specifies at which level the mapping will start fromthe following options:
    - / - map all fields of the message. Note that if you choose
/ as root, you will have to ensure that you map all fields, including
headers, contexts and body.
    - /headers - map only the headers of the message
    - /context - map only the contexts (transient, correlation,
shared)
    - /body - map the fields found in the body of the message
4. After selecting the root, look at the Input Message Body and Output
Message Body fields. These fields contain the names of the business
object types that you will be mapping. If you want to change them,
click Browse beside the one that you want to
change.
5. In the Change Message Type window, click Browse to
select an interface from the list and click OK.
6. Select an operation from the drop down box, followed by the message
category, either input or output.
7. Finally, select the message type and click OK.
8. When you have completed the wizard, click Finish.
The business object map editor opens with the input and output messages
in place.
9. To map fields, click the field in the business object on the left
side and drag it to the field you want to map it to on the right side.

## What to do next

For information on the different transformations available
see Transform types in the business object map editor.