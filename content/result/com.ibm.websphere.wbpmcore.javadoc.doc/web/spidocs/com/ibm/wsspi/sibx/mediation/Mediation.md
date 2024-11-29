- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Interface Mediation

- All Known Subinterfaces: ESBMediation All Known Implementing Classes: AbstractMediation , ESBMediationPrimitive public interface Mediation Defines the contract between mediation primitives and the mediation flow engine. Any mediation implementation must conform the the JavaBean specification by implementing a default constructor, and getters/setters for all properties. Indexed properties must be implemented using arrays, with the appropriate getters and setters. A mediation primitive has the following lifecycle: Note that mediation primitives are stateless objects, and the same instance is not guaranteed to be called on subsequent invocations of a flow. Also note that there is no explicit termination of the mediation, and as such, primitives should not maintain long-running resources such as database connections. In the mediate method, the mediation primitive may perform inspection and modification of the message. It may fire output terminals in any order, and at any time. The same output terminal may be fired multiple times. It may also throw a MediationConfigurationException or a MediationBusinessException to represent an error in the mediation processing. The mediation flow engine will invoke any failure terminal automatically on the throwing of an exception.

```
public interface Mediation
```

Any mediation implementation must conform the the JavaBean specification 
 by implementing a default constructor, and getters/setters for all 
 properties. Indexed properties must be implemented using arrays, with the 
 appropriate getters and setters.

A mediation primitive has the following lifecycle:

    1. The mediation engine will call the default constructor.
    2. The mediation engine will set all properties on the mediation primitive.
    3. The mediation engine will create the 
 MediationServices
 (including creating the input and output terminals) and set it using the 
 setMediationServices
 method.
    4. The mediation engine will call the 
 init 
 method upon when the mediation 
 primitive can perform any necessary initialization. The engine will only
 call init() once.
    5. At this point, the mediation is deemed to be ready, and the runtime will
 begin to invoke flows resulting in the 
 mediate
 method being called.

Note that mediation primitives are stateless objects, and the same 
 instance is not guaranteed to be called on subsequent invocations of a flow. 
 Also note that there is no explicit termination of the mediation, and as 
 such, primitives should not maintain long-running resources such as database 
 connections.

In the mediate method, the mediation primitive may perform 
 inspection and modification of the message. It may fire output terminals in 
 any order, and at any time. The same output terminal may be fired multiple 
 times. It may also throw a 
 MediationConfigurationException
 or a 
 MediationBusinessException
 to represent an error in the mediation processing. The mediation flow engine
 will invoke any failure terminal automatically on the throwing of an
 exception.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

void
init()
Initialises the mediation.

void
mediate(InputTerminal inputTerminal,
       commonj.sdo.DataObject message)
Invoked when a message arrives at the specified input terminal of this 
 mediation primitive.

void
setMediationServices(MediationServices mediationServices)
Sets the mediation services.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- $sccsid
static final java.lang.String $sccsid
See Also:Constant Field Values

- Method Detail

### Method Detail

    - setMediationServices
void setMediationServices(MediationServices mediationServices)
Sets the mediation services. Called by the engine during the setup of 
 the mediation primitive.
Parameters:mediationServices - the mediation services object
    - init
void init()
          throws MediationConfigurationException
Initialises the mediation. A lifecycle method which the engine 
 will call when setting up this mediation primitive. It will be guaranteed 
 to be called after the properties and mediation services have been set. 
 It will only be called once.
Throws:
MediationConfigurationException - if any configuration problems 
         occur in the initialization of this mediation primitive.
    - mediate
void mediate(InputTerminal inputTerminal,
           commonj.sdo.DataObject message)
             throws MediationConfigurationException,
                    MediationBusinessException
Invoked when a message arrives at the specified input terminal of this 
 mediation primitive. The mediation primitive may perform inspection and
 modification of the message. It may fire output terminals, and throw 
 an exception to indicate failure of the mediation.
Parameters:inputTerminal - the input terminal being invokedmessage - the message to mediate
Throws:
MediationConfigurationException - if there is a problem with the 
         configuration of the mediation primitive
MediationBusinessException - if there is a problem with the 
         business logic processing of the mediation primitive