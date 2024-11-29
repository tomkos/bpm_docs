# Cleaning up shared business objects

## About this task

When a shared business object is saved, it is required
that the original version is still available. In earlier versions
of Business Automation Workflow,
all versions of shared business objects were kept, and so the original
version was always available. Starting with Business Automation Workflow version
8.5.6, the system deletes old versions of business objects that are
no longer required. The system keeps track of which BPD instances
reference which version of a shared business object. The versions
referenced by active BPD instances are never deleted even if they
are eligible for deletion according to the configuration parameters.
But if you have just migrated to V8.5.6, that information is not available
for existing instances, and cleanup is disabled. If you enable cleanup,
when a BPD instance becomes active, the system starts tracking the
shared business objects referenced by the instance.

| Configuration parameter   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cleanupMaxVersionCount    | The cleanupMaxVersionCount parameter specifies the number of shared business object versions that you want to keep. For example, a cleanupMaxVersionCount of 4 indicates that at least 4 versions should be kept. For a newly installed Business Automation Workflow, the default for cleanupMaxVersionCount is 5. For a migrated Business Automation Workflow, the default for cleanupMaxVersionCount is -1. The -1 value means that shared business objects are not cleaned up. To enable the cleanup feature, change cleanupMaxVersionCount to a positive integer.Important: Before you enable cleanup, look in your code for shared business objects that do no have automatic synchronization enabled and make sure that load() is called before a change is made to the business object. For example, a script that has the following code:tw.local.sbo.property = "new value"; tw.local.sbo.save();Add a call to load() before the property is changed: tw.local.sbo.load(); tw.local.sbo.property = "new value"; tw.local.sbo.save();The load() method reloads the latest version from the database into the variable, however it comes with a performance cost. If you have a shared business object variable in a BPD that is not modified (it is not passed to other BPDs, or the BPDs and services to which it is passed do not modifiy it), then your local variable cannot be outdated. In this situation you do not need the load() method. |
| cleanupMinAge             | The cleanupMinAge parameter specifies a time in hours that prevents recent versions from being deleted. For example, a cleanupMinAge of 48 indicates that a version that was created less than 48 hours ago should not be deleted, regardless of the cleanupMaxVersionCount specified.The default for cleanupMinAge is 48 hours for both newly installed and migrated IBM® Business Automation Workflow systems. However, cleanupMinAge is not effective if cleanupMaxVersionCount is not enabled. Use cleanupMinAge to allow users enough time to complete interactions before the data is cleaned up. Set a value that is higher than the time it takes a user to look at a user interface, work on data and click save.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Example

The following example shows how to read and modify the
configuration parameters for cleaning up shared business objects using
wsadmin scripting:

```
// List all BPMSharedBusinessObjects objects. If there is only one deployment environment, then there is only one.
sboConfigurations = AdminUtilities.convertToList(AdminConfig.list("BPMSharedBusinessObjects"))

// Read the first item
sboConfiguration = sboConfigurations[0]

// Show one specific attribute of the Shared Business Object configuration
AdminConfig.showAttribute(sboConfiguration, "cleanupMaxVersionCount")
AdminConfig.showAttribute(sboConfiguration, "cleanupMinAge")

// Update one specific attribute of the Shared Business Object configuration
AdminConfig.modify(sboConfiguration, [["cleanupMaxVersionCount", 4]])
AdminConfig.modify(sboConfiguration, [["cleanupMinAge", 24]])

// Save the configuration
AdminConfig.save()
```