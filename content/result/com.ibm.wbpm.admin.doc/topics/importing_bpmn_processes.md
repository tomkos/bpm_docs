# Importing and exporting BPMN models

## Procedure

- To import a BPMN 2.0 model, complete the following steps:
    1. Open IBM® Workflow
Center and open the list of process apps.
    2. Click Import.
    3. Browse to the .zip file and import it.
- To export your process applications to a BPMN 2.0 file archive (.zip), complete thefollowing steps:

1. In the list of process applications, go to the application that you want to
export.
2. From the 3-dot menu on the application tile, click Export.
3. Select Export this project in BPMN 2.0 format (.zip).
4. Locate the directory to which you want to save the export file, name the file, and
then save it. 
The BPMN 2.0 export includes any process that is referenced in a process application or toolkit.
No data artifacts such as business objects or services are included in BPMN 2.0 export.
The exported file can be imported into any Workflow Center
repository.

- Mapping BPMN 2.0 constructs to workflow objects after import

You can import elements that use the Business Process Model and Notation (BPMN) Version 2.0 file format.
- Next steps after importing BPMN models

You have now imported your BPMN models successfully into the Workflow Center. The following procedure helps you identify the step-by-step actions you will take after a successful import. However these steps will vary depending on the contents of your model and how you intend to make use of these models in the future. If you had seen warning messages at the end of your import it is likely that you may need to take some remedial action. Warnings usually indicate an unsupported construct or invalid input model. For each warning, examine the contents of what was generated and take additional action as required.
- Exporting process applications to BPMN 2.0

You can export your process applications to a Business Process Model and Notation (BPMN) version 2.0 file format, which can be used with products that support the BPMN 2.0 import.