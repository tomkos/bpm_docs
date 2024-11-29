# Obtaining a solution description document

## About this task

A solution consists of a set of cases and supporting information,
including a definition file that describes the overall structure and
contents of the solution, a set of XPDL files describing workflows
that are associated with the cases in the solution, and a Content Platform Engine configuration file that
contains the Content Platform Engine configuration
details, such as queue, role, in-basket, roster, event log, application
space, and step processor definitions for the solution.

| Rules                 | Details                                 |
|-----------------------|-----------------------------------------|
| Namerule1 Description | TypeText-based rule Reference Namerule1 |

| Property layout views                  | Details             |
|----------------------------------------|---------------------|
| NameSystem-generated Default View true |                     |
| Nameview1                              | Reference Nameview1 |

| Page                        | Details                                                        |
|-----------------------------|----------------------------------------------------------------|
| NameCmAcmCASES\_DEFAULT\_PAGE | TypeStatic default page Reference Name CmAcmCASES\_DEFAULT\_PAGE |
| NameCmAcmCASES\_DEFAULT\_PAGE | TypeStatic default page Reference Name CmAcmCASES\_DEFAULT\_PAGE |

When you design solutions, you can use the solution
description document to view the organization of the solution and
its contents in an easy-to-read format that can be shared with case
workers and customers.

You can create a solution description document for only one solution at a time. You can choose
from one of the following types of output: PDF or XHTML.

## Procedure

To generate a solution description document:

1. Navigate to the Solution Documentation Generator location:

Operating system
Location

AIX®
install\_root/CaseManagement/docGenerator

Linux®
install\_root/CaseManagement/docGenerator

Linux for System z
install\_root/CaseManagement/docGenerator

Windows
install\_root/CaseManagement/docGenerator

Restriction: For the Solution Documentation Generator
to successfully create solution description documents, the IBM® Business Automation
Workflow installation path cannot
contain special non-English characters or symbols.
2 Open the docGenerator.properties file in a text editor and define yourIBM Business AutomationWorkflow environment. See the following example of a docGenerator.properties file: ceURI = http://myServer:9080/wsi/FNCEWS40MTOMobjectStoreName = CMDOSsolutionName = MySolutionoutputFormat = PDFoutputLocation = C:\IBM\BAW\CaseManagement\docGenerator\outputantOpts = -Xmx2000m -Dmax JavaMemory=2000m Tip: For the outputLocation , you must use a forward slash (/) toseparate folder names in the properties file regardless of your operating systemtype.
    1. For the ceURI property, enter the full URI of the Content Platform Engine server.
For example, http://localhost:9080/wsi/FNCEWS40TOM.
    2. For the objectStoreName property, enter the name of the design object store
that contains the solution that you want to generate a solution description document
for.
    3. For the solutionName property, enter the name of the solution that you want to
generate a description document for.
    4. For the outputFormat property, enter the output format for the solution
description document.

PDF
To get an Adobe Acrobat PDF file.
HTML
To get an XHTML file.
    5. For the outputLocation property, enter the directory location where you want
the solution description document to be created.
    6. Optional: 
For the antOpts property, enter the maximum memory to be allocated to the JVM
for a large solution.

```
ceURI = http://myServer:9080/wsi/FNCEWS40MTOM
objectStoreName = CMDOS
solutionName = MySolution
outputFormat = PDF
outputLocation = C:\IBM\BAW\CaseManagement\docGenerator\output
antOpts = -Xmx2000m -Dmax JavaMemory=2000m
```

3. Open a command prompt and run the Solution Document Generator.
You can append a parameter to the command to check in the generated document into the 
FileNet®
 repository:
checkin. The checkin parameter checks in the solution
description document into the same object store in the solution folder. By checking in the solution
description document into the same folder as the solution, you can iteratively monitor how the
solution design changes.

Operating system
Command

AIX
docgen.sh

Linux
docgen.sh

Linux for System z
docgen.sh

Windows
docgen.bat

For example, enter docgen.bat
-checkin
4. At the prompt, enter a user name and password that can
retrieve and add content to Content Platform Engine.

## Results