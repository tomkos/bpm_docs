# Process Federation Server messages reference

Reference list of all Process Federation Server messages.

## Message codes starting with CWMFS

| Explanation   | The Process Federation Server federated data repository monitoring service, that monitors the availability of the federated data repository, is starting. This message is expected at the start of Process Federation Server.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                                                                                              |

| Explanation   | The Process Federation Server federated data repository monitoring service, that monitors the availability of the federated data repository, is stopping. This message is expected when Process Federation Server is stopping.   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                                                                                               |

| Explanation   | A severe error (with message {0}) occurred in the federated data repository monitoring service, that monitors the availability of the federated data repository, causing it to stop running.                                                                                                                                                                                                              |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | In addition to the error displayed in the message, an FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. Once the error cause is solved, the Process Federation Server instance must be restarted in order for the federated data repository monitoring service to be restarted. |

| Explanation   | The remote federated data repository cluster is up and running and the federated data repository service, that connects Process Federation Server to the federated data repository service, is now available.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                                                                              |

| Explanation   | The remote federated data repository cluster is not responding and the federated data repository service, that connects Process Federation Server to the federated data repository service, is not available anymore.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Ensure that the remote federated data repository cluster is up and running and can be reached through the endpoint URLs specified in the  configuration element in server.xml.                                          |

| Explanation   | The status of the federated data repository cluster has changed and is now one of the following: "green" (all shards are assigned), "yellow" (all primary shards are assigned but one or more replica shards are unassigned), or "red" (one or more primary shards are unassigned).   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | If the displayed status is not "green", you must take action on the federated data repository cluster in order to bring it to a "green" state.                                                                                                                                        |

| Explanation   | A communication error occurred when monitoring the availability of the federated data repository cluster.   |
|---------------|-------------------------------------------------------------------------------------------------------------|
| Action        | use the error message {0} to diagnose and fix the cause of the communication error.                         |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | Process Federation Server failed to create an index in the federated data repository.                                                                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | In addition to the error displayed in the message, an FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | The indexName property of an ibmPfs\_federatedSystem configuration element in server.xml contains upper case characters, or begins with an underscore, or contains commas.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Update the indexName property value to use lower case charaters, not begin with an underscore and not contain any comma.                                                    |

| Explanation   | The authenticationMechanism property of an ibmPfs\_federatedSystem configuration element in server.xml has an unsupported value.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Action        | Use a supported value for authenticationMechanism: LTPA (default) or PFS\_ACCESS\_TOKEN                                             |

| Explanation   | Displays the value of the authenticationMechanism property of an ibmPfs\_federatedSystem configuration element in server.xml   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                            |

| Explanation   | A mandatory property for an ibmPfs\_federatedSystem configuration element in server.xml is missing.                                              |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Update the ibmPfs\_federatedSystem configuration element in server.xml to add a value for the mandatory property specified in the error message. |

| Explanation   | An error occurred in a BPD indexer indexing data in federated data repository index {0}.                                                                                                                                                 |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | In addition to the error displayed in the message at {1}, an FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | The maximum number of consecutive errors after which a BPD indexer will stop processing data, defined by attribute numberOfRetries of the ibmPfs\_bpdIndexer configuration element in server.xml has been reached.                                                                               |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | The PFS server must be restarted in order to restart the indexer. If BPD indexers shouldn't be stopped whatever the number of consecutive errors occurring during the indexing, attribute numberOfRetries of the ibmPfs\_bpdIndex configuration element in server.xml should be set to value -1. |

| Explanation   | A SyncTasks maintenance operation completed for a BPD indexer indexing data in federated data repository index {0}. The message details how many tasks where synchronized and how long it took.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                                                                |

| Explanation   | All the consumer columns defined in the PFS\_CHANGE\_LOG\_CONSUMER table have been claimed.                                                      |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Ensure that all the CONSUMER\_* columns defined in the PFS\_BPD\_CHANGE\_LOG table have a corresponding row in the PFS\_CHANGE\_LOG\_CONSUMER table. |

| Explanation   | A BPD indexer found a task that has been deleted from the federated BPD database and will delete it from the search index.   |
|---------------|------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                           |

| Explanation   | A BPD indexer cycle took more that the threshold defined by attribute indexProcessingWarningThreshold of the ibmPfs\_bpdIndexer configuration element in server.xml (default value: 3 seconds).                                                                                                                                                                                                                                                                                                     |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | If this warning is displayed for each cycle, it indicates that the indexing performances do not match the one specified with the threshold value. Low indexing performances can be caused by a slow connection to the federated database, a performance issue on the federated database, of performance issue with the federated data repository. Setting the trace level to com.ibm.bpm.federated.indexer.bpd.*=all will generate indexer traces that can help to diagnose the performance issue. |

| Explanation   | A maintenance operation of a BPD indexer took more that the threshold defined by attribute maintenanceProcessingWarningThreshold of the ibmPfs\_bpdIndexer configuration element in server.xml (default value: 5 seconds).   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | If this warning is displayed everytime a maintenance operation is run, that may indicate a performance issue with the federated BPD database or that the maintenance operation should be run more often.                    |

| Explanation   | The BPD indexer with identifier {0}, defined in server.xml for federated system {1}, has been activated.                                                                                                                             |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | This message is expected at the start of the PFS server for each BPD indexer defined in server.xml. If this message is not displayed in the logs, that means that the corresponding indexer has not been activated and will not run. |

| Explanation   | The BPD indexer with identifier {0}, defined in server.xml for federated system {1}, has been deactivated and will stop indexing data.                                                                                                                                                  |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | This message is expected for each BPD indexer defined in server.xml when the PFS server stops. If this message is displayed while the server is not stopping, it indicates that a dependency of the indexer component (such as the federated data repository) is not available anymore. |

| Explanation   | The timestamp attribute {1} defined in an ibmPfs\_bpdIndexer configuration element in server.xml is not in the expected format.   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------|
| Action        | Specify a value for this timestamp attribute that match the specified format {2}                                                 |

| Explanation   | The timestamp attribute {1} defined in an ibmPfs\_bpdIndexer configuration element in server.xml has a value that is not in the past.   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Specify a value that is in the past for this timestamp attribute                                                                       |

| Explanation   | Process Federation Server failed to register an MBean for a BPD indexer.                                                                                                       |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | An FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | Process Federation Server failed to unregister the MBean of a BPD indexer.                                                                                                     |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | An FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | A BPD indexer found a process instance that has been deleted from the federated BPD database and will delete it from the search index.   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                       |

| Explanation   | A SyncInstances maintenance operation completed for a BPD indexer indexing data in federated data repository index {0}. The message details how many process instances where synchronized and how long it took.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                                                                                |

| Explanation   | A request to run an unscheduled execution of maintenance operation {0} has been ignored by Process Federation Server because instance indexing is not enabled for federated system {1}, which means that running this maintenance operation is useless.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                                                                                                                        |

| Explanation   | An operation was triggered on a BPD indexer (for example, a request to backup the indexer state) while the state of the indexer does not allow it (the indexer is in an initializing state and is not yet able to perform the requested operation).   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Wait for the indexer initialization to have completed (log messages signaling that the indexer has started indexing) before re triggering the requested operation.                                                                                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | Indexing failure(s) have been reported by the federated data repository when a BPD indexer tried to update documents in index {0}.   |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Use the indexing failure messages reported in this log to diagnose and fix the issue in the federated data repository.               |

| Explanation   | A restoration of a BPD indexer state was requested but an error occurred when Process Federation Server tried to retrieve the restoration timestamp from the index.    |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Use the error message provided in the log to diagnose and fix the issue.                                                                                               |

| Explanation   | A restoration of a BPD indexer state was requested but no restoration timestamp was retrieved from the index, so the request has been cancelled.   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Make sure to perform backups before requesting a restoration.                                                                                      |

| Explanation   | A restoration of a BPD indexer state was requested and is now starting.   |
|---------------|---------------------------------------------------------------------------|
| Action        | No action required                                                        |

| Explanation   | The restoration of a BPD indexer state has completed.   |
|---------------|---------------------------------------------------------|
| Action        | No action required                                      |

| Explanation   | A request to restore a BPD indexer state has been recorded. The restoration will be performed on the next indexer restart.   |
|---------------|------------------------------------------------------------------------------------------------------------------------------|
| Action        | Restart a PFS server to trigger a restart of the BPD indexers.                                                               |

| Explanation   | A previous request to restore a BPD indexer state has been cancelled.                                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Action        | A new request to restore the BPD indexer state will need to be issued in order to trigger a restoration when the indexer restart. |

| Explanation   | A backup of the current state of a BPD indexer has successfully completed.   |
|---------------|------------------------------------------------------------------------------|
| Action        | A snapshot of the index can now be completed in order to backup it.          |

