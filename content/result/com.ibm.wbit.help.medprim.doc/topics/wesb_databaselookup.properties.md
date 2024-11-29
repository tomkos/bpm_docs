# Database Lookup mediation primitive properties

## Data source dataSourceJNDIName

The JNDI name of the
datasource.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | StringNote:       |

## Table tableName

The name of the database table, including the
schema name; for example, myschema.mytable.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | StringNote:       |

## Search column keyColumnName

The name of the database's primary key
column. The specified Search column must contain a unique value; multi-column
database keys are not supported. In addition, the unique value must be of the same element type as
the value located in the message using the Search location.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | StringNote:       |

## Search location keyPath

Where, in the input message, to find the database
key. Specified as an XPath 1.0 expression; the value returned from the XPath expression is used as
the key into the database.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | XPathNote:        |

## Validate input validateInput

If you select the check box, the input
message is validated before the mediation is performed.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | false             |

## Data Elements dataElements

| Field detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Value and notes   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Column valueColumnName The name of the database column from which to copy information. The valid type is String. Type messageValueType The information type: the only supported String types are a simple XML schema type, or an XML schema type that extends a simple XML schema type. At run time, the value obtained from the database is converted to the type defined by the Type property. Java primitive types or string are supported only for compatibility with old mediation flows.  Target location messageElement Where, in the message, to store the information obtained from the database. The valid type is String. Specified as an XPath 1.0 expression describing the location of a message element. The XPath expression must evaluate to a single element in the message. |                   |

## Considerations

Consider the following when using the Database Lookup mediation
primitive:

- You must set up a database, datasource and any server authentication
settings for the Database Lookup mediation primitive to use. You can
do this using the runtime administrative console.
- The list of supported databases is provided on the systems requirements
web page for the runtime product.
- The Database Lookup mediation primitive can read only from one
table.
- You can route a message to the same location whether or not the
key is found in the database. To do this you wire both the out terminal
and the keyNotFound terminal to the same output
location.

## Sample XML code

```
<node name="DatabaseLookup1" type="DatabaseLookup">
  <property name="dataSourceJNDIName" value="jdbc/datasource"/>
  <property name="tableName" value="myTable"/>
  <property name="keyColumnName" value="searchColumn"/>
  <property name="keyPath" value="searchLocation"/>
  <table name="dataElements">
    <row>
      <property name="valueColumnName" value="nameColumn"/>
      <property name="messageValueType" value="{http://www.w3.org/2001/XMLSchema}String"/>
      <property name="messageElement" value="body/myRequestMsg/person/name"/>
    </row>
  </table>
  <inputTerminal/>
  <outputTerminal>
    <wire targetNode="SetMessageType"/>
  </outputTerminal>
  <outputTerminal name="keyNotFound"/>
  <failTerminal/>
</node>
```