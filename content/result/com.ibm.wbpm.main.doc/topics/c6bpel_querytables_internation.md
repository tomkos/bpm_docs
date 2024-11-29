<!-- image -->

# Internationalization for query table meta data

Internationalization is supported for query table meta
data.

Display names and descriptions can be provided for composite query
tables in different locales. For example, a composite query table
can define a display name for the query table in the en\_US locale,
the de locale, and in the default locale. This is
done when the query table is developed using the Query Table Builder.
To deploy query tables with localized display names and descriptions,
the -deploy jarFile option must be used when the
query table is deployed on the Business Process Choreographer container.

In terms of locale handling, the behavior of the query table API
methods, queryEntities and queryRows,
and the meta data methods of the query table API, getQueryTableMetaData and findQueryTableMetaData,
is similar to that provided by Java resource bundles.

To make the display names and descriptions of the query table meta
data consistent with the contents of the query table, the value of
the $LOCALE system parameter depends on the locales
for which display names and descriptions are specified on the query
table.

## Example

- The client did not specify the locale it uses to present informationto the user. It is likely that the application is not enabled fordifferent languages.
    - A default locale is specified on the query table for display names
and descriptions. This is the case for all composite and supplemental
query tables that are built with the current version of the Query
Table Builder. Therefore, the value of $LOCALE is
set to default.
    - The query table does not specify display names or descriptions
on the query table for the default locale. This is the case for all
predefined query tables and for all query tables that are deployed
using the -deploy qtdFile option. The value of $LOCALE is
based on the Java resource bundle method.
- The client specified the locale to use to present informationto the user. For example, this is the case when the REST API for querytables is used.

- Display names and descriptions are specified on the query table.
The Java resource bundle method is used to calculate the value of $LOCALE,
based on the locale that is passed in by the client.
- Display names and descriptions are not specified on the query
table. The value of $LOCALE is set to the value that
is passed in by the client.

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