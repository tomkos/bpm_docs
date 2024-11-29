# Example: Reusing a nested client-side human service

## About this task

Assume that you want to augment an Order Confirmation task with a step to
change the shipping address. As a developer, you might want to define a nested client-side human
service for the Change Address step, which you could reuse in other tasks
that are part of a more complex order form.

The following example
shows you how to build the nested client-side human service for the Change
Address step and how to insert the nested client-side
human service into the root client-side human service for the Order
Confirmation. For simplicity, let's assume that the root
client-side human service for the Order Confirmation task
already exists.

## Build the nested client-side human service

### Procedure

To build the nested client-side human service:

1. Open the process application in the designer view that contains the root client-side human service. 
In this example, the process application is called Order Confirmation.
2 Click the plus sign (+) next to User Interface , then click New > Client-Side Human Service and complete the wizard.
    1. Enter the name of the nested client-side human service: Change
Address.
    2. Select Intended for use on multiple devices to specify that you want the
new client-side human service to be used on multiple device types.
When Intended for use on multiple devices is selected, responsive views
are used for all the new pages and page content that is added to the client-side human
service.
3. Select Use as a nested service to
specify that this is a nested client-side human service that can be
reused in other client-side human services.
4 Click Finish . The client-side human service opens in the webeditor. The page in the diagram has a button that provides the boundary event that you can use to wirethe page to the end node. You can use the default button or you can replace it.

<!-- image -->

1 Switch to Overview , and verify that the Usage options are correctly set for a nested service:
    - Nested service is selected
    - Use as and Expose to start are disabled
2. To perform a client-side validation of the page contents or to control a button enablement
through a conditional variable, you can add a Data Change script similar to
the following example:
5. Click the plus sign (+) next to Data, then click New > Business Object and complete the wizard to create an Address business object with
the following parameters:
6. In the nested service diagram, add more pages and elements and wire them together to create the
logic for the nested service.
For example, the diagram for the Change Address nested service can
include the following steps:
7. In the Variables view, add input variables to support the nested
service.  Tip: Optionally, if you have environment variables or exposed process values (EPVs)
that you want to use in your client-side human service, link them to the client-side human service
in the Variables view.
8. Switch to Pages, and create the user interfaces by adding variables to the
canvas.
9. Click Save or Finish Editing.
10. To run the client-side human service in the web browser,
click Run .

### Results

## Nest the reusable client-side human service

### Procedure

To insert the nested client-side human service in the root client-side human service
for reuse:

1. Open the process application in the designer view that contains the root client-side human service.
2. Click User Interface and open the Order
Confirmation root client-side human service.
3 Switch to Overview , and set the following usage options:
    - Ensure that Nested service is clear.
    - From the Use as list, specify the type of usage for the root service
by selecting one of the available options: Task (Service contained in a
process), Startable Service (Launched from Process Portal), Dashboard (Available in the Process Portal Dashboards
menu),
URL (Available from a URL), or Instance details UI for a
process. Note that the Use as option is disabled for nested
client-side human services.
4. In the Diagram view, add the nested client-side human service  to the canvas and wire it in your diagram.
5. Open the nested service node properties. Under Implementation, under
Behavior, click Select next to Nest a
client-side human service and, from the list of client-side human services, select
Change Address.
6 Switch to the Variables view of the root service, and use data mapping toinitialize the shipToSame variable in the nested service:

1. Select the activity for the nested service and open its Data Mapping
properties.
2. Under Input Mapping, use the picker to select the
shipToAddress root variable that will be mapped to the
shipToSame variable in the nested service.
3. Repeat sub-step b to map the address root variable to the
address variable in the nested service.
4. Optional: 
Alternatively, if you want the data mapping to be done automatically, click the auto-map icon
 to
automatically map all the input or output nested variables that do not have a mapping to input
variables of the same name and data type in the root service. Existing mappings are not
replaced.

Tip: Note the input and output icons that precede the variable names. The icons indicate
visually which variables are expected to have values at the start (input variables) and which
variables are expected to have meaningful values at the end (output variables).
7. Optional: If you want to synchronize the customer's shipping and
billing addresses as part of your Create Order page, add a post-execution script to the page, which
can be similar to the JavaScript code in the following example. The post-execution script runs
immediately after the execution of the page completes and synchronizes the two addresses. 

After you assigned the post-execution script to the page, the page node in the diagram view
displays a circular indicator on the right side (post-execution).
8. Click Save or Finish Editing.
9. To run the root client-side human service, click Run
. 
The nested service runs as part of the root service.