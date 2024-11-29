# Cannot reset the test environment because target object server
does not exist

## Symptoms

```
FNRPA001E Data cannot be retrieved from the connection definition because the
following error occurred: The requested item was not found. Non-repository 
object {91DC01CE-B104-42B6-9CooA-EEE9F62731DB2} not found.
```

## Causes

The
target object store was accidentally removed or it is corrupt.

## Resolving the problem

1. In the Firefox browser, download the Post plugin.
2. In the Post plugin window, enter the information for your target
object server and click Post.