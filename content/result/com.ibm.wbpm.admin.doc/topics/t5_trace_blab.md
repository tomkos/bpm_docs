<!-- image -->

# Enabling tracing for Business Process Choreographer

## Trace settings

| Trace string                   | What is logged                                                                 |
|--------------------------------|--------------------------------------------------------------------------------|
| com.ibm.bpe.*                  | All available trace information for BPEL processes                             |
| com.ibm.bpe.basic.navigation.* | Major navigation steps and state changes for BPEL processes                    |
| com.ibm.bpe.basic.api*         | Time and sequence of methods called by the Business Flow Manager API           |
| com.ibm.task.*                 | All available trace information for human tasks                                |
| com.ibm.task.basic.api*        | Time and sequence of methods called by the Human Task Manager API              |
| com.ibm.task.basic.core*       | Major steps in the processing of human tasks, state changes, and calls to SPIs |
| com.ibm.ws.staffsupport.*      | All available trace information for the people directory providers             |

```
com.ibm.bpe.*=all:com.ibm.task.*=all:com.ibm.ws.staffsupport.*=all
```

## What to send to support

- The WebSphere® Application
Server FFDC
log, located in the ffdc folder
- The following log files: If your problem scenario causes a lot of logging, backup filesfor the logs might be created with names, such as SystemOut\_07.10.01\_11.00.51.log .You can use the administrative console to change the number of backupfiles that are created and the size of the log files. It might begood to increase both of these values to ensure that you capture allof the data.
    - SystemOut.log
    - SystemErr.log
    - trace.log
    - On Linux® and UNIX systems,
these files are located in the profile\_root/logs/server\_name directory.
    - On Windows platforms
they are located in the profile\_root\logs\server\_name directory.

If your problem scenario causes a lot of logging, backup files
for the logs might be created with names, such as SystemOut\_07.10.01\_11.00.51.log.
You can use the administrative console to change the number of backup
files that are created and the size of the log files. It might be
good to increase both of these values to ensure that you capture all
of the data.