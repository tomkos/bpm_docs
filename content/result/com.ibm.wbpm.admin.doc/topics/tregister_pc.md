# Traditional: Registering a Process Center (deprecated)

## Before you begin

- You can share content only to a Process Center that is the same
or later version.
- For versions of Process Center before V19.x,
the first three digits of the version number must match to enable sharing content.

## Procedure

To register a Process Center, complete
the following steps:

1. In Process Center, select
the Admin tab, and then click Registration.
2. On the Registration page, select Enable Registration and
Sharing, and then enter a unique name for your Process Center.
3. Click Create Registration.
4 In the Register a content source field, select RemoteProcess Center . Note: You can select either of the following options to register a remote source:
    - Remote Process Center - Register a remote Process Center.
    - Remote Content Source - Register an external source of assets, such
IBM
Rational® Team Concert®.
5. In the Remote Process Center URL field, enter the remote Process Center URL. The
Process Center URL
must be in the form of https://servername:port. When you configure a custom context
root on the target system, specify the Process Center URL with the
context root prefix as https://<servername>:<port>/<prefix>/ProcessCenter.
Before you specify the HTTPS protocol, you must set up a security trust between the participating
process centers. For more information, see Configuring cross-cell security for IBM Workflow Center.

Restriction: If you use a proxy server, you must specify the proxy server URL. This
restriction applies only to a clustered environment.

## What to do next

## Related tasks

- Traditional: Revoking a Process Center registration (deprecated)
- Traditional: Sharing toolkit (deprecated)
- Traditional: Stopping toolkit sharing (deprecated)
- Traditional: Subscribing to a toolkit (deprecated)
- Traditional: Managing subscriptions and monitoring toolkit (deprecated)

## Related reference

- Traditional: Rules for sharing and archiving toolkit (deprecated)