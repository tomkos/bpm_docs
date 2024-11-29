# Log data for the Business Automation Workflow configuration
tool

| Operating system                  | Default file path                                                                                                                                                              |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AIX®  Linux®  Linux for System z® | /opt/IBM/CaseManagement/logs/IBM\_Case\_Manager\_5.2.1.0\_CMCT.log /opt/IBM/CaseManagement/logs/IBM\_Case\_Manager\_5.2.1.0\_CMCT\_trace.log.                                           |
| Windows                           | drive:\Program Files (x86)\IBM\CaseManagement\logs\IBM\_Case\_Manager\_5.2.1.0\_CMCT.logdrive:\Program Files (x86)\IBM\CaseManagement\logs\IBM\_Case\_Manager\_5.2.1.0\_CMCT\_trace.log |

| Operating system               | Default file path                                                                    |
|--------------------------------|--------------------------------------------------------------------------------------|
| AIX  Linux  Linux for System z | /opt/IBM/CaseManagement/configure/configuration/cmlogging.properties                 |
| Windows                        | drive:\Program Files\IBM\CaseManagement\configure\configuration\cmlogging.properties |

```
# Only setup logging to files -- no Console Handling
# handlers are attached to root logger and inherited by all others
handlers = java.util.logging.FileHandler

# need it set to ALL, don't change. adjust tracing via Eclipse .options file
java.util.logging.FileHandler.level=ALL
com.ibm.ecm.configmr.level=ALL

# the next line does not actually seem to work -- formatter is also applied programmatically.
java.util.logging.FileHandler.formatter=com.ibm.ecm.configmgr.engine.util.CMLogFormatter

# set file handler to limit to 1Mb per log file, rotating 3 log files, store in user.home dir
java.util.logging.FileHandler.limit=10000000
java.util.logging.FileHandler.count=5
java.util.logging.FileHandler.pattern=C:/IBM/CaseManagement/logs/IBM\_Case\_Manager\_5.2.1.0\_CMCT%g.log
```

| Operating system               | Default file path                                                   |
|--------------------------------|---------------------------------------------------------------------|
| AIX  Linux  Linux for System z | /opt/IBM/CaseManagement/configure/tmp/task\_name.log                 |
| Windows                        | drive:\Program Files\IBM\CaseManagement\configure\tmp\task\_name.log |