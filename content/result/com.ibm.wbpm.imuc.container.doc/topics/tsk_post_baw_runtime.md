# Customizing Business Automation Workflow on containers properties

## About this task

This task provides the generic methods for modifying Liberty and 100Custom configuration settings
for Business Automation Workflow
deployment. The usage is generally paired with other documentation pages, which might describe a
specific Liberty or 100Custom configuration setting that needs to be modified.

- baw\_configuration[x].liberty\_custom\_xml to customize the Business Automation Workflow Runtime Liberty
server. If the customization does not contain sensitive information, you can use this property to
put the customization directly into the custom resource.
- baw\_configuration[x].custom\_xml\_secret\_name to customize Business Automation Workflow Runtime Liberty
server if the customization contains sensitive information
- baw\_configuration[x].lombardi\_custom\_xml\_secret\_name to customize the
Workflow Server Runtime 100Custom.xml

To modify settings, use the method for Business Automation Workflow Liberty
configuration settings either in baw\_configuration[x].liberty\_custom\_xml or in
baw\_configuration[x].custom\_xml\_secret\_name. Don't use both methods to specify
configuration values.

## Procedure

1 To customize Business Automation Workflow Runtime Libertyproperties, create a valid XML snippet with the Liberty configuration customization that you want,starting with the <server> element. Note:
    - baw\_configuration[x] is an array and you should ensure changes are applied to
the correct instance if you have multiple Business Automation Workflow instances. In the
examples, the changes are applied to the instance with the name bawins1.
    - If a password has a special character, you must encode it using XML special character encoding.
See Special Characters in XML Documents.
    - Customization that conflicts with the product setup and requirements isn't supported.
    - To use a plain XML snippet, add it in the liberty\_custom\_xml property.
The settings will be merged into the Liberty settings for the
component.    baw\_configuration:
    - name: bawins1
      liberty\_custom\_xml: |+
        <server>
          <!-- custom properties here -->
        </server>
    - To use a secret, do the following steps.
        1. Create a file, such as custom.xml, with the XML snippet you want.
        2. Create a secret with the file, such as custom-liberty-xml-secret, using the
following
command:kubectl create secret generic custom-liberty-xml-secret --from-file=sensitiveCustomConfig=./custom.xml
        3. In the CR, set the baw\_configuration[x].custom\_xml\_secret\_name property, as
shown in this example snippet.    baw\_configuration:
    - name: bawins1
      custom\_xml\_secret\_name: custom-liberty-xml-secret
2 You can also modify Business Automation Workflow Runtimeconfiguration properties in a 100Custom.xml file.

1. Create a 100Custom.xml file with the snippet you
want. For more information, see Creating a 100Custom.xml configuration file.
2. Create a secret with the file, such as
lombardi-custom-xml-secret, using the following command. 
kubectl create secret generic lombardi-custom-xml-secret --from-file=sensitiveCustomConfig=./100Custom.xml
3. In the CR, set the lombardi.custom\_xml\_secret\_name property, as
shown in this example snippet. 
    baw\_configuration:
    - name: bawins1
      lombardi\_custom\_xml\_secret\_name: lombardi-custom-xml-secret
3. After you modify the CR file, you must update your deployment to have it take effect.
Follow the instructions in Updating script-installed
deployments.
4. When you are making a Liberty customization, check that the Workflow server pod picks up
the changes after it restarts. After the reconciliation takes effect (which usually takes 30 minutes
to an hour, but can take longer), the XML file can be found at this location inside the pod. 
cd /opt/ibm/wlp/usr/shared/resources/sensitive-custom/
5. To verify the 100Custom.xml settings, check for the files on the
server pods. For more information, see Location of 100Custom configuration files.