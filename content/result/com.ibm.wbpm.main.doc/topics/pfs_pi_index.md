# BPD process instance indexing

By default, when configuring the <ibmPfs\_bpdIndexer> tag, BPD process
instances are indexed by Process Federation Server in the
federated data repository. Your federated systems must be properly set up for process instance
indexing. It is also possible to disable process instance indexing in your Process Federation Server configuration
file.

## Indexing BPD process instances from Process Federation Server

If the federated system is a Business Automation Workflow V20.0.0.1 server or
later, no further step is required to support BPD process instance indexing from Process Federation Server.

- If the federated system is a Business Automation Workflow server V18.0.0.2 to
V19.0.0.3 (included), you must first install APAR JR61986.
- If the federated system is a Business Automation Workflow server V18.0.0.1 or
earlier and has APAR JR59873 installed, you must first uninstall APAR JR59873 by using Installation
Manager.
- If the federated system is an IBM® BPM server and has APAR
JR59873 installed, you must first uninstall APAR JR59873 by using Installation Manager.

## Disabling BPD process instance indexing

```
<ibmPfs\_federatedSystem>
	id="mySystem"
	indexProcessInstances="false"
	...
</ibmPfs\_federatedSystem>
```