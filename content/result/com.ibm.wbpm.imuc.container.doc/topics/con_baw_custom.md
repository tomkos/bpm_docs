# Customizing Business Automation Workflow on
containers

- Customizing Workflow Server on containers to connect to Workflow Center

 Containers: 
 Using IBM Business Automation Workflow on containers, you can establish and work with IBM Workflow Center running on a traditional runtime environment.
- Customizing Business Automation Workflow on containers with multiple target object stores

 Containers: 
You can configure more than one target object store for case management.
- Customizing Business Automation Workflow on containers properties

 Containers: 
You can make Liberty and 100Custom configuration changes to Business Automation Workflow deployment.
- Preparing customized versions of JDBC drivers for Business Automation Workflow on containers

 Containers: 
The Cloud Pak operator includes a single version of Db2 (db2jcc4.jar), Oracle (ojdbc8.jar), MicrosoftSQL (mssql-jdbc.jre11.jar), and PostgreSQL (postgresql-42.6.0.jar) JDBC drivers to use in your production deployments. If you need to use other versions, then you must package these files into a compressed file and use the sc\_drivers\_url configuration parameter to download them from an accessible web server. This step is optional.
- Providing certificates for external routes for Business Automation Workflow on containers

 Containers: 
 IBM Business Automation Workflow creates routes to allow clients outside the Red Hat OpenShift cluster to interact with user interfaces and APIs over HTTPS. By default, these endpoints are secured with generated certificates that are signed by a generated self-signed root CA certificate. For production environments, it is likely that you want to use your own certificates that are trusted by your clients.
- Using a reverse proxy for Business Automation Workflow on containers

 Containers: 
You can configure a reverse proxy for IBM Business Automation Workflow on containers. When you use a reverse proxy in front of Business Automation Workflow on containers, you must use the external endpoint as the hostname suffix.
- Configuring LDAP for Business Automation Workflow on containers

 Containers: 
A server that runs the Lightweight Directory Access Protocol (LDAP) can be configured by more than one component on Kubernetes.
- Updating the Business Automation Workflow on containers deployment after an LDAP password change

 Containers: 
After an update to the Lightweight Directory Access Protocol (LDAP) administrator password, for example, when the password expired, you might need to update the Business Automation Workflow deployment to avoid errors.
- Setting the time zone in Business Automation Workflow on containers

 Containers: 
You might need to change the default JVM setting for the time zone in Business Automation Workflow because it is set to Central European Time (CET) by default. By changing a JVM argument to a different time zone, you can change the dates and calendars you see in the user interface.
- Configuring email for Workplace notifications for Business Automation Workflow on containers

 Containers: 
To be notified when a new task is assigned to them or their teams, users can set up email notifications in Workplace. For the email notifications to work, you must first configure the email environment to send notifications.
- Configuring how external user interfaces open in Workplace

 Containers: 
If you have a task in your process that calls an external service that has an external implementation, you can configure how the external UI opens in Workplace.
- Configuring custom Liberty data sources for Business Automation Workflow on containers

 Containers: 
To integrate custom datasources into your applications, configure the data source in the Liberty configuration for Business Automation Workflow.
- Enabling the Liberty feature to integrate with IBM MQ for Business Automation Workflow on containers

 Containers: 
To integrate with IBM MQ, enable the MQ JMS client feature and add the IBM MQ resource adapter. JavaMail is enabled by default.
- Enabling full text search for Business Automation Workflow on containers

 Containers: 
You can customize IBM Business Automation Workflow to enable full text search.
- Customizing Process Federation Server for Business Automation Workflow on containers

 Containers: 
 You can add custom configuration for Process Federation Server.
- Customizing an independent JMS server for Business Automation Workflow on containers

 Containers: 
 You can deploy an independent Java Message Service (JMS) server instead of the embedded JMS server.
- Configuring event emitters for IBM Business Automation Workflow on containers

 Containers: 
You can enable event emitters with the IBM Business Automation Insights Extension for Workflow. When events are emitted, you can monitor your business events in the IBM Business Automation Insights Extension. You can enable either the BPMN event emitter, the Case event emitter, or both.
- Configuring Intelligent Task Prioritization on IBM Business Automation Workflow on containers

 Containers: 
Intelligent Task Prioritization uses historic runtime data to provide a prioritized task list for the user, improving workforce efficiency and maximizing throughput. Tasks are assigned to a user based on their task expertise and the predicted value from processing time predictions. You can configure IBM Business Automation Workflow to enable Intelligent Task Prioritization.
- Enabling the audit log

You can enable an audit log to keep track of changes that are made by administrators in the Process Admin Console.
- Configuring CORS for an external identity provider

 Containers: 
You can configure an external identity provider for IBM Business Automation Workflow on containers.