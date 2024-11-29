# Formats of case property values

Strings must be used to serialize case property values in numerous case operations, such as the
following operations:

- getCasePropertyValues
- getParentActivityPropertyValues
- setCasePropertyValues
- setParentActivityPropertyValues
- createCaseUsingSameCaseType
- createDiscretionaryTaskWithProps
- createCaseUsingSpecifiedCaseType

Descriptions and parameters for these case operations are provided in the topic JavaScript API in processes and service flows.

The case operations include one or more of the following property types:

- Boolean
- DateTime
- Float
- Integer
- String
- Multiple value of simple type
- Multiple value of business object type

These property types are described in the following sections.

## Boolean

A Boolean type has a value of either true or false.
For example:

```
"true"
```

## DateTime

A DateTime type is specified in the following format:

yyyy-MM-dd'T'HH:mm:ss'Z'

- yyyy-MM-dd is the year, month, and date.
- The character T is a delimiter.
- HH:mm:ss is the hour, minute, and second.

For example:

```
"2020-07-30T23:59:45Z"
```

## Float

A float is a decimal number that can be expressed with or without exponential notation. For
example:

```
"0.00123"
"123e-5"
```

## Integer

An integer is a non-decimal number that can be expressed with or without exponential notation.
For example:

```
"12300000"
"123e5"
```

## String

A string is a series of alphanumeric characters enclosed in double quotation marks. For
example:

```
"Hello World 2000"
```

## Multiple values of a simple type

Multiple values of a simple type are specified in the following format (where each value is
enclosed within single quotation marks and separated from other values by a comma, with all values
enclosed in curly brackets):

```
{‘value1’,’value2’…}
```

For example:

```
"{'one','two',’and three'}"
```

## Multiple values of a business object type

Multiple values of a business object type are expressed in a JSON string that includes a business
object name and the values. The JSON string is specified in the following format:

```
{
    "objects": [{
            "properties": [{
                    "name": "PropertyUniqueName1",
                    "value": "valueA"
                }, {
                    "name": "PropertyUniqueName2",
                    "value": "valueB"
                }, {
                    "name": "PropertyUniqueName3",
                    "value": "{'valueC1','valueC2’…}"
                }
                …
            ]
        }, {
            "properties": [{
                    "name": "PropertyUniqueName1",
                    "value": "valueD"
                }
                …
            ]
        }
        …
    ],
    "requiredClass": "BOuniqueName"
}
```

For example:

```
"{\
    \"objects\": [{\
            \"properties\": [{\
                    \"name\": \"SOL\_Property1\",\
                    \"value\": \"Value A\"\
                }, {\
                    \"name\": \"SOL\_Property2\",\
                    \"value\": \"Value B\"\
                }, {\
                    \"name\": \"SOL\_Property3\",\
                    \"value\": \"{'Value C One','Value C Two'}\"\
                }\
            ]\
        }, {\
            \"properties\": [{\
                    \"name\": \"SOL\_Property1\",\
                    \"value\": \"Value D\"\
                }, {\
                    \"name\": \"SOL\_Property2\",\
                    \"value\": \"Value E\"\
                }, {\
                    \"name\": \"SOL\_Property3\",\
                    \"value\": \"{'Value F'}\"\
                }\
            ]\
        }\
    ],\
    \"requiredClass\": \"SOL\_BO\"\
}"
```