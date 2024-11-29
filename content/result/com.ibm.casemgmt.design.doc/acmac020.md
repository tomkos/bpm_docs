# execute\_sa command

## Syntax

```
configmgr\_cl execute\_sa -operation operation\_type
 -file input\_file\_name
 [-silent] [-force] [-help]
```

## Parameters

| Option             | Description                                                                        |
|--------------------|------------------------------------------------------------------------------------|
| copy               | Copies a solution.                                                                 |
| createFromTemplate | Creates a solution from a template.                                                |
| list               | Creates the CSV files with the properties and document classes in an object store. |
| convertToTemplate  | Converts a solution to a template.                                                 |

Specifies the full path to the input file that you created
with the generate\_input\_sa command. The input file
provides Content Platform Engine authentication
information and other information for the selected operation. You
must edit the property values in the input file before you run the execute\_sa command.

For
example, use C:\propertylist\propertylist.txt.

## Sample commands

```
configmgr\_cl execute\_sa -operation list
 -file C:\propertylist\propertylist.txt
```

```
configmgr\_cl execute\_sa -operation copy
 -file C:\solutions\copy\_solution\_input.txt
```

```
configmgr\_cl execute\_sa -operation createFromTemplate 
 -file C:\solutions\from\_template\_input.txt
```

```
configmgr\_cl execute\_sa -operation convertToTemplate 
 -file C:\solutions\to\_template\_input.txt
```

```
configmgr\_cl execute\_sa -help
```