# Error when sending event (NameNotFoundException)

## Cause

- The event service has not been deployed.
- The event service is disabled.

## Remedy

1. Start the wsadmin tool.
2. Use the AdminTask object to run the deployEventService administrative
command.
3. Restart the server.

1. Start the wsadmin tool.
2. Use the AdminTask object to run the enableEventService administrative
command.
3. Restart the server.

1. Click Applications > Application
Types > WebSphere enterprise
applications > server > Container Services > Common Event Infrastructure
Service.
2. Select the Enable service at server startup property.
3. Click OK to save your changes.
4. Restart the server.