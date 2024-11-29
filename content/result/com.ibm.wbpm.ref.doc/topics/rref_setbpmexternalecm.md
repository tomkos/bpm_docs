# setBPMExternalECM command

Traditional: 
 Use the
setBPMExternalECM command to configure IBM® Business Automation
Workflow to use an external
Enterprise Content Management server.

If you are
using Content Platform Engine as a
container for integration with Business Automation Workflow and the Content Platform Engine version is 5.5.3, you
must run the BPMConfig command, and the -update and
-enableContentObjectSupport parameters to disable content object
support.

The setBPMExternalECM command is run
by using the AdminTask object of the wsadmin scripting client.

## Prerequisites

The following conditions
must be met:

- Before the setBPMExternalECM command is run, the Business Automation Workflow system must be at version
8.5.6 or higher with any necessary upgrade or migration procedures already completed. You must run
the setBPMExternalECM command before the
startDocumentStoreMigration command.
- In clustered environments, the command must be run on the deployment manager node. In
nonclustered environments, the command must be run on the stand-alone server.
- Ensure the deployment manager or stand-alone server is running. You must connect with a user ID
that has WebSphere® Application
Server
configurator privileges. Do not use the wsadmin -conntype none option.
- The Content Platform Engine must not be shut down.

## Location

Start the wsadmin scripting client
from the profile\_root/bin directory.
The setBPMExternalECM command does not write to
a log file, but the wsadmin scripting client always writes a profile\_root/logs/wsadmin.traceout log
file where you find exception stack traces and other information.

## Syntax

```
setBPMExternalECM
[-de deployment\_environment\_name]
-ceUrl external\_FileNet\_content\_engine\_url
[-backLinkUrl bpm\_url]
-ecmEnvironment NEW\_EXTERNAL\_OBJECT\_STORE  | REASSIGN\_OBJECT\_STORE | REASSIGN\_DOMAIN
-domainName external\_FileNet\_domain\_name
-objectStoreName external\_FileNet\_object\_store\_name
-designObjectStoreName external\_FileNet\_design\_object\_store\_name
-clientDownloadServicePort port\_number
-clientDownloadServiceHostname CPE\_server\_hostname
[-targetObjectStoreName external\_FileNet\_target\_object\_store\_name]
[-GraphqlEndpoint content\_services\_graphql\_endpoint] 
[-omitBPMContentStoreValidation true]
```

## Parameters

If IBM Business Automation
Workflow and Content Platform Engine are in the same WebSphere Application
Server cell, you can use the
simpler corbaloc URI notation for this parameter, for example
corbaloc:rir:/cell/clusters/your\_websphere\_cluster\_name/FileNet/Engine. If you use
this notation, you must specify the clientDownloadServiceHostname parameter for
downloading Content Platform Engine
client .jar files from the Content Platform Engine server.

- NEW\_EXTERNAL\_OBJECT\_STORE is used if you created a new object store on an
existing external Content Platform Engine. Select this option if you followed the instructions in Configuring an existing external Content Platform Engine.
- REASSIGN\_OBJECT\_STORE is used if you used the FileNet Deployment Manager on
an external FileNet Content Platform Engine to connect to the objects
stores in Business Automation Workflow. Then,
you moved the object stores to a Content Platform Engine domain. Select this
option if you followed the instructions in Reassigning the BPM document store.
- REASSIGN\_DOMAIN is used if you created a new installation of Content Platform Engine that contains the object
stores in a Content Platform Engine
domain. Select this option if you followed the instructions in Configuring a new external Content Platform Engine.

```
http://host\_name:port\_number/clientDownload?command=getVersion
```

A parameter that specifies the endpoint of the Content Services GraphQL for your Content Services
toolkit. If you want to use the Content Services toolkit, this parameter is required.

An optional parameter that omits the check for whether the BPM content object store name already
exists. If you are migrating from Business Automation Workflow to the same version on
new hardware, you can specify this parameter to omit the check so that the BPM content object store
can be reused.

## Examples

```
wsadmin -user admin -password admin -lang jython
wsadmin>print AdminTask.setBPMExternalECM(['-clientDownloadServicePort', '9444', '-de', 'De1', '-ceUrl', 'iiop://CE.mycompany.com:2809/FileNet/Engine', '-ecmEnvironment', 'NEW\_EXTERNAL\_OBJECT\_STORE', '-domainName', 'p8domain', '-objectStoreName', 'bpmdocs', '-designObjectStoreName', 'bpmdos'])
wsadmin>AdminConfig.save()
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>print AdminTask.setBPMExternalECM(['-clientDownloadServicePort', '9444', '-clientDownloadServiceHostname', 'CPE\_server\_hostname', '-de', 'De1', '-ceUrl', 'iiop://CE.mycompany.com:2809/FileNet/Engine', '-ecmEnvironment', 'NEW\_EXTERNAL\_OBJECT\_STORE', '-domainName', 'p8domain', '-objectStoreName', 'bpmdocs', '-designObjectStoreName', 'bpmdos'])
wsadmin>AdminConfig.save()
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>print AdminTask.setBPMExternalECM(['-de', 'De1', '-ceUrl', 'iiop://CE.mycompany.com:2809/FileNet/Engine', '-ecmEnvironment', 'REASSIGN\_OBJECT\_STORE', '-domainName', 'bpm', '-objectStoreName', 'bpmdocs' '-designObjectStoreName', 'bpmdos'])
wsadmin>AdminConfig.save()
```

```
wsadmin -user admin -password admin -lang jython
wsadmin>print AdminTask.setBPMExternalECM(['-de', 'De1', '-ceUrl', 'iiop://CE.mycompany.com:2809/FileNet/Engine', '-backLinkUrl', 'corbaloc:iiop:BPM.mycompany.com:9010', '-ecmEnvironment', 'REASSIGN\_DOMAIN'])
wsadmin>AdminConfig.save()
```

```
iiop://external FileNet Content Engine server:2809/FileNet/Engine
```

```
corbaloc::node1\_hostname:BOOTSTRAP\_ADDRESS, :node2\_hostname:BOOTSTRAP\_ADDRESS/cell/clusters/your\_websphere\_cluster\_name/FileNet/Engine
```

```
corbaloc:iiop:<Business Process Manager cluster member>:9010
```

```
BPMclustermember1-hostname:bootstrapaddr>,<BPMclustermember2-hostname:bootstrapaddr>, ... corbaloc:iiop:<Business Process Manager cluster member1-hostname:bootstrapaddr>,iiop:<Business Process Manager cluster member2-hostname:bootstrapaddr>[,...]
```

A configuration changes over time. For example, a cluster member is added. Use the
updateBPMExternalECM command to update your configuration. See updateBPMExternalECM command.