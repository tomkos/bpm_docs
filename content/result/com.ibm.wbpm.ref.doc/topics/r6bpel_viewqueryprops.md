<!-- image -->

# QUERY\_PROPERTY view

| Column name     | Type      | Comments                                                                                                                                                                  |
|-----------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PIID            | ID        | The process instance ID.                                                                                                                                                  |
| VARIABLE\_NAME   | String    | The name of the process-level variable.                                                                                                                                   |
| NAME            | String    | The name of the query property.                                                                                                                                           |
| NAMESPACE       | String    | The namespace of the query property.                                                                                                                                      |
| GENERIC\_VALUE   | String    | A string representation for property types that do not map to one of the defined types: STRING\_VALUE, NUMBER\_VALUE, DECIMAL\_VALUE, or TIMESTAMP\_VALUE.                    |
| STRING\_VALUE    | String    | If a property type is mapped to a string type, this is the value of the string.                                                                                           |
| NUMBER\_VALUE    | Integer   | If a property type is mapped to an integer type, this is the value of the integer.If the property type is Boolean, the value is mapped to 0 (for false), or 1 (for true). |
| DECIMAL\_VALUE   | Decimal   | If a property type is mapped to a floating point type, this is the value of the decimal.                                                                                  |
| TIMESTAMP\_VALUE | Timestamp | If a property type is date, time, or timestamp, the value is mapped to a timestamp type, and this column contains the value of the timestamp.                             |