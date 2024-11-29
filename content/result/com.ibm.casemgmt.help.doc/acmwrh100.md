# Search widget

The Search widget provides a basic search and an advanced search. Case workers can use the basic
search to find cases based on a specific property value. The basic search help search across all
case types. Case workers can use the advanced search to find cases in a specific case type or to
narrow the search based on various properties.

You specify the properties that are available in the basic search and Advanced
Search dialog box by configuring the case type Search view.

The Case List widget runs the search by using the criteria that
is entered in the Search widget and displays the results.

You can edit the settings for the Search widget to
select the case properties that are to be displayed by default in
the Advanced Search dialog box.

Typically, searches are not case-sensitive. An exception is object store searches, which are
case-sensitive by default. You can change this default search behavior and enable case-insensitive
searches for object stores. For more information, seehttps://www.ibm.com/docs/en/filenet-p8-platform/5.5.x?topic=foq-setting-case-insensitive-search-behavior-object-store-searches.

For the search widget, the basic search interface helps you to select multiple values when you
try to search against multi-value properties. When you click Search for
multiple value search, an include all search occurs against the multi-value
property. In advance search, you can choose the type of search criteria for the multiple values,
like, include all, include any etc.

Search operators

- The basic search on the case search widget uses the STARTSWITH operator.
- The Advanced search where the case search properties are listed by default, uses the
EQUAL operator. The equal operator does not support the wildcard search. You can do
other operator searches in the advanced search that uses the User-specified
properties.

## Case widget settings

The search widget has the following settings:

1. 'Include properties from the Summary view in a search across case types'.
2 'Show My Cases Search' setting that helps you to view a list of cases:
    - Where you are a member of a case team that is assigned to a case. See Managing access to cases through roles and case teams.
    - Where you are assigned to a quick task that is associated with the case. See Adding quick tasks.
3. 'Restrict search to solution roles' setting that enables you to view only the users who are
assigned to the solution roles. This setting also applies to the 'Added by' and Modified by' user
selection.Note: This setting does not restrict the advanced search. An advanced search always
displays all the users.
4. 'Hide the advanced search'

- Search widget events

The Search widget uses events to enable users to search for cases in a solution.