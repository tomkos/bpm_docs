# Enabling the Liberty feature to integrate with IBM MQ for Business Automation Workflow on
containers

## Procedure

To integrate with MQ, complete the following steps.

1. To download and generate the MQ resource adapter file, follow steps 1 - 4 in Installing the resource adapter in Liberty.
2. Add the downloaded MQ resource adapter files, such as
wmq.jmsra.rar, to the Workflow server pod, by using the filestore persistent
volume claim (PVC) that is mounted at /opt/ibm/bawfile. For more information,
see Accessing files for applications and
configurations.
 For example, run the following command to copy the file to the Workflow server location
/opt/ibm/bawfile, where wmq.jmsra.rar is the file you want
to copy and workflow-server-pod is the name of one of your Workflow
pods.oc cp wmq.jmsra.rar workflow-server-pod:/opt/ibm/bawfile/The files are
stored in the persistent volume (PV) related to the PVC and are kept between restarts.
3. Configure the resource adapter and JMS queue to connect to your MQ engine by customizing
the Liberty custom XML file that is set in the liberty\_custom\_xml parameter.
The settings will be merged into the Liberty settings for the component. For more information about
Liberty customization, see Administering Liberty manually. The XML snippet must be in the
<server> element, as shown in the following
example.<server>
   <!-- configure wmqJmsClient.rar.location pointing to your resoruce adapter file -->
   <variable name="wmqJmsClient.rar.location" value="/opt/ibm/bawfile/wmq.jmsra.rar" />
 
   <!-- configure queue connection factory and queue to connect to your MQ engine -->
   <variable name="MQ\_CONNECTION\_LIST" value="yourmq.connect.name(1414)" />
   <variable name="MQ\_QMGR\_NAME" value="VDCTQMI" />
   <variable name="JMS\_ASPC001\_ECE\_CHN" value="VDI.ASPC001" />
   <jmsQueueConnectionFactory id="jms/QCF" jndiName="jms/QCF">
       <properties.wmqJms connectionNameList="${MQ\_CONNECTION\_LIST}"
           queueManager="${MQ\_QMGR\_NAME}" channel="SYSTEM.DEF.SVRCONN"
           transportType="CLIENT" targetClientMatching="false" />
       <connectionManager connectionTimeout="20s"></connectionManager>
   </jmsQueueConnectionFactory>
    <!-- JMS Queues -->
   <jmsQueue jndiName="jms/ASPC001\_ECE\_CHN" id="jms/ASPC001\_ECE\_CHN">
       <properties.wmqJms baseQueueManagerName="${MQ\_QMGR\_NAME}" baseQueueName="${JMS\_ASPC001\_ECE\_CHN}" />
   </jmsQueue>

<server>
4. To customize Liberty with your XML snippet, follow the instructions in
Customizing Business Automation Workflow properties.