| Explanation   | The last state backup of BPD indexer has been deleted.                 |
|---------------|------------------------------------------------------------------------|
| Action        | Request a new backup of the BPD indexer state when a backup is needed. |

| Explanation   | The initialization of the BPD indexer has completed and it will now start to index data in the federated data repository.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                          |

| Explanation   | An error occured when a BPD indexer tried to index data in the federated data repository.   |
|---------------|---------------------------------------------------------------------------------------------|
| Action        | Use the error message provided in the log to diagnose and fix the issue.                    |

| Explanation   | An error occurred in a BPEL indexer indexing data in federated data repository for federated system {0}.                                                                                                                                 |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | In addition to the error displayed in the message at {1}, an FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | The maximum number of consecutive errors after which a BPEL indexer will stop processing data, defined by attribute numberOfRetries of the ibmPfs\_bpelIndexer configuration element in server.xml has been reached.                                                                               |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | The PFS server must be restarted in order to restart the indexer. If BPEL indexers shouldn't be stopped whatever the number of consecutive errors occurring during the indexing, attribute numberOfRetries of the ibmPfs\_bpelIndex configuration element in server.xml should be set to value -1. |

| Explanation   | An error occurred when a BPEL indexer tried to retrieve data of process instance {0} from the federated BPEL database.                                                                                                                   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | In addition to the error displayed in the message at {1}, an FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | An error occurred when a BPEL indexer tried to retrieve data of process template {0} from the federated BPEL database.                                                                                                                   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | In addition to the error displayed in the message at {1}, an FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | An error occurred when a BPEL indexer tried to retrieve data of object {0} from the federated BPEL database.                                                                                                                                        |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | In addition to the error displayed in the message at {1}, an FFDC file with a complete stack trace of the error may have been generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | A NullPointerException error occurred when a BPEL indexer tried to retrieve data of task instance {1} from the federated BPEL database.                                                                                                  |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | In addition to the error displayed in the message at {1}, an FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | An error occurred when a BPEL indexer tried to retrieve data of task instance {1} from the federated BPEL database.                                                                                                                      |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | In addition to the error displayed in the message at {0}, an FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | An error occurred when a BPEL indexer tried to retrieve data of task template {1} from the federated BPEL database.                                                                                                                      |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | In addition to the error displayed in the message at {0}, an FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | An error occurred when a BPEL indexer tried to create a JDBC connection to the federated BPEL database.   |
|---------------|-----------------------------------------------------------------------------------------------------------|
| Action        | Use the exception details in {1} to diagnose and fix the issue.                                           |

| Explanation   | A BPEL indexer was not able to retrieve the template data for a task and is therefore unable to index it.   |
|---------------|-------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                          |

| Explanation   | An error occurred when updating the properties of a BPEL indexer using the configuration attributes specified in server.xml   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------|
| Action        | Use the exception details in {0} and {1} to diagnose and fix the issue.                                                       |

| Explanation   | No BPEL process instance data could be retrieved by a BPEL indexer for a task: the task will be indexed without any business data.   |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                   |

| Explanation   | The BPEL indexer with identifier {0}, defined in server.xml for federated system {1}, has been activated.                                                                                                                             |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | This message is expected at the start of the PFS server for each BPEL indexer defined in server.xml. If this message is not displayed in the logs, that means that the corresponding indexer has not been activated and will not run. |

| Explanation   | The BPEL indexer with identifier {0}, defined in server.xml for federated system {1}, has been deactivated and will stop indexing data.                                                                                                                                                  |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | This message is expected for each BPEL indexer defined in server.xml when the PFS server stops. If this message is displayed while the server is not stopping, it indicates that a dependency of the indexer component (such as the federated data repository) is not available anymore. |

| Explanation   | The timestamp attribute {1} defined in an ibmPfs\_bpelIndexer configuration element in server.xml is not in the expected format.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Action        | Specify a value for this timestamp attribute that match the specified format {2}                                                  |

| Explanation   | Process Federation Server failed to register an MBean for a BPEL indexer.                                                                                                      |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | An FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | Process Federation Server failed to unregister the MBean of a BPEL indexer.                                                                                                    |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | An FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | Indexing failure(s) have been reported by the federated data repository when a BPEL indexer tried to update documents in index {0}.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Use the indexing failure messages reported in this log to diagnose and fix the issue in the federated data repository.                |

| Explanation   | A restoration of a BPEL indexer state was requested but an error occurred when Process Federation Server tried to retrieve the restoration timestamp from the index.    |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Use the error message provided in the log to diagnose and fix the issue.                                                                                                |

| Explanation   | A restoration of a BPEL indexer state was requested and is now starting.   |
|---------------|----------------------------------------------------------------------------|
| Action        | No action required                                                         |

| Explanation   | The restoration of a BPEL indexer state has completed.   |
|---------------|----------------------------------------------------------|
| Action        | No action required                                       |

| Explanation   | A restoration of a BPEL indexer state was requested but no restoration timestamp was retrieved from the index, so the request has been cancelled.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Make sure to perform backups before requesting a restoration.                                                                                       |

| Explanation   | A previous request to restore a BPEL indexer state has been cancelled.                                                             |
|---------------|------------------------------------------------------------------------------------------------------------------------------------|
| Action        | A new request to restore the BPEL indexer state will need to be issued in order to trigger a restoration when the indexer restart. |

| Explanation   | An operation was triggered on a BPEL indexer (for example, a request to backup the indexer state) while the state of the indexer does not allow it (the indexer is in an initializing state and is not yet able to perform the requested operation).   |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Wait for the indexer initialization to have completed (log messages signaling that the indexer has started indexing) before re triggering the requested operation.                                                                                     |

| Explanation   | A backup of the current state of a BPEL indexer has successfully completed.   |
|---------------|-------------------------------------------------------------------------------|
| Action        | A snapshot of the index can now be completed in order to backup it.           |

| Explanation   | The last state backup of BPEL indexer has been deleted.                 |
|---------------|-------------------------------------------------------------------------|
| Action        | Request a new backup of the BPEL indexer state when a backup is needed. |

| Explanation   | A request to restore a BPEL indexer state has been recorded. The restoration will be performed on the next indexer restart.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------|
| Action        | Restart a PFS server to trigger a restart of the BPEL indexers.                                                               |

| Explanation   | The initialization of the BPEL indexer has completed and it will now start to index data in the federated data repository.   |
|---------------|------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                           |

| Explanation   | An error occured when a BPD indexer tried to index data in the federated data repository.   |
|---------------|---------------------------------------------------------------------------------------------|
| Action        | Use the error message provided in the log to diagnose and fix the issue.                    |

| Explanation   | A REST API has been called with a value for the system ID parameter that was not found for any federated system.                            |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Contact your system administrator for the ID value or check the federatedResults section of the query results for the 'systemID' attribute. |

| Explanation   | No additional information is available.                                                                                      |
|---------------|------------------------------------------------------------------------------------------------------------------------------|
| Action        | Use one of the following values: WORK\_ON, WORK\_ON\_ACTIVE, ASSESS\_AVAILABLE, ASSESS\_AND\_WORK\_ON, CHECK\_COMPLETED, BROWSE\_ALL. |

| Explanation   | The value of the size or offset parameters is not valid.    |
|---------------|-------------------------------------------------------------|
| Action        | Verify that the value of the parameters is zero or greater. |

| Explanation   | The value of the size parameter is not valid.                                                     |
|---------------|---------------------------------------------------------------------------------------------------|
| Action        | Verify that the value of the parameter is less than the maximum value setup by the administrator. |

| Explanation   | No additional information is available.                    |
|---------------|------------------------------------------------------------|
| Action        | Check the system logs for issues with the query execution. |

| Explanation   | The Origin header in the REST request can have only one address.       |
|---------------|------------------------------------------------------------------------|
| Action        | Submit a REST request with an Origin header that has only one address. |

| Explanation   | The request to retrieve group information for the current user failed.   |
|---------------|--------------------------------------------------------------------------|
| Action        | Check system logs for issues with the retrieval.                         |

| Explanation   | No additional information is available.    |
|---------------|--------------------------------------------|
| Action        | Check the system logs for indexing issues. |

| Explanation   | The Process Federation Server server.xml file must have a least one configured federated system.                                             |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify the Process Federation Server server.xml file contains a configured ibmPfs\_federatedSystem element for each of the federated systems. |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Check the system logs for more details.   |

| Explanation   | No additional information is available.                  |
|---------------|----------------------------------------------------------|
| Action        | Check the system logs for issues with the query service. |

| Explanation   | No additional information is available.                 |
|---------------|---------------------------------------------------------|
| Action        | Check the system logs for issues about missing indexes. |

