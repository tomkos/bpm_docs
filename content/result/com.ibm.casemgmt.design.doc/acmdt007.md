# Creating a list of object store properties and document classes

## About this task

You can use the Case configuration tool to create two
comma-separated value text files, PropertyTemplates.csv and
DocumentTypes.csv.

- Property Template Display Name
- Symbolic Name
- Data Type
- Description
- Cardinality (single value or multi-value choice list)
- Default Value
- Min Value
- Max Value
- Max Length
- Choice List
- Required
- Hidden

- Display Name
- Symbolic Name
- Descriptive Text
- Is Hidden
- Is Persistent
- Properties (symbolic names of properties associated with this document class)

Creating a list of object store properties and document classes applies only in the development
environment.

## Procedure

To create a list of the object store properties and document classes in an object
store:

1 Start the Case configuration tool by running one of thefollowing commands: Operating system Command AIX® Linux® Linux for System z® Windows Perform one of the following actions:

| Operating system    | Command                                                                                                                                                                                                        |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AIX®                | Change to the install\_root/CaseManagement/configure directory.  Run the following command:./configmgr                                                                                                          |
| Linux®              | Change to the install\_root/CaseManagement/configure directory. Run the following command:./configmgr                                                                                                           |
| Linux for System z® | Change to the install\_root/CaseManagement/configure directory. Run the following command:./configmgr                                                                                                           |
| Windows             | Perform one of the following actions: Click Start  > All Programs > IBM® Business Automation Workflow > Case configuration tool. Run the following command:install\_root\CaseManagement\configure\configmgr.exe |

2. Click Tools > List Property Templates and Document Classes to create the list of properties by using the wizard.
3. Provide copies of the CSV files to your business analysts who design solutions in Case Builder.
You can open the CSV files in a text editor, a spreadsheet, or other program to review the
list of available document classes or property templates and their settings.