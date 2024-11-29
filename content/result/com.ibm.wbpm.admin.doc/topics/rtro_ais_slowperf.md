# Numerous synchronous AIS requests can slow performance

You might notice the performance impact in a Java core as a large set of blocked threads on
com/ibm/bpm/sca/core/SCARuntime@0x000000011A173C40: owner
"WorkManager.bpm-em-workmanager".

## Resolving the problem

1. From the IBM Business Automation
Workflow installation
directory:
/profiles/<NodeProfile>/installedApps/<CellName>/IBM\_BPM\_CMIS\_SingleCluster.ear/fncmis.war/WEB-INF/classes/cmis.properties2,
open the cmis.properties file in a text editor.
2. Add the following line:
com.ibm.xml.xlxp2.api.util.encoding.DataSourceFactory.bufferLength=655363
Save
and close the file.
3. Restart the JVM.
4. In the SystemOut.log file, verify that the
com.ibm.xml.xlxp2.api.util.encoding.DataSourceFactory.bufferLength system
property is changed: 
CMISBootstrap I com.ibm.ecm.cmis.util.CMISBootstrap processedSystemProperties Overriding system property 
com.ibm.xml.xlxp2.api.util.encoding.DataSourceFactory.bufferLength with the configured value, 65536