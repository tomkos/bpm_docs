# Example: Creating
a ServiceMessageObject object

## Context

## Requirements

## Java
imports

```
import javax.xml.namespace.QName; 
import com.ibm.websphere.sibx.smobo.ServiceMessageObject; 
import com.ibm.websphere.sibx.smobo.ServiceMessageObjectFactory;
```

## Code sample

```
. 
. 
. 
QName qName = new QName("http://Examples/Interface", "Operation1RequestMsg"); 
ServiceMessageObjectFactory smoFactory = ServiceMessageObjectFactory.eINSTANCE; 
ServiceMessageObject smo = smoFactory.createServiceMessageObject(qName);
```

## Further information