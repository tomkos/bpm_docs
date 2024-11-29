# Example:
Creating a new JMS header

## Context

## Requirements

## Java
imports

```
import com.ibm.websphere.sibx.smobo.JMSHeaderType; 
import com.ibm.websphere.sibx.smobo.ServiceMessageObjectFactory;
```

## Code sample

```
. 
. 
. 
ServiceMessageObjectFactory smoFactory = ServiceMessageObjectFactory.eINSTANCE; 
JMSHeaderType jmsHeader = smoFactory.createJMSHeaderType();
```