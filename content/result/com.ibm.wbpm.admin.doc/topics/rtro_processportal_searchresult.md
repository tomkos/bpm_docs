# Process Portal:
Troubleshooting problems with search results

## Symptom and cause

- In the Overview page of the Process Performance and
the Team Tasks page of the Team Performance dashboard:
The search result is too large. Refine your search and try again.
- In the Work or saved search dashboards:
CWTBG0567E:Too many potential search results. To limit the number of search
results, use more specific search terms or AND operators with the search terms.

```
[99-9-99 13:03:04:354 CST] 00000064 TaskSearchRet 1 com.ibm.bpm.search.task.search.TaskSearchRetrievalImpl searchTaskIndex
Task Search Found 108601                                                
[99-9-99 13:03:04:354 CST] 00000064 TasksResource 2                    
com.ibm.bpm.rest.impl.task.TasksResource getWleQueryResult Found too    
many hits, exceeding the allowed maximum of 100000
```

In both error situations, the search results are limited by the value of
the <index-search-max-hits> property in the 99Local.xml
server configuration file. The default value of the property is 100000. Be aware that setting a
higher property value might impact the response time and the memory usage according to the available
environment resources. In the trace file example, the full-text search returns 108601 results, which
is more than the configured default limit of 100000.

## Resolving the problem

- Process Portal users
can refine their searches by including filters in the search criteria.
- Administrators can override the default value by increasing the value of the
<index-search-max-hits> property in the 100Custom.xml file.
Before you increase the value of the property in production environments, test the effect of the
higher search limit on performance.