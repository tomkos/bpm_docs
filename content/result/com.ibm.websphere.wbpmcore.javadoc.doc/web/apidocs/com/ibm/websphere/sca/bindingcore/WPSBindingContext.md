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

## Interface WPSBindingContext

- All Superinterfaces:
commonj.connector.runtime.BindingContext, java.io.Serializable

public interface WPSBindingContext
extends commonj.connector.runtime.BindingContext
IBM Business Automation Workflow binding context used to specify Process Server specific
 binding context types and values.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String BINDING\_TYPE\_GENERIC\_JMS Value for BINDING\_TYPE, specifying the GENERIC\_JMS. static java.lang.String BINDING\_TYPE\_HTTP Value for BINDING\_TYPE, specifying the HTTP. static java.lang.String BINDING\_TYPE\_JMS Value for BINDING\_TYPE, specifying the JMS. static java.lang.String BINDING\_TYPE\_MQ Value for BINDING\_TYPE, specifying the MQ. static java.lang.String BINDING\_TYPE\_MQ\_JMS Value for BINDING\_TYPE, specifying the MQ\_JMS. static java.lang.String BINDING\_TYPE\_SLSB Value for BINDING\_TYPE, specifying the Stateless Session Bean static java.lang.String COPYRIGHT static java.lang.String EXPECTED\_ELEMENT expected element static java.lang.String FAULT\_NAME Fault name static java.lang.String TRANSFORMED\_DATA The data that is already transformed.

### Field Summary

| Modifier and Type       | Field and Description                                                           |
|-------------------------|---------------------------------------------------------------------------------|
| static java.lang.String | BINDING\_TYPE\_GENERIC\_JMS Value for BINDING\_TYPE, specifying the GENERIC\_JMS.    |
| static java.lang.String | BINDING\_TYPE\_HTTP Value for BINDING\_TYPE, specifying the HTTP.                  |
| static java.lang.String | BINDING\_TYPE\_JMS Value for BINDING\_TYPE, specifying the JMS.                    |
| static java.lang.String | BINDING\_TYPE\_MQ Value for BINDING\_TYPE, specifying the MQ.                      |
| static java.lang.String | BINDING\_TYPE\_MQ\_JMS Value for BINDING\_TYPE, specifying the MQ\_JMS.              |
| static java.lang.String | BINDING\_TYPE\_SLSB Value for BINDING\_TYPE, specifying the Stateless Session Bean |
| static java.lang.String | COPYRIGHT                                                                       |
| static java.lang.String | EXPECTED\_ELEMENT expected element                                               |
| static java.lang.String | FAULT\_NAME Fault name                                                           |
| static java.lang.String | TRANSFORMED\_DATA The data that is already transformed.                          |

- Fields inherited from interface commonj.connector.runtime.BindingContext
BINDING\_COMMUNICATION, BINDING\_COMMUNICATION\_INBOUND, BINDING\_COMMUNICATION\_OUTBOUND, BINDING\_CONFIGURATION, BINDING\_INVOCATION, BINDING\_INVOCATION\_FAULT, BINDING\_INVOCATION\_REQUEST, BINDING\_INVOCATION\_RESPONSE, BINDING\_NAME, BINDING\_REGISTRY, BINDING\_TYPE, BINDING\_TYPE\_EIS, EXPECTED\_TYPE, INTERACTION\_SPEC

- Method Summary

### Method Summary

    - Methods inherited from interface commonj.connector.runtime.BindingContext
setBindingContext