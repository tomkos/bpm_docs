# Removing proxy documents that are associated with external documents

## Procedure

To remove one or more proxy documents:

1. Open the target object store in IBM Administration Console for
Content Platform Engine.
2. Select the Search node, then open a new search.
3. Click Simple View, then select External Document
class.
4. Under SQL View, add the following WHERE condition
before the OPTIONS condition:  
WHERE [CmAcmAssociatedCase]IS NULL
5. Run the search.
6. Click Search Results and select all the unreferenced proxy documents,
and then select Batch Operations.
7. Select the Delete option, click OK, and then
confirm the deletion.