<!-- image -->

# Binding events

WBIEventMonitor.CEI.SCABinding.*=all:
WBIEventMonitor.LOG.SCABinding.*=all

## JMS binding

| Event Name                 | Event Nature   | Event Contents       | Type                                                   |
|----------------------------|----------------|----------------------|--------------------------------------------------------|
| WBI.SCA.JMSBINDING.ENTRY   | ENTRY          | MODULE\_NAME          | string                                                 |
| WBI.SCA.JMSBINDING.ENTRY   | ENTRY          | BINDING\_NAME         | string                                                 |
| WBI.SCA.JMSBINDING.ENTRY   | ENTRY          | OPERATION\_NAME       | string                                                 |
| WBI.SCA.JMSBINDING.ENTRY   | ENTRY          | BINDING\_TYPE         | string restriction: import and export                  |
| WBI.SCA.JMSBINDING.ENTRY   | ENTRY          | BINDING\_PROTOCOL     | string restriction: JMS                                |
| WBI.SCA.JMSBINDING.ENTRY   | ENTRY          | DESTINATION          | string                                                 |
| WBI.SCA.JMSBINDING.ENTRY   | ENTRY          | REPLY\_DESTINATION    | string                                                 |
| WBI.SCA.JMSBINDING.ENTRY   | ENTRY          | CALLBACK\_DESTINATION | string                                                 |
| WBI.SCA.JMSBINDING.ENTRY   | ENTRY          | DIRECTION            | string restriction: REQUEST, RESPONSE                  |
| WBI.SCA.JMSBINDING.ENTRY   | ENTRY          | JMS\_TYPE             | string restriction: SIBus, GenericJMS, MQJMS, MQNative |
| WBI.SCA.JMSBINDING.ENTRY   | ENTRY          | DATABINDING\_NAME     | string                                                 |
| WBI.SCA.JMSBINDING.ENTRY   | ENTRY          | MESSAGE\_ID           | string                                                 |
| WBI.SCA.JMSBINDING.ENTRY   | ENTRY          | CORRELATION\_ID       | string                                                 |
| WBI.SCA.JMSBINDING.EXIT    | EXIT           | MODULE\_NAME          | string                                                 |
| WBI.SCA.JMSBINDING.EXIT    | EXIT           | BINDING\_NAME         | string                                                 |
| WBI.SCA.JMSBINDING.EXIT    | EXIT           | OPERATION\_NAME       | string                                                 |
| WBI.SCA.JMSBINDING.EXIT    | EXIT           | BINDING\_TYPE         | string restriction: import and export                  |
| WBI.SCA.JMSBINDING.EXIT    | EXIT           | BINDING\_PROTOCOL     | string restriction: JMS                                |
| WBI.SCA.JMSBINDING.EXIT    | EXIT           | DESTINATION          | string                                                 |
| WBI.SCA.JMSBINDING.EXIT    | EXIT           | REPLY\_DESTINATION    | string                                                 |
| WBI.SCA.JMSBINDING.EXIT    | EXIT           | CALLBACK\_DESTINATION | string                                                 |
| WBI.SCA.JMSBINDING.EXIT    | EXIT           | DIRECTION            | string restriction: REQUEST, RESPONSE                  |
| WBI.SCA.JMSBINDING.EXIT    | EXIT           | JMS\_TYPE             | string restriction: SIBus, GenericJMS, MQJMS, MQNative |
| WBI.SCA.JMSBINDING.EXIT    | EXIT           | DATABINDING\_NAME     | string                                                 |
| WBI.SCA.JMSBINDING.EXIT    | EXIT           | MESSAGE\_ID           | string                                                 |
| WBI.SCA.JMSBINDING.EXIT    | EXIT           | CORRELATION\_ID       | string                                                 |
| WBI.SCA.JMSBINDING.FAILURE | FAILURE        | MODULE\_NAME          | string                                                 |
| WBI.SCA.JMSBINDING.FAILURE | FAILURE        | BINDING\_NAME         | string                                                 |
| WBI.SCA.JMSBINDING.FAILURE | FAILURE        | OPERATION\_NAME       | string                                                 |
| WBI.SCA.JMSBINDING.FAILURE | FAILURE        | BINDING\_TYPE         | string restriction: import and export                  |
| WBI.SCA.JMSBINDING.FAILURE | FAILURE        | BINDING\_PROTOCOL     | string restriction: JMS                                |
| WBI.SCA.JMSBINDING.FAILURE | FAILURE        | DESTINATION          | string                                                 |
| WBI.SCA.JMSBINDING.FAILURE | FAILURE        | REPLY\_DESTINATION    | string                                                 |
| WBI.SCA.JMSBINDING.FAILURE | FAILURE        | CALLBACK\_DESTINATION | string                                                 |
| WBI.SCA.JMSBINDING.FAILURE | FAILURE        | DIRECTION            | string restriction: REQUEST, RESPONSE                  |
| WBI.SCA.JMSBINDING.FAILURE | FAILURE        | JMS\_TYPE             | string restriction: SIBus, GenericJMS, MQJMS, MQNative |
| WBI.SCA.JMSBINDING.FAILURE | FAILURE        | DATABINDING\_NAME     | string                                                 |
| WBI.SCA.JMSBINDING.FAILURE | FAILURE        | MESSAGE\_ID           | string                                                 |
| WBI.SCA.JMSBINDING.FAILURE | FAILURE        | CORRELATION\_ID       | string                                                 |
| WBI.SCA.JMSBINDING.FAILURE | FAILURE        | Exception            | string                                                 |

