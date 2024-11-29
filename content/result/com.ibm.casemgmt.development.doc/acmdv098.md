# Error responses for an external data service

For example, the response code 404 Not Found indicates
that the method did not find a resource, such as the specified solution
or case type. The response code 400 Bad Request indicates
that a required parameter was not provided or that an incorrect value
was specified for a parameter.

```
#Response
HTTP/1.1 404 Not Found
Content-Type: application/json;charset-UTF-8
{
  "userMessage":
  {
    "text":"The specified object type is not a valid object type.",
  }
  "underlyingDetails":
  {
    "causes": 
    [
      "More detailed message 1",
      "More detailed message 2",
    ]
  }
}
```