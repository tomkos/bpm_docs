<!-- image -->

# Query table queries for meta data retrieval

Queries are run on query tables in Business Process Choreographer
using the query table API. Methods are available to retrieve meta
data from query tables.

| Purpose                                                                                                        | Method                 |
|----------------------------------------------------------------------------------------------------------------|------------------------|
| Return the meta data of a specific query table                                                                 | getQueryTableMetaData  |
| Return a list of query table meta data with specific properties                                                | findQueryTableMetaData |
| Return contents of a query table, based on entities, and a subset of the meta data for the selected attributes | queryEntities          |
| Return contents of a query table, based on rows, and a subset of the meta data for the selected attributes     | queryRows              |

Meta data of query tables consists of data that relates to structure
and data that relates to internationalization.

| Meta data                | Description                                                                                                                           | Returned by getQuery- TableMetaData    | Returned by findQuery- TableMetaData   | Returned by queryEntities                             | Returned by queryRows                                 |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|----------------------------------------|-------------------------------------------------------|-------------------------------------------------------|
| Query table name         | The name of the query table                                                                                                           | Yes                                    | Yes                                    | Yes                                                   | Yes                                                   |
| Primary query table name | For supplemental and predefined query tables, name of the query table; for composite query tables the name of the primary query table | Yes                                    | Yes                                    | Yes                                                   | Yes                                                   |
| Kind                     | The type of query table: predefined, composite, or supplemental                                                                       | Yes                                    | Yes                                    | No                                                    | No                                                    |
| Authorization            | The authorization that is defined on the query table:  Use of work items Instance-based, role-based, or no authorization              | Yes                                    | Yes                                    | No                                                    | No                                                    |
| Defined attributes       | Meta data of the attributes that are defined on the query table                                                                       | Yes                                    | Yes                                    | No, meta data of the selected attributes is returned. | No, meta data of the selected attributes is returned. |
| Key attributes           | Key attributes of the query table                                                                                                     | Yes                                    | Yes                                    | Yes                                                   | No, not applicable to row-based queries.              |

| Meta data                                        | Description                                                                                     | Returned by getQuery- TableMetaData    | Returned by findQuery- TableMetaData   | Returned by queryEntities   | Returned by queryRows   |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------|----------------------------------------|----------------------------------------|-----------------------------|-------------------------|
| locales[]                                        | Locales for which display names and descriptions of the query table and attributes are defined. | Yes                                    | Yes                                    | No                          | No                      |
| Locale                                           | Value of the $LOCALE system parameter which results from the locale that is passed to the API.  | Yes                                    | Yes                                    | Yes                         | Yes                     |
| Display name and description of the query table  | Display names and descriptions for the query table, which are provided for all defined locales. | Yes                                    | Yes                                    | No                          | No                      |
| Display names and descriptions of the attributes | Display names and descriptions for the attributes, which are provided for all defined locales.  | Yes                                    | Yes                                    | No                          | No                      |

All EJB query table API methods which return query table meta data
accept a locale parameter, such as FilterOptions.setLocale and MetaDataOptions.setLocale.
This parameter should be set to the Java locale that the client uses
to present information to the user. This locale parameter is used
to calculate the value of the $LOCALE system parameter,
which can be used in filters and selection criteria. The locale that
is returned contains the actual Java locale that is used for $LOCALE.

If the display names and descriptions of a specific query table
are retrieved, pass getLocale to the related methods
to get the display names and descriptions in the same locale as the
descriptions of the tasks. For example, these descriptions are attached
using a selection criterion of 'LOCALE=$LOCALE'.

## Example

```
// the following example shows how meta data for a particular
// composite query table can be retrieved

…
// run the query
MetaDataOptions mdo = new MetaDataOptions("TASK", null, false, new Locale("en\_US"));
List list = bfm.findQueryTableMetaData(mdo);

// to get the meta data of a specific query table
// use bfm.getQueryTableMetaData(...)

// iterate through the list of query tables that have TASK as primary query table
// => at least one query table is returned: the predefined query table TASK

Iterator iter = list.iterator();
while (iter.hasNext()) {
	QueryTableMetaData md = (QueryTableMetaData) iter.next();
	Locale effectiveLocale = md.getLocale();
	String queryTableDisplayName = md.getDisplayName(effectiveLocale);
	System.out.println("found query table: " + queryTableDisplayName);
	List attributesList = md.getAttributeMetaData();
	Iterator attrIter = attributesList.iterator();
	while (attrIter.hasNext()) {
		AttributeMetaData amd = (AttributeMetaData) attrIter.next();
		String attributeDisplayName = amd.getDisplayName(effectiveLocale);
		System.out.println("\tattribute:" + attributeDisplayName);
	}
}
```

## Best match locale

When
specifying the conditions on an attached query table, using the value $LOCALE can
return unexpected results if the specified locale does not match the
metadata exactly. For example if you pass a locale en\_US with
a query against a query table that has metadata specifying the language
as en, the result returned will be null.

To
avoid such cases, you can use LOCALE=$LOCALE\_BEST\_MATCH,
which applies a best-match algorithm to calculate the actual locale
used in the query. For example, a query with locale en\_US against
a query table in language en is performed using en.

You
cannot specify any other logical or comparison operators in the condition LOCALE=$LOCALE\_BEST\_MATCH.
You can only use the best-match locale condition on attached query
tables, specifying it as a condition on other queries results in an
error.