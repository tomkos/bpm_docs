# Synchronizing users between the BPM database and the user registry

1. Remove the user from the user registry.
2. If you are using a federated repository, clear the user from the
cache of the federated repository adapter as described in clearIdMgrUserFromCache command. This is not
necessary if you are using a ﻿local operating system registry, standalone
LDAP registry, or standalone custom registry.
3 Synchronize the BPM database and the user registry by performingone of the following:
    - Run the syncExistingUsers.[bat|sh] script,
as described in Synchronizing users.
    - Run the BPMSyncExistingUsersTask command
with the parameter -userState, as described in Runtime user availability and lifecycle.
    - Call the BPM operations REST API POST
https://host:port/ops/std/bpm/users/user\_id/sync?sync\_user\_state=true will
activate the user ID if it is present in the user registry or will
deactivate the user ID if it is not in the user registry. For more
information about the synchronize user API, see Workflow REST API programming.Important: The synchronize
user API must be called with an HTTP header that contains a valid
BPMCSRFToken, which is obtained as described in Preventing cross site request forgery.