| Explanation   | No additional information is available.                           |
|---------------|-------------------------------------------------------------------|
| Action        | Check the system logs for issues with the query service indexing. |

| Explanation   | No additional information is available.                                                                                                    |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify that the ibmPfs\_federatedSystem element in the Process Federation Server server.xml file has a configured allowedOrigins attribute. |

| Explanation   | No additional information is available.                 |
|---------------|---------------------------------------------------------|
| Action        | Check the system logs for issues with the REST service. |

| Explanation   | No additional information is available.                 |
|---------------|---------------------------------------------------------|
| Action        | Check the system logs for issues with the REST service. |

| Explanation   | No additional information is available.        |
|---------------|------------------------------------------------|
| Action        | You must configure at least a federated system |

| Explanation   | No additional information is available.                                   |
|---------------|---------------------------------------------------------------------------|
| Action        | Verify that the value of the 'offset' query parameter is zero or greater. |

| Explanation   | No additional information is available.                                 |
|---------------|-------------------------------------------------------------------------|
| Action        | Verify that the value of the 'size' query parameter is zero or greater. |

| Explanation   | No additional information is available.            |
|---------------|----------------------------------------------------|
| Action        | Remove the specified sort fields from the request. |

| Explanation   | The specified user does not have access to any federated systems.        |
|---------------|--------------------------------------------------------------------------|
| Action        | Check the requesting user has access to all necessary federated systems. |

| Explanation   | No additional information is available.                                                                                                          |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify that the federated system retriever in the Process Federation Server server.xml file has a value for the internalRestUrlPrefix attribute. |

| Explanation   | A request from the REST service to a federated system failed.                           |
|---------------|-----------------------------------------------------------------------------------------|
| Action        | Check the system logs for issues with the REST service request to the federated system. |

| Explanation   | No additional information is available.                                |
|---------------|------------------------------------------------------------------------|
| Action        | Check that the user has access to all the necessary federated systems. |

| Explanation   | No additional information is available.                      |
|---------------|--------------------------------------------------------------|
| Action        | Check security authorization is enabled on the REST service. |

| Explanation   | No additional information is available.                                              |
|---------------|--------------------------------------------------------------------------------------|
| Action        | Check the system logs for issues with REST service requests to the federated system. |

| Explanation   | The retrieval agent was not found for this federated system.                                               |
|---------------|------------------------------------------------------------------------------------------------------------|
| Action        | Verify Process Federation Server has a retriever defined in the server.xml file for each federated system. |

| Explanation   | The federated system did not respond to the request for information or status.   |
|---------------|----------------------------------------------------------------------------------|
| Action        | Verify the federated system configuration in the server.xml file.                |

| Explanation   | A federated system has a unique system ID. Process Federated Server accesses the federated system and requests the system ID. When two federated systems have the same system ID, it means that the two definitions point to the same system.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify the addresses of the federated system definitions in the server.xml file.                                                                                                                                                                |

| Explanation   | There may be a difference in system clocks between Process Federated Server and the federated system causing the SSO token to be invalid on the Federated system and not on the Process Federated Server.    |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Check the system clocks for this Process Federated Server and the federated system.                                                                                                                          |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | No action required.                       |

| Explanation   | There is a user required sort field that does not exist on this index. Indexes cannot be sorted on non-existent fields.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------|
| Action        | If the index is required, remove the sort field from the request.                                                         |

| Explanation   | No additional information is available.                                              |
|---------------|--------------------------------------------------------------------------------------|
| Action        | Check the system logs for issues with REST service requests to the federated system. |

| Explanation   | No additional information is available.                                         |
|---------------|---------------------------------------------------------------------------------|
| Action        | Verify the field name is a predefined field name or a business data field name. |

| Explanation   | The field name that was requested is not allowed to be returned. Only fields that are listed in the saved search are allowed.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify the field name exists in the saved search.                                                                               |

| Explanation   | The field name that was requested is not allowed to be used for sorting. Only fields that are listed in the saved search are allowed.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify the sort field name exists in the saved search.                                                                                  |

| Explanation   | No additional information is available.                                              |
|---------------|--------------------------------------------------------------------------------------|
| Action        | Verify that the federated systems have indexing enabled and the systems are running. |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the field name.                    |

| Explanation   | The value of the sort parameter must be a comma-separated list of fields. It can include a sort order, either 'ASC' or 'DESC', for example: 'DUE ASC, PRIORITY'.   |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify the sort parameter.                                                                                                                                         |

| Explanation   | The sort order must be one of 'ASC', 'DESC', or not used, for example: 'DUE ASC, PRIORITY'.   |
|---------------|-----------------------------------------------------------------------------------------------|
| Action        | Verify the sort order.                                                                        |

| Explanation   | No additional information is available.                                                                                        |
|---------------|--------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify that the value of the query parameter is a valid date formated as YYYY-MM-DDThh:mm:ssZ (example: 2011-08-04T03:12:53Z). |

| Explanation   | No additional information is available.                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify that the value of the 'searchFilterScope' query parameter is one of the following: AppShortName, InstanceName, All. |

| Explanation   | No additional information is available.                                                                                                               |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify that the value of the 'statusFilter' query parameter is one of the following: Active, Completed, Failed, Terminated, Did\_not\_Start, Suspended. |

| Explanation   | The Process Federation Server server.xml file must have a least one configured federated system which performs process instance indexing.                                                                                                           |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify the Process Federation Server server.xml file contains either a configured ibmPfs\_federatedSystem element with indexProcessInstances attribute set to "true" for a BPD system or a ibmPfs\_federatedSystem element for a Case Manager system. |

| Explanation   | The value of the system ID parameter does not match a federated system with process instance indexing enabled.                              |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Contact your system administrator for the ID value or check the federatedResults section of the query results for the 'systemID' attribute. |

| Explanation   | No additional information is available.                                                                         |
|---------------|-----------------------------------------------------------------------------------------------------------------|
| Action        | Verify that the value of the 'processTypeFilter' query parameter is one of the following: Workflow, Workstream. |

| Explanation   | No additional information is available.                                     |
|---------------|-----------------------------------------------------------------------------|
| Action        | Make sure that the team exists and that the user is a manager of this team. |

| Explanation   | No additional information is available.                    |
|---------------|------------------------------------------------------------|
| Action        | Make sure that the user is a manager of at least one team. |

| Explanation   | No additional information is available.                                                  |
|---------------|------------------------------------------------------------------------------------------|
| Action        | Verify that the value of the 'units' query parameter is one of the following: DAY, HOUR. |

| Explanation   | No additional information is available.                                                       |
|---------------|-----------------------------------------------------------------------------------------------|
| Action        | Verify that the value of the 'numPeriods' query parameter is one of the following: DAY, HOUR. |

| Explanation   | No additional information is available.                                                              |
|---------------|------------------------------------------------------------------------------------------------------|
| Action        | Verify that the value of the 'caseScope' query parameter is one of the following: Allowed, Assigned. |

| Explanation   | No additional information is available.                                                                                                |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify that the value of the 'searchFilterScope' query parameter is one of the following: AppShortName, InstanceName, TemplateId, All. |

| Explanation   | No additional information is available.                                                                                                                                           |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify that the value of the 'statusFilter' query parameter is one of the following: Active, Completed, Failed, Terminated, Did\_not\_Start, Suspended, New, Initializing, Working. |

| Explanation   | No additional information is available.                                                                                             |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify that the value of the 'statusFilter' query parameter is one of the following: New, Initializing, Working, Completed, Failed. |

| Explanation   | No additional information is available.                                                              |
|---------------|------------------------------------------------------------------------------------------------------|
| Action        | Verify that the value of the 'instanceType' query parameter is one of the following: BPD, Case, All. |

| Explanation   | No additional information is available.                                                                       |
|---------------|---------------------------------------------------------------------------------------------------------------|
| Action        | Make sure that the team exists, that the user is a manager of this team and that the team member also exists. |

| Explanation   | No additional information is available.                                                      |
|---------------|----------------------------------------------------------------------------------------------|
| Action        | Make sure that the user has access to at least one process with exposed performance metrics. |

| Explanation   | The maximum number of processes that can be processed by the process summary API is limited by the lowest index.max\_terms elasticsearch or opensearch setting of the federated systems indices.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Make sure that the elasticsearch or opensearch index setting index.max\_terms is at least equal to the number of processes to get summary information about.                                       |

| Explanation   | No additional information is available.                                       |
|---------------|-------------------------------------------------------------------------------|
| Action        | Make sure that the user has access to the performance metrics of the process. |

| Explanation   | No additional information is available.                    |
|---------------|------------------------------------------------------------|
| Action        | Use one of the following values: Overdue, AtRisk, OnTrack. |

| Explanation   | No additional information is available.                        |
|---------------|----------------------------------------------------------------|
| Action        | Use one of the following values: AGE, RISK, DUEDATE, ALPHABET. |

