# The unload event handler

## Usage

Use the unload function
to clean up resources before the view is removed. The binding handle
is an example of such a resource. The binding handle is returned when bindAll() or bind() is
invoked. You can release the binding in the unload event
handler by calling handle.unbind().

```
this.connectHandles = [];
this.connectHandles.push(dojo.connect(..., "onSelected",...));
this.connectHandles.push(dojo.connect(..., "onDeselected",...));
```

```
Array.forEach(this.connectHandles, function(handle) {
  dojo.disconnect(handle);
});
```

## Parameters

The unload function
does not take any parameters.