# Configuring email for task notification assignment

## Before you begin

Verify that the Workflow Center server and Workflow Server are stopped.

## About this task

## Procedure

1. Open the 99Local.xml file and locate
the email properties section.
2. Open the 100Custom.xml file and copy and paste the email properties
section into the 100Custom.xml file between the properties tags.
3 In the <email> element, insert the values that are appropriate foryour environment. <mail-template> element The template used to generate the text of the email notification that is sent to a registereduser who is assigned a new task. The available templates are: Important: The default email template for task notificationassignment is the Workplace template: <process>externalmailprocessworkplace\_{0}.html</process> Tochange to the Process Portal email template, add the following customization:<mail-template><process>externalmailprocesslink\_{0}.html</process></mail-template> <smtp-server> element Ensure that the value of this element is a valid SMTP server. <default-from-address> element Ensure that the value of this element is a valid email address. <send-external-email> element If you want notification emails to be sent, ensure that the value is set totrue . <send-email-notifications-to-list> element By default, separate email is sent to each user that is assigned to the task and is registeredfor email notifications. To avoid lock time-outs when there are many users registered fornotifications, change the value to true so that users receive notification emailgrouped by locale. <send-email-notifications-async> element By default, notification email is sent synchronously with the navigation transaction of thebusiness process definition (BPD). To avoid lock time-outs when there are many users registered fornotifications, change the value to true so that notification email is sentasynchronously in a separate thread. <send-in-federation> element Set the value to true to ensure that the task links from all the Business Automation Workflow systems that do not hostthe federated Process Portal include a systemId parameter. The systemId parameter isneeded for the links to successfully open the task or instance details UI page in the federatedProcess Portal . <send-on-reassignment> element Set the value to true if you want users to be notifiedwhen a task is reassigned. By default, the value is set to false . <case-client> element Set the value to true to enable tasks in case processes to open inCase Client . When the value isset to true , non-case processes continue to link to the template defined inthe <process> element. By default, the <case-client> valueis set to false . The following example shows the values that you set for the <email> element in the 100Custom.xml file.<server merge="mergeChildren"> <email merge="mergeChildren"> <!-- SMTP server that mail should be sent to --> <smtp-server merge="replace">smtp.example.com</smtp-server> <mail-template> <process>externalmailprocesslink\_{0}.html</process> <no-process>externalmailnoprocess\_{0}.html</no-process> </mail-template> <valid-from-required merge="replace">true</valid-from-required> <default-from-address merge="replace">username@example.com</default-from-address> <send-external-email merge="replace">true</send-external-email> <send-email-notifications-to-list merge="replace">false</send-email-notifications-to-list> <send-email-notifications-async merge="replace">false</send-email-notifications-async> <send-in-federation merge="replace">true</send-in-federation> <send-on-reassignment merge="replace">true</send-on-reassignment> <case-client merge="replace">false</case-client> </email></server> Formore information, see The 100Custom.xml file and configuration and Setting configuration properties using100Custom.xml .
    - externalmailprocess\_*.html: Java-Script-based template for tasks that have an
associated process.
    - externalmailnoprocess\_*.html: JavaScript-based template for tasks that do not
have an associated process.
    - externalmailprocesslink\_*.html: Template that uses a link instead of
JavaScript.

```
<process>externalmailprocessworkplace\_{0}.html</process>
```

```
<mail-template>
<process>externalmailprocesslink\_{0}.html</process>
</mail-template>
```

```
<server merge="mergeChildren">
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
          <case-client merge="replace">false</case-client>
	</email>
</server>
```

4. Save your changes.
5 Optional: If you want toforce URLs that are included in emails to go through a network router,see the following scenario keys in Configuring endpoints to match your topology .

- SERVER\_EMAIL\_GADGET\_LINK
- SERVER\_EMAIL\_PORTAL\_LINK
- SERVER\_EMAIL\_PORTAL\_PROCESS\_INFO\_LINK
- SERVER\_EMAIL\_PORTAL\_RUN\_TASK\_LINK
- SERVER\_EMAIL\_TEMPLATE\_CLIENT\_LINK
6. Start the Workflow Center server and Workflow Server.

## What to do next

So that process participants receive email notifications,
ask them to update their user preferences.