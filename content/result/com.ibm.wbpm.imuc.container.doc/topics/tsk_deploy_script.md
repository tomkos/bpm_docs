# Installing IBM Business Automation
Workflow
capability

## About this task

A custom resource YAML file is a configuration file that describes an ICP4ACluster instance and
includes the parameters to install some or all of IBM Business Automation
Workflow on containers.

A single custom resource file is used to include all of the components that you want to deploy
with an operator instance. Each time that you need to make an update or modification, you must use
this same file to apply the changes to your deployments. When you apply a new custom resource to an
operator, you must make sure that all previously deployed resources are included; otherwise, the
operator deletes them.

## Procedure

1. Create a custom resource file by copying the sample custom resource template from
ibm\_cp4a\_cr\_production\_FC\_workflow-standalone.yaml under
descriptors/patterns.
2 Before you apply the compiled custom resource file to the operator, you must check andedit all sections.
    1 Check and edit the shared sections. See Checking the cluster configuration .Note:
        - If the purchased production license is for Business Automation Workflow, then the
shared\_configuration.sc\_deployment\_context must be BAW
and the possible values for shared\_configuration.sc\_deployment\_baw\_license are:
non-production and production.
        - If the purchased production license is for Cloud Pak for Business Automation, then the
shared\_configuration.sc\_deployment\_context must be CP4A
and the possible values for shared\_configuration.sc\_deployment\_baw\_license are:
user, non-production, and production.
2. Check and edit the section for Workflow Runtime. See Configuring Workflow Runtime and Workstream
Services.
3. Check and edit the section for User Management Services (UMS). See Configuring User Management Services.
4. Check and edit the section for Business Automation Navigator. See Configuring Business Automation Navigator.
5. Check and edit the section for FileNet® Content
Manager. See
Configuring FileNet Content Manager.
3. Validate your custom resource file before you apply it. It is likely that you edited the
file multiple times, and possibly introduced errors or missed values during your
customizations. See Validating the YAML in your custom resource
file.
4 To install the deployment, apply the custom resource to the operator. Forexample, using the OpenShiftCLI:oc apply -f ibm\_cp4a\_cr\_production\_FC\_workflow-standalone.yaml Alternatively, using the OCP Admin console

```
oc apply -f ibm\_cp4a\_cr\_production\_FC\_workflow-standalone.yaml
```

Alternatively, using the OCP Admin console

1. Click the plus icon on the upper right .
2. Open the custom resource (CR) file you customized and verified on your local
machine.
3. Select all of the lines, and then copy and paste it into the editor.
4. Click Create.