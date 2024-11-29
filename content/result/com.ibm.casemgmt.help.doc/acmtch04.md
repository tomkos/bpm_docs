# Reducing the time needed for advanced searches

## Symptoms

## Resolving the problem

To
optimize performance of searches, ensure that you have an index that
corresponds to each of the most important searches that are run during
working hours. However, too many indexes can degrade performance.
Therefore, if you have many different ORDER BY conditions
or search conditions, create only those indexes that will improve
performance for most searches.

```
SELECT * FROM ECMPerfCase1 WHERE (CmAcmCaseState = 2 AND 
  cmis:createdBy = 'user\_2')
ORDER BY CmAcmCaseIdentifier ASC.
```

- If the search returns only a few results, use the following index: create index I\_CREATOR\_STATE on Container (creator, 
u<xy>\_CmAcmCaseState)
- If the search returns a large number of matches, sorting by the ORDER
BY CmAcmCaseIdentifier element might take too much time.
In this situation, use the following index:create index I\_CREATOR\_STATE\_ID on Container (creator, 
u<xy>\_CmAcmCaseState, u<xy>\_CmAcmCaseIdentifier)

```
SELECT * FROM <case type> WHERE (CmAcmCaseState = 2 AND 
   cmis:lastModifiedBy = <user\_name>) 
ORDER BY CmAcmCaseIdentifier ASC
```

```
create index I\_ModifyUser\_STATE\_ID on Container (modify\_user,
u<xy>\_CmAcmCaseState, u<xy>\_CmAcmCaseIdentifier)
```

```
SELECT * FROM ECMPerfCase1 WHERE (CmAcmCaseState = 2 AND 
   cmis:createdBy = 'user\_2' 
AND CCDM\_customername= 'value1') 
ORDER BY CmAcmCaseIdentifier ASC
```

- An index such as the I\_CREATOR\_STATE\_ID index
shown in Example 2 is not used in the query plan for this search.
- An index such as the I\_CREATOR\_STATE\_ID index
is used, but the index scans are still taking a long time.

```
create index I\_CNAME on container (u<xy>\_CCDM\_customername, creator, 
u<xy>\_CmAcmCaseState, u<xy>\_CmAcmCaseIdentifier)
```