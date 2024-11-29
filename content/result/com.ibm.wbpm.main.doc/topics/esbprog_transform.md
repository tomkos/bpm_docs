<!-- image -->

# Message Element Setter and Data Handler mediation
primitives

1. Message Element Setter mediation primitive
2. Data Handler mediation primitive

## Message Element Setter mediation primitive

The Message Element Setter mediation primitive provides a simple mechanism for setting message
content. It does not change the type of the message. You can set, copy, append or delete message
elements using statements containing XPath expressions. You can specify multiple statements in one
Message Element Setter mediation primitive by setting multiple targets, with the changes carried out
in the sequence specified.

You can set target message elements to a constant value, or to a value copied from a location in
the input SMO. If the target message element you specify does not exist then it will be created in
the SMO. You can also delete message elements if they are optional or repeating elements.

## Example scenario for Message Element Setter mediation primitive

Figure 1. Message Element Setter in a mediation flow component

<!-- image -->

1. Copying the value of the PersonalHolidaysClient SOAP header to the
appropriate position in the correlation context.
2 Override the PersonalHolidaysClient to bePersonalHolidaysInternalHeader by:
    1. Setting the name of the PersonalHolidaysClient SOAP header to
PersonalHolidaysInternalHeader.
    2. Setting the value of the PersonalHolidaysInternalHeader SOAP header to
EXTERNAL\_CLIENT\_SERVICE\_CALL.

Figure 2. Message Element Setter properties within Integration Designer

<!-- image -->

## Data Handler mediation primitive

Figure 3. Data Handler Configuration

<!-- image -->

## Example scenario for Data Handler mediation primitive

```
<menuCourseDetails>
	<menuCourseID>DessertABC1234</menuCourseID>
	<menuCourseDescription>Sticky Date Pudding served with Caramel Sauce</menuCourseDescription>
	<menuCourseIngredients>Dates,Butter,Sugar,Bicarbonate of Soda,Eggs,Flour,
	  Cream,Vanilla essence</menuCourseIngredients>
</menuCourseDetails>
```

```
<menuCourseDetails>
	<menuCourseID>DessertABC1234</menuCourseID>
	<menuCourseDescription>Sticky Date Pudding served with Caramel Sauce</menuCourseDescription>
	<menuCourseIngredients>Dates,Butter,Sugar,Bicarbonate of Soda,Eggs,Flour,
	  Cream,Vanilla essence</menuCourseIngredients>
	<ingredientsList>
		<ingredients>Dates</ingredients>
		<ingredients>Butter</ingredients>
		<ingredients>Sugar</ingredients>
		<ingredients>Bicarbonate of Soda</ingredients>
		<ingredients>Eggs</ingredients>
		<ingredients>Flour</ingredients>
		<ingredients>Cream</ingredients>
		<ingredients>Vanilla essence</ingredients>
	</ingredientsList>
</menuCourseDetails>
```

Figure 4. Data Handler within a mediation flow component

<!-- image -->

Figure 5. Data Handler in Integration Designer

<!-- image -->