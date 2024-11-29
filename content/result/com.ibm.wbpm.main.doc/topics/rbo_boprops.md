<!-- image -->

# BusinessObject.properties file

## Parameters

| Scenario                                                         | Value = "1"                                                    | Value = "2"                                       |
|------------------------------------------------------------------|----------------------------------------------------------------|---------------------------------------------------|
| DataObject.isSet() API                                           | Throws runtime exceptions                                      | Return true or false                              |
| DataObject.get<T>(String) API with invalid XPaths                | Throws runtime exceptions                                      | Return null                                       |
| ChangeSummary.getOldValues() API when there are no changes       | Returns null                                                   | Returns an empty list                             |
| DataObject.get/set<T>(int)                                       | Uses underlying model index                                    | Uses property index                               |
| setDate() on property of type dDay, gMonth, gMonthDay, or gTime, | Value set is java,util.Date.toString()                         | Value set is corresponding part of the Date value |
| BOEquality API                                                   | Does not properly compare gYear, gYearMonth, date, or dateTime | Compares all date values as specified in the XSD. |

<!-- image -->