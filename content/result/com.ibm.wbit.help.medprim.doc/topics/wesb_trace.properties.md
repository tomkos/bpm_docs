# Trace mediation primitive properties

## Enabled

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | true              |

## Destination

| Field detail   | Value and notes                                                                                                                                                                                                                                                                                                                                                |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                                                                                                                                                                                                                                                            |
| Valid values   | Local Server Log 0 The Trace primitive outputs INFO level java.util.logging messages to the server system console.  User Trace 1 The trace messages are logged to a UserTrace.log file in the server logs directory, as specified by the LOG\_ROOT WebSphere Variable.  File 2 The trace messages are logged to the file specified by the File property.  Note: |
| Default        | Local Server Log                                                                                                                                                                                                                                                                                                                                               |

## File path

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Message

| Field detail   | Value and notes              |
|----------------|------------------------------|
| Required       | Yes                          |
| Valid values   | StringNote:                  |
| Default        | {0}, {1}, {2}, {3}, {4}, {5} |

## Root path

| Field detail   | Value and notes                       |
|----------------|---------------------------------------|
| Required       | Yes                                   |
| Valid values   | XPathNote:                            |
| Default        | /The default value is the entire SMO. |

## Sample XML code

```
<node name="Trace1" type="Trace">
  <property name="root" value="/body"/>
  <inputTerminal/>
  <outputTerminal/>
  <failTerminal/>
</node>
```