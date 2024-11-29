# Configuring Business Automation Workflow and VMM by using a
group membership property that reflects direct users in a group

## About this task

To configure VMM and IBM Business Automation Workflow by using
a group membership property that reflects direct users in a group, you make all file changes in the
deployment manager profile (DmgrProfile). After you are finished, you stop the JVMs, deployment
manager, and node agents, and then you restart the deployment manager, synchronize the node agents,
and start the servers.

## Procedure

1. Extend the VMM entity type Group to include an extra property with the name
groupmember. 

The file is called wimxmlextension.xml and is located in the
install\_root/profiles/profile/config/cells/cell/wim/model directory. If this
directory contains no such file, create a file called wimxmlextension.xml. For
example:
IBM/BPM/v8.5/profiles/DmgrProfile/config/cells/PCCell1/wim/model/wimxmlextension.xml

In a cluster, the wimxmlextension.xml file is on the deployment manager for
each server of the cluster.
Add the following configuration to the wimxmlextension.xml file:
<sdo:datagraph xmlns:sdo="commonj.sdo"
        xmlns:wim="http://www.ibm.com/websphere/wim">
      <wim:schema>
    	<wim:propertySchema nsURI="http://www.ibm.com/websphere/wim" dataType="STRING"
            multiValued="true" propertyName="groupmember">
          <wim:applicableEntityTypeNames>Group</wim:applicableEntityTypeNames>
        </wim:propertySchema>
      </wim:schema>
    </sdo:datagraph>
2. For each LDAP directory that is configured for VMM, you must define the mapping between the VMM
property name groupmember and the corresponding available LDAP attribute, such as
the member. 
For a typical Microsoft Active Directory configuration, include the following entry in the
install\_root/profiles/profile/config/cells/cell/wim/config/wimconfig.xml
file, or in a cluster, include this entry on the deployment manager for each server in the
cluster:<config:repositories xsi:type="config:LdapRepositoryType" ...>
    ...
    <config:attributeConfiguration>
    ...
    <config:attributes name="member" propertyName="groupmember">
      <config:entityTypes>Group</config:entityTypes>
    </config:attributes>
    ...
   </config:attributeConfiguration>
</config:repositories>
3. For each LDAP directory configured for VMM, tune your LDAP configuration in
					the wimconfig.xml file to allow for the retrieval of all
					groups in one VMM query.

Refer to the VMM tuning documents. Select an appropriate setting for
configurationProvider->maxSearchResults and adapt other values, such as
ldapServers->connectTimeout and attributesCache->cacheSize, as
necessary.
4. Enable the use of the groupmember properties by Business Automation Workflow. 
Include the following entry in the 100Custom.xml
file:<common merge="mergeChildren">
    		<security>
    			<vmm-options>
    				<group-member-prop>groupmember</group-member-prop>		
    			</vmm-options>
    		</security>
    	</common>The
100Custom.xml file is in the
install\_root/profiles/profile/config/cells/cell/nodes/node/servers/server/process-center|process-server/config
directory. In a cluster, the 100Custom.xml file is on the deployment manager
for each server of the cluster.
5. After all files are created or updated, stop all Business Automation Workflow JVMs, node agent, and deployment manager.
6 Start the servers in the following order by running the appropriate commands.
    1. Start Deployment Manager.
    2. Run a syncNodes command in the node profile. For more information, see the
WebSphere® Application
Server synchronization
process page.
    3. Start nodeAgent.
    4. Start the messaging servers.
    5. Start AppTarget servers.
    6. Start the Support server.