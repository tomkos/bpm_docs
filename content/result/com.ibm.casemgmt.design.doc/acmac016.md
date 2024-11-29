# generate\_input\_sa command

## Syntax

```
configmgr\_cl generate\_input\_sa -operation operation\_type
 -file input\_file\_name
 [-silent] [-force] [-help]
```

## Parameters

| Option             | Description                                                                                |
|--------------------|--------------------------------------------------------------------------------------------|
| copy               | Creates the input file for copying a solution.                                             |
| createFromTemplate | Creates the input file for creating a solution from a template.                            |
| list               | Creates the input file for listing the properties and document classes in an object store. |
| convertToTemplate  | Converts a solution to a template.                                                         |

Specifies the full path to the input file to create. The directory
structure in the path must already exist. You can use any valid file
name, but the .txt extension is recommended.
For example, use C:\propertylist\propertylist.txt.

## Sample commands

```
configmgr\_cl generate\_input\_sa -operation list
 -file C:\propertylist\propertylist.txt
```

```
configmgr\_cl generate\_input\_sa -operation copy
 -file C:\solutions\copy\_solution\_input.txt
```

```
configmgr\_cl generate\_input\_sa -help
```