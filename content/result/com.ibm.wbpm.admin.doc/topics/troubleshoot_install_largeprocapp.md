# Preventing timeout and out-of-memory exceptions during installation
or deployment

## About this task

```
CWPFD2064W: A timeout occurred during processing of the job
With a root cause: WTRN0124I: When the timeout occurred the thread with which the transaction ... sun.misc.Unsafe.park(Native Method)
```

```
CWPFD1300E: Service deploy failed with return code 3 
With a root cause: java.lang.OutOfMemoryError
```

- com.ibm.bpm.pal.deploy.timeout Use this property to set a new
timeout value for the installation. The value is specified in seconds.
To revert to the default behavior, delete the system property or set
the value to 720.
- com.ibm.bpm.fds.sca.deploy.outOfProcess Set the value of this
property to true so that serviceDeploy runs
in a new process for each SCA module in the process application. Be
aware that this causes noticeable performance degradation of the overall
installation process. If you set this system property, consider also
setting the com.ibm.bpm.pal.deploy.timeout property to a value larger
than the default. 
To revert to the default behavior, delete
the system property or set the value to false.

## Procedure

To set one or both of these system properties, use the
following steps.

1. Log in to the WebSphere Application Server administrative
console.
2. Select the server by clicking Servers  > Server Types > WebSphere application
servers > server\_name.
3. From the Server Infrastructure area, click Java and Process Management > Process
definition > Java Virtual Machine > Custom Properties.
4. Create one or both of these custom properties: name = com.ibm.bpm.pal.deploy.timeout
value = timeout\_value

name = com.ibm.bpm.fds.sca.deploy.outOfProcess
value = trueThe timeout value is specified in seconds.
5. Click OK and save the changes to
the configuration when prompted.
6. Restart the server.