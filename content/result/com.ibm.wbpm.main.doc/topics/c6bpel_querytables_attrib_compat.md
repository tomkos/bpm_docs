<!-- image -->

# Attribute type compatibility

| Attribute type   | ID   | STRING   | NUMBER   | TIMESTAMP    | DECIMAL   | BOOLEAN   |
|------------------|------|----------|----------|--------------|-----------|-----------|
| ID               | X    |          |          |              |           |           |
| STRING           |      | X        |          |              |           |           |
| NUMBER           |      |          | X        |              | X         |           |
| TIMESTAMP        |      |          |          | X            |           |           |
| DECIMAL          |      |          | X        |              | X         |           |
| BOOLEAN          |      |          |          |              |           | X         |

In query table expressions that specify filter and condition criteria,
types of attributes or values that are compared must be compatible.
For example, WI.OWNER\_ID=1 is an invalid filter because
the left-side operand is of type STRING, and the right-side operand
is of type NUMBER.