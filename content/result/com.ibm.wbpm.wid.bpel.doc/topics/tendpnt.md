<!-- image -->

# Modeling dynamic partner assignment with endpoint references

## About this task

- You can change the existing partner endpoint using an assign activity.
- You can save the partner endpoint to a variable.

BPEL partner links for outbound service interactions have
corresponding SCA references, which are statically wired to other
SCA components or Imports.

BPEL partner links may be the target
of a dynamic assignment of an endpoint reference - in this case the
corresponding SCA reference can be left unwired.

- all binding and quality of service specifications are taken from
the SCA Import
- the service endpoint address of the endpoint reference dynamically
overrides any endpoint specified in the pre-wired SCA Import.

## Procedure

- To assign an endpoint to a partner from within a process,proceed as follows:
    1. Drop an assign activity onto the canvas.
    2. In the properties area, click the Details tab.
    3. In the Assign From field, choose Endpoint
Reference from the drop down list.
    4. Configure the fields to point to the existing endpoint
reference.
    5. In the Assign To: field, click Partner
Reference, and select the partner that you want to assign
the endpoint to.
- To save an endpoint into a variable, you will first haveto import a new data type for your variable, and then use an assignactivity. To do this, proceed as follows:

1. Create a new library called EndpointReference by
clicking File > New > Library. Alternatively,
you can choose an existing library and import the data types into
there.
2. While still in the Dependencies view, expand Predefined
Resources, and enable the WS-Addressing Schema
Files check box and then save and close the dependencies.
This will create new business objects in your library.
3. Return to the BPEL process editor, and confirm that
the module that hosts the BPEL process has a dependency to the EndpointReference library
that you created earlier. To do so, open the Dependencies entry under
your module, and make sure the Library is listed.
4. In the tray of the BPEL process editor, create a new
variable. The endpoint information must be stored in a data object
of type ServiceRefType.
5. In the Description area, click Browse to
set the type of your newly created variable to be ServiceRefType. 
Make sure that the fields of that new variable are properly
populated with the information of the endpoint that you'd like to
call.
6. Drop an assign activity onto the canvas, and click the Details tab
in the properties area.
7. In the From field, select the
variable of type ServiceRefType from the drop
down list.
8. In the To: field, choose Partner
Reference and select a partner.

## Example