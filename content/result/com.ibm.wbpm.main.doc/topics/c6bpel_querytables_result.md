<!-- image -->

# Results of query table queries

## EntityResultSet

| Property       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| queryTableName | Name of the query table on which the query was run.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| entityTypeName | If the query was run on a composite query table, this is the name of the primary query table.  If the query was run on a predefined query table or on a supplemental query table, this is the name of the query table, that is, the same value as the queryTableName property.                                                                                                                                                                                                                                                                                                 |
| EntityInfo     | This property contains the meta information of the entities that are contained in the entity result set. A java.util.List list of com.ibm.bpe.api.AttributeInfo objects if the Business Flow Manager EJB is used, or a list of com.ibm.task.api.AttributeInfo objects if the Human Task Manager EJB is used, can be retrieved on this object. This list contains the attribute names and attribute types of the information contained in the entities of this result set. Meta information about the attributes which constitute the key for these entities is also contained. |
| entities       | A java.util.List list of com.ibm.bpe.api.Entity objects if the Business Flow Manager EJB is used, or a list of com.ibm.task.api.Entity objects if the Human Task Manager is used.                                                                                                                                                                                                                                                                                                                                                                                              |
| locale         | The locale that is calculated for the $LOCALE system parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

Instances of the Entity class contain
the information that is retrieved from the query table query. An entity
represents a uniquely identifiable object such as a task, a process
instance, an activity, or an escalation. The following properties
are available for entities:

| Property                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EntityInfo                             | The EntityInfo object which is also contained in the entity result set. A java.util.List list of com.ibm.bpe.api.AttributeInfo objects if the Business Flow Manager EJB is used, or a list of com.ibm.task.api.AttributeInfo objects if the Human Task Manager EJB is used, can be retrieved on this object. This list contains the attribute names and attribute types of the information contained in the entities of this result set. Meta information about the attributes which constitute the key for these entities is also contained. |
| attributeValue (attributeName)         | The value of the specified attribute that is retrieved for this entity. The type is contained in the related AttributeInfo object of this attribute.                                                                                                                                                                                                                                                                                                                                                                                          |
| attributeValuesOfArray (attributeName) | An array of values. Use this property if the attribute info property array is set to true which is currently the case only if the attribute refers to work item information.                                                                                                                                                                                                                                                                                                                                                                  |

The number
of entities in the entity result set is retrieved using the size method
on the list of entities.

```
…
// the following example shows a query against
// predefined query table TASK, using the entity-based API

…
// run the query
// service is a (Local)BusinessFlowManager object or a
// (Local)HumanTaskManager object
EntityResultSet rs = service.queryEntities("TASK", null, null, null);

// get the entities meta information
EntityInfo ei = rs.getEntityInfo();
List atts = ei.getAttributeInfo();

// get the entities and iterate over it
Iterator entitiesIter = rs.getEntities().iterator();
while (entitiesIter.hasNext()) {

      // work on a particular entity
      Entity en = (Entity) entitiesIter.next();

      for (int i = 0; i < atts.size(); i++) {
            AttributeInfo ai = (AttributeInfo) atts.get(i);
            Serializable value = en.getAttributeValue(ai.getName()) ;
            
            // process…
      }
}
…
```

## RowResultSet

An instance of the com.ibm.bpe.api.RowResultSet class
is returned by the method queryRows if the Business
Flow Manager Enterprise JavaBeans is used. An instance of the com.ibm.task.api.RowResultSet class
is returned by the method queryRows if the Human
Task Manager Enterprise JavaBeans is used. This type of result set
is similar to a JDBC result set. A row result set has the following
properties:

| Property                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| primaryQueryTableName       | If the query was run on a composite query table, this is the name of the primary query table.  If the query was run on a predefined query table or on a supplemental query table, this is the name of the query table, that is, the same value as property queryTableName.                                                                                                                                                                                                      |
| attributeInfo               | This property contains a list of com.ibm.bpe.api.AttributeInfo objects if the Business Flow Manager Enterprise JavaBeans is used or a list of com.ibm.task.api.AttributeInfo objects if the Human Task Manager Enterprise JavaBeans is used. They describe the meta information for this result set. AttributeInfo objects contain the attribute names and attribute types of the information. Meta data about keys is not contained because row result sets do not have a key. |
| attributeValue              | The value of the specified attribute that was retrieved for this row. The type is contained in the related AttributeInfo object of this attribute.                                                                                                                                                                                                                                                                                                                              |
| next, first, last, previous | The row result set is navigated using these methods. Compare its usage to iterators, enumerations, or JDBC result sets.                                                                                                                                                                                                                                                                                                                                                         |

The number of rows in the row result set is retrieved
using the size method on the list of rows.

```
…
// the following example shows a query against
// predefined query table TASK, using the entity-based API
…
// run the query
// service is a (Local)BusinessFlowManager object or a
// (Local)HumanTaskManager object
RowResultSet rs = service.queryRows("TASK", null, null, null);

// get the entities meta information
List atts = rs.getAttributeInfo();

// get the entities and iterate over it
while (rs.next()) {

      // work on a particular row
      for (int i = 0; i < atts.size(); i++) {
            AttributeInfo ai = (AttributeInfo) atts.get(i);
            Serializable value = rs.getAttributeValue(ai.getName()) ;
            
            // process…
      }
}
…
```