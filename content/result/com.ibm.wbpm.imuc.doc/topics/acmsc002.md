# Configuring security for case management solutions

## About this task

You can assign permissions to different users, groups,
and roles to determine the areas and objects of a solution in a FileNet® P8 object
store that these users can access. A set of permissions is called
a security configuration.

- Case types
- Case folders and subfolders
- Documents
- Activities
- Queues
- Rosters
- Comments
- Application spaces

The Case administration client provides
a wizard that can help you to create, modify, delete, and apply a
basic security configuration for your solution.  If your solution requires more complex permissions
than the defaults that are provided by the wizard, you can also customize
the permissions in the wizard.

Some environments
have specific or rigorous security requirements. If the security requirements
for your environment cannot be met by customizing the security wizard,
you can also use the FileNet P8 security
tools to set permissions manually on individual case objects.

Security for running work items that are associated with task objects in the target object store
are configured with service groups along with security on queues and rosters. For more information
related to IBM® Business Automation Workflow security roles and groups, see Security roles and groups.

- Configuring security by using the Case administration client wizard

In the production environment, you configure security on the case management objects that are controlled by Content Platform Engine. You must also configure security on Content Platform Engine process services queues, rosters, and application spaces. For Case Client, you configure view and edit access to pages.
- Customizing privileges and permissions

You can add, delete, or modify the permissions that you assign to roles and administrators in the Case administration client  security configuration wizard.
- Configuring security manually

The Case administration client security wizard provides basic case security. However, if you want to use a different security model or more specific settings, you can edit the permission settings on the case objects that are controlled by Content Platform Engine. You can also manually configure security for process services.