# Creating relationships between process instances

To add and remove relationships or to query the relationships of
a process instance, use either the JavaScript API or the REST API
provided by IBM® Business Automation
Workflow.

- Process instance relationships

Relationships between process instances can be either independent or dependent. Independent relationships allow a user to view the information about the related instances together. Dependent relationships group process instances together so that a dependent process instance cannot complete until all the instances that it depends on are complete. You can create relationships between processes.
- Adding a relationship between process instances by using JavaScript

You can use the JavaScript API that IBM Business Automation Workflow provides to add relationships between process instances. You can create an independent relationship between two process instances, make the current process instance depend on another process instance, or make another instance depend on the current instance.
- Removing a relationship between process instances by using JavaScript

You can use JavaScript to remove a relationship between two process instances.
- Querying relationships between process instances by using JavaScript

You can get a list of the relationships that a process instance has by using JavaScript. You can also get a filtered list (by status) of the process instances that are related to the current process instance. For example, you can filter on all the active process instances that are related to the current process instance.
- Creating relationships between process instances by using REST API

You can add, remove, update, or query process instance relationships by using the REST APIs that IBM Business Automation Workflow provides.