# Formulas

Formulas are supported by the following views: Badge, Button, Caption box, Collapsible panel, Decimal, Integer, Link, Note,
Notification, Display text, Panel, Progress bar, QR code, Slider, Status box, Plain text, and Tooltip.

## Syntax for references to views

- ${ControlName} refers to the view whose control id =
ControlName.
- @{ControlName} refers to the value of the view whose
control id = ControlName.
- ${ControlName}.getValue() and
@{ControlName} are equivalent.
- For the Decimal and Integer views, you
can use the standard arithmetic operators ('+", '-', '*', '/', '%') or the equivalent
functions.
- Because formulas are JavaScript expressions, anything valid in a JavaScript expression is valid
in a formula.

```
@{Quantity} * @{Cost}
```

```
@{Quantity=} * @{Cost=}
```

## Aggregate functions

When you process a table, you might need to use aggregate functions. The *
character might follow any ControlName and indicates all the rows in a specified
column.

- COUNT(${ControlName})
- SUM(${ControlName}, expression)
- AVG(${ControlName}, expression)
- MIN(${ControlName}, expression)
- MAX(${ControlName}, expression)

```
FOR\_EACH{expression}
```

- Amount1 with control Id 'tblAmount1' bound to the
amount1 parameter
- Amount2 with control Id 'tblAmount2' bound to the
amount2 parameter
- Total with control Id 'tblTotal' bound to the formula
@{tblAmount1=} * @{tblAmount2=}

```
SUM(${Table1},FOR\_EACH{#{amount1} * #{amount2}})
```