<!-- image -->

# Creating query tables for Business Process Choreographer Explorer

You can use query tables instead of the EJB query API to improve the
performance of Business Process Choreographer Explorer. To create the query tables, use the Query
Table Builder.

## Before you begin

The Query Table Builder is available as an Eclipse plug-in
and can be downloaded from the SupportPacs site. Look for PA71 WebSphere® Process
Server -
Query Table Builder. To access the link, see the related references
section of this topic.

## Procedure

1. In the Query Table Builder, right-click your project, then select New > Composite Query Definition for Business Space. 
This option ensures that all of the columns that are required for Business Process
Choreographer Explorer are preselected.
2. Follow the wizard instructions to create a query table
definition. If required, add more properties to the query
table definition. Consider the following aspects when you define your
query table:
Filter criteria
When you create views in Business Process Choreographer Explorer
based on query tables, you cannot specify additional filter or variables
for your search criteria. You must specify these filter criteria and
the parameters for the variables when you create the query table. You
can use a query table for more than one view in Business Process Choreographer
Explorer by using parameters in the query table definition. For more
flexibility, you can also specify whether the default values of the
parameters can be overwritten when the query for the custom view is
run. 

Authorization
When you create views in Business Process Choreographer Explorer
based on query tables, you cannot filter your search criteria based
on the user role. You must set the filter criteria for user roles
when you define the query table. For primary query tables based on
template information, use instance-based authorization as the authorization
type and not role-based authorization. For primary query tables based
on instance information, specify the appropriate instance-based authorization
filter.
Internationalization
When you define properties in the Query Table Builder, you
can also specify the names and descriptions of these properties in
different languages. When the query for the customized view is run,
Business Process Choreographer Explorer uses the translation that
is appropriate for the language setting of your browser.
Display name and description for the query table definition
In the Query Table Builder, you can provide a display name and
description for all of the languages that are supported by the view.
Display name and description for the columns
At run time, Business Process Choreographer Explorer retrieves
the appropriate internationalized column names that are displayed
in a result list. For columns that come from your primary query table,
such as PIID, Business Process Choreographer Explorer uses the translations
that are already available for all of the supported languages. For
columns that come from an attached query table, such as QUERY\_PROPERTY,
you need to provide display names and descriptions in the Query Table
Builder in all of the languages that are supported by your business. 

Task names and description
If you have internationalized task names and descriptions in IBM Integration
Designer,
they are displayed in Business Process Choreographer Explorer according
to the language and country settings of your browser. If your browser
settings do not match the settings that are defined in the process
model, the translation of the default language is used.
Sort criteria
When you define sort criteria for a query table definition, be
aware that several properties, for example, process state, are stored
as integer values, while Business Process Choreographer Explorer displays
them as translated strings in the resulting list. This might produce
unexpected sorting results in some languages.

The new query
table definition consists of the predefined properties and any additional
properties that you define.

## What to do next