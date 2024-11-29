# HTTP methods supported by the BPD and BPEL REST APIs

| HTTP method   | Description                   |
|---------------|-------------------------------|
| POST          | Creates a new resource.       |
| GET           | Retrieves a resource.         |
| PUT           | Updates an existing resource. |
| DELETE        | Deletes a resource.           |

```
curl --location 'https://localhost:9443/ops/system/login' \
--user 'user:password' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
  "refresh\_groups": true,
  "requested\_lifetime": 7200
}'
```

The GET method is a safe method because the state of the resource remains
unchanged by this operation.

```
// Assuming that "dateFromREST" is a java.util.Date object
DateFormat df = DateFormat.getDateTimeInstance();
TimeZone tz = TimeZone.getDefault();
df.setTimeZone(tz);
String formattedDate = df.format(dateFromREST);
// formattedDate has the date you want to show to the user.
```

## Security considerations

When using HTTP methods, consider the following security aspects:

- Some firewalls do not allow HTTP PUT or DELETE trafficthrough the firewall because of security considerations. To accommodate this restriction, you cansend these requests in one of the following ways:
    - Use the X-Method-Override or X-HTTP-Method-Override HTTP
header fields to tunnel a PUT or DELETE request through a
POST request.
    - If the request is for a BPD-related resource, you can use the x-method-override or the x-http-method-override URI
parameters. For
example:POST /rest/bpm/htm/v1/task?...&x-method-override=PUT
- You can use some of the HTTP methods for the BPD-related resources to evaluate JavaScript
expressions. Because of security considerations, JavaScript support is not enabled by default. To
enable JavaScript support, set the associated property in the 100Custom.xml
file for the process server: <properties>
  <common>
    <enable-javascript-execution>true</enable-javascript-execution>
  </common>
</properties>

## URI length considerations for REST API requests

1. Use the POST method in the HTTP request.
2. Set the X-HTTP-Method-Override HTTP header to the intended method from your
original request. For example, if you intended your original request to be a PUT
request, then set the value of this header to PUT.
3. Set the value of the Content-Type HTTP header to
application/x-www-form-urlencoded.
4. Add all of the request parameters from your original request URI query string to the HTTP
request body.

```
PUT http://host1.company.com:9080/rest/bpm/wle/v1/task/3?action=finish&params={"orderNumber":"5","customerName":{"firstName":"John","lastName":"Doe"}}
Headers:
  Accept application/json
```

```
POST http://host1.company.com:9080/rest/bpm/wle/v1/task/3
Headers
  Accept application/json
  Content-Type: application/x-www-form-urlencoded
  X-Method-Override:  PUT
Request Body:
  action=finish&params={"orderNumber":"5","customerName":{"firstName":"John","lastName":"Doe"}}
```