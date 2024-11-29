# JavaScript API namespaces

- The BPD namespace is used by scripts in processes and BPDs.
- The Service namespace is used by scripts in service flows and services.
- For scripts in client-side human services, see  JavaScript API for client-side human service development.

## BPD namespace

The following APIs are only available in the BPD namespace:

- tw.decision (only in gateways)
- tw.message
- tw.system.currentProcessInstance
- tw.system.enclosingCaseInstance
- tw.system.process
- tw.system.step

## Service namespace

The following APIs are only available in the Service namespace:

- tw.resource
- tw.system.coachValidation
- tw.system.currentTask
- tw.system.serviceFlow
- tw.system.task\_id
- tw.system.user\_fullName
- tw.system.user\_id
- tw.system.user\_locale
- tw.system.user\_localeCountry (deprecated)
- tw.system.user\_localeDescription
- tw.system.user\_localeLanguage (deprecated)
- tw.system.user\_loginName
- tw.system.user\_timeZone
- tw.system.user\_timeZoneOffset