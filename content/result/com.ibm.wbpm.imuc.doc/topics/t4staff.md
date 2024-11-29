<!-- image -->

# Configuring the people directory provider

## About this task

| People directory provider                              | People directory provider plug-in name   |
|--------------------------------------------------------|------------------------------------------|
| Virtual Member Manager (VMM)                           | VMM people directory provider            |
| Lightweight Directory Access Protocol (LDAP) directory | LDAP people directory provider           |
| Local operating system user registry                   | System people directory provider         |
| WebSphere Application Server user registry             | User Registry people directory provider  |

- To use VMM and LDAP, you will probably need to customize the configuration
before using it, as described in the following topics.
- You can use the user registry and system plug-ins with the default configurations.
Because you can use these people directory providers without further customization,
they are often ideal for development and test environments.

- Configuring the Virtual Member Manager people directory provider

You configure the Virtual Member Manager (VMM) people directory provider so that Business Process Choreographer can perform people assignment, which determines who can start processes or claim activities or tasks. The default configuration of the VMM people directory provider is ready to use, and only needs to be configured if you introduce custom people assignment criteria.
- Configuring the LDAP people directory provider

You configure the Lightweight Directory Access Protocol (LDAP) people directory provider so that Business Process Choreographer can perform people assignment, which determines who can start processes or claim activities or tasks.

<!-- image -->

## Related tasks

- Troubleshooting people assignment

## Related information

- Authorization and people assignment for human tasks
- People resolution