# Calling services from views

## Before you begin

## About this task

To call a service in a view, you must specify configuration options of type Service in the view
variable declarations and select an Ajax service or service flow as a default service to be used. The default
service is the API for which custom services must match. The names and types of both inputs
and outputs must match.

You can implement the service using either a simple JavaScript call syntax or a REST API.

## Procedure

1 Open a view and then specify a Service type configuration option in the variabledeclarations.
    1. In the Variables page, click the plus sign next to
Configuration Options.
    2. Under Data, select the Service type option,
select the default service, and then provide a name to represent this configuration option
service.

Note: The default service can optionally be overridden with a compatible service by users of this
view.
2 Implement the Ajax service or service flow . The service can be invoked by a simple JavaScript call syntax or by a REST API.In theBehavior page, under Event Handlers , select a method(load , unload , view ,change , or collaboration ) and then provide code forcalling the Ajax service or service flow . Use the following guidelines for your event handler code.

- Restriction: If the Ajax service or service flow uses an error end event with error code and error data, thecontent of the modeled error in the service is not available in either the JavaScript error property or in the REST API error property. The errormessage returned contains the error code but no error data.
    - Invoking the service using a JavaScript call syntax:
        - Use:
this.context.options.<service\_option\_name>(args)
Table 1. Optional properties for args
JavaScript object

Property
Description

params 
(String or Object) A JSON string that represents the input to the service. If
an object is provided, it will be serialized into JSON format using
JSON.stringify(). As such, the object must be JSON serializable.

load 
(function) A callback function when the service call returns successfully. The
callback function has a single parameter containing the output(s) of the service call.

error
(function) A callback function when the service call results in error. The
callback function has a single parameter containing the error information.

Note: The service is invoked only using JSON input and output.
- Invoking the service using a REST API:
    - Use:
this.context.options.<service\_option\_name>.url
(This contains the URL of the Ajax service or service flow.)
    - Serialize your input data in JSON format and add it to the URL using params as
the parameter name.
    - Invoke the URL using an XHR call and specify the following properties
appropriately: handleAs, headers, sync,
load, error properties.
3. Click Save or Finish Editing.

## Example

```
var \_this = this;
var input = {text: this.context.options.service\_option\_name.get("value")};
var serviceArgs = {
  params: JSON.stringify(input),
  load: function(data) {
console.log("service returned: ", data);  
    // now dynamically create the img tag
    require(["dojo/\_base/url"], function(url) {
       var relPath = new url(data.path).path;
       domConstruct.create("img", {src:relPath, style:"margin:5px 0px"}, \_this.context.element, "first");     
    });
  },
  error: function(e) {console.log("service call failed: ", e);}
} 
this.context.options.service\_name(serviceArgs);
```

```
{"status":"200","data":{"serviceStatus":"end","key":"@54","step":"End","data":
{"bookPlacedPosition":{"Floor":1,"Room":"101","Row":2,"@metadata":
{"dirty":true,"shared":false,"rootVersionContextID":"2064.c30905ba-8d17-41f4-
b2a8-08cbb6516ff0T","className":"PlacedPosition"}}},"actions":null}}
```

```
this.context.binding.get("value").set("BookPlacedPosition",data.bookPlacedPosition);
```

```
delete data.bookPlacedPosition['@metadata'];
\_this.context.binding.get("value").set("BookPlacedPosition",data.bookPlacedPosition);
```