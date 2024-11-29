# updateBPMExternalECM command

Traditional: 
When you add
or remove cluster members either on Business Automation Workflow or FileNet® Content
Manager, use the
updateBPMExternalECM command. This command reconciles the change from the old
list of cluster members and servers to the new list of cluster members and servers. When you update
the external Content Platform Engine,
you must run the updateBPMExternalECM command to download the Content Platform Engine libraries on the Business Automation Workflow server. See the related
topic  Updating the
Content Platform Engine client connector files. You must run this command only if Business Automation Workflow is configured with an
external ECM server.

If you are
using Content Platform Engine as a
container for integration with Business Automation Workflow and the Content Platform Engine version is 5.5.3, you
must run the BPMConfig command, and the -update and
-enableContentObjectSupport parameters to disable content object
support.

## Prerequisites

The updateBPMExternalECM command
is run by using the AdminTask object of the wsadmin scripting client.
The following conditions must be met:

- In a network deployment environment, run the
command on the deployment manager node. In a single-server environment,
run the command on the stand-alone server.
- In a network deployment environment, one or more application cluster
members must be running. In a single-server environment, the stand-alone
server must be running.
- Run the command in connected mode with a user ID that has WebSphere
Application Server configurator privileges. Do not use the wsadmin
-conntype none option.

## Location

Start the wsadmin scripting client from the
dmgr\_profile\_root/bin directory. The
updateBPMExternalECM command does not write to a log file, but the wsadmin
scripting client always writes a
profile\_root/logs/wsadmin.traceout log file where you find
exception stack traces and other information.

## Syntax

```
updateBPMExternalECM
[-de deployment\_environment\_name]
-ceUrl external\_FileNet\_content\_engine\_url
-designObjectStoreName external\_FileNet\_design\_object\_store\_name 
-clientDownloadServicePort port\_number
-clientDownloadServiceHostname CPE\_server\_hostname
[-backLinkUrl bpm\_url]
[-targetObjectStoreName external\_FileNet\_target\_object\_store\_name]
[-graphQLEndpoint content\_services\_graphql\_endpoint]
[-objectStoreName external\_FileNet\_content\_object\_store\_name]
[-omitBPMContentStoreValidation true]
```

## Parameters

If IBM® Business Automation
Workflow and Content Platform Engine are in the same WebSphere® Application
Server cell, you can use the
simpler corbaloc URI notation for this parameter, for example
corbaloc:rir:/cell/clusters/your\_websphere\_cluster\_name/FileNet/Engine. If you use
this notation, you must specify the clientDownloadServiceHostname parameter for
downloading Content Platform Engine
client .jar files from the Content Platform Engine server.

```
http://host\_name:port\_number/clientDownload?command=getVersion
```

Business Automation Workflow
automatically calculates the URL, so specify the URL only if the calculated URL is incorrect. If you
previously entered a URL but want to return to having the URL automatically calculated, enter
"".

- If you did not specify the -backLinkUrl parameter when you ran the
setBPMExternalECM admin task, you do not need to specify it with the
updateBPMExternalECM admin task. The list of available Business Automation Workflow cluster member servers is
maintained automatically.
- If you specified a list of cluster member servers by using the
-backLinkUrl parameter when you ran the setBPMExternalECM
admin task, specify this same parameter with the updateBPMExternalECM admin task.
You are responsible for updating the list of available Business Automation Workflow cluster member
servers.

A parameter that specifies the endpoint of the Content Services GraphQL for your Content Services
toolkit. If you want to use the Content Services toolkit, this parameter is required.

An optional parameter that omits the check for whether the BPM content object store name already
exists. If you are migrating Business Automation Workflow to the same version on
new hardware, you can specify this parameter to omit the check so that the BPM content object store
can be reused.

## Examples

```
wsadmin -user admin -password admin -lang jython
wsadmin>print AdminTask.updateBPMExternalECM(['-clientDownloadServicePort', '9444', '-de', 'De1', '-ceUrl', 'iiop://MigWPS7-856-T01.cn.ibm.com:2810/FileNet/Engine', '-designObjectStoreName', 'bpmdos'])
wsadmin>AdminConfig.save()
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>print AdminTask.updateBPMExternalECM(['-clientDownloadServicePort', '9444', '-clientDownloadServiceHostname', 'CPE\_server\_hostname', '-de', 'De1', '-ceUrl', 'iiop://MigWPS7-856-T01.cn.ibm.com:2810/FileNet/Engine', '-designObjectStoreName', 'bpmdos'])
wsadmin>AdminConfig.save()
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.updateBPMExternalECM(['-de', 'De1', '-backLinkUrl', 'corbaloc:iiop:BPM.mycompany.com:9010', '-ceUrl','iiop://MigWPS7-856-T01.cn.ibm.com:2810/FileNet/Engine', '-designObjectStoreName', 'bpmdos'])
wsadmin>AdminConfig.save()
```

```
iiop://external FileNet Content Engine server:2809/FileNet/Engine
```