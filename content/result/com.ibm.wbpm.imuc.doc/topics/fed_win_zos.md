# Federating nodes to the deployment manager

## Before you begin

- You have installed IBM® Business Automation Workflow and
created a deployment manager and a managed-node profile. This procedure
assumes you did not federate the managed-node profile during
its creation or augmentation by using the BPMConfig command,
Profile Management Tool, or manageprofiles command-line
utility.
- The deployment manager is running. If it is not, start it eitherby selecting Start the deployment manager fromits Quick Start console or by entering the following command, where profile\_root representsthe installation location of the deployment manager profile:
    - profile\_root\bin\startManager.bat
- The deployment manager has been created or augmented
to be an IBM Business Automation Workflow deployment
manager.
- The deployment manager is at the same release level or higher
than the managed-node profile you created or augmented.
- The deployment manager has a JMX administrative port enabled.
The default protocol is SOAP.

## Procedure

1 Go to the bin directoryof the managed-node profile you want to federate. Opena command window and go to the following directory (from a commandline), where profile\_root represents the installationlocation of the managed-node profile):
    - profile\_root\bin
2 Run the addNode command. Run the following command from the command line (where profile\_name isthe name of the custom profile that you are about to federate). Alsoensure that the -username and -password parametersare specified because the Business Automation Workflow deployment manager has securityenabled. An output window opens. If you see a messagesimilar to the following message, your managed-node profile was federatedsuccessfully:ADMU0003I: Node DMNDID2Node03 has been successfully federated.

Run the following command from the command line (where profile\_name is
the name of the custom profile that you are about to federate). Also
ensure that the -username and -password parameters
are specified because the Business Automation Workflow deployment manager has security
enabled.

- addNode.bat deployment\_manager\_host deployment\_manager\_SOAP\_port -username userID\_for\_authentication -password
 password\_for\_authentication -profileName profile\_name

```
ADMU0003I: Node DMNDID2Node03 has been successfully federated.
```

## Results

The managed-node profile is federated into the deployment
manager.

## What to do next

After federating the managed-node profile, federate
further profiles or go to the administrative console of the deployment
manager to create your Business Automation Workflow deployment environment.