# Specifying a timeout for a web service

Specify a value of  timeout runtime property that is reasonable for your web
service application. If the timeout value is set to an unrealistically short time, an exception
might result even in a case where the web service invocation is successful. If the timeout value is
set excessively long, performance might suffer because the system will be waiting too long before
generating an exception.

| Property                       |   Default Value | Description                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| timeout                        |              -1 | Timeout in seconds to wait when invoking web service using SOAPConnector.                                                                                                                                                                                                                                                                                                                |
| enable-wsdl-discovery-timeouts |              -1 | Timeout in milliseconds to wait when loading a WSDL file. The value is used for the socket and connection timeout. It only affects the discovery that is performed by Business Automation Workflow during authoring and runtime, and not the discovery that is implicitly done by the underlying application server. Use the value 0 to disable the timeout. Use -1 to keep the default. |

- Traditional:  The -1 value causes
the property to be ignored, and the underlying web service engine's default value of 300 seconds is
used for the request timeout.
- Containers:  The -1 value causes the property to be ignored, and 300 seconds is used for the
request timeout.

```
<server>
  <webservices>
   <timeout merge= "replace" >-1</timeout>
   <enable-wsdl-discovery-timeouts merge= "replace">-1</enable-wsdl-discovery-timeouts>
  </webservices>
</server>
```