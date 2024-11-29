<!-- image -->

# Setting up security for the Business Space component and Heritage Process Portal

## About this task

For best results, enable security before you configure the Business Space component. If you enable security later, use the
administrative console Global security administration page, to enable both administrative security
and application security. On the same administrative console page, you also can designate a user
account repository, including changing from the default federated repositories option to another
user repository. To designate which users can perform administrator actions in Heritage Process Portal, assign the Business Space superuser role. Other security
configuration might be needed for your specific environment.

- The Business Space component does not support
fine-grained access control in Java 2 security.
- Heritage Process Portal is deprecated.

- Selecting the user repository for Heritage Process Portal (deprecated) and the Business Space component

The federated repositories option is the default user account repository option for profiles. You can change the type of user account repository if needed for your environment.
- Allowing insecure access to Heritage Process Portal

The Business Space component is configured to be accessed by HTTPS by default.  You can change the protocol from the default or back to the default by running a script.
- Setting up security for system REST services

To set up security for the data in the widgets based on users and groups, you must modify the users that are mapped to the REST services gateway application.
- IBM Business Automation Workflow widget security considerations

Depending on the widgets you use in Heritage Process Portal (deprecated) for your product, you might assign either administrative user group roles to control access to data in a widget, or you might assign an additional layer of role-based access for your widget.
- Assigning the superuser role

You can assign users to be superusers (or Heritage Process Portal administrators). A superuser can view, edit, and delete all spaces and pages, can manage and create templates, and can change ownership of a space by changing the owner ID.
- Assigning the superuser by user group

You can assign users to be superusers (or Heritage Process Portal administrators) based on user groups.
- Preventing users from creating spaces

You can customize IBM Business Automation Workflow so that only users logging in with a superuser role can create spaces.
- Enabling searches for user registries without wildcards

If your user registry is set up to not use wildcards, you must complete additional configuration steps so that searches work properly in Heritage Process Portal (deprecated) and for widgets that search the user registry.

## Related information

- WebSphere Application Server security documentation
- Configuring Lightweight Directory Access Protocol search filters
- Managing the realm in a federated repository configuration
- Selecting a registry or repository