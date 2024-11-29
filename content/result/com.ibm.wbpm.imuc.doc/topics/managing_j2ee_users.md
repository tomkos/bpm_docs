# IBM Business Automation Workflow application
Java EE roles

By default, IBM Business Automation Workflow maps
many of the Java EE roles to All Authenticated users.
If your IBM Business Automation Workflow system
is only accessed by a subset of users, for example, from your corporate
LDAP, you should create a group that contains all relevant IBM Business Automation Workflow users
and assign this group to the roles that are set to All Authenticated
users.

- Declarative authorization, which is configured in the web.xml and ejb-jar.xml files.
- Programmatic authorization, which uses of the standard Java EE
application programming interface.