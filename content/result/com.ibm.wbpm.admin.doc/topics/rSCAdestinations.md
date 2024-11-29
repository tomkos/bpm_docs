# SCA destinations aren't preserved when you uninstall and reinstall a service module

## Scenarios for preserving destinations

- When the application uses MQ JMS binding or MQ binding. The callback queue, or destination, must
be preserved even after applications are uninstalled or updated so the callback messages are not
lost for the processes that are still running.
- When event sequencing is used.

## Preserving SCA destinations

To preserve SCA destinations, use the SCA.recycleDestinations custom Java™
virtual machine (JVM) property for the module. Set the property to false.