For an example of JMS binding event code, see the related links at the end of this topic.

## JAX-WS binding

| Event Name                   | Event Nature   | Event Contents   | Type                                  |
|------------------------------|----------------|------------------|---------------------------------------|
| WBI.SCA.JAXWSBINDING.ENTRY   | ENTRY          | MODULE\_NAME      | string                                |
| WBI.SCA.JAXWSBINDING.ENTRY   | ENTRY          | BINDING\_NAME     | string                                |
| WBI.SCA.JAXWSBINDING.ENTRY   | ENTRY          | OPERATION\_NAME   | string                                |
| WBI.SCA.JAXWSBINDING.ENTRY   | ENTRY          | BINDING\_TYPE     | string restriction: import and export |
| WBI.SCA.JAXWSBINDING.ENTRY   | ENTRY          | BINDING\_PROTOCOL | string restriction: JAX-WS            |
| WBI.SCA.JAXWSBINDING.ENTRY   | ENTRY          | SERVICE\_QNAME    | string                                |
| WBI.SCA.JAXWSBINDING.ENTRY   | ENTRY          | PORT\_QNAME       | string                                |
| WBI.SCA.JAXWSBINDING.ENTRY   | ENTRY          | ENDPOINT         | string                                |
| WBI.SCA.JAXWSBINDING.EXIT    | EXIT           | MODULE\_NAME      | string                                |
| WBI.SCA.JAXWSBINDING.EXIT    | EXIT           | BINDING\_NAME     | string                                |
| WBI.SCA.JAXWSBINDING.EXIT    | EXIT           | OPERATION\_NAME   | string                                |
| WBI.SCA.JAXWSBINDING.EXIT    | EXIT           | BINDING\_TYPE     | string restriction: import and export |
| WBI.SCA.JAXWSBINDING.EXIT    | EXIT           | BINDING\_PROTOCOL | string restriction: JAX-WS            |
| WBI.SCA.JAXWSBINDING.EXIT    | EXIT           | SERVICE\_QNAME    | string                                |
| WBI.SCA.JAXWSBINDING.EXIT    | EXIT           | PORT\_QNAME       | string                                |
| WBI.SCA.JAXWSBINDING.EXIT    | EXIT           | ENDPOINT         | string                                |
| WBI.SCA.JAXWSBINDING.FAILURE | FAILURE        | MODULE\_NAME      | string                                |
| WBI.SCA.JAXWSBINDING.FAILURE | FAILURE        | BINDING\_NAME     | string                                |
| WBI.SCA.JAXWSBINDING.FAILURE | FAILURE        | OPERATION\_NAME   | string                                |
| WBI.SCA.JAXWSBINDING.FAILURE | FAILURE        | BINDING\_TYPE     | string restriction: import and export |
| WBI.SCA.JAXWSBINDING.FAILURE | FAILURE        | BINDING\_PROTOCOL | string restriction: JAX-WS            |
| WBI.SCA.JAXWSBINDING.FAILURE | FAILURE        | SERVICE\_QNAME    | string                                |
| WBI.SCA.JAXWSBINDING.FAILURE | FAILURE        | PORT\_QNAME       | string                                |
| WBI.SCA.JAXWSBINDING.FAILURE | FAILURE        | ENDPOINT         | string                                |
| WBI.SCA.JAXWSBINDING.FAILURE | FAILURE        | Exception        | string                                |