| Explanation   | No additional information is available.     |
|---------------|---------------------------------------------|
| Action        | Use one of the following values: ASC, DESC. |

| Explanation   | No additional information is available.                             |
|---------------|---------------------------------------------------------------------|
| Action        | Check that the federated system REST API can be called by the user. |

| Explanation   | No additional information is available.                                                                                                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify that the value of the query parameter is a valid time zone provided as a IANA time zone id (example: America/Los\_Angeles) or as a GMT offset between GMT-18:00 and GMT+18:00 included (example: GMT+01:00). |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the field name.                    |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the operator.                      |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the operator and field.            |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the operator and the values.       |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the field and the value.           |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the value.                         |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the value.                         |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the query filter.                  |

| Explanation   | No additional information is available.                                                           |
|---------------|---------------------------------------------------------------------------------------------------|
| Action        | Verify the contents of all search words and place the fuzzy '~' symbol only at the end of a word. |

| Explanation   | The federated index was built without word positioning information. Current field mappings on new index will include position information.   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Rebuild the federated system index.                                                                                                          |

| Explanation   | An unknown error occured when processing the query filter.   |
|---------------|--------------------------------------------------------------|
| Action        | Report the error to your administrator.                      |

| Explanation   | The value of the size parameter is not valid.                                                     |
|---------------|---------------------------------------------------------------------------------------------------|
| Action        | Verify that the value of the parameter is less than the maximum value setup by the administrator. |

| Explanation   | The value of the size parameter is not valid.             |
|---------------|-----------------------------------------------------------|
| Action        | Verify that the value of the parameter is more than zero. |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the saved search definition.       |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify that the meta type exists.         |

| Explanation   | No additional information is available.    |
|---------------|--------------------------------------------|
| Action        | Verify the name or ID of the saved search. |

| Explanation   | No additional information is available.    |
|---------------|--------------------------------------------|
| Action        | Use a different name for the saved search. |

| Explanation   | No additional information is available.                 |
|---------------|---------------------------------------------------------|
| Action        | Valid organization values are 'byTask' and 'byProcess'. |

| Explanation   | No additional information is available.      |
|---------------|----------------------------------------------|
| Action        | Valid sort order values are 'ASC' and 'DESC' |

| Explanation   | No additional information is available.                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------------------|
| Action        | Valid operators are 'Equals', 'NotEquals', 'StartsWith', 'Contains', 'LessThan', 'GreaterThan', and 'FullTextSearch' |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the field name.                    |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the field name.                    |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the sort contains a field name.    |

| Explanation   | No additional information is available.     |
|---------------|---------------------------------------------|
| Action        | Verify the condition contains a field name. |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the condition has a value.         |

| Explanation   | When you update a saved search by name, the JSON definition name in the request payload must match the name in the URL request.                |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify the same name is used for both definition and the URL. Alternatively, if you are changing the saved search name, use the ID in the URL. |

| Explanation   | No additional information is available.     |
|---------------|---------------------------------------------|
| Action        | Verify the setting is either true or false. |

| Explanation   | No additional information is available.              |
|---------------|------------------------------------------------------|
| Action        | Verify the saved search contains the 'name' setting. |

| Explanation   | No additional information is available.                                     |
|---------------|-----------------------------------------------------------------------------|
| Action        | Verify the condition is a valid combination of field, operation, and value. |

| Explanation   | No additional information is available.                                  |
|---------------|--------------------------------------------------------------------------|
| Action        | Check the system logs for issues with the federated persistence service. |

| Explanation   | No additional information is available.                                                                                                                 |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Check the system logs for issues with the federated persistence service and the definition of the federated persistence service in the server.xml file. |

| Explanation   | No additional information is available.                                                                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify that the user belongs to the ACTION\_CREATE\_SHARED\_SAVED\_SEARCH or ACTION\_ADMINISTER\_SHARED\_SAVED\_SEARCHES action role as defined by the REST service security role. |

| Explanation   | No additional information is available.                                                                                        |
|---------------|--------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify that the user belongs to the ACTION\_ADMINISTER\_SAVED\_SEARCHES action role as defined by the REST service security role. |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Change the name.                          |

| Explanation   | No additional information is available.                                                                                                                                                         |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify that the user is the owner of the saved search that is being deleted or belongs to the ACTION\_ADMINISTER\_SHARED\_SAVED\_SEARCHES action role as defined by the REST service security role. |

| Explanation   | No additional information is available.                                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Assign the user to one of the roles that allows the creation and update of saved searches as defined by the REST service security role. |

| Explanation   | To avoid confusion with the saved search ID, saved search names cannot be numbers.   |
|---------------|--------------------------------------------------------------------------------------|
| Action        | Verify that the name is not a number.                                                |

| Explanation   | Saved search IDs are assigned by the system. A new saved search cannot contain an 'id' setting.   |
|---------------|---------------------------------------------------------------------------------------------------|
| Action        | Verify that the create request does not contain an 'id' setting.                                  |

| Explanation   | No additional information is available.       |
|---------------|-----------------------------------------------|
| Action        | Verify the size setting is a positive number. |

| Explanation   | No additional information is available.                                |
|---------------|------------------------------------------------------------------------|
| Action        | Verify the name is not longer than the specified number of characters. |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify that the field name exists.        |

| Explanation   | No additional information is available.                           |
|---------------|-------------------------------------------------------------------|
| Action        | Verify that the name value contains characters other than spaces. |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the name.                          |

| Explanation   | No additional information is available.                             |
|---------------|---------------------------------------------------------------------|
| Action        | Verify the condition is a valid combination of operation and field. |

| Explanation   | No additional information is available.                   |
|---------------|-----------------------------------------------------------|
| Action        | Verify the owner is not longer then the specified number. |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the ID is unchanged.               |

| Explanation   | No additional information is available.               |
|---------------|-------------------------------------------------------|
| Action        | Verify the user saved search role or shared settings. |

| Explanation   | No additional information is available.               |
|---------------|-------------------------------------------------------|
| Action        | Verify the user saved search role or shared settings. |

| Explanation   | No additional information is available.       |
|---------------|-----------------------------------------------|
| Action        | Verify the owner exists in the user registry. |

| Explanation   | No additional information is available.             |
|---------------|-----------------------------------------------------|
| Action        | Verify the team is not specified in the definition. |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the aliases contains a field name. |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify that the field name exists.        |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify that the field is a business data. |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify that the alias name is a string.   |

| Explanation   | No additional information is available.         |
|---------------|-------------------------------------------------|
| Action        | Verify that the aliases contains an alias name. |

| Explanation   | No additional information is available.                                   |
|---------------|---------------------------------------------------------------------------|
| Action        | Verify that the alias name length is less than or equal to 40 characters. |

| Explanation   | No additional information is available.                        |
|---------------|----------------------------------------------------------------|
| Action        | Verify that the saved search contains the appropriate setting. |

| Explanation   | No additional information is available.    |
|---------------|--------------------------------------------|
| Action        | Verify that the input is correctly formed. |

| Explanation   | No additional information is available.                 |
|---------------|---------------------------------------------------------|
| Action        | Verify that each saved search name to import is unique. |

| Explanation   | No additional information is available.                        |
|---------------|----------------------------------------------------------------|
| Action        | Ensure that the federated BPD system is version 8.5.7 or later |

| Explanation   | No additional information is available.                          |
|---------------|------------------------------------------------------------------|
| Action        | Ensure that the federated BPD systems are version 8.5.7 or later |

| Explanation   | No additional information is available.                                               |
|---------------|---------------------------------------------------------------------------------------|
| Action        | Ensure that the request from the REST service only applies to a federated BPD system. |

| Explanation   | No additional information is available.                                              |
|---------------|--------------------------------------------------------------------------------------|
| Action        | Ensure that the request from the REST service only applies to federated BPD systems. |

| Explanation   | No additional information is available.                                                                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify that the user belongs to the ACTION\_CREATE\_SHARED\_SAVED\_SEARCH or ACTION\_ADMINISTER\_SHARED\_SAVED\_SEARCHES action role as defined by the REST service security role. |

| Explanation   | No additional information is available.                                                                        |
|---------------|----------------------------------------------------------------------------------------------------------------|
| Action        | Make sure that the saved search definition attribute ''shared'' is set to true to use the ''teams'' attribute. |

| Explanation   | No additional information is available.                                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Make sure that the saved search definition attribute ''teams'' is an array containing at most one JSON object with at least ''teamId'' string attribute. |

| Explanation   | No additional information is available.                                                                                           |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Action        | Make sure that the team that you are sharing the saved search with exists and that the owner is a member or manager of this team. |

