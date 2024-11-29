# Creating or augmenting network deployment profiles

You must create or augment a deployment manager
profile and one or more custom profiles before creating the deployment
environment. Using profiles, you can have more than one runtime environment
on a system, without having to install multiple copies of IBM® Business Automation Workflow.

- Creating a deployment manager and managed-node profiles with the BPMConfig command

You can use the BPMConfig command to create the deployment manager and managed node profiles separately from creating the deployment environment.
- Creating or augmenting deployment manager profiles

To start the network deployment configuration, create or augment a deployment manager profile. You can create or augment deployment manager profiles using either the Profile Management Tool or the manageprofiles command-line utility.
- Creating or augmenting managed-node profiles

As part of the network deployment configuration, you must create or augment at least one custom profile. A custom profile contains an empty node that you must federate into a deployment manager cell to make operational. Federating the node changes it into a managed node.
- Federating nodes to the deployment manager

After creating a custom profile, you can use the addNode command to federate the node into a deployment manager cell. This is only required if you specified the -federateLater parameter with the manageprofiles command or if the deployment manager was not running during the initial profile creation. You can manage all federated nodes from the deployment manager. (You can also use the BPMConfig command to federate nodes.)