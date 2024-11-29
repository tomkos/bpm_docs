<!-- image -->

# Behavior of store-and-forward feature after server restart, application stoppage, or
application uninstallation

- If there are events in the queue when the user uninstalls the application, the queue and all
stored events are deleted.
- If the application is stopped and restarted, the store remains activated.
- If there are events in the queue and the server is restarted, the state changes from store to
forward and all the events in the queue are processed.