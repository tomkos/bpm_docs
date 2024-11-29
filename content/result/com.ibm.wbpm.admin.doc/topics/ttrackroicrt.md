# Tracking changes in the number instances created and service
requests

1. Log in to the Process Admin console, by entering the url. For example:
http://servername:9080/ProcessAdmin, where servername is the
name of your server and 9080 is the default port.
2. In the side menu of the Process Admin Console, expand
Monitoring to list the available monitoring options.
3. Click Instrumentation. You can see how many process instances were
created for each BPD since the server started. You can also see how many service requests were made
to each process app, for services such as integration service, human service, Ajax service.
4. Click Save to save the instrumentation data as an XML file.

- Retrieve instrumentation data as XML by using the InstrumentationManager
MBean
- See the rate of change by monitoring the BPDInstancesStarted MBean

- Monitoring MBeans with JConsole
- Process Monitor MBeans reference