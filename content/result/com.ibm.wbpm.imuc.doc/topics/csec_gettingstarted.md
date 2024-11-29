# Security considerations

For architecture considerations, see Chapter 4: Security architecture
considerations in Business Process
Management Design Guide: Using IBM Business Process Manager.

- Application security

Applications that run in IBM Business Automation Workflow are secured through a number of elements such as authentication, access control, data integrity, privacy, and identity propagation.
- Case management security

You manage the security for case management with users and groups that you configure in your Lightweight Directory Access Protocol (LDAP) repository and apply throughout the system. You must plan for different groups of users and different permission levels for your design environment and your production environment.
- Considerations for securing adapters

An adapter is the mechanism used by an application to communicate with an Enterprise Information System (EIS). The information exchanged between an application and an EIS can be highly sensitive and therefore important to ensure the security of this information transaction.