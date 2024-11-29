<!-- image -->

# JSON format properties and data type conversions

## Configurable properties

The following properties
can be configured.

| Property name   | Explanation                                                                                                   | Possible values   | Default value   |
|-----------------|---------------------------------------------------------------------------------------------------------------|-------------------|-----------------|
| Encoding        | This is the encoding that will be used in converting bytes to string and string to bytes wherever applicable. | Enum              | All encodings   |

## Data type conversions

JSON type system is
more constrained than the XSD type system. JSON supports a value of
type String, Number and Boolean. It does not support octal and hexdecimal
values. The data handler will delegate all type conversions to the
business object. Hence, all conversions that are supported by the
business object will be supported by the data handler.  We recommend
that the type should match between the JSON data and the corresponding
data objects but we are tolerant with certain formats as shown in
the tables below.

## JSON to DataObject conversions

| JSON/DataObject   | String   | Long                   | Double                   | boolean                         | Date, datetime               |
|-------------------|----------|------------------------|--------------------------|---------------------------------|------------------------------|
| String            | Valid    | Valid if value is long | Valid if value is double | Valid if value is true or false | Valid if the value is a date |
| Long              | Valid    | Valid                  | Valid                    | Invalid                         | Valid if the value is a date |
| Double            | Valid    | Valid if value is long | Valid                    | Invalid                         | Invalid                      |
| Boolean           | Valid    | Invalid                | Invalid                  | Valid                           | Invalid                      |

For simple type lists, the types between the JSON data
and the schema have to match.

For the base64Binary
and hexBinary types, the business object will be converted to byte[],
however this is not a JSON data supported type. JSONDataHandler will
automatically convert the byte[] to a string based on the encoding
information configured on the JSON format properties.

## DataObject to JSON conversions

| DataObject   | JSON    |
|--------------|---------|
| String       | String  |
| Long         | Long    |
| Integer      | Long    |
| Double       | Double  |
| Float        | Double  |
| Boolean      | Boolean |
| Date         | String  |
| Datetime     | String  |