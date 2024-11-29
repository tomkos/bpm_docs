# Configuring Business Automation Workflow to use the external
Content Platform Engine

## About this task

Running a command and then starting Business Automation Workflow
finishes the configuration. However, you must also verify that the configuration is working.

## Procedure

1 Set up a network shared directory between all computers in the IBM Business Automation Workflow cluster and theContent Platform Engine cluster. The shared directory must be the same on all computers. The computers must have the sameoperating system.
    - By default, the shared directory on the IBM Business AutomationWorkflow computer isinstall\_root /CaseManagement/properties . If you customizedthe path to the shared directory, use that customized path.

<!-- image -->

<!-- image -->

        - On the Content Platform Engine
computer, create a folder with the same path as the IBM Business Automation
Workflow shared directory.
        - You can mount remote file systems. You can also use network file systems or distributed file
systems to share files across computers, such as NFS, GPFS.
- By default, the shared path on the IBM Business AutomationWorkflow computer isinstall\_root \CaseManagement\properties . If you customizedthe path to the shared directory, use that customized path. If the path is a UNC path to share filesamong Windows servers, use a forward slash, for example //WIN129146/shareFolder instead of \\WIN129146/shareFolder .

<!-- image -->

    1. On the Content Platform Engine
computer, create a folder with the same path as the IBM Business Automation
Workflow shared directory.
    2. Share the directories between the computers.
2 Run the setBPMExternalECM admin command to configure Business Automation Workflow to use an external ECM server.

1. Shut down the Business Automation Workflow deployment
environment; for example, by using the BPMConfig command. BPMConfig
-stop. See BPMConfig command-line utility. In a network deployment environment, the
deployment manager and node agents can be left running. The Content Platform Engine must be running.
2. Run wsadmin. If you have a   Business Automation Workflow
Express server or if you stopped the deployment manager of your network deployment environment, run
wsadmin in local mode; that is, by using the parameter -conntype
none.
3. Run the setBPMExternalECM admin command. See setBPMExternalECM command. Use REASSIGN\_DOMAIN as the value for the
-ecmEnvironment parameter.
For
example:./wsadmin.sh -lang jython -username  celladmin -password celladmin
AdminTask.setBPMExternalECM(['-de', 'BPM', '-ceUrl', 'iiop://xxxx.cn.ibm.com:2809/FileNet/Engine', '-ecmEnvironment', 'REASSIGN\_DOMAIN', '-clientDownloadServicePort','9080'])
AdminConfig.save()
Important: If you used an LDAP group as PEWorkfowSystemAdminGroup
when you ran the createObjectStoreForContent command to create the design object store
and target object store, you can choose to reassign the domain or the object store when you switch
to an external Content Platform Engine. Otherwise, you cannot
reassign domain or object store and must choose NEW\_EXTERNAL\_OBJECT\_STORE when
you configure Business Automation Workflow to use an external
Content Platform Engine.
4. Save the configuration by invoking AdminConfig.save().
5. If you stopped the deployment manager and node agents, manually restart them.
6. In a network deployment environment, synchronize the configuration of the nodes.
7. Restart the Business Automation Workflow deployment environment
by using the BPMConfig
-start command. See BPMConfig command-line utility.
3. Check that the Content Platform Engine server is running.
Check for errors in the Business Automation Workflow logs. If you
discover errors, resolve them and restart the Business Automation Workflow server.
4. Unlike the BPM content store setup, where you check
the health of the configuration by using the EmbeddedECM component, an external ECM configuration
uses the CMIS component. Check the CMIS component in the Component Health Center to verify that your
external ECM server is up and running.
5 Start the IBM Business AutomationWorkflow Case configuration tool and reconfigure case:

1. Update the Content Platform Engine properties in
the profile to the external Content Platform Engine hostname
and connection information. Test the connection.
2. Rerun all enabled tasks. In the Configure Business Rules task, make
sure that you create the rules repository directory on the Content Platform Engine server before you run the task.
3. After all the tasks are finished, sync the nodes and restart the whole
environment.
6. In the external Content Platform Engine, open the
IBM Administration Console for Content Platform Engine and
validate that the administrator can perform all tasks.