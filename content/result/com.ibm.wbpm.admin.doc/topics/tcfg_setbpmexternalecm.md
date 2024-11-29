# setBPMExternalECM command fails

## About this task

## Procedure

1. Back up the FileNetEngine.ear file.
2. Create a copy of the com.filenet.deployment.rcp\_6.0.0.jar file from
a Content Platform Engine 5.5.2 or later
environment. Place it in the uncompressed .EAR of the deployed Content Platform Engine application within
WebSphere. For example, the file path might look like: 
C:\IBM\WebSphere\AppServer\profiles\CPEsrv01\installedApps\FD-551Oracle1Cell01\FileNetEngine.ear\client-download.war\FileNet\Download\dap551.1021\FDM\com.filenet.deployment.rcp\_6.0.0.jar
3. While in the uncompressed .EAR folder, return to the
.EAR directory \FileNetEngine.ear\client-download.war\WEB-INF.
Create a copy of the file package.xml and move this copy as a backup out from
the uncompressed .EAR file.
4. Open the package.xml file and add the following lines under the
IBM
FileNet® Deployment Manager Integration
section: 
<component type="jar">/FileNet/Download/dap551.1021/FDM/com.filenet.deployment.rcp\_6.0.0.jar</component>
<value type="classpath">com.filenet.deployment.rcp\_6.0.0.jar</value>
For example, the section might look
like:<description>FileNet Deployment Manager Integration</description>
<buildnumber>dap551.1021</buildnumber>
<language>java</language>
<applicationservertype>WebSphere</applicationservertype>
<keyfile>imex.jar</keyfile>
<components>
<component type="jar">/FileNet/Download/dap551.1021/FDM/com.filenet.deployment.common\_6.0.0.jar</component>
<component type="jar">/FileNet/Download/dap551.1021/FDM/com.filenet.deployment.engine\_6.0.0.jar</component>
<component type="jar">/FileNet/Download/dap551.1021/FDM/com.filenet.deployment.modules\_6.0.0.jar</component>
<component type="jar">/FileNet/Download/dap551.1021/FDM/com.filenet.deployment.rcp\_6.0.0.jar</component>
<component type="jar">/FileNet/Download/dap551.1021/FDM/zipfile6or7\_7.0.0.jar</component>
<component type="jar">/FileNet/Download/dap551.1021/FDM/zipfile6or7\_6.0.0.jar</component>
<component type="jar">/FileNet/Download/dap551.1021/FDM/imex.jar</component>
<component type="jar">/FileNet/Download/dap551.1021/FDM/derby.jar</component>
<component type="jar">listener.jar</component>
<component type="jar">/FileNet/Download/dap551.1021/stax-api.jar</component>
<component type="jar">xlxpScanner.jar</component>
<component type="jar">xlxpScannerUtils.jar</component>
<component type="jar">/FileNet/Download/dap551.1021/FDM/org.eclipse.equinox.common\_3.8.0.v20160509-1230.jar</component>
<component type="jar">/FileNet/Download/dap551.1021/FDM/org.eclipse.osgi\_3.11.3.v20170209-1843.jar</component>
<component type="jar">/FileNet/Download/dap551.1021/FDM/org.eclipse.core.runtime\_3.12.0.v20160606-1342.jar</component>
<component type="jar">/FileNet/Download/dap551.1021/FDM/org.eclipse.equinox.preferences\_3.6.1.v20160815-1406.jar</component>
</components>
<configuration>
<value type="classpath">com.filenet.deployment.common\_6.0.0.jar</value>
<value type="classpath">com.filenet.deployment.engine\_6.0.0.jar</value>
<value type="classpath">com.filenet.deployment.modules\_6.0.0.jar</value>
<value type="classpath">com.filenet.deployment.rcp\_6.0.0.jar</value>
<value type="classpath">zipfile6or7\_7.0.0.jar</value>
<value type="classpath">Jace.jar</value>
<value type="classpath">imex.jar</value>
<value type="classpath">derby.jar</value>
<value type="classpath">pe.jar</value>
<value type="classpath">peResources.jar</value>
<value type="classpath">log4j-1.2.17.jar</value>
<value type="classpath">listener.jar</value>
<value type="classpath">stax-api.jar</value>
<value type="classpath">xlxpScanner.jar</value>
<value type="classpath">xlxpScannerUtils.jar</value>
<value type="classpath">org.eclipse.equinox.common\_3.8.0.v20160509-1230.jar</value>
<value type="classpath">org.eclipse.osgi\_3.11.3.v20170209-1843.jar</value>
<value type="classpath">org.eclipse.core.runtime\_3.12.0.v20160606-1342.jar</value>
<value type="classpath">org.eclipse.equinox.preferences\_3.6.1.v20160815-1406.jar</value>
</configuration>
</feature>
5. Save your changes and refresh the browser that you are using for Administration Console for Content Platform
Engine.
6. Download the com.filenet.deployment.rcp\_6.0.0.jar file from Administration Console for Content Platform
Engine.
7. Make sure that the .JAR file shows up in the IBM
FileNet Deployment Manager Integration
section.