# Upgrading IBM Business Automation
Workflow
on containers

## Before you begin

- To save federated-saved searches in the Elasticsearch index, you must save them before you
upgrade. Otherwise, your saved searches are lost.
- Before you start an upgrade, back up your data and take snapshots if necessary. If you do not
have your data that is backed up, you cannot properly roll back. Read Backing up your environments for more instructions that are
not covered in the container upgrade sections.
- To prevent any connection problems during the upgrade, make sure that the passwords that you use
for databases and lightweight directory access protocol (LDAP) are not about to expire. If they are
about to expire, refresh the passwords. For example, an out-of-date ldapPassword
key in the LDAP bind secret stops UMS pods from restarting. These pods can also prevent other pods
that integrate with UMS from restarting. The LDAP bind secret "ldap-bind-secret" is
set in the lc\_bind\_secret parameter in the following
ldap\_configuration
section.ldap\_configuration:
   lc\_bind\_secret: ldap-bind-secret
- The full text search is not enabled in Business Automation Workflow Runtime deployment.
After upgrade, this new behavior is applied by default. Follow step 5 to enable full text search, which is the same as
before the upgrade.

Don't set shared\_configuration.sc\_egress\_configuration.sc\_restricted\_internet\_access as
true until after you finish the upgrade.

The Process Federation Server
and Application Engine are removed from
the default deployment and can be enabled as advanced configuration. See Container runtime. By default, the topology is changed to a new topology after upgrade.
Follow step 5 to keep the Business Automation Workflow federated by
Process Federation Server, which
is the same as before the upgrade.

- After you run the upgrade script:
    - pfs\_configuration and elasticsearch\_configuration are removed
from your custom resource. Since 23.0.2, the Process Federation Server operator is
managed separately. Process Federation Server does not
federate Business Automation Workflow by
default.
    - applicationengine\_configuration still exists in the custom resource. Workplace deployed in Application Engine still integrates with Process Federation Server. Process Federation Server does not
federate Business Automation Workflow by
default.
- Full text search is not enabled by default in the latest version. To enable full text search
manually, see Enabling full text search.
- The embedded Java Message Service (JMS) server, running on the Workflow server pod, is
configured by default. To deploy an independent JMS server, follow the steps in Customizing an independant JMS server.

## Procedure

To upgrade to the latest version.

1. Upgrade dependencies to the new supported versions. See Upgrading.
2. Get access to the container images by following the steps in Getting access to images from the public IBM Entitled
Registry.
3 Upgrade the operator to the new version before you apply your custom resource upgrades.
    - Go to https://github.com/ibmbpm/BAW-Ctnr/tree/24.0.0/archive and get the latest
.tar file for the IBM Business Automation
Workflow repository. Extract the
contents from the .tar file, Use the tar -xvzf command to
extract it to the cert-kubernetes directory.
    - Run the command to update baw related
operators:./scripts/upgradeOperator.sh -n <project\_name> -a accept -m baw
4 Get the custom resource that you used to install Business Automation Workflow and update it forthe new deployment.

1. Change the metadata.labels.release parameter value to the new version, for
example, 24.0.0.0.
2. Change the appVersion parameter value in the spec
section to the new version.
3 Compare the new custom resource template underdescriptors/patterns (for example, templateibm\_cp4a\_cr\_production\_FC\_workflow-standalone.yaml ) with the custom resource that you usedto install. Change the image.tag parameter values in all sections to the newversion. Where required, add mandatory parameters to the file and provide specific values forparameters that previously used the default value. If you did not run the script to upgrade:

If you did not run the script to upgrade:

    1. The pfs\_configuration and elasticsearch\_configuration
sections, along with their titles, can be removed from your configuration. If you upgraded from
23.0.1 or a previous release, and choose to not use IBM Process Federation
Server, you can remove
the host\_federated\_portal setting from the baw\_configuration.
    2 Perform the following actions to update baw\_configuration[0].case section tothe new structure:
        - Move the value of object\_store\_name\_tos to
baw\_configuration[0].case.tos\_list[0].object\_store\_name.
        - Move the value of connection\_point\_name\_tos to
baw\_configuration[0].case.tos\_list[0].connection\_point\_name. If
connection\_point\_name\_tos is not configured, get the value from
initialize\_configuration.ic\_obj\_store\_creation.object\_store. Find the target object
store and copy the value of oc\_cpe\_obj\_store\_workflow\_pe\_conn\_point\_name.
        - Move the value of target\_environment\_name to
