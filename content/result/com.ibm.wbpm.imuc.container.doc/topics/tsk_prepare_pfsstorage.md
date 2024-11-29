# Prepare for Process Federation Server

- Preparing storage
- Creating secrets to protect sensitive configuration data
- Prepare the federated data repository

## Preparing storage

- Option 1: If your environment supports dynamic provisioning. Enable dynamic provisioning by
setting pfs\_configuration.logs.storage.use\_dynamic\_provisioning to
true and provide the storage class name of
pfs\_configuration.logs.storage.storage\_class in the custom resource file. If you
also want to persist dump files, set pfs\_configuration.dump.persistent to
true.
- Option 2: If your environment does not support dynamic provisioning. Disable dynamic
provisioning by setting pfs\_configuration.logs.storage.use\_dynamic\_provisioning to
false. Then, create a PV manually and set
pfs\_configuration.logs.storage.existing\_pvc\_name in the custom resource file to the
value of the name property of your PV. To persist dump files, disable dynamic
provisioning by setting  pfs\_configuration.dump.storage.use\_dynamic\_provisioning to
false. Then, create a PV manually and set
pfs\_configuration.dump.storage.existing\_pvc\_name in the custom resource file to the
value of the name property of your PV.

## Creating secrets to protect sensitive configuration data

A secret is an object that contains a small amount of sensitive data such as a password, a token,
or a key. If you set the Process Federation Server admin secret
name in pfs\_configuration.admin\_secret\_name, the operator creates this secret
automatically. However, if you want to create it manually, use the following content.

```
apiVersion: v1
kind: Secret
metadata:
  name: ibm-pfs-admin-secret
type: Opaque
data:
  ltpaPassword: <LTPA\_PASSWORD>
  sslKeyPassword: <SSL\_KEY\_PASSWORD>
```

Where

- ltpaPassword is used to set the Lightweight Third-Party Authentication (LTPA)
password.
- sslKeyPassword is used as the keystore and truststore password.
- All values under data are Base64-encoded.

## Prepare the federated data repository

1. To prepare storage for the federated data repository (Elasticsearch or OpenSearch) cluster
deployed for Process Federation Server, see Preparing storage for a federated data repository. 
If you prefer, you can also use your own external federated data repository. See Referencing your own federated data repository for Business Automation Workflow on containers.Note: Linux on IBM® Z must use an external
federated data repository.
2. To set up SCC for the federated data repository, see Setting up the security context constraint for a federated data repository.