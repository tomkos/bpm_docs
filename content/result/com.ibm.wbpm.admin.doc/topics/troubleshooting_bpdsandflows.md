# Troubleshooting business process definitions and service flows

## Trace settings

You
can configure the following lightweight trace specifications:

- WLE.wle\_engine (for BPDs)
- WLE.wle\_engine\_basic
(for BPDs)
- WLE.wle\_svcflow (for service flows)
- WLE.wle\_svcflow\_basic
(for service flows)
- WLE.wle\_external\_service (for external services)
- WLE.wle\_scheduler (for Event Manger)
- WLE.wle\_sched\_basic
(for Event Manager)
- com.ibm.bpm.rest.* (for REST APIs)

| Trace specifications                   | Trace settings           | What is logged                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WLE.wle\_engine\_basic=trace\_setting     | FINER                    | The major navigation steps and key data.                                                                                                                                                                                                                                                                                                                                                       |
| WLE.wle\_engine\_basic=trace\_setting     | FINEST, ALL              | The major navigation steps and key data, as well as input and output parameter values. It logs the input and output data and associated variable values for process/BPD/services and activity/event/step. Depending on the size of the data, this can impact performance (such as potential data retrieval and writing to the trace file).CAUTION:Variables values may contain sensitive data. |
| WLE.wle\_svcflow\_basic=trace\_setting    | FINER                    | The major navigation steps and key data.                                                                                                                                                                                                                                                                                                                                                       |
| WLE.wle\_svcflow\_basic=trace\_setting    | FINEST, ALL              | The major navigation steps and key data, as well as input and output parameter values. It logs the input and output data and associated variable values for process/BPD/services and activity/event/step. Depending on the size of the data, this can impact performance (such as potential data retrieval and writing to the trace file).CAUTION:Variables values may contain sensitive data. |
| WLE.wle\_external\_service=trace\_setting | ALL                      | The discovery and execution of external services.                                                                                                                                                                                                                                                                                                                                              |
| WLE.wle\_sched\_basic=trace\_setting      | FINER                    | The major navigation steps and key data.                                                                                                                                                                                                                                                                                                                                                       |
| WLE.wle\_sched\_basic=trace\_setting      | FINEST, ALL              | The major navigation steps and key data, as well as Event Manager task details. Depending on the size of the data, this can impact performance (such as potential data retrieval and writing to the trace file).                                                                                                                                                                               |
| WLE.wle\_engine=trace\_setting           | FINE, FINER, FINEST, ALL | The component trace of the BPD engine, which includes lightweight trace output.                                                                                                                                                                                                                                                                                                                |
| WLE.wle\_svcflow=trace\_setting          | FINE, FINER, FINEST, ALL | The component trace of the service flow engine, which includes lightweight trace output.                                                                                                                                                                                                                                                                                                       |
| WLE.wle\_scheduler=trace\_setting        | FINE, FINER, FINEST, ALL | The component trace of the Event Manager, which includes lightweight trace output.                                                                                                                                                                                                                                                                                                             |
| com.ibm.bpm.rest.*=trace\_setting       | ALL                      | The component trace of the REST API. To get lightweight REST API traces, specify the trace setting FINER instead of ALL.                                                                                                                                                                                                                                                                       |

```
WLE.wle\_engine\_basic=ALL
WLE.wle\_svcflow\_basic=ALL
WLE.wle\_sched\_basic=ALL
com.ibm.bpm.rest.*=FINER
```

## Setting the trace specifications

For specific
information about setting the trace specifications for BPDs and REST
APIs, see the following topics:

- Collect troubleshooting data for Business Process
Definition problems in IBM Business Process Manager (BPM)
- Collect troubleshooting data for BPM REST API problems
in IBM Business Process Manager (BPM)
- Setting up a trace in WebSphere Application Server

For general information about gathering troubleshooting data
for Business Automation Workflow,
see the topic Collect troubleshooting data for the IBM Business
Process Manager products.

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