# Example:
Creating a new MQ header

## Context

## Requirements

## Java
imports

```
import com.ibm.websphere.sibx.smobo.MQHeaderType; 
import com.ibm.websphere.sibx.smobo.ServiceMessageObjectFactory;
```

## Code sample

```
. 
. 
. 
ServiceMessageObjectFactory smoFactory = ServiceMessageObjectFactory.eINSTANCE; 
MQHeaderType mqHeader = smoFactory.createMQHeaderType();
```