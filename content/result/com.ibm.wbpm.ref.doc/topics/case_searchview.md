# Case Search

The properties that appear in the Case Search view must be defined as described in Designing views, under Case Search. If no properties are defined, the view provides
the default Case State, Case Identifier, and
Date Created properties to be used in the search. The Case Search view provides
the following optional capabilities:

- Preload case instances in the case list view without performing a search by enabling the
Preload cases configuration option.
- Provide a custom search filter capability that enables you to modify the search payload and
manually add filters through an event. To enable this capability, select the Enable
custom search filter configuration option, and define the logic in the On custom
search filter event. A customizable sample code is built in the event.
- Provide an optional parameter to control the number of cases to fetch at a time. If you do not
set this parameter, 200 cases are fetched by default.
- For a search that uses date related
"is", the scope of the search result is equal to the selected locale date time for
the next 24 hours.

## Configuration properties

| Property                           | Description                                                                                                                                                                                                                                                                                                   | Data type   |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Target object store name           | The name of the repository to which the view needs to connect.                                                                                                                                                                                                                                                | String      |
| Solution prefix                    | The prefix of the case solution.                                                                                                                                                                                                                                                                              | String      |
| Case identifier                    | (Optional) The identifier of the case instance. This parameter is optional when used in the context of a solution layout, and required when it is used in the context of related cases.                                                                                                                       | String      |
| Preload cases                      | (Optional) Select this checkbox to load the case list by running a default search.                                                                                                                                                                                                                            | Boolean     |
| Enable custom search filter        | (Optional) Enables the custom search filter. It enables you to add code for a custom search filter to the On custom search filter event at design time.                                                                                                                                                       | Boolean     |
| Number of cases to fetch at a time | (Optional) The number of cases to fetch through a search at one time. If this parameter is not set, the default number of cases is 200.                                                                                                                                                                       | Integer     |
| Control ID of a Case List view     | (Optional) The control ID of the target Case List view to which your Case Search view exclusively sends its search results for rendering. If this parameter is not set and more Case List views are available, all the Case List views receive the search results that are broadcast by the Case Search view. | String      |

## Events

Set
or modify the event handlers for the view in the Events properties. You can set
events to be triggered programmatically or when a user interacts with the view. For information about how to define and code events, see User-defined events.

- On custom search filter : The event handler helps to modify the searchpayload to add additional search filters programmatically rather than using the UI. Select theEnable Custom Search Filter configuration option and define the search logicin this event handler.For example, the following code adds a new search filter by using theproperty TSF\_FirstName whose value is set to Tom . TheTSF\_FirstName property is of type String and cardinalitysingle , as defined in fieldDetails . The search filter is appendedto any existing search filter that is already set in the UI. The event handler returns the modifiedsearchPayload . var custom\_searchPayload = searchPayload;custom\_searchPayload.conditions.push({"field": "TSF\_FirstName","value": "Tom","operator": "EQUAL"});custom\_searchPayload.fieldDetails.push({"field": "TSF\_FirstName","cardinality": "single","dataType": "xs:string"});return custom\_searchPayload; Note that searchPayload.conditions andsearchPayload.fieldDetails must be defined for any custom filter to be added. Thefollowing conditions must be met:

For example, the following code adds a new search filter by using the
property TSF\_FirstName whose value is set to Tom. The
TSF\_FirstName property is of type String and cardinality
single, as defined in fieldDetails. The search filter is appended
to any existing search filter that is already set in the UI. The event handler returns the modified
searchPayload.

```
var custom\_searchPayload = searchPayload;
custom\_searchPayload.conditions.push({"field": "TSF\_FirstName","value": "Tom","operator": "EQUAL"});
custom\_searchPayload.fieldDetails.push({"field": "TSF\_FirstName","cardinality": "single","dataType": "xs:string"});
return custom\_searchPayload;
```

    - In the searchPayload.conditions array, use valid operator values such as
"EQUAL", "NOTEQUAL", "CONTAINS",
"STARTSWITH", "LESS", or "GREATER".
    - In the searchPayload.fieldDetails array, use valid dataType
values such as “xs:string” (for String),
“xs:integer” (for Integer), “xs:double” (for
Float or Decimal), “xs:timestamp” (for
Datetime), and “xs:boolean” (for Boolean).
    - Field parameters in the searchPayload.conditions and
searchPayload.fieldDetails arrays must contain the symbolic name of the case
property that includes the solution prefix.
    - The cardinality parameter in searchPayload.fieldDetails can take the value
“single” or “multi”.
    - Use the value parameter in searchPayload.conditions for the search, which can
take a string, numeric, or datetime value.