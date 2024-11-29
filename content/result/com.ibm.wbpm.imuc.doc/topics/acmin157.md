# Configuring stand-alone IBM
FileNet Process Designer to work with IBM Business Automation
Workflow in Cloud Pak for Business Automation

## About this task

## Procedure

Follow the steps to configure IBM Business Automation
Workflow with IBM Cloud Pak for Business
Automation:

1. Install the stand-alone IBM
FileNet Process Designer on your local system.
 For more information about installing and running IBM
FileNet Process Designer, see Installing FileNet Process Designer, and Running FileNet Process Designer.
2. Copy the ICMSolutionEdit.jar file to resources in workflow-authoring
pod.  From the /resources directory on the infrastructure node, copy
the ICMSolutionEdit.jar file to the
<install-dir>\peclient\peclient\lib on the Content Platform Engine Tools server.Important:
ICM\_Operations, ICM\_RuleOperations and other custom component
queues that are available when a case solution is opened from IBM
FileNet Process Designer will not be listed in
higher versions of Java (Java 11 and Java 17). In order to work on the custom component and ICM
operations queues of a case solution, configure the standalone IBM
FileNet Process Designer with Java 8.
To change the Java JRE used by Process Designer, edit cpetoolenv.bat and change
the JAVA\_HOME setting:set JAVA\_HOME=C:\myJava\jre
3 Copy the Resources/ICMSolutionEdit.jar file to the stand-aloneIBMFileNet Process Designer installlocation. On the infrastructure node, copy the ICMSolutionEdit.jar by using the following command: oc rsync `oc get pods | grep workflow-authoring-baw-server* | head -1 | awk {'print $1'}`:/opt/ibm/wlp/usr/servers/defaultServer/apps/expanded/CaseBuilder.ear/CaseBuilder.war/WEB-INF/lib/ICMSolutionEdit.jar /resources Note:

```
oc rsync `oc get pods | grep workflow-authoring-baw-server* | head -1 | awk {'print $1'}`:/opt/ibm/wlp/usr/servers/defaultServer/apps/expanded/CaseBuilder.ear/CaseBuilder.war/WEB-INF/lib/ICMSolutionEdit.jar /resources
```

    - If the ICMSolutionEdit.jar is not installed correctly in the classpath forthe stand-alone FileNet ProcessDesigner client, you mightsee the following behaviors:
        - UTF-8 multibyte names or labels do not display correctly in languages other than English.
        - The message "FNRPA0663E The component queue definition should not be present in the solution's
PE configuration" is displayed during solution deployment.
- If the IBM Cloud Pak for Business
Automation
environment is upgraded to later versions, you must repeat (copying files) the step 2 and step 3
after the upgrade.
4. Configure WcmApiConfig.  The Content Engine Web Service
URL is stored in the file WcmAPIConfig.properties as the value for the
parameter RemoteServerUrl. WcmAPIConfig.properties file is
in <install\_dir>\peclient\peclient\config directory.For a Workflow
Authoring environment, it would be similar to: RemoteServerUrl =
https://cpe.mydeployment.apps.myhost.mydomain/wsi/FNCEWS40MTOM
5. Set Java JRE The stand-alone Process Designer requires a Java JRE. The Content Platform Engine Tool provides a
compatible IBM JRE. Expand the compressed (.zip) file and add the jre\bin to
the PATH environment variable so that the IBM JRE is available in the execution
environment.
For example, PATH=
<PATH>;<install\_dir>\ibm-java-jre-8.0-6.15-win-x86\_64\jre\bin.
6. Set PE\_CLIENT\_TOOLS\_DIR in
cpetoolsenv.bat. In the file
<install\_dir>\peclient\peclient\batch\cpetoolsenv.bat, the parameter
PE\_CLIENT\_TOOLS\_DIR must be set to the directory in which the Content Platform Engine tool is expanded. For
example, set
PE\_CLIENT\_TOOLS\_DIR=<install\_dir>\peclient.

Configuring Content Platform Engine SSL certificate for
FileNet Process Engine client JRE

1 Extract the Privacy Enhanced Mail (PEM) certificate from Content Platform Engine . The PEMcertificate of Content Platform Engine on Workflow Authoring in IBM Cloud Pak for BusinessAutomation can be downloadedfrom a browser.
    1. In a Firefox browser, connect to RemoteServerURL, for example,
https://cpe.mydeployment.apps.myhost.mydomain/wsi/FNCEWS40MTOM.
    2. Click the lock icon to the left of the URL.
    3. Click Show connection details and click More
information.
    4. Click View Certificate.
    5. Scroll down to find the link to download the PEM file. Click the link and download the
file to a known location. For example, C:\icp4a-fncm-svc.pem.
2 Import the certificate to the keystore.

1. Go to cd
<install\_dir>\ibm-java-jre-8.0-6.15-win-x86\_64\jre\bin
2. Import the key from keytool -importcert -file C:\icp4a-fncm-svc.pem -alias
icp4a -keystore <install\_dir>\ibm-java-jre-8.0-6.15-win-x86\_64\jre\lib\security\cacerts
-storepass changeit Where C:\icp4a-fncm-svc.pem is the
downloaded PEM certificate and icp4a is the alias for storing the
certificate.The certificate must be added to cacerts keystore in the
\jre\lib\security folder as mentioned in step 8.b.