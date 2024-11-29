# Configuring email for Workplace notifications for Business Automation Workflow on
containers

## Before you begin

- If you do not want to configure network policies to manage access to external services (egress),
you can update sc\_restricted\_internet\_access: false in your custom resource(CR)
file.
- If you need to configure network policies to manage access to external services (egress), you
can keep sc\_restricted\_internet\_access: true in your CR file and follow Network policies to manage access to external services
(egress) to create egress network policies for workflow authoring or workflow runtime. If you
are creating a custom "component-level" egress network policy, set the podSelector.match
Labels.com.ibm.cp4a.networking/egress-external-app-component parameter to
BAW for Business Automation Workflow Runtime or
BAS for Business Automation Workflow Authoring.

## Procedure

To update the configuration file to enable the email notification for Workplace, complete the following
steps in the OpenShift Container Platform (OCP) starter pattern:

1. Compose an XML file with the following email
properties: <server merge="mergeChildren">
	<email merge="mergeChildren">
		<!-- SMTP server that mail should be sent to -->
		<smtp-server merge="replace">smtp.example.com</smtp-server>
     <mail-template>
        <process>externalmailprocesslink\_{0}.html</process>
        <no-process>externalmailnoprocess\_{0}.html</no-process>      
     </mail-template> 
		  <valid-from-required merge="replace">true</valid-from-required>
		  <default-from-address merge="replace">username@example.com</default-from-address>
		  <send-external-email merge="replace">true</send-external-email>
		  <send-email-notifications-to-list merge="replace">false</send-email-notifications-to-list>
		  <send-email-notifications-async merge="replace">false</send-email-notifications-async>
		  <send-in-federation merge="replace">true</send-in-federation>	
          <send-on-reassignment merge="replace">true</send-on-reassignment>
	</email>
</server>For more information, see Configuring email for task notification assignments.
2 Apply the configuration changes:
    - In a non-production deployment using IBM Business Automation Studio, apply the XML
configuration to the bastudio\_configuration.bastudio\_custom\_xml property in the
custom resource (CR) yaml file.For more information, see IBM Business Automation Studio parameters.
    - In a production deployment of Business Automation Workflow Authoring orBusiness Automation Workflow Runtime,save the XML configuration changes to a file, for example 112Custom.xml , andcreate a secret from the file by using the followingcommand:kubectl create secret generic custom-xml-secret-name --from-file=sensitiveCustomConfig=./112Custom.xml Formore information, see Business Automation Workflow Authoringparameters and Business Automation Workflow Runtimeparameters . Then apply the secret to thelombardi\_custom\_xml\_secret\_name property: For more information, see Optional: Customizing Business Automation Studio properties .

```
kubectl create secret generic custom-xml-secret-name --from-file=sensitiveCustomConfig=./112Custom.xml
```

For
more information, see Business Automation Workflow Authoring
parameters and Business Automation Workflow Runtime
parameters.

        - workflow\_authoring\_configuration.lombardi\_custom\_xml\_secret\_name to customize
Workflow Authoring.
        - baw\_configuration[x].lombardi\_custom\_xml\_secret\_name to customize the Workflow
Server.

For more information, see Optional: Customizing Business Automation Studio properties.

3. Save your changes.
4. Wait for the Cloud Pak for Business Automation operator to reconcile the
changes.
5. Optional: If you want to customize the sender's name in the email
notification header, you can customize the name of the system user who created the task, typically
the admin. To do that, specify a value for the userToCreateTask property, which
represents the user ID that is set in the task's receivedFrom field and is assigned
the admin role. For more information, see Security configuration properties
.

## Results