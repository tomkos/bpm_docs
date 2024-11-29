# Federated systems and authorization for saved searches

```
<!-- REST WEB ENDPOINT (REQUIRED) -->
<!-- SAMPLE URL: https://pfsHost.com:9443/rest/bpm/federated/v1/systems -->
<!-- THE FOLLOWING AUTHORIZATIONS ARE USED BY THE REST WEB ENDPOINT -->
<authorization-roles id="com.ibm.bpm.federated.rest.authorization">
    <!--  The following role is used to allow users read access to federated REST APIs without the ability to update or create saved searches -->
    <!--  Any user that has this role and not any of the other roles will not be able to create or update saved searches -->
    <security-role name="restrictedBpmuser">
    </security-role>
    <!--  The following role is used to allow users read access to federated REST APIs plus the ability to create only personal saved searches -->
    <security-role name="bpmuser">
        <special-subject type="ALL\_AUTHENTICATED\_USERS"/>
    </security-role>
    <!--  The following role is used to allow users read access to federated REST APIs plus the ability to create personal and shared saved searches -->
    <security-role name="createSharedSavedSearch">
        <special-subject type="ALL\_AUTHENTICATED\_USERS"/>
    </security-role>
    <!--  The following role is used to allow users read access to federated REST APIs plus the ability to fully administer shared saved searches from all users-->
    <security-role name="adminSharedSavedSearch">
        <!-- TO SPECIFY ADMIN SHARED SAVED SEARCH MEMBERSHIP, ADD user, group, OR special-subject ELEMENTS -->
    </security-role>
    <!--  The following role is used to allow users read access to federated REST APIs plus the ability to fully administer saved searches from all users-->
    <security-role name="adminSavedSearch">
        <!-- TO SPECIFY ADMIN SAVED SEARCH MEMBERSHIP, ADD user, group, OR special-subject ELEMENTS -->
    </security-role>
    <!--  The following role is used to allow users read access to federated REST APIs without the ability to update or create saved searches -->
    <!--  Any user that has this role will not be able to create or update saved searches, whatever the other roles he's in -->
    <security-role name="doNotCreateSavedSearch">
    </security-role>
</authorization-roles>
```

| Security role           | Description                                                                                                                                                                                                      | Default membership   |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| restrictedBpmUser       | Users in this role can only run saved searches but cannot create or update them.                                                                                                                                 | Nobody               |
| bpmuser                 | In addition to the authorizations of the restrictedBpmUser role, users in this role are authorized to create personal saved searches, which are saved searches that they own and that are not shared.            | All PFS users        |
| createSharedSavedSearch | In addition to the authorizations of the bpmuser role, users in this role are authorized to share the saved searches that they own.                                                                              | All PFS users        |
| adminSharedSavedSearch  | In addition to the authorizations of the createSharedSavedSearch role, users in this role are authorized to fully administer shared saved searches. They can create, update, or delete them, whatever the owner. | Nobody               |
| adminSavedSearch        | In addition to the authorizations of the createSharedSavedSearch, users in this role are authorized fully administer all saved searches. They can create, update, or delete them, whatever the owner.            | Nobody               |
| doNotCreateSavedSearch  | Users in this role cannot create or update saved searches but can run them, whatever the other roles they are in.                                                                                                | Nobody               |

For more information about how to assign users, groups, or special subjects to a security role,
see the Authorization page of the WAS Liberty documentation.