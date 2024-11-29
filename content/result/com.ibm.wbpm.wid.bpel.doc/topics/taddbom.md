<!-- image -->

# Adding a data map activity

## About this task

## Procedure

1. In the business integration view, create two business objects.
To access the New Business Object wizard, click File > New > Business
Object.
2. Create a new BPEL process.
3. In the BPEL process editor, create two new variables that
point to the two business objects defined in your project. Note: For business object maps, simple types such as strings or integers
are not shown in the wizard since they cannot be mapped. XML maps
can map simple types and so this restriction does not apply to XML
maps and simple types are displayed in the wizard. This is one of
the advantages of using XML maps.
4. Drop a Data map activity on the
canvas.
5. Select either XML map or Business object map and click Next.
6. In the New Data Map wizard, give the
new map a name and click Next.
7. Select one of the variables as the Input and the other
one as the Output, and click Finish.

## Results

## Related concepts

- Creating or importing data maps

## Related tasks

- Creating a data map
- Reusing a business object map