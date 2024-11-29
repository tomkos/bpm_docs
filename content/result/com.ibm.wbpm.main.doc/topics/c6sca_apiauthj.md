<!-- image -->

# (Deprecated)Authorization for JMS renderings (deprecated)

When Business Flow Manager is configured, the role JMSAPIUser must
be mapped to a user ID. This user ID is used to issue all JMS API
requests. For example, if JMSAPIUser is mapped to "User A",
all JMS API requests appear to the BPEL process engine to originate
from "User A".

| Request        | Required authorization                            |
|----------------|---------------------------------------------------|
| forceTerminate | Process administrator                             |
| sendEvent      | Potential activity owner or process administrator |

Special authority is granted to a person with the role of business
process administrator. A business process administrator is a special
role; it is different from the process administrator of a process
instance. A business process administrator has all privileges.

```
no unique ID for: <user ID>
```