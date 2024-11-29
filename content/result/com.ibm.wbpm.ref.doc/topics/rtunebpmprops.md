# Sample performanceTuning.properties file (removed)

The performanceTuning.properties file
is in the directory BPM\_home\BPM\scripts\performanceTuning.
The properties file is populated with the recommended default values
and options for IBM BPM deployment environments. Information about
running the tuneBPM command to apply the file properties
to your deployment environment is found in the topic "tuneBPM command-line
utility".

```
############################################
# Standard configuration tuning properties #
############################################
# Specify the flag for whether to send external email.
# Modify the application cluster members in the specified deployment environment.
# Modify the value of <send-external-email> in the 99Local.xml file, file path: 
# <WAS\_HOME>/profiles/<dmgr\_profile\_name>/config/cells/<cell\_name>/nodes/<node\_name>/servers/<server\_name>/process-center|process-server/config/system 
appCluster.sendExternalEmail=false  
# Specify the number of simultaneous tasks that can execute on the BPD queue. The value should be 10 * #VCPUs, capped at 80. 
# Modify the application cluster members in the specified Process Server deployment environment. 
# Modify the value of <bpd-queue-capacity> in the 80EventManager.xml file, file path: 
# <WAS\_HOME>/profiles/<dmgr\_profile\_name>/config/cells/<cell\_name>/nodes/<node\_name>/servers/<server\_name>/process-server/config/system 
appCluster.bpdCapacity=80  
# Specify the maximum number of threads for the engine thread pool. The value should be 10 * #VCPUs + 30, capped at 80 + 30. 
# Modify the application cluster member in the specified Process Server deployment environment. 
# Modify the value of <max-thread-pool-size> in the 80EventManager.xml file, file path: # <WAS\_HOME>/profiles/<dmgr\_profile\_name>/config/cells/<cell\_name>/nodes/<node\_name>/servers/<server\_name>/process-server/config/system 
appCluster.threadPoolSize=110
```