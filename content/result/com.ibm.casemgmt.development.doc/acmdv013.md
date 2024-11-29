# Case management REST resource URIs

## Syntax

```
http://host:port/context/CASEREST/v1/resourceName[?resourceParameters]
```

The REST protocol version identification (/v1) enables subsequent updates to the REST
protocol.

The following example shows a URI for the particular activity instance resource.

```
http://example.com:9080/CaseManager/CASEREST/v1/task
/7A75A997-0E42-406E-AZC4-EE55D7DER9PF?TargetObjectStore=MyExampleObjectStore
&Grouping=ROD
```

## Special characters

Besides ASCII letters
and decimal digits, you can use the following characters without any
special notation in the case management REST URIs:  $ - \_ . + ! *
' ( ) ,

You must escape any other character, including spaces,
double quotation marks (“ and ”), and percent signs (%). To escape
a character in UTF-8 encoding, use %xy where
xy is the two-digit hexadecimal value of the character. For example,
%20 is the escaped representation of a space in a URI.