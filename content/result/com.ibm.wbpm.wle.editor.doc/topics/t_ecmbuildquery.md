# Building a query for an Enterprise Content Management (ECM) search operation

## Before you begin

## About this task

Follow these steps to add a query that can be used in a search operation.

## Procedure

1. Open an Integration Service, Ajax Service or
Heritage Human Service.
2. From the palette, drag a Content Integration task to the canvas and
provide a meaningful name for it.
3. Click Implementation in the Properties view. Select a server and select
Search as the operation name.
4. Click the Content Filters tab.

Note: The Content Filters tab is not available in the Heritage Human Service Editor in the Process Designer. You can view the query in the Data
Mapping tab. To change the query, you can either edit it in the desktop  Process Designer, or change the method of search to Data
Mapping. You can then edit the query in the Data Mapping tab and make future changes using the
Process Designer. To switch to Data Mapping,
click the information icon   beside the input field and in the pop-up click Switch from Content Filters to
Data Mapping.
5. In the left column, select the search node you want to
create your query for, if you created more than one search step.
6 Beneath Build Search Filters completethe fields appropriate to your query.
    - In the Method of creating search field,select one of the following:
        - Content Filters: (Default) Select if you
want to use the fields on this Content Filters page to define your
search.
        - Data Mapping: Select if you are experienced
in writing Content Management Interoperability Services (CMIS) queries
and want to write your own hand-coded query (see the query section of the CMIS specification for
information on the syntax).Selection will disable the fields in
the Content Filters page and make the CMIS
query Input Mapping field editable on the Data
Mapping tab.
- Under Object Type , select the type of objectfor the search. These types are also discussed in the input and outputfields described in Data mapping in Enterprise Content Management operations .
    - Document: A type of document. For example,
the server could have an email type of document for storing critical
information sent by email. Click Select and
choose the document type from those available on the server. Examine
your application to decide what document type to select. For example,
an application about insurance claims might select insurance forms.
    - Folder: A type of folder that contains
documents. For example, the server could have a security type of folder
for containing documents related to security. Click Select and
choose the folder type from those available on the server.
- Under Properties, click Add to
see a list of properties for the type you selected previously. Select
additional properties based on your application. Using the application
about insurance claims mentioned previously, you might want to add
the property of when the insurance claim was made. As you select a
property, it appears as a column in the pane beneath Properties along
with sample data from the selected Enterprise Content Management server.
Columns are added from left to right. The layout of the result
set, the sorting of items in columns, and the priority of which column
is sorted first, second, third and so on is described in the following
table.

Table 1. Layout and sorting sequence of the result
set

Layout and items sorted
How to change the order

Layout of columns from left to right.
Select a column and use the arrows at the bottom
of the pane to move the column to the left or right. Use the Add or Remove buttons
to add or remove property columns. Alternately, for removal, select
the triangle at the top of the column and from the menu select Remove
property.

Ascending or descending order of items in each
column.
Click the number at the top of a column. Depending
on the direction of the triangle, the items will be arranged in an
ascending or descending order. If the column does not have a number
at the top, click the triangle and select Add sort order. 

Sorting priority of the result set; that is,
which column is sorted first, second, third and so on.
Click the triangle at the top of a column and
select Change sort order. The columns with
a number open in a dialog box. Select the arrows at the side of the
pane to move a selection up or down in the priority list. Click X to
remove a column from the sorting priority. 

The sorting priority of the result set can alternately
be done by selecting Result set order specified by process
variable and mapping to a variable containing the sorting
priority. The content of this variable is a CMIS query following the
standard CMIS syntax (see the link to the CMIS standard page in the Data
Mapping description). This option is helpful for having
the sorting priority set at run time. You may also use JavaScript.
- Under Search Criteria, you can specify
constraints for specific properties by selecting Add Search
Criterion. For example, you might want to only search
for objects whose Current State is equal to Working. Match
criteria lets you select all or any as a match criteria. All returns
items matching all the criteria specified in the filter. Any returns
items matching any single field in the filter. The match criteria
does not affect the search result columns shown in the Properties table
though it will affect the rows.
7. Save your work. File > Save All.

## What to do next

Using Document List and Document Viewer views, you can
turn your search into a list of documents that a user can browse,
select and view.

If the Search operation is used with a Document
List view, the ID column is not shown in the Document List. However,
the ID column should not be removed from the query. The IDs provide
the links to each document in the content repository. An ID is required
to perform any actions on the document, including showing the document
in a Document Viewer.