# A search returns too many results

## Symptoms

## Causes

```
"Case State >= Working" OR Prop1 = "a" OR Prop2 = "b"
```

This
statement returns all cases that are in the working, failed, or complete
state.

## Resolving the problem

To resolve the problem, the solution designer can
create a custom search widget that handles     queries that contain
both AND operators and OR operators.