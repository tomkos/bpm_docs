# Troubleshooting ECMException ObjectStore.get\_RootFolder returns null

## Symptoms

This issue is specific to IBM Content
Navigator, Version 2.0.3
Fix Pack 1.

Assume that a customer has created several object stores and is granted administrative access to
different service accounts of each object store. For Instance,

1. A service account Admin1 is granted administrative access to object stores OS1 and OS3.
2. A service account Admin2 is granted administrative access to object store OS2, and so on.

When Admin1 runs a first CMIS operation, for example - query documents on the object store
OS1, IBM CMIS for FileNet Content Manager would
retrieve all object stores (OS1 and OS3) that Admin1 has administrative access. This also caches the
list of object stores to use against subsequent CMIS operations.

Later when Admin2 runs another CMIS operation, say create a document on its object store
OS2, IBM CMIS for FileNet Content Manager assumes
that OS2 is available in the cache and tries to access its root folder, which results in the
ECMException that ObjectStore.get\_RootFolder is null. This is because the cache
does not contain OS2.

## Resolving the problem

1. Grant administrative access to a common admin user for all object stores. This common user
should always make the first operation against IBM CMIS for FileNet Content Manager. However, this is difficult to
achieve in a scenario, where there might be multiple users, who must wait for the first user to be
the common user. So this is a not an optimal approach.
2. Alternatively, configure IBM CMIS for FileNet Content Manager to use a J2C authentication
alias as described in IBM CMIS for FileNet Content Manager known problem - You must create
an IBM FileNet P8 administrator alias to ensure that object store data is cached
correctly.This would ensure that all information on the visible object stores in the
domain is retrieved and that the necessary information is available to complete user
requests.