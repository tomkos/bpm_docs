# Extending a network deployment environment using the BPMConfig command

## Before you begin

- You must have installed the product on the computer where you
want to extend the deployment environment.
- You must have an existing deployment environment.
- The deployment manager must be running.

## About this task

- Creates any local profiles specified in the configuration properties file that
do not already exist. BPMConfig cannot augment existing WebSphere® Application
Server profiles with Business Automation Workflow. If you want to use existing WebSphere Application
Server profiles, you must augment them first. See Creating or augmenting managed-node profiles on Linux.
- Federates the node of the profile and adds the managed node to the deployment environment.
- Creates any missing cluster members.

## Procedure

To extend an existing deployment environment to
include additional nodes (profiles) or cluster members:

1. If you do not already have
a customized configuration properties file based on the existing deployment
environment that you want to extend, use the BPMConfig command
with the -export parameter to create a configuration
properties file that reflects your current deployment environment.
Determine the minimum settings for a new node by examining the sample
configuration files that are provided in the following directory:
install\_root/BPM/samples/config
2. Modify the properties file to add the additional nodes (profiles) and cluster members to extend
the existing environment. 

When adding managed nodes to an existing deployment environment,
define each new node by duplicating the set of bpm.de.node properties that exist in
the properties file and specifying the values that apply to the new managed node. 
Duplicate a set of node and cluster member properties in the file, and then increment the
sequence number in the property names that you added. 

For example, if you currently have two sets of properties for your nodes and associated cluster
members, and you want to add a third, the third set of properties that you add should look like the
following
properties:##########################
	# Node properties: Node3 #
	##########################

	bpm.de.node.3.name=Node3
	bpm.de.node.3.hostname=<hostname>
	bpm.de.node.3.installPath=<WAS\_HOME\_path>
	bpm.de.node.3.profileName=<Node3Profile>
	# optional profilePath  defaults to <WAS\_HOME\_path/profiles/profileName>
	bpm.de.node.3.profilePath=
	# optional initialPortAssignment
	bpm.de.node.3.initialPortAssignment=
	# Enter location of the jdbcdriver path 
	bpm.de.node.3.jdbcDriverPath=${WAS\_INSTALL\_ROOT}/jdbcdrivers/DB2
	###################################################
	# Cluster member properties: SingleClusterMember3#
	###################################################
	bpm.de.node.3.clusterMember.1.name=SingleClusterMember3
	bpm.de.node.3.clusterMember.1.cluster=SingleCluster 
	bpm.de.node.3.clusterMember.1.weight=2
	bpm.de.node.3.clusterMember.1.initialPortAssignment= 

For more information about the available properties, read the comments in the sample files, or
see the BPMConfig command-line utility and the examples.
3. Run the following command to verify that the modified
properties file contains valid properties: 
install\_root/bin/BPMConfig -validate properties\_file
4 To add new nodes or cluster members:
    1. Ensure the deployment manager is running.
    2. For each profile that you want to create on a remote installation, run the following command on
the computer with the remote installation (not on the deployment manager):
install\_root/bin/BPMConfig -create -de properties\_fileThe
managed node profile will be created if it does not already exist. Only one node can be federated to
the deployment manager at a time. Ensure that you are running only one BPMConfig
command at a time.
    3. On the deployment manager, run the BPMConfig -create -de command.

install\_root/bin/BPMConfig -create -de properties\_file
5. Synchronize all the nodes in the deployment environment to propagate the configuration from the
deployment manger to all nodes. 
Use the syncNode command or restart the node agents. Before you start the new
cluster members, ensure that synchronization has completed by checking the
syncNode.log file or the node agent logs found in the
profile\_root/logs directory.