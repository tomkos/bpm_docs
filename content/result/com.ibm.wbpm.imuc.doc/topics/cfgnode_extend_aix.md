# Extending the deployment environment using the configureNode
command

After you have created a deployment environment
using the configureNode command, you can run the
command at a later time to extend the deployment environment.

## Before you begin

- You must have installed the product on the machine where you want
to extend the deployment environment.
- The deployment manager must be running.
- You must have created the deployment environment by running the configureNode command.

## Procedure

1. On the machine where you want to extend
the deployment environment, locate the sample custom node files:
install\_root/util/ndUtils/samples/
2. Copy the sample file that is most similar
to the properties file that you need. 
For example, to extend the deployment environment
for IBM® BPM Advanced for
Workflow Server, choose the sample\_adv\_ps\_node.properties file.Modify the new custom node file to reflect
your environment, including the details of the deployment manager.
For
more information about the available properties, read the comments
in the sample files, or see the configureNode command
reference and the examples.Restriction: The parameters
listed in the sample files are the only parameters that can be customized.
3 Run the configureNode command,passing it the name of the sample file. For example: Note: If you receive the Failed to performSecurity setting update error, check to ensure that the globalIP address has not been appended to 127.0.0.1 localhost inthe hosts file. For example: 127.0.0.1 localhost example.ibm.com .
    - install\_root/util/ndUtils/configureNode.sh
-response node01\_response\_file.properties

## Results

You have extended the deployment environment.

Messages are recorded in the file
install\_root/logs/config/configureNode.log.

## Related information

- Topologies of a network deployment environment
- configureNode command-line utility
- Removing a managed node profile from a deployment environment