# Specifying search criteria for the IBM\_BPM\_Document\_Properties
property

## About this task

To specify a search
condition in the Content Filter page or to provide your own CMIS search
query, complete the steps in the following procedure:

## Procedure

1 To specify a search condition in the ContentFilter page, complete the following steps: Additional information about specifying search criteria is foundin the topic "Building a query for an Enterprise Content Managementsearch operation."
    1. In the Search Criteria section, select the Properties property.
    2. For the operator, select the contains property.
    3. Specify the search value in the format BPM\_property\_name,search\_value.
For example, the search condition approved,true would
find all BPM documents that have a BPM property name approved with
a value of true.
2. To provide your own CMIS search query, use the same format
that is used for the search condition in the Content Filter page.
For example, the following search query will return the same results
as the above search condition: ANY IBM\_BPM\_Document\_Properties IN('approved,true')Additional
information about specifying a CMIS query is found in the "Query"
section of the OASIS Content Management Interoperability Standard
(CMIS) specification.