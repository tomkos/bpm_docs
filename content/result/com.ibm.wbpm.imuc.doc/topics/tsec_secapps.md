# Configuring application security

## About this task

The applications that you host in your IBM Business Automation Workflow environment perform many business critical
functions that require security. Some applications will access, transfer, or alter sensitive
information (for example, payroll information or credit card details). Others will perform billing
or inventory management. The security of these applications is vitally important.

## Procedure

1. Ensure that administrative security is enabled.
2 Ensure that application security is enabled.
    1. On the administrative console, expand Security and
click Global security.
    2. Select Enable application security so
that IBM Business Automation Workflow will
require authentication from users who try to access a secured application.
3. Develop your applications in Integration Designer using
all appropriate security features.
4. Deploy your applications to your IBM Business Automation Workflow environment,
assigning users or groups to appropriate security roles.
5. Maintain the security of your IBM Business Automation Workflow environment.

- Enabling security for additional components

When a profile is created, default values are used for security credentials. After the profile is created, the security settings can be configured using the administrative console.

## Related information

- Configuring administrative and application security