# Problems testing a connection to a data source in a network
deployment

The test connection service provided by WebSphere® Application
Server often works only if the
variables that contain path infomation (such as WAS\_INSTALL\_ROOT and
ORACLE\_DRIVER\_INSTALL\_PATH) are set on cell scope, which is not the case in
IBM® Business Automation
Workflow network
deployments.

If you attempt to test the data source connection, for
example in the Health Center, or in the administrative console using Resources > JDBC > Data
sources, and you get a message saying that
the test connection operation failed with the exception com.ibm.wsspi.runtime.variable.UndefinedVariableException:
Undefined Variable variable\_name, it does
not necessarily indicate that there will be a problem accessing the
data source at run time. Ensure that the location of your JDBC driver
files is accessible to every client that must use the data source,
and configure the variable with the full path of that location. Disregard
the test connection error unless you are also experiencing trouble
connecting to the data store at run time.

Generally, if the
exception UndefinedVariableException: Undefined Variable variable\_name is
logged in the deployment manager log files when the Health Center
is opened in the WebSphere administrative console, you can ignore
the exception unless the Health Center indicates that there is a problem.