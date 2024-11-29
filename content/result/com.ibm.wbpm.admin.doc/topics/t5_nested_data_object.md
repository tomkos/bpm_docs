<!-- image -->

# Copying a nested data object to another data object destroys the reference
on the source object

## Reason

The reference to Child is
moved from Father to Mother.

## Resolution

```
BOCopy copyService = (BOCopy)ServiceManager.INSTANCE.locateService
                      ("com/ibm/websphere/bo/BOCopy"); 
DataObject Child = Father.get("Child"); 
DataObject BCopy = copyService.copy(Child); 
Mother.set("Child", BCopy);
```