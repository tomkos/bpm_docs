<!-- image -->

# Exporting relationship instance data to the comma-separated
values (CSV) format

## About this task

## Procedure

1. From the File menu, select Export > Business Integration > Relationship instance data and
click Next (Note that you can also export a
.csv file from the Properties page of a relationship using the Export button).
2. The Export Relationship Instance Data window opens. Click
the drop-down list to select a static relationship to export.
3 Specify the target file format using one of the followingoptions:
    1. Contains only instance values: Selecting this target file format type provides only the instance values. Selecting this option means that if the data is modified after it was exported, you will need to reconcile the values when importing them back into IBM Integration
Designer. For example, upon importing, you will need to indicate which columns correspond to which roles and key attributes. Note that this format type is not supported when importing the output file into IBM Business Automation
Workflow.
    2. Contains properties and metadata: Selecting this target file format type provides all of the data that can be converted into the ri (relationship instance) file. Selecting this option means that if the data is modified after it was exported, you will not need to further reconcile the values when importing them back into IBM Integration
Designer. Note that this format type is supported when importing the output file into IBM Workflow
Server.
4. Click Browse to set the target .csv
file.
5. Click Finish to export the data.