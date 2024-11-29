<!-- image -->

# Administering the store-and-forward feature

## About this task

The Store and Forward widget has two states: Store and Forward. The state should bet set to Store
if you want to store failed events for future processing. The first failed message is sent to the
failed event manager, but subsequent failures are prevented because messages are stored until the
destination becomes available again. When the service is available, stored messages can be forwarded
by setting the service control point to its Forward state.

You can also see store-and-forward service control point properties. Some of these properties can
be edited.

For more information related to manually starting the store or forwarding stored messages, see
the online help provided in the Store and Forward widget.

- Enabling common base event generation during store-and-forward processing

Enable the store-and-forward function to create common base events when the store is started or stopped using the administrative console in IBM Business Automation Workflow.