<!-- image -->

# Filters and selection criteria of query tables

Filters and selection criteria are defined during query table development using the Query
Table Builder, which uses a syntax similar to SQL WHERE clauses. Use these clearly defined filters
and selection criteria to specify conditions that are based on attributes of query
tables.%;

For information about installing the Query Table Builder, see the SupportPacs site. Look for PA71
WebSphere Process Server - Query Table Builder. To access the link, see the related references
section of this topic.

## Attributes

| Where                 | Expression                                                                                               | Available attributes                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Query table API       | Query filter                                                                                             | All attributes defined on the query table. If instance-based authorization is used, all attributes defined on the WORK\_ITEM query tables, prefixed with 'WI.'.  Examples:  STATE=STATE\_READY, if the query table contains a STATE attribute and if a STATE\_READY constant is defined for this attribute. STATE=STATE\_READY AND WI.REASON=REASON\_POTENTIAL\_OWNER, if the query table contains a STATE attribute and the query table uses instance-based authorization. |
| Composite query table | Query table filter                                                                                       | All attributes defined on the query table. If instance-based authorization is used, all attributes defined on the WORK\_ITEM query tables, prefixed with 'WI.'.  Examples:  STATE=STATE\_READY, if the query table contains a STATE attribute and if a STATE\_READY constant is defined for this attribute. STATE=STATE\_READY AND WI.REASON=REASON\_POTENTIAL\_OWNER, if the query table contains a STATE attribute and the query table uses instance-based authorization. |
| Composite query table | Primary query table filter                                                                               | All attributes defined for the primary query table.   Example: STATE=STATE\_READY, if the query table contains a STATE attribute and a STATE\_READY constant is defined for this attribute.                                                                                                                                                                                                                                                                             |
| Composite query table | Authorization filter                                                                                     | All attributes defined on the WORK\_ITEM predefined query table, prefixed with 'WI.'.  Example: WI.REASON=REASON\_POTENTIAL\_OWNER                                                                                                                                                                                                                                                                                                                                       |
| Composite query table | Selection criterion                                                                                      | All attributes defined on the related attached query table.  Example:  LOCALE='en\_US', if the attached query table contains a LOCALE attribute, such as the TASK\_DESC query table.                                                                                                                                                                                                                                                                                    |
| Composite query table | Selection criterion defined for supplemental query tables (with the optimizeForFiltering option enabled) | All attributes defined on the supplemental query table.  Example: VALUE='xyz', if the attached supplemental query table contains an attribute with this value.                                                                                                                                                                                                                                                                                                        |

Figure 1. Filters and selection criteria in expressions

<!-- image -->

## Expressions

```
expression  ::=  attribute binary\_op value |
                 attribute unary\_op |
                 attribute list\_op list |
                 (expression) |
                 expression AND expression |
                 expression> OR expression
```

- AND takes precedence over OR.
Subexpressions are connected using AND and OR.
- Brackets can be used to group expressions and must be balanced.

- STATE = STATE\_READY
- NAME IS NOT NULL
- STATE IN (2, 5, STATE\_FINISHED)
- ((PRIORITY=1) OR (WI.REASON=2)) AND (STATE=2)

An expression is executed in a certain scope which determines
the attributes that are valid for the expression. Selection criteria,
or query filters, are run in the scope of the query table on which
the query is run.

```
'(STATE=STATE\_READY AND WI.REASON=REASON\_POTENTIAL\_OWNER) 
OR (WI.REASON=REASON\_OWNER)'
```

## Binary operators

```
binary\_op ::= = | < | > | <> | <= | >= | LIKE | NOT LIKE
```

- The left-side operand of a binary operator must reference an attribute
of a query table.
- The right-side operand of a binary operator must be a literal
value, constant value, or parameter.
- The LIKE and NOT LIKE operators
are only valid for attributes of attribute type STRING.
- The left-side operand and the right-side operand must be of compatible
attribute types.
- User parameters must be compatible to the attribute type of the
left-side attribute.

- STATE > 2
- NAME LIKE 'start%'
- STATE <> PARAM(theState)

## Unary operators

```
unary\_op ::= IS NULL | IS NOT NULL
```

- The left-side operand of a unary operator must reference an attribute
of a query table. Valid attributes depend on the location of the filter
or selection criterion.
- All attributes can be checked for null values, for example: CUSTOMER
IS NOT NULL.

```
DESCRIPTION IS NOT NULL
```

## List operators

```
list\_op ::= IN | NOT IN
```

- The right-side of a list operator must not be replaced by a user
parameter.
- User parameters can be used within the list on the right-side
operand.

```
STATE IN (STATE\_READY, STATE\_RUNNING, PARAM(st), 1)
```

```
list ::= value [, list]
```

- The right-side of a list operator must not be replaced by a user
parameter.
- User parameters can be used within the list on the right-side
operand.

- (2, 5, 8)
- (STATE\_READY, STATE\_CLAIMED)

## Values

- Constant: A constant value, which is defined for the attribute
of a predefined query table. For example, STATE\_READY is
defined for the STATE attribute of the TASK query table.
- Literal: Any hardcoded value.
- Parameter: A parameter is replaced when the query is run
with a specific value.

Constants are available for some attributes of
predefined query tables. For information about constants that are
available on attributes of predefined query tables, refer to the information
about predefined views. Only constants that define integer values
are exposed with query tables. Also, instead of constants, related
literal values, or parameters can be used.

- STATE\_READY on the STATE attribute of the TASK
query table can be used in a filter to check whether the task is in
the ready state.
- REASON\_POTENTIAL\_OWNER on the REASON attribute
of the WORK\_ITEM query table can be used in a filter to check whether
the user who runs the query against a query table is a potential owner.
- Query filter STATE=STATE\_READY is the same as STATE=2,
if the query is run on the TASK query table.

Literals can also be used in expressions. A special
syntax must be used for timestamps and for IDs.

- STATE=1
- NAME='theName'
- CREATED > TS ('2008-11-26 T12:00:00')
- TKTID=ID('\_TKT:801a011e.9d57c52.ab886df6.1fcc0000')

- User parameters are specified using PARAM (name).
This parameter must be provided when the query is run. It is passed
as an instance of the com.ibm.bpe.api.Parameter class
into the query table API.
- System parameters are parameters that are provided at run time,without being specified when the query is run. The system parameters $USER and $LOCALE areavailable.
    - $USER, which is a string, contains the value
of the user who runs the query.
    - $LOCALE, which is a string, contains the value
of the locale that is used when the query is run. An example for the
value of $LOCALE is 'en\_US'.

- STATE=PARAM(theState)
- LOCALE=$LOCALE
- OWNER=$USER