# Registration of the IBM Business Automation
Workflow plug-in fails

## Symptoms

```
The task failed because of the following error: The plug-in JAR file was not found at the specified location. Ensure that JAR file is on the web application server and that the URL or the fully qualified path of the JAR file is correct.
```

## Causes

- The network shared directory, bpm.de.caseManager.networkSharedDirectory,
specified in the properties file and in the Case configuration tool profile properties must be a network-mounted
directory that is shared by all the nodes in the cluster. To export the properties file, use the
following
command:BPMConfig.sh -export -profile profileName [-de deName] [-db [input\_file]] [-system input\_file] [-outputDir configurationOutputDir]
- If you have high latency between cluster nodes, it might take a few seconds for files that are
copied from one node in the network shared directory to be accessible by the other nodes in the
cluster.
- Because of an IBM Content
Navigator limitation,
when you run the task to register the plug-in, some nodes might not have the plug-in, which is
loaded.

## Resolving the problem

- Ensure that the network shared directory is shared by all nodes in the cluster. If the directory
is not correct, reconfigure the directory by running the following
commands:BPMConfig -update -profile dmgr -de De1 -component ContentNavigator -networkDirectory /dir
BPMConfig -update -profile dmgr -de De1 -component CaseManager -networkDirectory /dir
For more information, see Enabling the case management features. Note: The
-component
ContentNavigator option is used only for embedded IBM Content
Navigator.
- Ensure that the system is properly configured to minimize latency in updates between different
nodes.
- Restart the Business Automation Workflow
cluster.