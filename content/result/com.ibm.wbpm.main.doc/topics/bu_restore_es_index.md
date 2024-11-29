# Backing up and restoring Process Federation Server indexes in the
federated data repository

The following procedures apply to BPD and BPEL systems when indexing is done by Process Federation Server, and are based
on standard Elasticsearch and OpenSearch snapshots. It also includes backing up Process Federation Server indexers states
in Elasticsearch or OpenSearch indexes.

## Limitations

This section only concerns Process Federation Server traditional on
premise deployments (not supported on container deployments).

## Prerequisites

To be able to create backups and restore indexes you must:

- Allow the federated data repository in which Process Federation Server creates indexes
for the federated systems to perform snapshots and restore operations. See Elasticsearch: Snapshot and restore or OpenSearch: Take and restore snapshots depending on whether
you use Elasticsearch or OpenSearch for the federated data repository.
- Have the pfsAdministrator role to be able to use the new Process Federation Server Management REST
API. To do so, add the following entry in the <authorization-roles
id="com.ibm.bpm.federated.rest.authorization"> section of the Process Federation Server
server.xml configuration
file:<!--  The following role is used to allow users access to the Process Federation Server management API. It does not grant any authorization related to saved searches -->
<security-role name="pfsAdministrator">
<!-- TO SPECIFY PFS ADMINISTRATOR MEMBERSHIP, ADD user, group, OR special-subject ELEMENTS -->
</security-role>

## Backing up the current state

You can perform a backup of the current state of your federated systems indexes. When necessary,
you can resume indexing from when the backup was done instead of having to rebuild the complete
index.

1 Back up the current state of the indexers by calling the following Process Federation Server Management RESTAPI:PUT /rest/bpm/federated/v2/management/indexers/backupState See PUTmethod . For each federated system that has at least one indexer defined in the Process Federation Server server.xml configuration file, the API will try to create a backup document for theindexer state in the corresponding federated system index. It will then report the result of theoperation by returning a JSON array that contains one document per processed federated system, withthe following attributes for each one: Process Federation Server console displays the following message per indexer that created a backup of its state:

PUT /rest/bpm/federated/v2/management/indexers/backupState

See PUT
method.

    - federatedSystem : a JSON object describing the federated system with thefollowing attributes:
        - id: the id of the federated system, as declared in the
server.xml configuration file
        - systemID: the id of the federated system, as returned by the /systems API
        - displayName: the display name of the federated system, as declared in the
server.xml configuration file
- indexName: the name of the federated data repository index for this federated
system
- status: the status of the operation, which is ok if the backup
was performed and error if it failed.
- errorMessage: when the status attribute is
error, this attribute contains a message that explains why the backup failed for
this federated system.
- restorationTimestamp: when the status attribute is
ok, this attribute contains an UTC timestamp that indicates the timestamp of the
Process Federation Server Change
log table entries in the federated system database from which indexing will resume if the backup is
restored.
- recordTimestamp: when the status attribute is
ok, this attribute contains an UTC timestamp that indicates when the backup was
performed.

- BPD indexers: [INFO ] CWMFS2544I: Agent XXX for XXX: backup of the current indexer state
has been performed in index XXX with restoration timestamp XXX.
- BPEL indexers: [INFO ] CWMFS3330I: Agent XXX for XXX: backup of the current indexer state
has been performed in index XXX with restoration timestamp XXX.
2. Verify if there are any unexpected failure reported for a federated system. If it is the case,
fix the issue and then re-attempt the backup. An index cannot be properly restored if it does not
contain the backup document created when performing the backup.
Note: Having a backup document
for the index state on an index has a side effect on the change log table operations for the
corresponding federated system: if a task or process is deleted from the federated system after the
restorationTimestamp recorded in the backup document, the corresponding task or
process will be deleted from the federated data repository index but the corresponding change log
entries will not be deleted (so that they can be properly deleted in a restored index). Because
those entries will only be deleted after a new backup of the indexer state has been performed, you
must perform regular backups to avoid unexpected growth of the change log table. For the same
reason, you must not delete the backup document from an index after the Elasticsearch or OpenSearch
snapshot has been performed (step 4).
3 Retrieve the latest backup documents for all federated system indexes by calling the followingProcess Federation Server Management REST API:GET/rest/bpm/federated/v2/management/indexers/backupState See GETmethod . For each federated system that have at least one indexer defined in theProcess Federation Server server.xml configuration file, this API will try to create a backup document forthe indexer state in the corresponding federated system index and will report the result of theoperation by returning a JSON array that contains one document per processed federated system, withthe following attributes for each one: Note: If you need to delete the latest indexer state backup document, use the deletion APIDELETE /rest/bpm/federated/v2/management/indexers/backupState . See DELETEmethod . After a successful deletion, the Process Federation Server consoledisplays the following message per indexer that deleted the backup of its state:

GET
/rest/bpm/federated/v2/management/indexers/backupState

See GET
method.

- federatedSystem : a JSON object describing the federated system with thefollowing attributes:
    - id: the id of the federated system, as declared in the
