# Customizing Process Federation Server
for Business Automation Workflow on
containers

## About this task

After you install Business Automation Workflow, the
<CR\_Name>-federated\_ps\_short-secret-custom secret contains a Process Federation Server configuration
file named user.xml. If
federated\_ps\_short\_configuration.enable\_default\_security\_roles is set to
true in the custom resource (CR) file, you can use the
user.xml to configure the user registry and user roles for Process Federation Server.

```
kubectl create secret generic ibm-federated\_ps\_short-config --from-file=/opt/federated\_ps\_short/configDropins
```

## Procedure

The following example shows how to update the custom configuration roles for Process Federation Server by changing the user.xml
file.

1. Get the content of the user.xml file.
The file is encoded with base64 in the ibm-federated\_ps\_short-config secret. Run the
following command to get it:
oc get secret <CR\_Name>-federated\_ps\_short-secret-custom -o yaml
2. Decode the data in the user.xml file and update the content, then encode the
updated content with base64. If you are on a Linux based system, you can decode and encode with the
base64 command. For more information, see Base64 Linux man page. If you are on Windows, you
can decode and encode with the built-in certutil command. For more information, see
Certutil windows command.
3. Update ibm-federated\_ps\_short-config to add the new secret.
Run the following
command:oc edit secret <CR\_Name>-federated\_ps\_short-secret-customReplace the data in
user.xml with the updated base64-encoded content. 
When you save and quit, the content is updated in the Process Federation Server Pod
starter-ibm-process-federation-server-0 synchronously.

## What to do next