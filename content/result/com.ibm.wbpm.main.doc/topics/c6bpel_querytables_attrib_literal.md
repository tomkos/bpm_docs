<!-- image -->

# Attribute type to literal representation mapping

Literal values can be used in expressions to define filter and
selection criteria, such as in filters of composite query tables,
and in filters that are passed to the query table API. The following
table describes the attribute types and their mapping to literal values.

| Attribute type   | Syntax and usage as literal value in expressions                                                                                                                                                                                                                                                                                     |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID               | ID ('string representation of an ID' )                                                                                                                                                                                                                                                                                               |
| ID               | When developing client applications, IDs are represented either as a string or as an instance of the com.ibm.bpe.api.OID interface. The string representation can be obtained from an instance of the com.ibm.bpe.api.OID interface using the toString method. The string must be enclosed in single quotation marks.                |
| STRING           | 'the string'                                                                                                                                                                                                                                                                                                                         |
| STRING           | The string must be enclosed in quotation marks.                                                                                                                                                                                                                                                                                      |
| NUMBER           | number                                                                                                                                                                                                                                                                                                                               |
| NUMBER           | The number as text, and no quotation marks. Constants are defined for some number attributes on predefined query tables, and can be used.                                                                                                                                                                                            |
| TIMESTAMP        | TS ('YYYY-MM-DDThh:mm:ss')                                                                                                                                                                                                                                                                                                           |
| TIMESTAMP        | The timestamp must be specified as:  YYYY is the 4-digit year  MM is the 2-digit month of the year  DD is the 2-digit day of the month  hh is the 2-digit hour of the day (24-hour)  mm is the 2-digit minutes of the hour  ss is the 2-digit seconds of the minute The timestamp is interpreted as defined in the user's time zone. |
| DECIMAL          | number.fraction                                                                                                                                                                                                                                                                                                                      |
| DECIMAL          | The decimal number as text and no quotation marks; the .fraction part is optional.                                                                                                                                                                                                                                                   |
| BOOLEAN          | true, false                                                                                                                                                                                                                                                                                                                          |
| BOOLEAN          | The Boolean value as text.                                                                                                                                                                                                                                                                                                           |

## Example

- filterOptions.setQueryCondition("STATE=2");
- filterOptions.setQueryCondition("STATE=STATE\_READY");
- a selection criterion on an attached query table TASK\_DESC:
"LOCALE='en\_US'"
- filterOptions.setQueryCondition( "PTID=ID('\_PT:8001011e.1dee8e51.247d6df6.29a60000')");