# Configuring IBM Business Automation
Workflow to use the
stand-alone IBM
FileNet Process Designer

## Procedure

To configure IBM
FileNet Process Designer as a stand-alone
component:

1. Install the stand-alone IBM
FileNet Process Designer on your local system. For
more information about installing and running IBM
FileNet Process Designer, see IBM FileNet P8 process stand-alone Process Designer
application, Installing FileNet Process Designer, and Running FileNet Process Designer.
2 When you use the stand-alone IBMFileNet Process Designer , copy theinstall\_root /CaseManagement/CaseAPI/lib/ICMSolutionEdit.jar file to the lib folder in your Content Platform Engine installation directory in which you installedthe stand-alone IBMFileNet Process Designer . This file enables stand-alone IBMFileNet Process Designer to support editing bymultiple users. Note: If the ICMSolutionEdit.jar is not installed correctly in the classpathfor the stand-alone FileNet ProcessDesigner client, you mightsee the following behaviors: Important: ICM\_Operations , ICM\_RuleOperations and other custom componentqueues that are available when a case solution is opened from IBMFileNet Process Designer will not be listed inhigher versions of Java (Java 11 and Java 17). In order to work on the custom component and ICMoperations queues of a case solution, configure the standalone IBMFileNet Process Designer with Java 8. To change the Java JRE used by Process Designer, edit cpetoolenv.bat and changethe JAVA\_HOME setting:set JAVA\_HOME=C:\myJava\jre
    - UTF-8 multibyte names or labels do not display correctly in languages other than English.
    - The message "FNRPA0663E The component queue definition should not be present in the solution's
PE configuration" is displayed during solution deployment.

ICM\_Operations, ICM\_RuleOperations and other custom component
queues that are available when a case solution is opened from IBM
FileNet Process Designer will not be listed in
higher versions of Java (Java 11 and Java 17). In order to work on the custom component and ICM
operations queues of a case solution, configure the standalone IBM
FileNet Process Designer with Java 8.

```
set JAVA\_HOME=C:\myJava\jre
```

## What to do next

To use stand-alone IBM
FileNet Process Designer to edit workflow for
your Business Automation Workflow solution, start the stand-alone IBM
FileNet Process Designer, and click File > Solution > Edit to navigate to the workflow definition file in your design object store. The workflow
definition file is located in /IBM Case Manager/Solutions/Solution
Name.