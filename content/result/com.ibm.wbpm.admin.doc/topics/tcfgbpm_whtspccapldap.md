# Configuring Business Automation Workflow to handle
white space and letter case variations in the LDAP 		server

You can configure Business Automation Workflow to 			enable
or disable the actions of detecting and removing white spaces and
normalizing 			capitalization in distinguished names in a Virtual
Member Manager (VMM) LDAP 			repository.

When you synchronize group membership between your user repository (for example, LDAP) and the
IBM® Business Automation
Workflow database by using one of the
administrative scripts (syncGroupMembershipForGroups or
syncGroupMembershipForAllGroups), run time can be very long. When you run one of
the scripts, Business Automation Workflow matches the distinguished
names (DNs) of the group members in the user repository to the DNs stored for users in the Business Automation Workflow database. This process relies on removing
unexpected white spaces from the DNs and on normalizing the capitalization used in them, which you
can do by configuring Business Automation Workflow.

## About this task

- normalize-whitespaces-for-distinguished-names-prop with atrue or false value
    - Set this property to false if you have a well-maintained VMM LDAP repository
that avoids variations in white space usage.
    - Set this property to true if the DNs stored in a VMM LDAP repository showvarying usage of white spaces in DNs referring to the same user or group, as in the following examples.
        - DN for user entry: uid=user1, ou=mycomp
        - DN for group member reference: uid =user1, ou =mycomp
- By default, the property is not set and Business Automation Workflow assumes that the property is associated with
true.
- normalize-case-for-distinguished-names-prop with an INSQL or INJAVA value INSQL During group membership synchronization for a group, Business Automation Workflow performs the following actions: Some user repositories provide inconsistent variations of capitalization when they are queriedfor group members instead of user names. With the default setting of INSQL , anBusiness Automation Workflow database with thecase-insensitive-security-cache set to true first performs acase-sensitive search for users based on the response to the group members queries. For groupmembers that are not found during this case-sensitive search, a second case-insensitive query isrequired. Case insensitivity is achieved by applying the SQL function UPPER to theuser name, which is likely to significantly affect performance.Note: For all database systems otherthan Microsoft SQL Server, the default value of thecase-insensitive-security-cache property is true . The defaultvalue in the Microsoft SQL Server database system is false . As a result, the default setting of INSQL is good for the following environments. INJAVA If your environment has frequent inconsistent responses from the user registry, set the value toINJAVA . This setting achieves case insensitivity by storing the correspondingdistinguished name for each user in a normalized fashion, converting it to lowercase as part of usersynchronization performed with one of the available user synchronization scripts or, implicitly,when the user logs in. When you synchronize group memberships, group members in the Business Automation Workflow database are searched for by a transformation ofthe group member name to its normalized counterpart, such as by converting it to lowercase in Java.This configuration avoids a second database query for synchronizing group memberships by increasingthe processing cost of user synchronization. Note: The normalization procedure requires normalized values to be available for user DNs inthe user records in the Business Automation Workflow database. As aconsequence, you must recompute the user DNs in the user records whenever the setting is switchedfrom INSQL to INJAVA by running thesyncExistingUsers administrative script. Conversely, whenever you switch thesetting from INJAVA to INSQL , recompute the user DNs in the userrecords to restore non-normalized DNs. The same action applies when the value for whitespace-related normalization is changed; the syncExistingUsers script must be run,too.

- You do not need to set this property if you have a well-maintained VMM LDAP repository that
avoids variations in capitalization.
- Set this property if the DNs stored in a VMM LDAP repository show varying usage ofcapitalization in DNs referring to the same user or group, for example:
    - DN for user entry: uid=user1, ou=mycomp
    - DN for group member reference: uiD=UsEr1, ou=MyComp
- By default, the property is not set and Business Automation Workflow assumes that the property is associated with the
INSQL modeNote: This value does not have performance implications for a
well-maintained VMM LDAP repository.

- Queries the group entry for the group members in the user repository.
- Resolves the user record in the Business Automation Workflow
database for each group member by using the retrieved group member DN.
- Updates the group membership in the Business Automation Workflow
database table by using the retrieved user ID for each group member.

- Environments that receive consistent data from the user registry and, therefore, never require a
second case-insensitive query
- Environments that receive inconsistent data from the user registry only occasionally and,
therefore, fall back to the second query only in exceptional cases
- Environments that have the case-insensitive-security-cache property set to
false because the second query (which would provide the same result) is not
necessary and is omitted anyway.

If your environment has frequent inconsistent responses from the user registry, set the value to
INJAVA. This setting achieves case insensitivity by storing the corresponding
distinguished name for each user in a normalized fashion, converting it to lowercase as part of user
synchronization performed with one of the available user synchronization scripts or, implicitly,
when the user logs in.

When you synchronize group memberships, group members in the Business Automation Workflow database are searched for by a transformation of
the group member name to its normalized counterpart, such as by converting it to lowercase in Java.
This configuration avoids a second database query for synchronizing group memberships by increasing
the processing cost of user synchronization.

## Procedure

1 To normalize white spaces and capitalization, completethe following steps:
    - For white space normalization, include the following setting
in your 							100Custom.xml file in your 						topology:<common merge="mergeChildren">
   <security>
    <vmm-options>
        <normalize-whitespaces-for-distinguished-names-prop>true
        </normalize-whitespaces-for-distinguished-names-prop>
    </vmm-options>
   </security>
</common>
    - If you know of or suspect variations in capitalization that need normalization, include the
following setting in your 100Custom.xml file in your
topology:<common merge="mergeChildren">
   <security>
      <vmm-options>
         <normalize-case-for-distinguished-names-prop>INJAVA
         </normalize-case-for-distinguished-names-prop>
      </vmm-options>
   </security>
</common>
2. Restart servers and run the syncExistingUsers script to refresh the user
entries in the Business Automation Workflow database.
3. Run one of the group membership synchronization scripts.