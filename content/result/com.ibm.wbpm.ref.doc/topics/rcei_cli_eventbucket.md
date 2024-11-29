# eventbucket command-line utility

Buckets are used by the rapid purge utility to purge old event data from the event database. By
running this command, you can determine the current bucket configuration, or you can swap the active
and inactive buckets.

## Prerequisites

If WebSphere® security is enabled, your user ID must
be mapped to the eventAdministrator role to view or change the event database
bucket configuration.

## Syntax

```
eventbucket
[-status]
[-change]
```

## Parameters

## Examples

```
eventbucket -status
```

```
eventbucket -change
```