## HTTP binding

| Event Name                  | Event Nature   | Event Contents   | Type                                  |
|-----------------------------|----------------|------------------|---------------------------------------|
| WBI.SCA.HTTPBINDING.ENTRY   | ENTRY          | MODULE\_NAME      | string                                |
| WBI.SCA.HTTPBINDING.ENTRY   | ENTRY          | BINDING\_NAME     | string                                |
| WBI.SCA.HTTPBINDING.ENTRY   | ENTRY          | OPERATION\_NAME   | string                                |
| WBI.SCA.HTTPBINDING.ENTRY   | ENTRY          | BINDING\_TYPE     | string restriction: import and export |
| WBI.SCA.HTTPBINDING.ENTRY   | ENTRY          | BINDING\_PROTOCOL | string restriction: HTTP              |
| WBI.SCA.HTTPBINDING.ENTRY   | ENTRY          | ENDPOINT         | string                                |
| WBI.SCA.HTTPBINDING.ENTRY   | ENTRY          | HTTPMETHOD       | string                                |
| WBI.SCA.HTTPBINDING.EXIT    | EXIT           | MODULE\_NAME      | string                                |
| WBI.SCA.HTTPBINDING.EXIT    | EXIT           | BINDING\_NAME     | string                                |
| WBI.SCA.HTTPBINDING.EXIT    | EXIT           | OPERATION\_NAME   | string                                |
| WBI.SCA.HTTPBINDING.EXIT    | EXIT           | BINDING\_TYPE     | string restriction: import and export |
| WBI.SCA.HTTPBINDING.EXIT    | EXIT           | BINDING\_PROTOCOL | string restriction: HTTP              |
| WBI.SCA.HTTPBINDING.EXIT    | EXIT           | ENDPOINT         | string                                |
| WBI.SCA.HTTPBINDING.EXIT    | EXIT           | HTTPMETHOD       | string                                |
| WBI.SCA.HTTPBINDING.FAILURE | FAILURE        | MODULE\_NAME      | string                                |
| WBI.SCA.HTTPBINDING.FAILURE | FAILURE        | BINDING\_NAME     | string                                |
| WBI.SCA.HTTPBINDING.FAILURE | FAILURE        | OPERATION\_NAME   | string                                |
| WBI.SCA.HTTPBINDING.FAILURE | FAILURE        | BINDING\_TYPE     | string restriction: import and export |
| WBI.SCA.HTTPBINDING.FAILURE | FAILURE        | BINDING\_PROTOCOL | string restriction: HTTP              |
| WBI.SCA.HTTPBINDING.FAILURE | FAILURE        | ENDPOINT         | string                                |
| WBI.SCA.HTTPBINDING.FAILURE | FAILURE        | HTTPMETHOD       | string                                |
| WBI.SCA.HTTPBINDING.FAILURE | FAILURE        | Exception        | string                                |

## EJB binding