server.xml configuration file
    - systemID: the id of the federated system, as returned by the /systems API
    - displayName: the display name of the federated system, as declared in the
server.xml configuration file
- indexName: the name of the federated data repository index for this federated
system
- status: the status of the operation, which is ok if the backup
was performed and error if it failed.
- errorMessage: when the status attribute is
error, this attribute contains a message that explains why the backup failed for
this federated system.
- restorationTimestamp: when the status attribute is
ok, this attribute contains an UTC timestamp that indicates the timestamp of the
Process Federation Server Change
log table entries in the federated system database from which indexing will resume if the backup is
restored.
- recordTimestamp: when the status attribute is
ok, this attribute contains an UTC timestamp that indicates when the backup was
performed.

- BPD indexers: [WARNING ] CWMFS2545W: Agent XXX for XXX: last indexer state backup has
been deleted from index XXX.
- BPEL indexers:[WARNING ] CWMFS3331W: Agent XXX for XXX: last indexer state backup has
been deleted from index XXX.
4. Backup the federated systems Elasticsearch or OpenSearch indexes, including the dedicated
document created during the back up of the current state of the indexers, by using the vendor
snapshot REST API. See Elasticsearch: Create a snapshot or OpenSearch: Take snapshots depending on whether you use
Elasticsearch or OpenSearch for the federated data repository.

## Restoring federated systems indexes

You can restore the federated systems indexes from their backup state to resume the indexing from
this state.

1. Restore the Elasticsearch or OpenSearch indices from a snapshot by calling the vendor restore
REST API. See Elasticsearch: Restore a snapshot or OpenSearch: Restore snapshots depending on whether you use
Elasticsearch or OpenSearch for the federated data repository.
2 Request Process Federation Server indexers toresume the indexing from their backup state by calling the following Process Federation Server Management RESTAPI:PUT /rest/bpm/federated/v2/management/indexers/restoreState See PUTmethod . For each federated system that have at least one indexer defined in theProcess Federation Server server.xml configuration file, this API will try to create a backup document forthe indexer state in the corresponding federated system index and will report the result of theoperation by returning a JSON array that contains one document per processed federated system, withthe following attributes for each one: The Process Federation Server consoledisplays the following message per indexer that have properly recorded the request to resumeindexing from the backup state:

PUT /rest/bpm/federated/v2/management/indexers/restoreState

See PUT
method.

    - federatedSystem : a JSON object describing the federated system with thefollowing attributes:
        - id: the id of the federated system, as declared in the
server.xml configuration file
        - systemID: the id of the federated system, as returned by the /systems API
        - displayName: the display name of the federated system, as declared in the
server.xml configuration file
- id: the id of the federated system, as declared in the
server.xml configuration file
- systemID: the id of the federated system, as returned by the /systems API
- displayName: the display name of the federated system, as declared in the
server.xml configuration file
- indexName: the name of the federated data repository index for this federated
system
- status: the status of the operation, which is ok if the backup
was performed and error if it failed.
- errorMessage: when the status attribute is error, this
attribute contains a message that explains why the backup failed for this federated system.
- restorationTimestamp: when the status attribute is
ok, this attribute contains an UTC timestamp that indicates the timestamp of the
Process Federation Server Change
log table entries in the federated system database from which indexing will resume if the backup is
restored.
- recordTimestamp: when the status attribute is
ok, this attribute contains an UTC timestamp that indicates when the backup was
performed.

- BPD indexers: [INFO ] CWMFS2542I: Agent XXX for XXXX: re-indexing of events has been
requested for index XXX. This will be performed on the next indexers restart
- BPEL indexers: [INFO ] CWMFS3332I: Agent XXX for XXXX: re-indexing of events has been
requested for index XXX. This will be performed on the next indexers restart.
3. Verify if there are any unexpected failure reported for a federated system. If it is the case,
fix the issue and then re-attempt the restoration. If indexing cannot be resumed from a backup state
for a restored index, the only alternative is to completely rebuild the index using the documented
procedure. See Rebuilding an index
Note: If you ever call the Process Federation Server Management REST
API PUT /rest/bpm/federated/v2/management/indexers/restoreState by mistake, you can
cancel it by calling the DELETE
/rest/bpm/federated/v2/management/indexers/restoreState before restarting the indexers. See
DELETE method.
4 Restart the Process Federation Server indexers sothat they resume their indexing by restarting all servers.The Process Federation Server consoledisplays the following message after restart, when the indexers notify that they started resumingthe indexing:

- BPD indexers
    - [INFO ] CWMFS2540I: Agent XXX for XXX: rebuild of index XXX has been requested and
partial re-indexing of events from XXX will be performed....
    - [INFO ] CWMFS2541I: Agent XXX for XXX: reset of all consumer column XXX entries after XXX
has been completed.
- BPEL indexers

- [INFO ] CWMFS3325I: Agent XXX for XXX: rebuild of index XXX has been requested and
partial re-indexing of events from XXX will be performed....
- [INFO ] CWMFS3326I: Agent XXX for XXX: reset of all consumer column XXX entries after XXX
has been completed.