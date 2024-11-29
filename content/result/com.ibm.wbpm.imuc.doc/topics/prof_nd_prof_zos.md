# Creating or augmenting network deployment profiles (deprecated)

- Creating a deployment manager and managed-node profiles with the BPMConfig command (deprecated)

You can use the BPMConfig command to create the deployment manager and managed node profiles separately from creating the deployment environment.
- Creating or augmenting deployment manager profiles (deprecated)

To start the network deployment configuration, create or augment a deployment manager profile. You can create or augment deployment manager profiles using either the Profile Management Tool or the manageprofiles command-line utility.
- Creating or augmenting managed-node profiles (deprecated)

As part of the network deployment configuration, you must create or augment at least one custom profile. A custom profile contains an empty node that you must federate into a deployment manager cell to make operational. Federating the node changes it into a managed node.
- Federating nodes to the deployment manager (deprecated)

After creating a custom profile, you can use the addNode command to federate the node into a deployment manager cell. This is only required if you specified the -federateLater parameter with the manageprofiles command or if the deployment manager was not running during the initial profile creation. You can manage all federated nodes from the deployment manager. (You can also use the BPMConfig command to federate nodes.)