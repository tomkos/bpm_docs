# Updating case property values in a reused process

## About this task

## Procedure

To update case property values:

1. Insert submap steps into the global workflow definition
at points where you want to update the case properties.
2. Create submaps in the global workflow definition.
Any
of the submap steps can call the same submap, or each one can call
a different submap, or both.
3. In any of the task workflows that inherit or extend this global workflow definition,
     override the submaps and add Assignment instructions to update the case or task
     properties.