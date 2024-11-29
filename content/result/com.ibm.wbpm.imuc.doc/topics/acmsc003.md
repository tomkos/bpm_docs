# Customizing privileges and permissions

## About this task

- create
- view
- update
- manage

Similarly, the "Define the administrators and assign privileges" window shows a single privilege
by default: Full Control.

```
<secdef:privilegeDefinition name="create" category="icm">
     <secdef:allow>createCase</secdef:allow>
     <secdef:allow>startTask</secdef:allow>
</secdef:privilegeDefinition>
```

You can modify a privilege by adding or removing permissions in <secdef:allow> elements
under each <secdef:privilegeDefinition> element. You can also remove a privilege column from
the security configuration wizard by removing the corresponding <secdef:privilegeDefinition>
element and its associated <secdef:allow> child elements.

```
<secdef:privilegeDefinition name="manage" category="icm">
     <secdef:allow>manageCase</secdef:allow>
     <secdef:allow>startTask</secdef:allow>
     <secdef:allow>manageRole</secdef:allow>
</secdef:privilegeDefinition>
```

You can add a new privilege to the security configuration wizard by adding a new
<secdef:privilegeDefinition> element with appropriate <secdef:allow> child elements. In
the <secdef:privilegeDefinition> element, specify category="icm" to add the privilege to the
"Modify permissions for roles" window in the security configuration wizard. Specify category="admin"
to add the privilege to the "Define the administrators and assign privileges" window.

```
<secdef:privilegeDefinition name="view and comment" category="icm">
     <secdef:allow>viewCase</secdef:allow>
     <secdef:allow>addComment</secdef:allow>
</secdef:privilegeDefinition>
```

After you edit the security privilege definition file and check it in, your changes are reflected
in the Case administration client
security configuration wizard. For example, in the previous example, a column entitled "Custom
Permission: view and comment" is added to "Modify permissions for roles" window in the security
configuration wizard.

## Procedure

To customize privileges:

1. Using IBM® Administration Console for
Content Platform Engine,
navigate to the ICMPrivilegeDefinition.xml file
in the object\_store\_name\Root Folder\IBM Business Automation
Workflow\Security
Configurations\Privilege Definitions folder and check out
the file.
2. Add, modify, or delete privileges by editing the ICMPrivilegeDefinition.xml file.
See the comments in the file for descriptions of all available
permissions.
3. Check in the revised ICMPrivilegeDefinition.xml file
by using IBM Administration Console for
Content Platform Engine.
In the Check In Content window, ensure that the Automatically
classify this document version on Check In option is selected.
4. Run the security configuration wizard in the  Case administration client to
view your changes.

- Privilege definition reference

The security configuration wizard in the Case administration client  sets permissions on workflow and content objects. A set of predefined privileges are available in the security configuration wizard by default. You can customize the default settings by editing the privilege definition file.