| Event Name                 | Event Nature   | Event Contents   | Type                                  |
|----------------------------|----------------|------------------|---------------------------------------|
| WBI.SCA.EJBBINDING.ENTRY   | ENTRY          | MODULE\_NAME      | string                                |
| WBI.SCA.EJBBINDING.ENTRY   | ENTRY          | BINDING\_NAME     | string                                |
| WBI.SCA.EJBBINDING.ENTRY   | ENTRY          | OPERATION\_NAME   | string                                |
| WBI.SCA.EJBBINDING.ENTRY   | ENTRY          | BINDING\_TYPE     | string restriction: import and export |
| WBI.SCA.EJBBINDING.ENTRY   | ENTRY          | BINDING\_PROTOCOL | string restriction: EJB               |
| WBI.SCA.EJBBINDING.ENTRY   | ENTRY          | JNDI\_NAME        | string                                |
| WBI.SCA.EJBBINDING.ENTRY   | ENTRY          | DATABINDING\_NAME | string                                |
| WBI.SCA.EJBBINDING.EXIT    | EXIT           | MODULE\_NAME      | string                                |
| WBI.SCA.EJBBINDING.EXIT    | EXIT           | BINDING\_NAME     | string                                |
| WBI.SCA.EJBBINDING.EXIT    | EXIT           | OPERATION\_NAME   | string                                |
| WBI.SCA.EJBBINDING.EXIT    | EXIT           | BINDING\_TYPE     | string restriction: import and export |
| WBI.SCA.EJBBINDING.EXIT    | EXIT           | BINDING\_PROTOCOL | string restriction: EJB               |
| WBI.SCA.EJBBINDING.EXIT    | EXIT           | JNDI\_NAME        | string                                |
| WBI.SCA.EJBBINDING.EXIT    | EXIT           | DATABINDING\_NAME | string                                |
| WBI.SCA.EJBBINDING.FAILURE | FAILURE        | MODULE\_NAME      | string                                |
| WBI.SCA.EJBBINDING.FAILURE | FAILURE        | BINDING\_NAME     | string                                |
| WBI.SCA.EJBBINDING.FAILURE | FAILURE        | OPERATION\_NAME   | string                                |
| WBI.SCA.EJBBINDING.FAILURE | FAILURE        | BINDING\_TYPE     | string restriction: import and export |
| WBI.SCA.EJBBINDING.FAILURE | FAILURE        | BINDING\_PROTOCOL | string restriction: EJB               |
| WBI.SCA.EJBBINDING.FAILURE | FAILURE        | JNDI\_NAME        | string                                |
| WBI.SCA.EJBBINDING.FAILURE | FAILURE        | DATABINDING\_NAME | string                                |
| WBI.SCA.EJBBINDING.FAILURE | FAILURE        | Exception        | string                                |

## EIS binding

| Event Name                 | Event Nature   | Event Contents   | Type                                  |
|----------------------------|----------------|------------------|---------------------------------------|
| WBI.SCA.EISBINDING.ENTRY   | ENTRY          | MODULE\_NAME      | string                                |
| WBI.SCA.EISBINDING.ENTRY   | ENTRY          | BINDING\_NAME     | string                                |
| WBI.SCA.EISBINDING.ENTRY   | ENTRY          | OPERATION\_NAME   | string                                |
| WBI.SCA.EISBINDING.ENTRY   | ENTRY          | BINDING\_TYPE     | string restriction: import and export |
| WBI.SCA.EISBINDING.ENTRY   | ENTRY          | BINDING\_PROTOCOL | string restriction: EIS               |
| WBI.SCA.EISBINDING.ENTRY   | ENTRY          | RESOURCE\_ADAPTER | string                                |
| WBI.SCA.EISBINDING.EXIT    | EXIT           | MODULE\_NAME      | string                                |
| WBI.SCA.EISBINDING.EXIT    | EXIT           | BINDING\_NAME     | string                                |
| WBI.SCA.EISBINDING.EXIT    | EXIT           | OPERATION\_NAME   | string                                |
| WBI.SCA.EISBINDING.EXIT    | EXIT           | BINDING\_TYPE     | string restriction: import and export |
| WBI.SCA.EISBINDING.EXIT    | EXIT           | BINDING\_PROTOCOL | string restriction: EIS               |
| WBI.SCA.EISBINDING.EXIT    | EXIT           | RESOURCE\_ADAPTER | string                                |
| WBI.SCA.EISBINDING.FAILURE | FAILURE        | MODULE\_NAME      | string                                |
| WBI.SCA.EISBINDING.FAILURE | FAILURE        | BINDING\_NAME     | string                                |
| WBI.SCA.EISBINDING.FAILURE | FAILURE        | OPERATION\_NAME   | string                                |
| WBI.SCA.EISBINDING.FAILURE | FAILURE        | BINDING\_TYPE     | string restriction: import and export |
| WBI.SCA.EISBINDING.FAILURE | FAILURE        | BINDING\_PROTOCOL | string restriction: EIS               |
| WBI.SCA.EISBINDING.FAILURE | FAILURE        | JNDI\_NAME        | string                                |
| WBI.SCA.EISBINDING.FAILURE | FAILURE        | RESOURCE\_ADAPTER | string                                |
| WBI.SCA.EISBINDING.FAILURE | FAILURE        | Exception        | string                                |

- Generic JMS binding event code example

Here is a sample of the code for a generic JMS binding event.