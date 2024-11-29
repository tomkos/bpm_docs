# Supporting external documents in production environments

## About this task

In a production environment, users cannot add external documents into case folders because the
default instance security settings of the External Document class are removed incorrectly.

To work around this issue, manually configure the default instance security settings of the
External Document class:

## Procedure

1. In the Administration Console for Content Platform Engine, open your
target object store and click Data Design > Classes > Document > External Document.
2. On the Default Instance Security tab, add an entry with the name
#CREATOR-OWNER and assign it the View properties permission. Also, ensure
that the Default Instance Owner field is set to
#CREATOR-OWNER.