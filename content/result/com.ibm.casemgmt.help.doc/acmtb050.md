# Solution deployment fails if a value is not found for a required property

## Symptoms

```
11/17/17 4:21:48 AM PST FNRPA0180E The MULTI\_DocType1 document type cannot be 
associated with the MyTest case type (unique identifier: MULTI\_MyTest) because 
the case type has a required property that has no default value.
```

## Causes

- The property is not set as required in the document class.
- The property is multivalued, but the Map document class properties check
box is not selected for the document class.

## Resolving the problem

- Select the Required check box.
- Select the Map document class properties check box.