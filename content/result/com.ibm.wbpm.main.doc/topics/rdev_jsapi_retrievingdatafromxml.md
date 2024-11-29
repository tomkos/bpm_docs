# Retrieving data from XML

Generally speaking, walking the XML is more efficient
than using XPath because it does not call the parser.

The XML
example here is the resultSet from an Integration
Component. For the purposes of the example, assume that the following
XML is stored in a variable called myXML.

```
<resultSet recordCount="2" columnCount="2">
  <record>
    <column name="FIRST\_NAME">Daniel</column>
    <column name="ZIP">78703</column>
  </record>
  <record>
    <column name="FIRST\_NAME">Helen</column>
    <column name="ZIP">15228</column>
  </record>
</resultSet>
```