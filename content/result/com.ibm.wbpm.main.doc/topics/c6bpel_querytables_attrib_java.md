<!-- image -->

# Attribute type to Java object type mapping

| Attribute type   | Related Java object type   |
|------------------|----------------------------|
| ID               | com.ibm.bpe.api.OID        |
| STRING           | java.lang.String           |
| NUMBER           | java.lang.Long             |
| TIMESTAMP        | java.util.Calendar         |
| DECIMAL          | java.lang.Double           |
| BOOLEAN          | java.lang.Boolean          |

## Example

```
…
// the following example shows a query against a composite query table
// COMP.TA; attribute "STATE" is of attribute type NUMBER
…
// run the query
// the business flow manager Enterprise JavaBeans or the
// human task manager Enterprise JavaBeans can be used to access query tables
EntityResultSet rs = bfm.queryEntities("COMP.TA",null,null,params);

// get the entities and iterate over it
List entities = rs.getEntities();
for (int i = 0 ; i < entities.size(); i++) {

      // work on a particular entity
      Entity en = (Entity) entities.get(i);
      
      // note that the following code could be written
      // more generalized using the attribute info objects
      // contained in ei.getAttributeInfo()

      // get attribute STATE
      Long state = (Long) en.getAttributeValue("STATE");
      …
}
…
```