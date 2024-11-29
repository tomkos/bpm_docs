<!-- image -->

# Additional Query Examples

In these examples different properties and wildcard values ('\_', '%') are used
with different operators (AND, OR, LIKE,
NOT\_LIKE, EQUAL, and NOT\_EQUAL).

## Example

For the examples, queries will be performed that return between different combinations of 4
business rule groups. It is important to understand the different attributes and properties of the
business rule groups as these are used in the queries.

```
Name: BRG1
Targetnamespace : http://BRG1/com/ibm/br/rulegroup
Properties:
organization, 8JAA
department, claims
ID, 00000567
region: SouthCentralRegion
manager: Joe Bean

Name: BRG2
Targetnamespace : http://BRG2/com/ibm/br/rulegroup
Properties:
organization, 7GAA
department, accounting
ID, 0000047
ID\_cert45, ABC
region: NorthRegion

Name: BRG3
Targetnamespace : http://BRG3/com/ibm/br/rulegroup
Properties:
organization, 7FAB
department, finance
ID, 0000053
ID\_app45, DEF
region: NorthCentralRegion

Name: BRG4
Targetnamespace : http://BRG4/com/ibm/br/rulegroup
Properties:
organization, 7HAA
department, shipping
ID, 0000023
ID\_app45, GHI
region: SouthRegion
```

## Query business rule groups by NOT\_LIKE operator and wildcard ('\_')

This is an example of a query of business rule group by NOT\_LIKE operator and wildcard ('\_').

```
brgList =
BusinessRuleManager.getBRGsBySingleProperty("organization",
QueryOperator.NOT\_LIKE,
		"7\_\_A", 0, 0);

// Returns BRG1 and BRG3
```

```
brgList =
BusinessRuleManager.getBRGsBySingleProperty("organization",
QueryOperator.NOT\_LIKE,
		"7%", 0, 0);

// Returns BRG1
```

## Query business rule groups by a list of nodes and Not node combined with an OR
operator

This is an example of a query business rule groups by a list of nodes and Not node combined with
an OR operator.

```
// OR list with Not node
List<QueryNode> list = new ArrayList<QueryNode>();

QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("region",
		QueryOperator.LIKE,
		"%thRegion");

list.add(rightNode);

QueryNode rightNode2 =
QueryNodeFactory.createPropertyQueryNode("organization",
		QueryOperator.LIKE,
		"8%");

NotNode notNode =
QueryNodeFactory.createNotNode(rightNode2);

list.add(notNode);

QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode("department",
		QueryOperator.LIKE,
		"%ing");

list.add(leftNode);

QueryNode leftNode2 =
QueryNodeFactory.createPropertyQueryNode("organization",
		QueryOperator.LIKE,
		"8%");

list.add(leftNode2);

OrNode orNode = QueryNodeFactory.createOrNode(list);

brgList = BusinessRuleManager.getBRGsByProperties(orNode,
0, 0);

//Returns BRG1, BRG2, BRG3, and BRG4
```

## Query business rule groups by multiple properties with a single NOT node

This is an example of a query of business rule groups by multiple properties with a single NOT
node.

```
// Prop AND NOT Prop
QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("department",
		QueryOperator.EQUAL, "accounting");

NotNode notNode =
QueryNodeFactory.createNotNode(rightNode);

QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode("ID",
		QueryOperator.LIKE, "00000%");

AndNode andNode = QueryNodeFactory.createAndNode(leftNode,
		notNode);

brgList = BusinessRuleManager.getBRGsByProperties(andNode,
0, 0);

// Returns BRG2
```

## Query business rule groups by multiple properties with multiple NOT nodes combined with OR
operator

This is an example of a query business rule groups by multiple properties with multiple NOT nodes
combined with OR operator.

