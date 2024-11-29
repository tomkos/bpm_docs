# Configuring the Business Space component and registering REST endpoints on the
administrative console

## Before you begin

- Install the product software and create a profile. When you install
your product, Business Space files
are included with the installation for the profiles that you set up.
Your profile is not configured for Heritage Process Portal until you explicitly configure the Business Space component on
the profile.
- Optionally, set up a secured environment for Heritage Process Portal by enabling security.
- Configure Representational State Transfer (REST) services. If
you have a stand-alone server environment or you are using the Deployment
Environment wizard to configure your runtime environment, the REST
service endpoints are configured and enabled automatically. For other
environments, use the REST services administrative console page to
configure the REST services. To have widgets available in Heritage Process Portal, you must configure the REST services
for those widgets. On the Business Space Configuration administrative
console page, you register the REST endpoints so that Business Space
associates widgets with the endpoints and the widgets appear in the
palette for use.
- Configure the Business Space component
on a server or cluster by using a different data source than the product
data source: create the data source in the server or cluster scope
with the correct JNDI name of jdbc/mashupDS before configuring the Business Space component by
using the administrative console.
- (Oracle) Optionally, to use a different schema for the Business Space database tablesthan the one that the product database uses, complete the followingsteps to create a data source manually before you open the Business Space Configurationpage:
    1. Create the schema using the database product software.
    2. Use the administrative console to configure the JDBC provider.
    3. Use the administrative console to create a data source with the
JNDI name of jdbc/mashupDS at the server or cluster scope, depending
on your environment.
    4. Use the administrative console to create an authentication alias.
Set the user name to the schema you created and set the authentication
according to your Oracle setup.
    5. Set the authentication alias on the data source.

## About this task

If you are using deployment environments or other advanced
profile configuration, you must use the administrative console to
configure the Business Space component
to work with Heritage Process Portal in your runtime environment.

## Procedure

1. Ensure that the administrative console is running.
2. In the navigation pane click Servers > Server Types > WebSphere application
servers or Servers > Clusters > WebSphere application server
clusters.
3. Select the name of your server or cluster target.
4. On the Configuration page, in the Business Process Manager section,
click Business Space rest services endpoint registration. 
The REST service endpoint registration page opens. If Business Space has already been configured, you can view this
page, but you cannot edit the fields.
5. Select Install Business Space service.
6. In the Database schema name box,
type the name of the database schema that you want to use for the Business Space database. 
Note: In Oracle, the schema is the same as the user name set
on the authentication alias on the data source.
7. If no data source is designated in the Existing
Business Space data source field, go to the Create
Business Space data source using section and select a
data source that connects to the database you want to use with Business Space.  Designating
a data source in the Create Business Space data source
using section creates a data source for Business Space with a JNDI
name of jdbc/mashupDS that is modeled on the data source you selected.
The Business Space data source
is created on the server or cluster on which you are configuring Business Space, even if the
product data source is on a different server or cluster. 
Tip: If you do not see an existing data source that you want
to use, you must cancel the Business Space Configuration
page, set up the database and the data source that you want to use,
and then restart the Business Space Configuration
page to complete the configuration. For more information, see the
Before you begin section.
8. Click OK.
9. To register the proper deployment target (cluster or server)
for the system REST endpoints for each of the widgets you are using
in Business Space, click REST
service endpoint registration. The target
that you select for a REST service endpoint type can set the scope
of the data displayed in some widgets. Or, you might want to select
a particular cluster or server for better performance or availability.
If you are using Human Task Management widgets,
you can select more than one REST service provider for a server or
a cluster in the row for the Process Services and Task Services types.
Select the provider with Name=Federated REST Services,
the provider with Name=Business Process Choreographer REST
services, or the provider with Name=BPD engine REST
services.  If you have tasks and processes running in both
Business Process Choreographer and the business process definition
(BPD) engine, select the federated REST services. If you are using
only processes and tasks that are running in the Business Process
Choreographer (modeled in Integration Designer), select the Business
Process Choreographer REST services. If you are using only processes
and tasks that are running in the BPD engine (modeled in Process Designer),
select the BPD engine.  
If you do not specify the target, the
REST endpoint of this type is not registered with Business Space,
and any widgets that need the REST service endpoint of this type will
not be visible in Business Space.
10. Save the configuration.
11. Run the scripts to configure the Business Space database tables
before starting the deployment environment or the clusters. The
scripts were generated when you completed the configuration. .

## What to do next

If you are using Oracle, the password of the authentication
alias of the Business Space data
source is set to same as the Business Space schema name.
The default value of the schema is IBMBUSSP. When you configure the Business Space component,
you can specify a different schema on the administrative console or
on the command line. In that case, the default password is the same
as the schema you specify. To use a different password for the Business Space user name,
you must use the administrative console to updated JDBC Resources:
Find the data source jdbc/mashupsDS. Modify the value of the authentication
alias to make it match the password of the Business Space schema name.
 Save your changes and restart the server.