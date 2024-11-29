# Retrieving a user's full name in an easier-to-read format

Traditional: 
 When you use
federated repositories, you can configure the user property in the
100Custom.xml to use the displayName attribute so that the
output is easier to read.

By default, IBM® Business Automation Workflow uses the
cn attribute that is stored in the WebSphere® Application
Server user registry to retrieve a user's full name.
When you use the cn attribute, the name renders in a less readable format, such
as js1234. If you use the displayName attribute, the
output is easier to read, for example John Smith.

## Procedure

To retrieve the user's full name from the displayName attribute,
set the user-full-name-prop property:

1. Add the following configuration change in each appropriate 100Custom.xml
file to your topology: 

<common merge="mergeChildren">
      <security merge="mergeChildren">
           <vmm-options merge="mergeChildren"> 
                 <user-full-name-prop merge="replace">displayName</user-full-name-prop>                
           </vmm-options>
      </security>       
</common>
For information about the individual 100Custom.xml files that need to be
updated and their locations, see Location of
configuration files.
2. Deploy the changes, restart the environment and verify the settings have been updated.
3 Synchronize your existing LDAP users because the former full name is saved in the database andwon't be updated automatically:
    1. Open the Process Admin Console.
    2. From Server Admin, go to User Management > User Synchronization.
    3. Click Existing User Synchronize.
4. Confirm the wimconfig.xml in the DMGR has the
config:userDisplayNameMapping set to displayName:

<config:userDisplayNameMapping propertyForInput="displayName"propertyForOutput="displayName"/>
If the synchronize fails with the following message
com.ibm.websphere.wim.exception.MaxResultsExceededException: CWWIM1018E, read A MaxResultsExceededException: CWWIM1018E exception occurs when
upgrading to IBM Business Process Manager (BPM) V7.5.x or 8.x from WebSphere Process Server (WPS)
.