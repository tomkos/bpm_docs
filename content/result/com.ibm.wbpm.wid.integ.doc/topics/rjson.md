<!-- image -->

# JavaScript Object Notation (JSON) format

JavaScript Object Notation
(JSON) is a lightweight data-interchange format. JSON is easy for
humans to read and write. JSON is easy for machines to parse and generate.
JSON is based on a subset of the JavaScript Programming
Language, Standard ECMA-262 3rd Edition - December 1999. JSON is a
text format that is completely language independent but uses conventions
that are familiar to programmers of the C-family of languages, including
C, C++, C#, Java™, JavaScript,
Perl, Python, and many others. These properties make JSON an ideal
data-interchange language. More details on the JSON format can be
found at Introducing
JSON.

Note: The property name in the JSON data should
match exactly with the property name in the business object.

## Single cardinality contained business object

Given
the following business object:

<!-- image -->

And given the following
values for the business object properties:

| Business Object    | Property                                                                               | Value                                                                |
|--------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Customer  	Address | firstName lastName streetAddress city state postalCode phoneNumbers[0] phoneNumbers[1] | John Smith 21 2nd Street New York NY 10121 212-732-1234 646-123-4567 |

The JSON format is the following:

```
1	{
2	    "firstName": "John",
3	    "lastName": "Smith",
4	    "address": {
5	        "streetAddress": "21 2nd Street",
6	        "city": "New York",
7	        "state": "NY",
8	        "postalCode": 10021
9	    },
10	    "phoneNumbers": [
11	        "212-732-1234",
12	        "646-123-4567"
13	    ]
14	}
```

## Multiple cardinality contained business object

Given
the following business object:

<!-- image -->

And given the
following values for the business object properties:

| Business Object                      | Property                                                                                                                   | Value                                                                                                     |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Customer  	Address[0]    	Address[1] | firstName lastName streetAddress city state postalCode streetAddress city state postalCode phoneNumbers[0] phoneNumbers[1] | John Smith 21 2nd Street New York NY 10121 577 Airport Blvd Burlingame CA 94010 212-732-1234 646-123-4567 |

The JSON format is the following:

```
15	{
16	    "firstName": "John",
17	    "lastName": "Smith",
18	    "address": [{
19	        "streetAddress": "21 2nd Street",
20	        "city": "New York",
21	        "state": "NY",
22	        "postalCode": 10021
23	    },{
24	        "streetAddress": "577 Airport Blvd",
25	        "city": "Burlingame",
26	        "state": "CA",
27	        "postalCode": 94010
28	    }],
29	    "phoneNumbers": [
30	        "212-732-1234",
31	        "646-123-4567"
32	    ]
33	}
```

- JSON format properties and data type conversions

Properties and data type conversions of the JSON format are described.
- Handling JSON null and empty arrays and objects

Handling null and empty arrays and objects used in JSON data is described.

## Related reference

- Atom feed format
- Delimited format
- Fixed width format
- SOAP data handler