```
// NOT Prop OR NOT Prop
QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("department",
		QueryOperator.LIKE, "acc%");

NotNode notNode =
QueryNodeFactory.createNotNode(rightNode);

QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode(
		"department", QueryOperator.EQUAL,
		"claims");

NotNode notNode2 =
QueryNodeFactory.createNotNode(leftNode);

OrNode orNode = QueryNodeFactory.createOrNode(notNode,
notNode2);

brgList = BusinessRuleManager.getBRGsByProperties(orNode,
0, 0);

//Returns BRG1, BRG2, BRG3, and BRG4
```

## Query business rule groups by multiple properties combined with multiple AND
operators

This is an example of a query business rule groups by multiple properties combined with multiple
AND operators.

```
// (Prop AND Prop) AND (Prop AND Prop)
QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("department",
		QueryOperator.LIKE, "acc%");

QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode("organization",
		QueryOperator.EQUAL, "7GAA");

AndNode andNodeLeft =
QueryNodeFactory.createAndNode(leftNode,rightNode);

QueryNode rightNode2 =
QueryNodeFactory.createPropertyQueryNode("ID",
QueryOperator.LIKE,"000004\_");

QueryNode leftNode2 =
QueryNodeFactory.createPropertyQueryNode("region",
QueryOperator.EQUAL,
		"NorthRegion");

AndNode andNodeRight =
QueryNodeFactory.createAndNode(leftNode2, rightNode2);

AndNode andNode =
QueryNodeFactory.createAndNode(andNodeLeft,andNodeRight);

brgList = BusinessRuleManager.getBRGsByProperties(andNode,
0, 0);

// Returns BRG2
```

## Query business rule groups by multiple properties with multiple NOT nodes combined with AND
operator

This is an example of a query business rule groups by multiple properties with multiple NOT nodes
combined with AND operator.

```
// NOT Prop AND NOT Prop
QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("department",
QueryOperator.EQUAL, "accounting");

NotNode notNode =
QueryNodeFactory.createNotNode(rightNode);

QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode("department",
		QueryOperator.LIKE, "cla%");

NotNode notNode2 =
QueryNodeFactory.createNotNode(leftNode);

AndNode andNode = QueryNodeFactory.createAndNode(notNode,
notNode2);

brgList = BusinessRuleManager.getBRGsByProperties(andNode,
0, 0);

// Returns BRG1 and BRG2
```

## Query business rule groups by NOT\_EQUAL operator

This is an example of a query of business rule group by the NOT\_EQUAL operator.

```
brgList =
BusinessRuleManager.getBRGsBySingleProperty("department",
QueryOperator.NOT\_EQUAL,
		"claims", 0, 0);
// Returns BRG1
```

## Query business rule groups by multiple properties combined with nested AND operators

This is an example of a query business rule groups by multiple properties combined with nested
AND operators.

```
// (Prop AND (Prop AND Prop)) AND Prop
QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("region",QueryOper
ator.LIKE,
"\_\_\_thRegion");

QueryNode rightNode2 =
QueryNodeFactory.createPropertyQueryNode("organization",
QueryOperator.LIKE,
"7%");

QueryNode leftNode2 =
QueryNodeFactory.createPropertyQueryNode("department",
QueryOperator.LIKE,
"%ing");

AndNode andNodeRight =
QueryNodeFactory.createAndNode(leftNode2,rightNode2);

AndNode andNodeLeft =
QueryNodeFactory.createAndNode(rightNode,andNodeRight);

QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode("ID\_app45",QueryOp
erator.LIKE, "GH\_");

AndNode andNode =
QueryNodeFactory.createAndNode(andNodeLeft, leftNode);

brgList = BusinessRuleManager.getBRGsByProperties(andNode,
0, 0);

// Returns BRG4
```

## Query business rule groups by properties and wildcard ('\_')

This is an example of a query of business rule groups by properties and wildcard (%).

```
brgList = BusinessRuleManager.getBRGsBySingleProperty("ID",
QueryOperator.LIKE, "00000\_3", 0, 0);

// Returns BRG3 and BRG4
```

