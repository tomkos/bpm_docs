<!-- image -->

# Business object (BO) instance data validation qualifier

The runtime validator that underlies this qualifier checks
the XSD types being passed by a business object are those that were
expected by the client.When
you add the qualifier to a Java™ interface,
only the business objects (passed in as data objects) are validated.

- For all of its interfaces
- For an individual interface
- For an individual operation of an interface

- Log error and continue (default) - If an error is encountered,
the error is logged and the requested operation is performed. There
is no guarantee that the service can handle data that is not valid,
so a runtime error could result.
- Throw exception - If an error is encountered, an exception
is thrown and the operation is not performed.

## Programming notes

Verifying data in this
way limits performance. When performance is a critical consideration,
you should not use this qualifier.

The IBM® Integration
Designer qualifier
is supported by the BO instance validator in IBM Business Automation
Workflow.
You can access  the API information about that qualifier in the IBM Business Automation
Workflow documentation.

The
following tables list the specific validation checks that are performed
on the business object XSD by the data validation feature. They show
which data types and constraints are supported (S), not supported
(NS), or partially supported (PS) by the validator. An empty cell
indicates that the pair is not supported according to the XML Schema
1.1 specification.

|                  | Length   | minLength   | maxLength   | Pattern   | Enumeration   | minInclusive   | maxInclusive   | minExclusive   | maxExclusive   | totalDigits   | fractionDigits   |
|------------------|----------|-------------|-------------|-----------|---------------|----------------|----------------|----------------|----------------|---------------|------------------|
| String           | S        | S           | S           | P         | S             |                |                |                |                |               |                  |
| boolean          |          |             |             | S         |               |                |                |                |                |               |                  |
| Decimal          |          |             |             | P         | S             | S              | S              | S              | S              | S             | S                |
| precisionDecimal |          |             |             | P         | S             | S              | S              | S              | S              | S             |                  |
| float            |          |             |             | P         | S             | S              | S              | S              | S              |               |                  |
| double           |          |             |             | P         | S             | S              | S              | S              | S              |               |                  |
| duration         |          |             |             | P         | P             | P              | P              | P              | P              |               |                  |
| dateTime         |          |             |             | P         | S             | S              | S              | S              | S              |               |                  |
| Time             |          |             |             | P         | P             | P              | P              | P              | P              |               |                  |
| Date             |          |             |             | P         | S             | S              | S              | S              | S              |               |                  |
| gYearMonth       |          |             |             | P         | S             | S              | S              | S              | S              |               |                  |
| gYear            |          |             |             | P         | S             | S              | S              | S              | S              |               |                  |
| gMonthDay        |          |             |             | P         | P             | P              | P              | P              | P              |               |                  |
| gDay             |          |             |             | P         | P             | P              | P              | P              | P              |               |                  |
| gMonth           |          |             |             | P         | P             | P              | P              | P              | P              |               |                  |
| hexBinary        | S        | S           | S           | S         | S             |                |                |                |                |               |                  |
| base64Binary     | S        | S           | S           | S         | S             |                |                |                |                |               |                  |
| anyURI           | S        | S           | S           | S         | S             |                |                |                |                |               |                  |
| QName            | N        | N           | N           | N         | S             |                |                |                |                |               |                  |
| NOTATION         | S        | S           | S           | S         | S             |                |                |                |                |               |                  |

- Pattern is a constraint on the value space of a data type
which is achieved by constraining the lexical space to literals which
match each member of a set of patterns. But only the value space is
available for the BO run time, it is hard for the BO run time to support
the lexical space.  For example, A Pattern for Decimal is "\+[0-9]*.[0-9]*"
(a decimal with a plus sign). "+9.9" should be a valid one. But when
"+9.9" is loaded into the runtime environment, it would be "9.9".
Then the validator would report pattern validation error.
- Duration is only partially supported because it requires
the validator to compare two strings. For these data types-gMonthDay,
gDay, gMonth- the corresponding java type is java.lang.String.
Consider this example: The time value `09:30:41+08:00' is greater
than time value `09:30:40' with string comparison, while the former
is in fact less than the latter with time comparison.
- For QName type, the BO instance data validator does not
support length, minLength, maxLength and pattern facet
validation. The value space of QName is the set of tuples {namespace
URI, local part}.  For length, minLength and maxLength, according
to XSD specification 1.1, any value is valid. And these three facets
are deprecated. It is impossible to apply a pattern on a namespace
URI.

|                    | Length   | minLength   | maxLength   | Pattern   | Enumeration   | minInclusive   | maxInclusive   | minExclusive   | maxExclusive   | totalDigits   | fractionDigits   |
|--------------------|----------|-------------|-------------|-----------|---------------|----------------|----------------|----------------|----------------|---------------|------------------|
| anySimpleType      |          |             |             |           |               |                |                |                |                |               |                  |
| anyAtomicType      |          |             |             |           |               |                |                |                |                |               |                  |
| normalizedString   | S        | S           | S           | S         | S             |                |                |                |                |               |                  |
| Token              | S        | S           | S           | S         | S             |                |                |                |                |               |                  |
| Language           | S        | S           | S           | S         | S             |                |                |                |                |               |                  |
| NMTOKEN            | S        | S           | S           | S         | S             |                |                |                |                |               |                  |
| NMTOKENS           | S        | S           | S           | S         | S             |                |                |                |                |               |                  |
| Name               | S        | S           | S           | S         | S             |                |                |                |                |               |                  |
| NCNAME             | S        | S           | S           | S         | S             |                |                |                |                |               |                  |
| ID                 | S        | S           | S           | S         | S             |                |                |                |                |               |                  |
| IDREF              | S        | S           | S           | S         | S             |                |                |                |                |               |                  |
| IDREFS             | S        | S           | S           | S         | S             |                |                |                |                |               |                  |
| ENTITY             | S        | S           | S           | S         | S             |                |                |                |                |               |                  |
| ENTITIES           | S        | S           | S           | S         | S             |                |                |                |                |               |                  |
| Integer            |          |             |             | P         | S             | S              | S              | S              | S              | S             | S                |
| nonPositiveInteger |          |             |             | S         | S             | S              | S              | S              | S              | S             | S                |
| negativeInteger    |          |             |             | S         | S             | S              | S              | S              | S              | S             | S                |
| Long               |          |             |             | P         | S             | S              | S              | S              | S              | S             | S                |
| Int                |          |             |             | P         | S             | S              | S              | S              | S              | S             | S                |
| Short              |          |             |             | P         | S             | S              | S              | S              | S              | S             | S                |
| Byte               |          |             |             | S         | S             | S              | S              | S              | S              | S             | S                |
| nonNegativeInteger |          |             |             | S         | S             | S              | S              | S              | S              | S             | S                |
| unsignedLong       |          |             |             | S         | S             | S              | S              | S              | S              | S             | S                |
| unsignedInt        |          |             |             | S         | S             | S              | S              | S              | S              | S             | S                |
| unsignedShort      |          |             |             | S         | S             | S              | S              | S              | S              | S             | S                |
| unsignedByte       |          |             |             | S         | S             | S              | S              | S              | S              | S             | S                |
| positiveInteger    |          |             |             | S         | S             | S              | S              | S              | S              | S             | S                |
| yearMonthDuration  |          |             |             | S         | P             | P              | P              | P              | P              | P             | P                |
| dayTimeDuration    |          |             |             | S         | P             | P              | P              | P              | P              | P             | P                |