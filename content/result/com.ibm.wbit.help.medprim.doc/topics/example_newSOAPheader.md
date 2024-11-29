# Example:
Creating a new SOAP header

## Context

## Requirements

## Java
imports

```
import com.ibm.websphere.sibx.smobo.SOAPHeaderType; 
import com.ibm.websphere.sibx.smobo.ServiceMessageObjectFactory;
```

## Code sample

```
. 
. 
. 
ServiceMessageObjectFactory smoFactory = ServiceMessageObjectFactory.eINSTANCE; 
SOAPHeaderType SoapHeader = smoFactory.createSOAPHeaderType();
```