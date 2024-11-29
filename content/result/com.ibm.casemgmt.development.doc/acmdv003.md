# Case history resource

The maintained case history is based on the Content Platform Engine audit feature. The entries
are stored as event objects in the Event table that is in the database for the object store. The
case history entries are audit events that are configured so that they can be retrieved by using the
GUID of the case folder. Therefore, not all audit entries correspond to a case history entry.

- GET method for the case history resource

The GET method returns the entries that make up the case history. You can set parameters to return only entries for specific object types, such as folders or activities, or for specific event types, such as creation or deletion of objects. If you do not set any parameters, all entries are returned. In addition, you can specify whether you want the complete information for the entries that are returned or only the summary information.