| Explanation   | No additional information is available.                          |
|---------------|------------------------------------------------------------------|
| Action        | Make sure that a federated data repository is available for PFS. |

| Explanation   | No additional information is available.              |
|---------------|------------------------------------------------------|
| Action        | Verify that the user have the adminSavedSearch role. |

| Explanation   | No additional information is available.                                |
|---------------|------------------------------------------------------------------------|
| Action        | Do not specify the outputFile parameter when exporting saved searches. |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Specify a supported value for searchType. |

| Explanation   | No additional information is available.        |
|---------------|------------------------------------------------|
| Action        | Failed to retrieve a SCIM authorization token. |

| Explanation   | No additional information is available.       |
|---------------|-----------------------------------------------|
| Action        | Failed to retrieve user information from SCIM |

| Explanation   | No additional information is available.        |
|---------------|------------------------------------------------|
| Action        | Failed to retrieve a SCIM authorization token. |

| Explanation   | No additional information is available.                                                                                       |
|---------------|-------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify that the user belongs to the ACTION\_SAVED\_SEARCH\_SUPER\_ADMIN action role as defined by the REST service security role. |

| Explanation   | No additional information is available.                  |
|---------------|----------------------------------------------------------|
| Action        | Check the error message in {0} to investigate the issue. |

| Explanation   | The action should be either start or status.                                            |
|---------------|-----------------------------------------------------------------------------------------|
| Action        | Verify that the value of the 'action' query parameter is either start, status or abort. |

| Explanation   | No additional information is available.                                                                                                              |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | The document with id "transfer-status" in the Federated Data Repository search queries index is not valid and should be deleted by an administrator. |

| Explanation   | No additional information is available.                                                                                                                         |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Signal that a search queries transfer operation was started. {0} is the timestamp of the operation start, {1} is the id of the user that started the operation. |

| Explanation   | No additional information is available.                                                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | After the start of a search queries transfer operation, this message indicates how many saved searches are candidate for transfer as reusable search queries. |

| Explanation   | No additional information is available.                                                                          |
|---------------|------------------------------------------------------------------------------------------------------------------|
| Action        | A transfer operation logs this message for each saved search successfully transfered as a reusable search query. |

| Explanation   | No additional information is available.                                                                               |
|---------------|-----------------------------------------------------------------------------------------------------------------------|
| Action        | A transfer operation logs this message for each saved search that could not be transfered as a reusable search query. |

| Explanation   | No additional information is available.                       |
|---------------|---------------------------------------------------------------|
| Action        | Signals that search queries transfer operation was terminated |

| Explanation   | No additional information is available.                  |
|---------------|----------------------------------------------------------|
| Action        | Check the error message in {0} to investigate the issue. |

| Explanation   | No additional information is available.                                         |
|---------------|---------------------------------------------------------------------------------|
| Action        | Signal that an abort of the current search queries transfer has been requested. |

| Explanation   | No additional information is available.                |
|---------------|--------------------------------------------------------|
| Action        | Only one search queries transfer can be run at a time. |

| Explanation   | The indexer component was not found for this federated system.                                            |
|---------------|-----------------------------------------------------------------------------------------------------------|
| Action        | Verify Process Federation Server has an indexer defined in the server.xml file for each federated system. |

| Explanation   | No additional information is available.                                                                        |
|---------------|----------------------------------------------------------------------------------------------------------------|
| Action        | A change log entry has been created to have the indexer update the document into the federated data repository |

| Explanation   | No additional information is available.                                                                        |
|---------------|----------------------------------------------------------------------------------------------------------------|
| Action        | A change log entry has been created to have the indexer delete the document from the federated data repository |

| Explanation   | No additional information is available.                                                            |
|---------------|----------------------------------------------------------------------------------------------------|
| Action        | There is no data for this process or task in the BPM database and in the federated data repository |

| Explanation   | A REST API was called without the mandatory processId parameter, or with an erroneous value for this parameter   |
|---------------|------------------------------------------------------------------------------------------------------------------|
| Action        | Provide a positive long value for the processId parameter                                                        |

| Explanation   | A REST API was called without the mandatory processId parameter, or with an erroneous value for this parameter   |
|---------------|------------------------------------------------------------------------------------------------------------------|
| Action        | Provide a positive long value for the taskId parameter                                                           |

| Explanation   | A REST API was called with a systemId parameter referencing a BPEL system while only BPD systems are supported.   |
|---------------|-------------------------------------------------------------------------------------------------------------------|
| Action        | Provide the ID of a BPD system for the systemId parameter                                                         |

| Explanation   | No additional information is available.                                                                 |
|---------------|---------------------------------------------------------------------------------------------------------|
| Action        | Enable instance indexing on the federated system declaration in server.xml in order to solve the issue. |

| Explanation   | No additional information is available.                                                                                                    |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify that the ibmPfs\_federatedSystem element in the Process Federation Server server.xml file has a configured allowedOrigins attribute. |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Verify the id of the search query.        |

| Explanation   | The datatype should be either TASKS or INSTANCES.                                     |
|---------------|---------------------------------------------------------------------------------------|
| Action        | Verify that the value of the 'datatype' query parameter is either TASKS or INSTANCES. |

| Explanation   | No additional information is available.                                                                                           |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Action        | Verify that the value of the 'systemTypes' query parameter is a space separated list of valid values from Process, BPEL and Case. |

| Explanation   | No additional information is available.                    |
|---------------|------------------------------------------------------------|
| Action        | Verify that the user is granted the pfsAdministrator role. |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | No action required                        |

| Explanation   | The ibmPfs\_federatedSystem configuration referenced by a BPD retriever in server.xml cannot be found.   |
|---------------|---------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                      |

| Explanation   | An error occurred when parsing the response returned by a federated system BPD REST API   |
|---------------|-------------------------------------------------------------------------------------------|
| Action        | Use the error message {2} to diagnose the issue                                           |

| Explanation   | Process Federation Server failed to register an MBean for a BPD retriever.                                                                                                     |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | An FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | Process Federation Server failed to unregister the MBean of a BPD retriever.                                                                                                   |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | An FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | No additional information available                                                                                                                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | In addition to the error message provided in {1}, an FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | No access token found in incoming request for a BPD federated system that is configured in server.xml with an authentication mechanism that requires this kind of token.                     |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Calls to the Process Federation Server REST API must include an access token if federated systems are configured with property authenticationMechanism set to PFS\_ACCESS\_TOKEN in server.xml |

| Explanation   | The ibmPfs\_federatedSystem configuration referenced by a Case retriever in server.xml cannot be found.   |
|---------------|----------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                       |

| Explanation   | An error occurred when parsing the response returned by a Case federated system REST API   |
|---------------|--------------------------------------------------------------------------------------------|
| Action        | Use the error message {2} to diagnose the issue                                            |

| Explanation   | Process Federation Server failed to register an MBean for a Case retriever.                                                                                                    |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | An FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | Process Federation Server failed to unregister the MBean of a Case retriever.                                                                                                  |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | An FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | No additional information available                                                                                                                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | In addition to the error message provided in {1}, an FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | No access token found in incoming request for a Case federated system that is configured in server.xml with an authentication mechanism that requires this kind of token.                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Calls to the Process Federation Server REST API must include an access token if federated systems are configured with property authenticationMechanism set to PFS\_ACCESS\_TOKEN in server.xml |

| Explanation   | The ibmPfs\_federatedSystem configuration referenced by a BPEL retriever in server.xml cannot be found.   |
|---------------|----------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                       |

| Explanation   | Process Federation Server cannot retrieve an SSL configuration to use to connect to a federated system.                                       |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | make sure server.xml set any one of 3 options: sslDefault, defaultSSLConfig, defaultKeyStore (contains target federated systems certificates) |

| Explanation   | Process Federation Server failed to register an MBean for a BPEL retriever.                                                                                                    |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | An FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | Process Federation Server didn't manage to connect to and get and get an answer from a federated system, with a connectTimeout or readTimeout configuration property set to less than 3 seconds in server.xml for a retriever.   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Use higher values for the connectTimeout and / or readTimeout configuration attribute of retrievers in server.xml                                                                                                                |

| Explanation   | Process Federation Server failed to unregister the MBean of a BPEL retriever.                                                                                                  |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | An FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | Process Federation Server failed to create the MBean of a BPEL retriever.    |
|---------------|------------------------------------------------------------------------------|
| Action        | Use the error message provided in {1} to diagnose and fix the issue.         |

| Explanation   | No additional information available                                                                                                                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | In addition to the error message provided in {1}, an FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | No access token found in incoming request for a BPEL federated system that is configured in server.xml with an authentication mechanism that requires this kind of token.                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Calls to the Process Federation Server REST API must include an access token if federated systems are configured with property authenticationMechanism set to PFS\_ACCESS\_TOKEN in server.xml |

