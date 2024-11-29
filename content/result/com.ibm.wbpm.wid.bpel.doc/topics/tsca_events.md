<!-- image -->

# Enabling SCA events to be emitted

## Procedure

To enable SCA events to be emitted, complete the following
steps:

- In the Websphere Application Server administrative console,
click Servers > Clusters > WebSphere application server clusters and select your application cluster .
- On the Configuration tab, under Business Process Manager,
expand Business Process Choreographer.
- Click Business Flow Manager.
- Under Additional Properties, click Custom Properties.
- Add a new property named Compat.SCAMonitoringForBFMAPI. Set the value as true.
- Save your changes and restart the application cluster.