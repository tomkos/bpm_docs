# Add Case

1. Click Add Case.
2. Select the case type from the dialog box.
3. Click OK.

## Configuration properties

| Property                 | Description                                                                                                    | Data type   |
|--------------------------|----------------------------------------------------------------------------------------------------------------|-------------|
| solutionPrefix           | The prefix of the case solution.                                                                               | String      |
| tosName                  | The target object store name that is passed as input to the Add Case.                                          | String      |
| isCaseClient             | The option set to indicate whether the view is used in the context of Case Client or Workplace.                | Boolean     |
| optionalInput            | Any optional input string that can be used for customizing the user interface.                                 | String      |
| colorStyle               | To change the button color style.                                                                              |             |
| shapeStyle               | To change the button shape style.                                                                              |             |
| sizeStyle                | To change the button size style.                                                                               |             |
| outline                  | To use an outline only appearance for the button.                                                              | Boolean     |
| icon                     | To change the button appearance to an icon.                                                                    | String      |
| width                    | To change the width of the button.                                                                             | String      |
| iconLocation             | The location of the inout icon.                                                                                |             |
| ghostMode                | To change the button appearance with no solid fill (the body of the button adopts the look of the background). | Boolean     |
| hideAddCaseButton        | Allows to hide the default Add case button from the Case Details page.                                         | Boolean     |
| eventOn\_Filter\_CaseTypes | To apply custom filters to Case types.                                                                         | Event       |

## Events

You can assign the following types of event handlers to events:

Filter Case Types- Apply custom filters to case types.

caseTypesList is an array of objects of all caseTypes for
specified solution that can be customized. Each caseType array is an object of:
caseTypeID (ID of the caseType), and state (state of the
caseType).

It returns the caseTypesList with customizable objects for case types, each
defined by caseTypeID and state (YES, NO).

- YES - Include in the case types list. This is the default state.
- NO - Do not include in the case types list.

```
customizedCaseTypeList.forEach(function(caseType){
	if (caseType.caseTypeID =="SolnID\_CaseType1"){
		caseType.state= "NO";
	}
	else if (caseType.caseTypeID =="SolnID\_CaseType2"){
		caseType.state= "NO";
	}
});
return customizedCaseTypeList;
```