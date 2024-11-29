# Error when the server starts after copying the deployment environment

```
[11/3/14 13:14:11:961 CST] 0000008c EmbeddedECMIn E CWTDS1100E: An error occurred while validating or creating the default configuration for the BPM document store.
com.ibm.bpm.embeddedecm.exception.UserMissesWritePermissionException: CWTDS0022E: The configuration was changed in a way that the technical user 'deadmin' of the BPM document store fails to change the object 'Domain'.
Explanation: The technical user defined in the BPM role type 'EmbeddedECMTechnicalUser' is not permitted to perform changes on an object.
Action: Revert the recent configuration changes. Ensure that the user defined by the BPM role type 'EmbeddedECMTechnicalUser' has access to the object. Verify this using the admin task 'getDocumentStoreStatus'.
```

## Resolving the problem

```
<wim:entities xsi:type="wim:PersonAccount">
    <wim:identifier  externalId="97d277cb-a47f-44b1-b522-37e01e1cb741" externalName="uid=deadmin,o=defaultWIMFileBasedRealm" uniqueId="97d277cb-a47f-44b1-b522-37e01e1cb741" uniqueName="uid=deadmin,o=defaultWIMFileBasedRealm"/>
     <wim:parent>
 ...
    <wim:uid>deadmin</wim:uid>
      <wim:cn>deadmin</wim:cn>
       <wim:sn>deadmin</wim:sn>
</wim:entities>
```