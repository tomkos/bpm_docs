# Storing events

- How the store-and-forward feature works

To enable the store-and-forward feature, you set the store-and-forward qualifier on the component that will be invoked asynchronously. If that component then calls a service that is unavailable, a failed event is created and a service unavailable exception is generated. Once a failed event triggers the store function, all subsequent asynchronous requests intended for the component are stopped and stored. When the service becomes available again, you can resubmit the failed events that triggered the store and set the Store and Foward widget to forward stored events for processing.
- Store-and-forward feature set up

Consider the following information when implementing store-and-forward processing.