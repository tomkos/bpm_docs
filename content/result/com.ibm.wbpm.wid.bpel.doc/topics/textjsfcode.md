<!-- image -->

# Preparing to extend generated JSF code

## About this task

When you generate a user interface, a dynamic web project
is generated. This project contains the generated artifact, which
consists of several Java™ Server
Faces (JSF) pages, Java code,
and the required configuration files. The artifacts are automatically
packaged into an EAR file, which is ready to be deployed and run on WebSphere® Application Server.
However, you might need to extend the JSF client code if the work
scope increases. Before you extend this code, you must update the
faces-config.xml file.

To update the faces-config.xml file,
complete the following steps:

## Procedure

1. Generate a new JSF client for all the affected human tasks.
2. Complete the actions in the following table. 

Newly generated faces-config.xml file section
Description
Action

Where clause extension for open and
under work ToDos
Contains the configuration of toDosWhereExtension
Copy the newly generated faces-config.xml file
section to same section in the faces-config.xml file of the client
to be enhanced.

Where clause extension for sub ToDos
Contains the configuration of subToDosWhereExtension
Copy the newly generated faces-config.xml file
section to same section in the faces-config.xml file of the client
to be enhanced.

Application meta info
Contains the configuration of toDosClientTypes,
toDosInEqualsOut, toDosMainInEqualsSubIn
Copy the newly generated faces-config.xml file
section to same section in the faces-config.xml file of the client
to be enhanced.

Navigation rules
Contains the map of logical name-to-file name
for all infrastructure, overview, and main pages.
Copy the newly generated faces-config.xml file
section to same section in the faces-config.xml file of the client
to be enhanced.
3. Save the faces-config.xml file of the client to be enhanced.

## What to do next

After you update the faces-config.xml file, download the
ModifyEnhanceJSFClient.pdf file and sample (OrderSolution\_PI\_V7.zip)
in  Understanding and enhancing the generated Java Server Faces client for human
tasks for information about how to extend your generated JSF
client for human tasks.

## Related concepts

- Before you begin: Client types and prerequisites

## Related tasks

- Defining user interfaces for a human task
- Generating HTML-Dojo pages for Heritage Process Portal spaces (deprecated)
- Integrating JavaScript in HTML-Dojo pages
- Customizing clients
- Deploying a generated client to an external runtime environment

## Related reference

- Design considerations for user interface generation