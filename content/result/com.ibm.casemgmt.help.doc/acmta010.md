# EAR file for custom widget package isn't deployed

## Symptoms

If the package contains an EAR file, the EAR file isn't deployed.

## Resolving the problem

1 Register the custom widget package:
    1. Extract the files in the package compressed file to a directory on the workflow server. For
example, extract the files to a temporary directory.
    2. Log in to the Case administration client on the server where
IBM Business Automation
Workflow is running.
    3. Point your browser to
https://server:port/navigator/?desktop=bawadmin
where server is the host name or IP address of the IBM Business Automation
Workflow server and port is the
IBM Content
Navigator port number.
    4. Navigate to Object Stores > Design Object Store > Widget Packages.
    5. Select Import Custom Widget and then browse to find the package
compressed file.
    6. Complete the wizard steps.
2 Manually deploy the EAR file:

1. Log in to the WebSphere® Application
Server administrative
console.
2. Point your browser to https://server:port/ibm/console
where server is the host name or IP address of the IBM Business Automation
Workflow server and port is the
IBM Content
Navigator port number.
3 Install the EAR application from the custom widget package:
    1. Navigate to Applications > Application Types > WebSphere enterprise applications.
    2. From the Enterprise Applications page, click Install.
    3. From the "Preparing for the application installation" page, select Local file
system and then select the local package compressed file.
    4. Complete the wizard steps.
    5. Start the EAR application by navigating to Applications > Application Types > WebSphere enterprise applications, selecting the EAR application, and clicking Start.
3. Ensure that the custom widget plug-in is enabled on the desktop where the Case feature is
enabled. This can be accomplished by opening the IBM Content
Navigator administration client and navigating
to the desktop used for Case. (The default Case desktop is IBM Business Automation
Workflow and it has an ID of baw.) On the General tab,
navigate down to Plug-ins and ensure that the custom
widget plugin is selected.