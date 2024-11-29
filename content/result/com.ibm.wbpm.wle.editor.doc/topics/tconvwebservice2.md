# Migrating heritage services that can be started by using a REST API

## About this task

- For a service flow, you configure the permission separately by using the Ajax Access property on
the Overview tab of the service flow editor.
- When converting a heritage service into a service flow, the setting is configured automatically:
    - If you convert a heritage Ajax service, the resulting service flow is configured to allow Ajax
calls from all users.
    - For all other types, for example, a general system service, the Ajax Access property is set to
"Do not allow Ajax calls". Important: In this case, if you used the system-wide
<startservice-valid-services> property to allow other types of services to be startable by using
the REST API, your converted service will not be startable from the REST API unless you configure
the Ajax Access property appropriately.

## Procedure

To reenable your scenario:

1. Convert all your heritage services into service flows.
2 For each of your converted services, check whether it must be startable from the REST API, andadjust the Ajax Access property accordingly:
    - Select Do not allow Ajax calls if the service flow has access to
private or confidential information that cannot be exposed through any Ajax calls.
    - Select Allow calls from trusted callers to allow only trusted
callers, such as known coach views or external implementations, to call the service flow. The users
who trigger the call must be authorized for the calling context. For example, if the service flow is
called in the context of a specified task, the user must be authorized for that task. This is the
default selection for service flows.
    - Select Allow calls from all users to allow any user that is
authenticated with Business Automation Workflow to call the service
flow.
3. Remove the property <startservice-valid-services> from the configuration files because it is
a compatibility setting that is no longer required.