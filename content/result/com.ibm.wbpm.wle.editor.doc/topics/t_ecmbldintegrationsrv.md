# Integrating with an ECM system or a BPM document store

## Before you begin

If you are working with an external ECM system, you should have added your Enterprise Content
Management (ECM) servers to your process application as shown in Adding an Enterprise Content Management server.
You don't need to define your server to work with one of built-in stores, such as the BPM managed store, BPM content store, BPM document store, and BPM target store.

You should add the Content
Management (SYSCM) toolkit to your dependencies, if it has not been
added as you will need access to the ECM types. To add this toolkit
dependency, select + beside TOOLKITS.
In the Add dependency menu, select the Content
Management toolkit version you require.

## About this task

To build a service that integrates with an ECM system or a BPM document store, follow these steps:

## Procedure

1 Create a service that contains a Content Integration step:
    - In Process Designer, click
Services and create a service flow.
    - To create a heritage human service in Process Designer, click User Interface > Heritage Human Service.
    - In the desktop Process Designer , select aservice from the library area that supports Content Integration steps. Thefollowing services contain a Content Integration step. Enter a name for the service and click Finish . The editor opens withthe Diagram view in focus.
        - Click + next to Implementation, and select
Integration Service
        - Click + next to User Interface, and select
Ajax Service.
        - Click + next to User Interface, and select
Heritage Human Service.

Enter a name for the service and click Finish. The editor opens with
the Diagram view in focus.

2. Add a Content Integration step to the canvas and provide a meaningful
name for it.
3 Under Properties , click Implementation . UnderEnterprise Content Management Server , <Use datamapping> is the default selection in the Server field. Itmeans that in the Data Mapping section, the Servername input map is enabled and editable. You can pass a server name by using a variablein that field. Alternatively, you can select one of the following server types in theServer field. For information about these server types, see Management of folders and documents for ECM systems . If you want to select the name of an ECM server but no ECM servers are available for selection,you can add a server in the Process App Settings editor. See Adding an Enterprise Content Management server .

Alternatively, you can select one of the following server types in the
Server field.

- BPM managed store
- BPM content store (deprecated)
- BPM document store
- BPM target store
- The name of an ECM server

For information about these server types, see Management of folders and documents for ECM systems.

If you want to select the name of an ECM server but no ECM servers are available for selection,
you can add a server in the Process App Settings editor. See Adding an Enterprise Content Management server.

4. Under Content Operation, select an appropriate ECM operation. See Outbound operations for external ECM systems and BPM stores.
5. Click Data Mapping. In this section you can create the map between the
variables for input and output. These variables need to be created. You can create them manually by
yourself or use the auto-map function. The auto-map function creates private variables for the
business objects, which are used by the service you create. To create these private variables, click
the auto-map icon  .
The mapping structure for each operation is discussed in Data mapping in Enterprise Content Management operations.Note: To use the auto-map function, you must be in the desktop Process Designer.
6. Click Save or Finish Editing.

## What to do next

As with any service, if you have errors at run time, use
catching error events to handle errors thrown by a content integration
step. A content integration step may raise an error with error code ECMError and
error data of type ECMError. See Handling errors in services.