## Query business rule groups by multiple properties combined with nested OR operators

This is an example of a query business rule groups by multiple properties combined with nested OR
operators.

```
// (Prop OR (Prop OR NOT Prop)) OR Prop
QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("region",
		QueryOperator.LIKE,
		"\_\_\_thRegion");

QueryNode rightNode2 =
QueryNodeFactory.createPropertyQueryNode("organization",
		QueryOperator.LIKE,
		"7%");

NotNode notNode =
QueryNodeFactory.createNotNode(rightNode2);

QueryNode leftNode2 =
QueryNodeFactory.createPropertyQueryNode("department",
		QueryOperator.LIKE,
		"%ing");

OrNode orNodeRight =
QueryNodeFactory.createOrNode(leftNode2,notNode);

OrNode orNodeLeft =
QueryNodeFactory.createOrNode(rightNode,orNodeRight);

QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode("ID\_cert45",
		QueryOperator.LIKE,
		"GH\_");

OrNode orNode = QueryNodeFactory.createOrNode(orNodeLeft,
leftNode);

brgList = BusinessRuleManager.getBRGsByProperties(orNode,
0, 0);

// Returns BRG3
```

## Query business rule groups by multiple properties combined with nested OR operators and a NOT
node

This is an example of a query business rule groups by multiple properties combined with nested OR
operators and a NOT node.

```
// Prop OR NOT(Prop OR Prop)
QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("region",
		QueryOperator.LIKE,
		"\_\_\_thRegion");

QueryNode rightNode2 =
QueryNodeFactory.createPropertyQueryNode(
		"organization",
		QueryOperator.LIKE,
		"7%");

QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode(
		"department",
		QueryOperator.LIKE,
		"%ing");

OrNode orNodeRight =
QueryNodeFactory.createOrNode(rightNode2,
		rightNode);

NotNode notNode =
QueryNodeFactory.createNotNode(orNodeRight);

OrNode orNodeLeft = QueryNodeFactory.createOrNode(leftNode,
notNode);

brgList =
BusinessRuleManager.getBRGsByProperties(orNodeLeft, 0, 0);

// Returns BRG3
```

## Query business rule group by properties with multiple wildcards ('\_' and
'%')

