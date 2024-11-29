# Business Automation Workflow interaction with the Content
Platform Engine

Most ECM-related commands that are run in Business Automation Workflow affect
the BPM content store.
These commands have no effect on an external ECM, which is controlled
by the external ECM's IBM Administration Console for Content Platform
Engine. However, adding or removing users and groups from the administrator
role is one area where a command can be run on the external ECM server.

| Command                            | Effect on external ECM server                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| maintainDocumentStoreAuthorization | This command adds or removes users and groups from the administrator role. The administrator role manages the external ECM server. The users and groups that are authorized by this command receive full administrative rights to the external ECM. The external ECM administrator also controls this role. The Content Platform Engine administrator and the Business Automation Workflow administrator must realize that each administrator shares responsibility. |