| Explanation   | Process Federation Server failed to call a federated system.                           |
|---------------|----------------------------------------------------------------------------------------|
| Action        | Use the error message in {0} and the error cause in {1} to diagnose and fix the issue. |

| Explanation   | The additionalHeaders configuration property of a retriever in server.xml is provided with an unsupported format.                                    |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Format the values of all additionalHeaders configuration properties as a comma separated list of key=value entries such as "key1=value1,key2=value2" |

| Explanation   | Set of registered agents to do work has changed   |
|---------------|---------------------------------------------------|
| Action        | No action is required.                            |

| Explanation   | Some agents have not responded to requests.  They will be removed from the available pool.   |
|---------------|----------------------------------------------------------------------------------------------|
| Action        | No action is required.                                                                       |

| Explanation   | All agents acknowledged the last message.   |
|---------------|---------------------------------------------|
| Action        | No action is required.                      |

| Explanation   | The controller is telling a registered agent to begin work.   |
|---------------|---------------------------------------------------------------|
| Action        | No action is required.                                        |

| Explanation   | The controller is removing a particular agent from the pool.   |
|---------------|----------------------------------------------------------------|
| Action        | No action is required.                                         |

| Explanation   | The controller is telling a particular agent to quiesce.   |
|---------------|------------------------------------------------------------|
| Action        | No action is required.                                     |

| Explanation   | This target has become the controller.   |
|---------------|------------------------------------------|
| Action        | No action is required.                   |

| Explanation   | Agent has registered   |
|---------------|------------------------|
| Action        | No action is required. |

| Explanation   | Agent needs to take action.   |
|---------------|-------------------------------|
| Action        | No action is required.        |

| Explanation   | Agent is quiescing.    |
|---------------|------------------------|
| Action        | No action is required. |

| Explanation   | Agent is beginning work.   |
|---------------|----------------------------|
| Action        | No action is required.     |

| Explanation   | Unable to access the database tables containing the partitioning meta-data.    |
|---------------|--------------------------------------------------------------------------------|
| Action        | Review the logs for root cause.                                                |

| Explanation   | Agent has expired.  It will re-register.   |
|---------------|--------------------------------------------|
| Action        | No action is required.                     |

| Explanation   | Unable to access the database tables containing the partitioning meta-data.    |
|---------------|--------------------------------------------------------------------------------|
| Action        | Review the logs for root cause.                                                |

| Explanation   | Unable to access the database tables containing the partitioning meta-data.    |
|---------------|--------------------------------------------------------------------------------|
| Action        | Review the logs for root cause.                                                |

| Explanation   | The controller was unable to update it's internal state.    |
|---------------|-------------------------------------------------------------|
| Action        | Review the logs for root cause.                             |

| Explanation   | The controller was unable to continue and will shut down.    |
|---------------|--------------------------------------------------------------|
| Action        | Review the logs for root cause.                              |

| Explanation   | The agent was unable to update it's internal state.    |
|---------------|--------------------------------------------------------|
| Action        | Review the logs for root cause.                        |

| Explanation   | The agent was unable to continue and will shut down.   |
|---------------|--------------------------------------------------------|
| Action        | Review the logs for root cause.                        |

| Explanation   | A required table does not exist.                                                                |
|---------------|-------------------------------------------------------------------------------------------------|
| Action        | Ensure that the required table has been created in specified database for the specified schema. |

| Explanation   | A required table does not exist.                                                                |
|---------------|-------------------------------------------------------------------------------------------------|
| Action        | Ensure that the required table has been created in specified database for the specified schema. |

| Explanation   | Target name for this server's partitioning service has been set. It will be used in column SOURCE\_ID of table PFS\_BPD\_CHANGE\_LOG\_CONSMR\_LOG, in column TARGET of table PFS\_PARTITIONING\_AGENT and in column TARGET of table PFS\_PARTITIONING\_CONTROLLER.   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action is required.                                                                                                                                                                                                                                     |

| Explanation   | A same partitioning agent was retrieved twice from the database, which is unexpected: the database query result has been updated to remove the duplicate.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action is required.                                                                                                                                      |

| Explanation   | Process Federation Server encountered an exception when unregistering the MBean identified by {0}.                                                                                                                                       |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | In addition to the exception information provided in {1}, an FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | Internal error: Process Federation Server was not able to register an MBean because its type is unsupported.   |
|---------------|----------------------------------------------------------------------------------------------------------------|
| Action        | Contact IBM support if this error occurs.                                                                      |

| Explanation   | Process Federation Server encountered an exception when registering the MBean identified by {0}.                                                                                                                                         |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | In addition to the exception information provided in {1}, an FFDC file with a complete stack trace of the error is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | No additional information available                                             |
|---------------|---------------------------------------------------------------------------------|
| Action        | Refer to the detail of the exception in the logs to identify and fix the issue. |

| Explanation   | No additional information available                                              |
|---------------|----------------------------------------------------------------------------------|
| Action        | Refer to the details of the exception in the logs to identify and fix the issue. |

| Explanation   | Internal error      |
|---------------|---------------------|
| Action        | Contact IBM support |

| Explanation   | The internal elasticsearch service cannot be found.                                                                                |
|---------------|------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Search for errors in the Process Federation Server logs to understand why the internal elasticsearch service has not been created. |

| Explanation   | The pageSize attribute of an HTTP request to the Process Federation Server diagnostic tool as an uncorrect value.   |
|---------------|---------------------------------------------------------------------------------------------------------------------|
| Action        | Call the diagnostic tool REST API with a positive value for the pageSize attribute.                                 |

| Explanation   | The Process Federation Server diagnostic tool cannot find any indexer for index {0}                                                          |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Provide the name of an index for which an indexer is defined in the server.xml configuration file when calling the diagnostic tool REST API. |

| Explanation   | The Process Federation Server diagnostic tool was unable to parse the body of a request.    |
|---------------|---------------------------------------------------------------------------------------------|
| Action        | Format the body of the request to the diagnostic tool API according to JSON standards.      |

| Explanation   | The Process Federation Server diagnostic tool was unable to process the request because a task list is missing in the request body.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Add a task list to the request body.                                                                                                  |

| Explanation   | The Process Federation Server diagnostic tool was unable to process the request because a task id list is missing in the request body.   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Add a task id list to the request body.                                                                                                  |

| Explanation   | The Process Federation Server diagnostic tool found an unexpected null value in the body of a request or in a document retrieved from the federated data repository   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Use the value provided in {0} to identify which field has an unexpected null value.                                                                                   |

| Explanation   | The Process Federation Server diagnostic tool was unable to retrieve the result of a processing job because the corresponding thread was interrupted.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Refer to the details of the exception in the logs to identify and fix the issue.                                                                        |

| Explanation   | The Process Federation Server diagnostic tool was unable to retrieve the result of a processing job.   |
|---------------|--------------------------------------------------------------------------------------------------------|
| Action        | Refer to the details of the exception in the logs to identify and fix the issue.                       |

| Explanation   | The Process Federation Server diagnostic tool was unable to stop a processing job because there is none matching the provided job id.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Make sure to provide the id of a job that is currently running.                                                                         |

| Explanation   | The Process Federation Server diagnostic tool was unable to parse a BPD task id.   |
|---------------|------------------------------------------------------------------------------------|
| Action        | Use a positive long value for BPD task id values.                                  |

| Explanation   | The Process Federation Server diagnostic tool was unable to parse a BPD instance id.   |
|---------------|----------------------------------------------------------------------------------------|
| Action        | Use a positive long value for BPD instance id values.                                  |

| Explanation   | The Process Federation Server diagnostic tool was unable to parse a BPEL task id.   |
|---------------|-------------------------------------------------------------------------------------|
| Action        | Use format "\_TKI:xxxxxxxx.xxxxxxx.xxxxxxxx.xxxxxxx" for BPD instance id values.     |

| Explanation   | The Process Federation Server diagnostic tool was unable to parse a date value.   |
|---------------|-----------------------------------------------------------------------------------|
| Action        | Use the format provided in {0} for the date value.                                |

| Explanation   | The Process Federation Server diagnostic tool encountered an error when querying the federated data repository                 |
|---------------|--------------------------------------------------------------------------------------------------------------------------------|
| Action        | Use the error message in {0} and the stack trace provided in the Process Federation Server logs to diagnose and fix the issue. |

| Explanation   | The Process Federation Server diagnostic tool was unable to perform the requested operation on index {0} because instance indexing is not enabled for the corresponding federated system.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                                                          |

| Explanation   | The Process Federation Server diagnostic tool was unable to process the request because task and instance lists are missing in the request body.   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Add a task and instance lists to the request body.                                                                                                 |