This is an example of a query of business rule group by properties with multiple wildcards (

```
brgList =
BusinessRuleManager.getBRGsBySingleProperty("region",
QueryOperator.LIKE, "\_\_uth%Region",
		0, 0);

// Returns BRG1 and BRG4
```

## Query business rule groups by multiple properties combined with nested AND operators and a
NOT node

This is an example of a query business rule groups by multiple properties combined with nested
AND operators and a NOT node.

```
// Prop AND (Prop AND (Prop AND NOT Prop))
QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("organization",
		QueryOperator.LIKE,
		"7%");

QueryNode rightNode2 =
QueryNodeFactory.createPropertyQueryNode("region",
		QueryOperator.LIKE,
		"%lRegion");

NotNode notNode =
QueryNodeFactory.createNotNode(rightNode2);

QueryNode leftNode2 =
QueryNodeFactory.createPropertyQueryNode("department",
		QueryOperator.LIKE,
		"%ing");

AndNode andNodeRight =
QueryNodeFactory.createAndNode(leftNode2,notNode);

AndNode andNodeLeft =
QueryNodeFactory.createAndNode(rightNode,andNodeRight);

QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode("ID\_cert45",
		QueryOperator.LIKE,
		"AB\_");

AndNode andNode = QueryNodeFactory.createAndNode(leftNode,
andNodeLeft);

brgList = BusinessRuleManager.getBRGsByProperties(andNode,
0, 0);

// Returns BRG2
```

## Query business rule groups by multiple properties combined with NOT and OR operators

This is an example of a query business rule groups by multiple properties combined with NOT and
OR operators.

```
// NOT (Prop AND Prop) OR Prop
QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("organization",
		QueryOperator.LIKE,
		"8\_A\_");

QueryNode rightNode2 =
QueryNodeFactory.createPropertyQueryNode("organization",
		QueryOperator.LIKE,
		"7%");

QueryNode leftNode2 =
QueryNodeFactory.createPropertyQueryNode("region",QueryOper
ator.LIKE,
		"%lRegion");

AndNode andNodeRight =
QueryNodeFactory.createAndNode(leftNode2,rightNode2);

NotNode notNode =
QueryNodeFactory.createNotNode(andNodeRight);

OrNode orNode = QueryNodeFactory.createOrNode(notNode,
rightNode);

brgList = BusinessRuleManager.getBRGsByProperties(orNode,
0, 0);

// Returns BRG3
```

## Query business rule groups by multiple properties combined with nested OR operators and a NOT
node

This is an example of a query business rule groups by multiple properties combined with nested OR
operators and a NOT node.

```
// NOT(Prop OR Prop) OR Prop
QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("region",
		QueryOperator.LIKE,
		"%lRegion");

QueryNode rightNode2 =
QueryNodeFactory.createPropertyQueryNode(
		"organization",
		QueryOperator.LIKE,
		"7%");

QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode(
		"department",
		QueryOperator.LIKE,
		"%ing");

OrNode orNodeRight =
QueryNodeFactory.createOrNode(rightNode2,rightNode);

NotNode notNode =
QueryNodeFactory.createNotNode(orNodeRight);

OrNode orNodeLeft =
QueryNodeFactory.createOrNode(notNode,leftNode);

brgList =
BusinessRuleManager.getBRGsByProperties(orNodeLeft, 0, 0);

// Returns BRG2 and BRG4
```

## Query business rule groups by multiple properties combined with nested AND operators

This is an example of a query business rule groups by multiple properties combined with nested
AND operators.

```
// (Prop AND (Prop AND Prop)) AND Prop - Return empty
QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("region",
		QueryOperator.LIKE,
		"\_\_\_thRegion");

QueryNode rightNode2 =
QueryNodeFactory.createPropertyQueryNode("organization",
		QueryOperator.LIKE,
		"7%");

QueryNode leftNode2 =
QueryNodeFactory.createPropertyQueryNode("department",
		QueryOperator.LIKE,
		"%ing");

AndNode andNodeRight =
QueryNodeFactory.createAndNode(leftNode2,rightNode2);

AndNode andNodeLeft =
QueryNodeFactory.createAndNode(rightNode,andNodeRight);

QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode("ID\_cert45",
		QueryOperator.LIKE,
		"GH\_");

AndNode andNode =
QueryNodeFactory.createAndNode(andNodeLeft, leftNode);

brgList = BusinessRuleManager.getBRGsByProperties(andNode,
0, 0);

//Returns no BRGs
```

## Query business rule groups by multiple properties combined with nested OR operators

This is an example of a query business rule groups by multiple properties combined with nested OR
operators.

```
// (Prop OR (Prop OR Prop)) OR Prop

QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("region",
		QueryOperator.LIKE,
		"\_\_\_thRegion");

QueryNode rightNode2 =
QueryNodeFactory.createPropertyQueryNode("organization",
		QueryOperator.LIKE,
		"7%");

QueryNode leftNode2 =
QueryNodeFactory.createPropertyQueryNode("department",
		QueryOperator.LIKE,
		"%ing");

OrNode orNodeRight =
QueryNodeFactory.createOrNode(leftNode2,rightNode2);

OrNode orNodeLeft =
QueryNodeFactory.createOrNode(rightNode,orNodeRight);

QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode("ID\_cert45",
		QueryOperator.LIKE,
		"GH\_");

OrNode orNode = QueryNodeFactory.createOrNode(orNodeLeft,
leftNode);

brgList = BusinessRuleManager.getBRGsByProperties(orNode,
0, 0);

// Returns BRG1
```

## Query business rule groups by a list of nodes that are combined with an AND operator

This is an example of a query business rule groups by a list of nodes that are combined with an
AND operator.

```
// AND list
List<QueryNode> list = new ArrayList<QueryNode>();

QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("region",
		QueryOperator.LIKE,
		"%thRegion");

list.add(rightNode);

QueryNode rightNode2 =
QueryNodeFactory.createPropertyQueryNode("organization",
		QueryOperator.LIKE,
		"7%");

list.add(rightNode2);

QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode("department",
		QueryOperator.LIKE,
		"%ing");

list.add(leftNode);

QueryNode leftNode2 =
QueryNodeFactory.createPropertyQueryNode("organization",
		QueryOperator.LIKE,
		"7H%");

list.add(leftNode2);

AndNode andNode = QueryNodeFactory.createAndNode(list);

brgList = BusinessRuleManager.getBRGsByProperties(andNode,
0, 0);

// Returns BRG4
```

## Query business rule groups by multiple properties combined with nested AND operators

This is an example of a query business rule groups by multiple properties combined with nested
AND operators.

```
// Prop AND (Prop AND (Prop AND Prop))
QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("region",
		QueryOperator.LIKE,
		"\_\_\_thRegion");

QueryNode rightNode2 =
QueryNodeFactory.createPropertyQueryNode("organization",
		QueryOperator.LIKE,
		"7%");

QueryNode leftNode2 =
QueryNodeFactory.createPropertyQueryNode("department",
		QueryOperator.LIKE,
		"%ing");

AndNode andNodeRight =
QueryNodeFactory.createAndNode(leftNode2,rightNode2);

AndNode andNodeLeft =
QueryNodeFactory.createAndNode(rightNode,andNodeRight);

PropertyIsDefinedQueryNode node2 =
QueryNodeFactory.createPropertyIsDefinedQueryNode("ID\_cert4
5");

AndNode andNode = QueryNodeFactory.createAndNode(node2,
andNodeLeft);

brgList = BusinessRuleManager.getBRGsByProperties(andNode,
0, 0);
// Returns BRG2
```

## Query business rule groups by a list of nodes and NOT node combined with an AND
operator

This is an example of a query business rule groups by a list of nodes and NOT node combined with
an AND operator.

```
// AND list with a notNode
List<QueryNode> list = new ArrayList<QueryNode>();

QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("region",
		QueryOperator.LIKE,
		"%thRegion");

list.add(rightNode);

QueryNode rightNode2 =
QueryNodeFactory.createPropertyQueryNode("organization",
		QueryOperator.LIKE,
		"8%");

NotNode notNode =

QueryNodeFactory.createNotNode(rightNode2);

list.add(notNode);

QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode("department",
		QueryOperator.LIKE,
		"%ing");

list.add(leftNode);

QueryNode leftNode2 =
QueryNodeFactory.createPropertyQueryNode("organization",

list.add(leftNode2);

AndNode andNode = QueryNodeFactory.createAndNode(list);

brgList = BusinessRuleManager.getBRGsByProperties(andNode,
0, 0);

// Return BRG4
```

## Query business rule groups by PropertyIsDefined

This is an example of a query of business rule groups by PropertyIsDefined.

```
PropertyIsDefinedQueryNode node =
QueryNodeFactory.createPropertyIsDefinedQueryNode("manager"
);

brgList = BusinessRuleManager.getBRGsByProperties(node, 0,
0);

// Returns BRG1
```

## Query business rule groups by multiple properties combined with AND and OR operators

This is an example of a query business rule groups by multiple properties combined with AND and
OR operators.

```
// (Prop AND Prop) OR (Prop AND NOT Prop)
QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("department",
		QueryOperator.LIKE, "acc%");

QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode("organization",
		QueryOperator.EQUAL, "7GAA");

AndNode andNodeLeft =
QueryNodeFactory.createAndNode(leftNode, rightNode);

QueryNode rightNode2 =
QueryNodeFactory.createPropertyQueryNode("organization",
		QueryOperator.EQUAL, "8JAA");

NotNode notNode =
QueryNodeFactory.createNotNode(rightNode2);

QueryNode leftNode2 =
QueryNodeFactory.createPropertyQueryNode("region",
		QueryOperator.LIKE, "%lRegion");

AndNode andNodeRight =
QueryNodeFactory.createAndNode(leftNode2, notNode);

OrNode orNode = QueryNodeFactory.createOrNode(andNodeLeft,
andNodeRight);

brgList = BusinessRuleManager.getBRGsByProperties(orNode,
0, 0);

// Returns BRG2 and BRG3
```

## Query business rule groups by multiple properties combined with AND and NOT operators

This is an example of a query business rule groups multiple properties combined with AND and NOT
operators.

```
// Prop AND NOT (Prop AND Prop)
QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode("ID",
QueryOperator.LIKE, "000005%");

QueryNode rightNode2 =
QueryNodeFactory.createPropertyQueryNode("organization",
QueryOperator.EQUAL,
		"8JAA");

QueryNode leftNode2 =
QueryNodeFactory.createPropertyQueryNode("region",QueryOper
ator.LIKE,
		"%lRegion");

AndNode andNodeRight =
QueryNodeFactory.createAndNode(leftNode2, rightNode2);

NotNode notNode =
QueryNodeFactory.createNotNode(andNodeRight);

AndNode andNode = QueryNodeFactory.createAndNode(leftNode,
notNode);

brgList = BusinessRuleManager.getBRGsByProperties(andNode,
0, 0);

// Returns BRG3
```

## Query by a single property

This is an example of a query by a single property.

```
List<BusinessRuleGroup> brgList = null;

brgList = BusinessRuleManager.getBRGsBySingleProperty(
		"department", QueryOperator.EQUAL,
		"accounting", 0, 0);
// Returns BRG2
```

## Query business rule groups by NOT PropertyIsDefined

This is an example of a query of business rule groups by NOT PropertyIsDefined.

```
// NOT Prop
QueryNode node =
QueryNodeFactory.createPropertyIsDefinedQueryNode("manager"
);

NotNode notNode = QueryNodeFactory.createNotNode(node);

brgList = BusinessRuleManager.getBRGsByProperties(notNode,
0, 0);

// Returns BRG1
```

## Query business rule groups by properties and wildcard (%) at the beginning and at the end of
the value

This is an example of a query of business rule groups by properties and wildcard (%) at the
beginning and at the end of the value.

```
// Query Prop AND Prop
QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode(
		"region", QueryOperator.LIKE,
		"%Region");

QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode(
		"ID", QueryOperator.LIKE,
		"000005%");

QueryNode queryNode =
QueryNodeFactory.createAndNode(leftNode,
		rightNode);

brgList =
BusinessRuleManager.getBRGsByProperties(queryNode, 0, 0);
// Returns BRG1 and BRG3
```

## Query business rule groups by a list of nodes that are combined with an OR operator

This is an example of a query business rule groups by a list of nodes that are combined with an
OR operator.

```
// OR list
List<QueryNode> list = new ArrayList<QueryNode>();

QueryNode rightNode =
QueryNodeFactory.createPropertyQueryNode("region",
		QueryOperator.LIKE,
		"%thRegion");

list.add(rightNode);

QueryNode rightNode2 =
QueryNodeFactory.createPropertyQueryNode("organization",
		QueryOperator.LIKE,
		"8%");

list.add(rightNode2);

QueryNode leftNode =
QueryNodeFactory.createPropertyQueryNode("department",
		QueryOperator.LIKE,
		"%ing");

list.add(leftNode);

OrNode orNode = QueryNodeFactory.createOrNode(list);

brgList = BusinessRuleManager.getBRGsByProperties(orNode,
0, 0);

//Returns BRG3
```