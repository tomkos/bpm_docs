<!-- image -->

# Preventing multiple failed events when a service is unavailable

- Storing events

You can set up your applications so that, when a runtime error occurs during application processing, the recovery service stores the events (specifically, asynchronous requests) for later submission instead of repeatedly generating failed events. For example, if you are deploying an application that calls a web service and that web service is unavailable, a failed event is generated and then subsequent associated asynchronous requests are stored. Then, when the service becomes available, you can forward stored asynchronous requests for processing.
- Administering the store-and-forward feature

Use the Store and Forward widget in a business space to change the state or configure service control point properties.