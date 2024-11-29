<!-- image -->

# Where clause

The syntax of a where clause is similar to the syntax of an SQL WHERE clause.
You do not need to explicitly add an SQL from clause or join predicates
to the API where clause, these constructs are added automatically
when the query runs. If you do not want to apply filter criteria,
you must specify null for the where clause.

The where-clause syntax supports:

- Keywords: AND, OR, NOT
- Comparison operators: =, <=, <, <>, >,>=, LIKEThe LIKE operation supports the
wildcard characters that are defined for the queried database.
- Set operation: IN

The following rules also apply:

- Specify object ID constants as ID('string-rep-of-oid').
- Specify binary constants as BIN('UTF-8 string').
- Use symbolic constants instead of integer enumerations. For example,
instead of specifying an activity state expression ACTIVITY.STATE=2,
specify ACTIVITY.STATE=ACTIVITY.STATE.STATE\_READY.
- If the value of the property in the comparison statement contains single quotation marks ('),
double the quotation marks, for example,
TASK\_CPROP.STRING\_VALUE='d''automatisation'.
- Refer to properties of multiple name-value pairs, such as custom properties, by adding a
one-digit suffix to the view name. For example: TASK\_CPROP1.NAME='prop1' AND
"TASK\_CPROP2.NAME='prop2'
- Specify time-stamp constants as TS('yyyy-mm-ddThh:mm:ss') .To refer to the current date, specify CURRENT\_DATE asthe timestamp.You must specify at least a date or a time valuein the timestamp:
    - If you specify a date only, the time value is set to zero.
    - If you specify a time only, the date is set to the current date.
    - If you specify a date, the year must consist of four digits; the
month and day values are optional. Missing month and day values are
set to 01. For example, TS('2003') is the same as TS('2003-01-01T00:00:00').
    - If you specify a time, these values are expressed in the 24-hour
system. For example, if the current date is 1 January 2003, TS('T16:04') or TS('16:04') is
the same as TS('2003-01-01T16:04:00').

## Examples of where clauses

- Comparing an object ID with an existing ID WORK\_ITEM.WIID = ID('\_WI:800c00ed.df8d7e7c.feffff80.38')This
type of where clause is usually created dynamically with an existing object ID from a previous call.
If this object ID is stored in a wiid1 variable, the clause can be constructed
as:WORK\_ITEM.WIID = ID('" + wiid1.toString() + "')
- Using time stampsACTIVITY.STARTED >= TS('2002-06-1T16.00.00')
- Using symbolic constantsWORK\_ITEM.REASON = WORK\_ITEM.REASON.REASON\_OWNER
- Using Boolean values true and falseACTIVITY.BUSINESS\_RELEVANCE = TRUE
- Using custom propertiesTASK\_CPROP1.NAME = 'prop1' AND " TASK\_CPROP1.STRING\_VALUE = 'v1' AND
 TASK\_CPROP2.NAME = 'prop2' AND " TASK\_CPROP2.STRING\_VALUE = 'v2'