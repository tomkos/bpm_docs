# Enabling security for additional components

## Before you begin

## About this task

- Service component architecture (SCA)
- Business Process Choreographer
- Common Event Infrastructure (CEI)

The identities associated with these components are used
to create authentication aliases that are required when security is
enabled. It is important to change these identities to appropriate
users from your account repository.

## Procedure

To create and configure the security settings for a profile,
use the administrative console to complete the following steps.

1. Display the Business Integration Security page. Expand Security,
and then click Business Integration Security.
2 For each of the component authentication aliases, providean appropriate user name and password that is to be used as the authenticationalias for this component.
    1. To select the alias that you want to change, click its
name in the Alias column. In some
cases, the Alias column might not provide a
link, in which case you select the check box in the Select column
corresponding to the alias that you want to edit, and click Edit.
    2. On the next page, provide
the user name and password that is to be used as the authentication
alias for this component. Note: The credentials that you
provide must exist in the user account repository that you are using.
    3. Click OK.

## Related information

- Modifying authentication aliases