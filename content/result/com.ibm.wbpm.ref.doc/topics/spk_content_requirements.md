# Settings for upload of large documents

In order to upload large documents of sizes greater than 1GB, some configuration settings
are required.

The default storage area of an object store is the Database storage areas. It is recommended to use File storage areas or Advanced storage areas if document size exceeds 100 MB.

## Settings

You can upload documents greater than 1 GB, using different settings.

- Use a different storage area like a file store area against a database storage area to upload
documents of size greater than 300 MB.
- Increase the value of clientInactivityTimeOut. For
example<server>
<transaction clientInactivityTimeout="1800s" propogatedOrBMTTranLifetimeTimeout="1800s" totalTranLifetimeTimeout="1800s"/>
</server> For more information, see Transaction Manager (transaction).
- Update the memory limits and the initial and max heap percentages. These parameters areconfigured through the related Content Platform Engine and CMIS CR parameter. Formore information, see For example ecm\_configuration: cmis: resources: limits: memory: 4096Mi cmis\_production\_setting: jvm\_initial\_heap\_percentage: 40 jvm\_max\_heap\_percentage: 66 querytime\_limit: 600cpe: resources: limits: memory: 4096Mi cpe\_production\_setting: jvm\_initial\_heap\_percentage: 40 jvm\_max\_heap\_percentage: 66
    - Content Platform Engine CR
parameter: https://github.ibm.com/dba/cert-kubernetes/blob/22.0.2/descriptors/patterns/ibm\_cp4a\_cr\_production\_FC\_content.yaml#L838-L841
    - CMIS CR
parameter: https://github.ibm.com/dba/cert-kubernetes/blob/22.0.2/descriptors/patterns/ibm\_cp4a\_cr\_production\_FC\_content.yaml#L1083-L1086

```
ecm\_configuration:
  cmis:
    resources:
      limits:
        memory: 4096Mi
    cmis\_production\_setting:
      jvm\_initial\_heap\_percentage: 40
      jvm\_max\_heap\_percentage: 66
    querytime\_limit: 600
cpe:
  resources:
    limits:
      memory: 4096Mi
  cpe\_production\_setting:
    jvm\_initial\_heap\_percentage: 40
    jvm\_max\_heap\_percentage: 66
```