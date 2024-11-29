# Access control
in business process and human task applications

| Roles                | Default permission                                                                                                                              | Notes                                                                                                                                    |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| System Administrator | User names, group names, or both, entered during configuration                                                                                  | Has access to all business processes and all operations.                                                                                 |
| System Monitor       | User names, group names, or both, entered during configuration                                                                                  | Has access to read operations.                                                                                                           |
| JMSAPIUser           | User name entered during configuration                                                                                                          | All Business Process Choreographer JMS APIs are run on behalf of this single user ID.                                                    |
| EscalationUser       | User name entered during configuration                                                                                                          | Used by the human task manager to process asynchronous API calls.                                                                        |
| AdminJobUser         | User name entered during configurationNote: The user supplied must be a member of the Business Process Choreographer System Administrator role. | Administrative jobs (for example, the cleanup service or business process instance migration) are run  on behalf of this single user ID. |

## Related information

- Authorization roles for BPEL processes
- Authorization roles for human tasks