# Working with a search result programmatically

Parsing search results programmatically
can be subdivided into two methods: parsing a generic search result,
that is, parsing a standard query returning a set of documents in
business objects and parsing a strongly typed search result where
the business object type is specified. A strongly typed search result
adds precision that can improve the performance when parsing it over
the generic search result.

- Parsing a generic search result
- Parsing a strongly typed search result

## Parsing a generic search result

The
following JavaScript code assumes that query for the search result
was created in the standard way as described in Building a query for an Enterprise Content Management search operation. In other words the query did
not make use of the optional Return type input parameter where a specific
business object type is specified. The Return type input parameter
is described in the Search operation section in Data mapping in Enterprise Content Management operations.

The SELECT statement used
in the following example is SELECT cmis:name, cmis:creationDate,
cmis:objectId FROM cmis:document ORDER BY cmis:name ASC.

In
this example, we take a generic search result and extract the IDs
of all the documents found, and store them in an array. Document IDs
are a basic piece of information used by most of the ECM operations.

When
there is no return type specified for the search operation, the ECMSearchResult.resultSet
field contains an ECMSearchResultSet object, which in turn holds a
list of ECMSearchResultRow objects.

The ECMSearchResult.propertyMetadata
has the column information as specified in the CMIS query, and can
be used to search for specific columns, as shown below.

```
/* Property metadata is captured by the ECMPropertyMetadata business object */
var columnMetadata = tw.local.searchResult.propertyMetadata;

var idColumnIndex = -1;

/*
 * Check if a search result found. Find which column contains the ID column and
 * save its index so we can retrieve the right value from each row.
 */

if (tw.local.searchResult.numItems > 0) {
	for (var i = 0; i < columnMetadata.length; i++) {
		if (columnMetadata[i].queryName == 'cmis:objectId') {
			idColumnIndex = i;
			break;
		}
	}

	tw.local.documentIds = new tw.object.listOf.ECMID();

	var resultSet = tw.local.searchResult.resultSet;
	for (var i = 0; i < resultSet.row.length; i++) {
		tw.local.documentIds[i] = resultSet.row[i].column[idColumnIndex];
	}
} else {
	/* No search result */
}
```

## Parsing a strongly typed search
result

The following JavaScript code assumes that the query
for the search result was created with the optional Return type input
parameter where a business object type is specified. The field for
the Return type input parameter is only editable if you selected the
Data Mapping option on the Content Filters page. The Return type input
parameter is described in the Search operation section in Data mapping in Enterprise Content Management operations.

The Return type parameter
should be mapped to a public output variable, for example, documentBO,
that has an ECMSearchResultBO type. Note that you create the ECMSearchResultBO;
it is not provided for you. Select the List check box.

The
SELECT statement used in the following sample is SELECT cmis:objectId
AS documentId FROM cmis:document .

```
/* In this example, we take a strongly typed result and extract the business objects 
returned by the search operation. The ID column is mapped to the business object's 
documentID property in the CMIS SELECT statement. So we simply return the array of 
business objects for the caller to process.
*/

/* Set the return list of ECMSearchResultBO to output the output variable and we are done */
var resultSet = tw.local.searchResult.resultSet;

if(resultSet.row.length > 0){
    tw.local.documentBO = resultSet.row;
}
```