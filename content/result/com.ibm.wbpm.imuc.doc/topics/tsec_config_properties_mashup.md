# Adding servers to the trusted server list

## Procedure

1. Open the administrative console and click Resources > Resource Environment > Resource Environment Provider.
2. On the Resource environment providers page,
click Mashups\_ConfigService.
3. Under Additional Properties, click Custom properties.
The list of custom properties opens.
4. Click postMessageWhiteList, add
domains (including protocol, host, and port) separated by commas for
the servers that you want to add in the Value field,
and then click OK. For example,
add the servers in the following format: https://myportal1.ibm.com:10039,https://myportal2.ibm.com,http://myportal3.ibm.com:10038,http://myportal4.ibm.com.
5. Save your changes to the master configuration.
6. Synchronize nodes and restart the application server instance.