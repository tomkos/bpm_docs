# Throwing errors in service flows

## About this task

## Procedure

To add an error end event to a service, complete the following steps:

1. Open the designer.
2. From the library, create or open the service flow or heritage human service that you want to
work with, and click its Diagram tab.
To create the service, see Creating a service flow or Building a heritage human service.
3. From the palette, drag an error end event  onto the canvas.
4. In its Implementation properties, under Error
code, specify the error code for the error to be thrown.
The error code is automatically included in the list of defined errors that you can select to
catch when you create an error intermediate event in a parent process or service. 
Click the Error mapping picker to map the error data to an error
mapping variable that was previously defined on the Variables tab.

Note: The error data cannot be mapped to a variable that is of a list type. If you want to pass
information that has the structure of a sequence as error data, create a business object that
contains a parameter that is of a list type and then use this business object as the variable's
type.
5. In the diagram, connect the error end event to the logic you want to run when the error
occurs.
6. Click Save or Finish Editing.