| Explanation   | No additional information available                                 |
|---------------|---------------------------------------------------------------------|
| Action        | This message is expected at the start of Process Federation Server. |

| Explanation   | No additional information available                            |
|---------------|----------------------------------------------------------------|
| Action        | This message is expected when Process Federation Server stops. |

| Explanation   | No additional information available                                                                                                             |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | This message is expected at the start of Process Federation Server of when the federated data repository configuration is updated in server.xml |

| Explanation   | This message signals that no username and password values are provided in the configuration of the federated data respository in server.xml   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                            |

| Explanation   | The index {1} contains more than one system info document while it is supposed to contains a single one. The federated data respository will use the first one as reference.                                            |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | A federated system index is supposed to contains a single system info document: remove all documents where field document.subtype equals systeminfo so that a Process Federation Server indexer recreates a single one. |

| Explanation   | No additional information available                                                                               |
|---------------|-------------------------------------------------------------------------------------------------------------------|
| Action        | Use the federated data respository error response provided in {0} for query {1} to investigate and fix the issue. |

| Explanation   | The Process Federation Server federated data repository client is creating a new index in the federated data repository   |
|---------------|---------------------------------------------------------------------------------------------------------------------------|
| Action        | This message is expected when Process Federation Server creates an index for a federated system.                          |

| Explanation   | The Process Federation Server federated data repository client is creating a new index in the federated data repository, without any default mappings   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                      |

| Explanation   | The Process Federation Server data repository client is not able to find the alias of an index.   |
|---------------|---------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                |

| Explanation   | The Process Federation Server data repository client is unable to parse the value of a date retrieved from an indexed document.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                |

| Explanation   | The Process Federation Server data repository client is deleting an index alias.   |
|---------------|------------------------------------------------------------------------------------|
| Action        | No action required                                                                 |

| Explanation   | The Process Federation Server data repository client is deleting an index.   |
|---------------|------------------------------------------------------------------------------|
| Action        | No action required                                                           |

| Explanation   | Creation of an index that already exist was requested to the Process Federation Server federated data repository client.   |
|---------------|----------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                         |

| Explanation   | The federated data repository has an unsupported version.                                |
|---------------|------------------------------------------------------------------------------------------|
| Action        | Use a supported version of Elasticsearch or Opensearch as the federated data repository. |

| Explanation   | This message is displayed the first time that Process Federation Server connects to the federated data repository and provide information about the federated data repository vendor and version.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                                                                  |

| Explanation   | Process Federation Server found a document with an \_ignored field when performing an index search.   |
|---------------|------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                   |

| Explanation   | The federated data repository has a deprecated version.                                  |
|---------------|------------------------------------------------------------------------------------------|
| Action        | Use a supported version of Elasticsearch or Opensearch as the federated data repository. |

| Explanation   | No additional information available                                                               |
|---------------|---------------------------------------------------------------------------------------------------|
| Action        | The corresponding configuration attributes can be removed from the server.xml configuration file. |

| Explanation   | Deletion of a document that does not exist was requested to the Process Federation Server federated data repository client.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                            |

| Explanation   | A JSON search query has an unknown attribute.            |
|---------------|----------------------------------------------------------|
| Action        | Remove the unknown attribute from the JSON search query. |

| Explanation   | A JSON search query has an attribute with an illegal value (a number instead of a string, an unknown constant, etc...).   |
|---------------|---------------------------------------------------------------------------------------------------------------------------|
| Action        | Update the value of the attribute in the JSON search query to provide a supported one.                                    |

| Explanation   | An error occurred when parsing a JSON search query      |
|---------------|---------------------------------------------------------|
| Action        | Use the error details provided in {0} to fix the issue. |

| Explanation   | A field name referenced in the search query is not valid   |
|---------------|------------------------------------------------------------|
| Action        | No action required                                         |

| Explanation   | No additional information is available.                             |
|---------------|---------------------------------------------------------------------|
| Action        | Fix the condition to use a valid combination of operator and field. |

| Explanation   | No additional information is available.                                     |
|---------------|-----------------------------------------------------------------------------|
| Action        | Fix the condition to use a valid combination of field, operator, and value. |

| Explanation   | An error occurred when validating a search query        |
|---------------|---------------------------------------------------------|
| Action        | Use the error details provided in {0} to fix the issue. |

| Explanation   | A list of teams to share a search query with was provided for an unshared search query   |
|---------------|------------------------------------------------------------------------------------------|
| Action        | Either remove the list of teams or set metadata.sharing.shared to true                   |

| Explanation   | A teamId attribute is missing in a team definition      |
|---------------|---------------------------------------------------------|
| Action        | Add the missing teamId attribute to the team definition |

| Explanation   | the id attribute is missing in a user definition    |
|---------------|-----------------------------------------------------|
| Action        | Add the missing id attribute to the user definition |

| Explanation   | A date attribute cannot be parsed           |
|---------------|---------------------------------------------|
| Action        | Format the date as YYYY-MM-DDTHH:mm:ss.SSSZ |

| Explanation   | A failure has been reported by the federated data repository when creating, updating or deleting a search query   |
|---------------|-------------------------------------------------------------------------------------------------------------------|
| Action        | Use the failure details provided in {0} to further analyze the issue.                                             |

| Explanation   | The name provided for the search query is not unique and cannot be used to persist it.   |
|---------------|------------------------------------------------------------------------------------------|
| Action        | Provide another name that is unique across persisted search queries.                     |

| Explanation   | No additional information is available.                             |
|---------------|---------------------------------------------------------------------|
| Action        | Use the error details provided in {0} to further analyze the issue. |

| Explanation   | No additional information is available.                             |
|---------------|---------------------------------------------------------------------|
| Action        | Use the error details provided in {0} to further analyze the issue. |

| Explanation   | No additional information is available.                             |
|---------------|---------------------------------------------------------------------|
| Action        | Use the error details provided in {0} to further analyze the issue. |

| Explanation   | No additional information is available.                                                                                                  |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Assign the user to one of the roles that allows the creation and update of search queries as defined by the REST service security roles. |

| Explanation   | A mandatory attribute is missing in the search query         |
|---------------|--------------------------------------------------------------|
| Action        | Add the missing attribute to the search query and try again. |

| Explanation   | To avoid confusion with a search query ID, reusable search query names cannot be numbers.   |
|---------------|---------------------------------------------------------------------------------------------|
| Action        | Verify that the name is not a number.                                                       |

| Explanation   | No additional information is available.                                                                               |
|---------------|-----------------------------------------------------------------------------------------------------------------------|
| Action        | Assign the user to one of the roles that allows sharing search queries as defined by the REST service security roles. |

| Explanation   | No additional information is available.                                                                                                        |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Grant the user to one of the roles that allows assigning shared search queries to another user, as defined by the REST service security roles. |

| Explanation   | No additional information is available.                                                                                                          |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Grant the user to one of the roles that allows assigning unshared search queries to another user, as defined by the REST service security roles. |

| Explanation   | No additional information is available.                   |
|---------------|-----------------------------------------------------------|
| Action        | Replace the faulty user id with the id of an actual user. |

| Explanation   | No additional information is available.                |
|---------------|--------------------------------------------------------|
| Action        | Reference a single team (or none) in sharing metadata. |

| Explanation   | No additional information is available.                                                                                   |
|---------------|---------------------------------------------------------------------------------------------------------------------------|
| Action        | Use the globalTeams metadata REST API to retrieve the list of teams that you are authorized to share search queries with. |

| Explanation   | No index is matching the datasource of the search query.                                  |
|---------------|-------------------------------------------------------------------------------------------|
| Action        | Update the datasource of the search query so that it matches at least one existing index. |

| Explanation   | No additional information is available.                                                                                           |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Action        | The user is not the owner of the search query and has not been granted a role that allows managing queries owned by other people. |

| Explanation   | No additional information is available.                         |
|---------------|-----------------------------------------------------------------|
| Action        | Check that the provided id references an existing search query. |

| Explanation   | Update the extension to remove the offending attribute.                                    |
|---------------|--------------------------------------------------------------------------------------------|
| Action        | When extending a search query it is not possible to change the value of certain attribute. |

| Explanation   | Update the extension to use a subset of the existing systemTypes.                                                   |
|---------------|---------------------------------------------------------------------------------------------------------------------|
| Action        | When extending a search query it is only possible to use a subset of the existing datasource.systemTypes attribute. |

| Explanation   | No additional information is available.   |
|---------------|-------------------------------------------|
| Action        | Use another population target.            |

| Explanation   | The Process Federation Server federated data repository client encountered an error when parsing a response from the federated data repository.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Gather more information about the error in the Process Federation Server logs.                                                                    |

| Explanation   | The Process Federation Server federated data repository client encountered an error when serializing a request to the federated data repository   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Gather more information about the error in the Process Federation Server logs.                                                                    |

