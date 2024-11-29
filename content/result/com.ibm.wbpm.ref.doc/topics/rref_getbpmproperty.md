# getBPMProperty command

The getBPMProperty command is run using
the AdminTask object of the wsadmin scripting client.

## Prerequisites

The following conditions must
be met:

- In a network deployment environment, run the
command on the deployment manager node. In a single-server environment,
run the command on the stand-alone server.
- If the deployment manager or stand-alone server is stopped, use
the wsadmin -conntype none option to run the command
in disconnected mode (which is the recommended mode for this command).
- If the deployment manager or stand-alone server is running, you
must connect with a user ID that has WebSphere Application Server
configurator privileges. Do not use the wsadmin -conntype
none option.

## Location

Start the wsadmin scripting client
from the profile\_name/bin directory.
The getBPMProperty command does not write to a
log file, but the wsadmin scripting client always writes a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
getBPMProperty
[-de deployment\_environment\_name]
-name custom\_property\_name
```

## Parameters

- BPC.ExternalActivityDefaultURL
(String) See Adding a Business Automation Workflow system to the federated environment and Changing custom properties for Process Portal.
- ProcessCenter.AdvancedDeploymentDEScoped
(Boolean) See Isolating deployment environments.
- ProcessCenter.BpdAutoTrackingEnabledDefault
(Boolean) For an overview, see Tracking IBM Business Automation Workflow performance data.
- ProcessCenter.BpdTrackingEnabledDefault
(Boolean) For an overview, see Tracking IBM Business Automation Workflow performance data.
- ProcessServer.AlertDefinitionsStatusEnabled
(Boolean) See Disabling and enabling the checking of alerts.
- ProcessServer.CompatibilityPortalNotificationSecurityCheck
(Boolean)
- ProcessServer.CustomURisVMM
(Boolean)
- ProcessServer.ExternalActivityDefaultURL
(String) See Adding a Business Automation Workflow system to the federated environment and Changing custom properties for Process Portal.
- ProcessServer.MinimumCoachViewRefreshInterval
(Integer) See The coach view context object and Changing custom properties for Process Portal.
- ProcessServer.ProvideOnlineStatusData
(Boolean) See Changing custom properties for Process Portal.
- ProcessServer.TimerCoachViewEnabled
(Boolean) See The coach view context object and Changing custom properties for Process Portal.
- ProcessServer.TimerCoachViewRefreshInterval
(Integer) See The coach view context object and Changing custom properties for Process Portal.
- ProcessServer.webService\_InvalidXSDTypeThrowException
(Boolean)
Here are some security-hardening properties. For information about
these properties and other security-hardening properties, see  Security-hardening properties.
- Security.AllowedHttpMethods
(String). The value is a comma-separated list of acceptable HTTP methods, such as
the methods GET,PUT,POST,DELETE,HEAD,OPTIONS that are set by default.
Requests with a method that is not on the allowlist will be rejected with the message
HTTP 403 (forbidden).Note: In Business Automation Workflow V8.6 2018.03, the
security-hardening properties were changed from
ProcessServer.property to
Security.property. When you upgrade to V8.6 2018.03, these
properties are automatically migrated to their new names. If you have automated scripts to set or
read these properties using AdminTask.getBPMProperty(...) or
AdminTask.setBPMProperty(...), the AdminTask will accept either name. However,
names with ProcessServer.property for these security-hardening
settings are deprecated.
- Security.CsrfProtectionRefererWhitelist
(String) in which the value is a comma-separated list of allowed REFERER headers to
prevent cross-site request forgery attacks.
- Security.CsrfProtectionOriginWhitelist
- Security.CsrfProtectionRefererallowlist
- Security.CsrfSessionTokenProtectedUris
(String)
- Security.CsrfSessionTokenSalt
(String)
- Security.XFrameOptionsHeaderValue
(String) (deprecated)
- Security.ContentSecurityPolicyHeaderValue

## Examples

```
wsadmin -user admin -password admin -lang jython
wsadmin>AdminTask.getBPMProperty(['-de', 'De1', '-name', 'ProcessServer.TimerCoachViewEnabled'])
```