baw\_configuration[0].case.tos\_list[0].target\_environment\_name. An example of a
target object store in
tos\_list:baw\_configuration:
  - case:
      tos\_list:
      - object\_store\_name: "BAWTOS"        
        connection\_point\_name: "pe\_conn\_target"
        desktop\_id: "baw"
        target\_environment\_name: "target\_env"
        is\_default: true where desktop\_id and
is\_default are optional parameters. For a single target object store, the default
value of desktop\_id is baw and the default value of
is\_default is true. If there are more than one target object
stores, specify the default target object store by using the is\_default
parameter.
3. Delete object\_store\_name\_tos, connection\_point\_name\_tos,
target\_environment\_name, and datasource\_name\_tos from
baw\_configuration[0].case section.
4 If the purchased production license is for:

- Business Automation Workflow, then
the shared\_configuration.sc\_deployment\_context must be
BAW and the possible values for
shared\_configuration.sc\_deployment\_baw\_license are
non-production and production.
- Cloud Pak for Business Automation, then the
shared\_configuration.sc\_deployment\_context must be CP4A
and the possible values for shared\_configuration.sc\_deployment\_baw\_license are
user, non-production, and production.
5 If you are using Red Hat OpenShift, continue to the next step.

- For Workflow Server
configuration, an example of a hostname update might be a change from
baw.test1.9.x.x.x.nip.io to baw-test1.9.x.x.x.nip.io. If you want
to keep the hostname that you defined in a previous release, add the hostname
attribute under the baw\_configuration section. For example:
baw\_configuration:
     hostname: "baw.test1.9.x.x.x.nip.io"
- For Process Federation Server configuration, an example of a hostname update might be a change from
pfs.test1.9.x.x.x.nip.io to pfs-test1.9.x.x.x.nip.io. If you want
to keep the hostname that you defined in a previous release, add the hostname
attribute under the pfs\_configuration section. For example,
pfs\_configuration:        hostname: "pfs.test1.9.x.x.x.nip.io"
6 Check the upgrade instructions for prerequisite capabilities that require more actions.

- Upgrading IBM Business Automation Application Engine.
- Upgrading IBM FileNet Content Manager.
- Upgrading User Management Service in
User Management Services on Containers.
- Upgrading IBM Business Automation Navigator.
5 Apply and verify the upgraded deployment.

- Run the following command to apply the custom resource:
oc apply -f <ibm\_cp4a\_cr\_production\_FC\_workflow-standalone.yaml> -p <baw\_project>
- See Verifying the installation to complete the upgrade and verify the  Business Automation Workflow component.
- See Completing post-upgrade tasks to verify that other components
are included as part of Business Automation Workflow on containers.
- If you want to enable full text search, similar to versions earlier than 23.0.2, see Enabling full text search. To continue using the saved searches used in federated
environments, follow the steps in Migrating saved searches to a new federated data
repository.
- If you want Business Automation Workflow to be federatedsimilar to versions earlier than 23.0.2, perform the following actions:
    1. Upgrade the Process Federation Server. For more
information, see Upgrading Process Federation Server on Red Hat OpenShift from 23.0.1 to 23.0.2.
    2. Set the following parameters.baw\_configuration:
  full\_text\_search:
    enable: true
  elasticsearch:
    endpoint:
    admin\_secret\_name:
  process\_federation\_server:
    hostname:
    port:
Note: If the port value is not set, the default value is
443.
To find the Process Federation Server information,
run the following
command.oc get pfs -o=jsonpath='{.items[0].status.endpoints[?(@.name=="Process Federation Server External base URL")].uri}'
To find Elasticsearch information, run the following command:oc get secret|grep elasticsearch
oc get pfs -o=jsonpath='{.items[0].status.endpoints[?(@.name=="Elasticsearch Internal https URL")].uri}'
You can choose whether Business Automation Workflow hosts federated
Process Portal. If yes, set
the following parameters. - name: bawins1
  host\_federated\_portal: trueNote: Only one Business Automation Workflow runtime server
connected to the Process Federation Server can host
federated portal.

## What to do next

- For rollback instructions, see Rolling back an upgrade.
- If you choose not to federate Business Automation Workflow Runtime, you can
delete the Process Federation Server custom resource
by using the following command.
oc delete pfs -n <YourNamespace> --all