| Explanation   | The Process Federation Server federated data repository client encountered an error when serializing a response.   |
|---------------|--------------------------------------------------------------------------------------------------------------------|
| Action        | Gather more information about the error in the Process Federation Server logs.                                     |

| Explanation   | The Process Federation Server federated data repository client detected a failure on the federated data repository endpoint {0} and will not try to use it again for at least {2} seconds.                                             |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | In addition to the failure displayed in the message at {1}, an FFDC file with a complete stack trace of the failure is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the cause. |

| Explanation   | The daemon thread that monitors the availability of the federated data repository endpoints has started.   |
|---------------|------------------------------------------------------------------------------------------------------------|
| Action        | This message is expected when Process Federation Server is starting.                                       |

| Explanation   | An exception occurred in the daemon thread that monitors the availability of the federated data repository endpoints                                                                                                                                                                                                                              |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Process Federation Server need to be restarted in order to reconnect to the federated data repository. In addition to the error displayed in the message at {1}, an FFDC file with a complete stack trace of the failure is generated in the logs/ffdc sub directory of the Process Federation Server directory to help diagnose the error cause. |

| Explanation   | The daemon thread that monitors the availability of the federated data repository endpoints has stopped.                                                                                     |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | This message is expected when Process Federation Server stops. In all other situations, Process Federation Server must be restarted in order to re connect to the federated data repository. |

| Explanation   | The daemon thread that monitors the availability of the federated data repository endpoints has been requested to stop.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------|
| Action        | This message is expected when Process Federation Server stops.                                                            |

| Explanation   | The federated data repository is configured in the server.xml configuration file with a list of endpoints to nodes that are not part of a same Elasticsearch or Opensearch cluster.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Update the endpoints parameters of the federated data repository in server.xml so that all endpoint URLs are to nodes of the same Elasticsearch of Opensearch cluster.                |

| Explanation   | The daemon thread that monitors the availability of the federated data repository endpoints has set one of the endpoints as available.   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                       |

| Explanation   | Internal error: The daemon thread that monitors the availability of the federated data repository endpoints was unable to remove an available endpoint from the list of unavailable endpoints because this endpoint was not in the list.   |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                                                                                                         |

| Explanation   | The daemon thread that monitors the availability of the federated data repository endpoints has set one of the endpoints as unavailable.   |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                         |

| Explanation   | Internal error: The daemon thread that monitors the availability of the federated data repository endpoints was unable to remove an unavailable endpoint from the list of available endpoints because this endpoint was not in the list.   |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                                                                                                         |

| Explanation   | No additional information available                                                           |
|---------------|-----------------------------------------------------------------------------------------------|
| Action        | This message is expected at the start of a Process Federation Server container in Kubernetes. |

| Explanation   | No additional information available                                                            |
|---------------|------------------------------------------------------------------------------------------------|
| Action        | This message is expected when a Process Federation Server container in Kubernetes is stopping. |

| Explanation   | No additional information available                                                           |
|---------------|-----------------------------------------------------------------------------------------------|
| Action        | This message is expected at the start of a Process Federation Server container in Kubernetes. |

| Explanation   | Process Federation Server container DBA registry client found a missing configuration parameter in a DBA resource registry entry.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                  |

| Explanation   | Process Federation Server container DBA registry client encoutered an error processing the entry with key {0} in the DBA resource registry.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                            |

| Explanation   | Process Federation Server container DBA registry client is removing a federated system entry from the Process Federation Server configuration because the corresponding key was removed from the DBA resource registry.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                                                                                        |

| Explanation   | Process Federation Server container DBA registry client is removing a configuration file.   |
|---------------|---------------------------------------------------------------------------------------------|
| Action        | No action required                                                                          |

| Explanation   | Process Federation Server container DBA registry client failed to delete a file.   |
|---------------|------------------------------------------------------------------------------------|
| Action        | Use the error provided in {1} to diagnose the cause of the failure.                |

| Explanation   | Process Federation Server container DBA registry client encountered an error while watching the key {0} in the DBA resource registry.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Use the error provided in {1} to diagnose the cause of the error.                                                                       |

| Explanation   | Process Federation Server container DBA registry client encountered an error while waiting between keys watch.     |
|---------------|--------------------------------------------------------------------------------------------------------------------|
| Action        | Use the error details provided in the Process Federation Server container logs to diagnose the cause of the error. |

| Explanation   | Process Federation Server container DBA registry client encountered an error when parsing the value {1} retrieved in the DBA resource registry under key {0}.     |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Use the error message provided in {2} to diagnose the cause of the error.                                                                                         |

| Explanation   | An entry in the DBA resource registry has an unsupported value for system type.   |
|---------------|-----------------------------------------------------------------------------------|
| Action        | No action required                                                                |

| Explanation   | Process Federation Server container DBA registry client did not managed to gracefully stop its federated system retriever thread while stopping.   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                 |

| Explanation   | Process Federation Server container DBA registry client did not managed to cancel its federated system retriever thread while stopping.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                        |

| Explanation   | Process Federation Server container DBA registry client is stopping its federated system retriever thread   |
|---------------|-------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                          |

| Explanation   | Process Federation Server container DBA registry client has stopped its federated system retriever thread   |
|---------------|-------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                          |

| Explanation   | The federated system retriever thread of the Process Federation Server container DBA registry client has stopped   |
|---------------|--------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                 |

| Explanation   | Process Federation Server container DBA registry client detected that an entry updated in the DBA resource registry has the same value than before and will ignore the update.   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                                               |

| Explanation   | Process Federation Server container DBA registry client detected that an entry updated in the DBA resource registry has a different value than before and will update the federated system configuration accordingly.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                                                                                      |

| Explanation   | Process Federation Server container DBA registry client detected that an entry in the DBA resource registry is referencing an on premise BAW server.   |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                     |

| Explanation   | Process Federation Server container DBA registry client detected that an entry in the DBA resource registry has its federate attribute set to false and will ignore it.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                                        |

| Explanation   | Error in the Process Federation Server container DBA registry client configuration: the URL to the DBA resource registry is missing.   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                     |

| Explanation   | Error in the Process Federation Server container DBA registry client configuration: the password to access the DBA resource registry is missing.   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                 |

| Explanation   | The Process Federation Server container DBA registry client configuration does not contains credentials to connect to the DBA resource registry.   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                 |

| Explanation   | Process Federation Server container DBA registry client failed to connect to the DBA resource registry.   |
|---------------|-----------------------------------------------------------------------------------------------------------|
| Action        | Use the error message provided in {Ã} to diagnose the issue.                                             |

| Explanation   | Process Federation Server container DBA registry client encountered an error when reading an entry in the DBA resource registry.   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------|
| Action        | Use the error message provided in {1} to diagnose the issue.                                                                       |

| Explanation   | Process Federation Server container DBA registry client has started watching DBA resource registry key {0}.   |
|---------------|---------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                            |

| Explanation   | Process Federation Server container DBA registry client has stopped watching DBA resource registry key {0}.   |
|---------------|---------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                            |

| Explanation   | Process Federation Server container DBA registry client encountered an error when watching DBA resource registry key {0}.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------|
| Action        | Use the error message provided in {2} to diagnose the issue.                                                                |

| Explanation   | Process Federation Server container DBA registry client received an unexpected HTTP response code from the DBA resource registry.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                  |

| Explanation   | Internal error: Process Federation Server container DBA registry client encountered an error when parsing the value {0} found in the DBA resource registry.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                                            |

| Explanation   | Process Federation Server container DBA registry client received an event of type {0} when watching the DBA resource registry key {0}.   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                       |

| Explanation   | Process Federation Server container DBA registry client received an untyped event when watching the DBA resource registry key {0}.   |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                   |

| Explanation   | Process Federation Server container DBA registry client coudn't find key {0} in the DBA resource registry   |
|---------------|-------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                          |

| Explanation   | Internal error: Process Federation Server container DBA registry client got a request to watch a key that it is already watching.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                  |

| Explanation   | Process Federation Server container DBA registry client received an outdated response from the DBA resource registry.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                      |

| Explanation   | Process Federation Server container DBA registry client failed to register a watch on the DBA resource registry.   |
|---------------|--------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                 |

| Explanation   | Process Federation Server container DBA registry client found entry with key {0} in the DBA resource registry.   |
|---------------|------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                               |

| Explanation   | Process Federation Server container DBA registry client lost its connection with the DBA resource registry and is reconnecting.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Action        | No action required                                                                                                                |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | No additional information available   |
|---------------|---------------------------------------|
| Action        | No action required                    |

| Explanation   | If SCIM must be used to check if a user exists, credentials to the SCIM API are required.   |
|---------------|---------------------------------------------------------------------------------------------|
| Action        | Verify the  properties.                                                                     |