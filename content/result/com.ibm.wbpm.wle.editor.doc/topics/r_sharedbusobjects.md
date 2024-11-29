# Shared business objects

## General considerations

```
// Create shared object
tw.local.sharedObject = new tw.object.SharedObject();
tw.local.sharedObject.property = "value";
```

```
// Retrieve key for shared object
tw.local.sharedObjectKey = tw.local.sharedObject.metadata("key");
log.info("sharedObjectkey: " + tw.local.sharedObjectKey);
```

```
// Retrieve shared object by key
var sharedObject2 = new tw.object.SharedObject(tw.local.sharedObjectKey);
log.info("sharedObject2.property: " + sharedObject2.property);
```

Data
in a shared business object is passed by reference between process
components; the object's values are accessible to other instances
at run time.

You can send data from one process to another
process either by using a message event or by loading the data into
the second process with the unique key of the shared business object.

## Data synchronization

Shared business objects
allow concurrent modification. For example, two users can view and
modify the same shared business object instance in a human service.
When users trigger a boundary event, the data of the shared business
object instance is saved. Only the fields that each user modifies
are saved. Therefore, if two users modify different fields, both changes
are saved. If both users modify the same field, the last user's update
is saved. In addition to having multiple users, you can have a situation
with automated steps, for example, a server script that modifies shared
business objects.

- The shared object is created. Restriction: If a service
is started independently of a process instance without a task, the
data is not synchronized when the shared business object is created.
- The state of a process instance is persisted and automatic synchronization
is enabled for the process. If you use linked processes, at run time,
the setting of the top-level business process definition is taken.
- The state of a task or service instance is persisted and automatic
synchronization is enabled for the service definition. If you use
nested services, the setting of the top-level server definition is
taken.

For processes and service implementations, you can specify whether the shared business objects
in a process instance are automatically updated and saved when the business object is changed in
other instances or tasks. You can control this behavior by using the setting for synchronizing
business objects in the Overview section of a process or service. This setting is always enabled for case types created with the Basic Case Management
feature in previous releases and cannot be turned off; it is never enabled for Ajax services and it
cannot be turned on.

```
// Save the variable data
tw.local.sharedObject.save();

// Load the variable data
tw.local.sharedObject.load();
```

- If changes to business objects in processes and services are automatically
synchronized and saved, do not include a save statement in your script.
- Activity preconditions that are based on shared business objects
require data synchronization so that they can be reevaluated when
changes happen. For processes that contain ad hoc activities, always
enable the synchronization setting. If you do not enable the setting,
you must call the JavaScript load and save methods
in a server script to load the latest content or to save changes.

Running process instances or services use the
synchronization setting of the top-level process or service. Linked
processes also use setting of the top-level process regardless of
what is set for the linked process. Nested services use the synchronization
setting of the top-level service.

## Limitations to property types

- Map
- XMLDocument
- XMLElement
- XMLNodeList

Changes that are made to the value of such a variable type cannot be recognized. For example, it
cannot recognize when you add an entry to a map. As a result, the shared business object instance
isn’t saved even if you invoke the save() function explicitly.

Consider using the Record business
object instead of the Map business object. It has similar capabilities
and is not affected by this limitation.

## Additional considerations for services