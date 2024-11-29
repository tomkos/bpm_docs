# Preparing storage for a federated data repository

Containers: 
Prepare
storage for the federated data repository (Elasticsearch or OpenSearch) for Process Federation Server.

## Procedure

- Option 1: If your environment supports dynamic provisioning:Enable dynamic provisioning
for storage by setting elasticsearch\_configuration.storage.use\_dynamic\_provisioning
to true and provide the storage class name of
elasticsearch\_configuration.storage.storage\_class\_name in the custom resource
file.
For snapshot storage, set
elasticsearch\_configuration.snapshot\_storage.use\_dynamic\_provisioning to
true and provide the storage class name of
elasticsearch\_configuration.snapshot\_storage.storage\_class\_name in the custom
resource file.
- Option 2: If your environment does not support dynamic provisioning:Disable dynamic
provisioning by setting
elasticsearch\_configuration.storage.use\_dynamic\_provisioning to
false. Then, create a PV manually and set
elasticsearch\_configuration.storage.storage\_class\_name in the custom resource file
to the value of the storageClassName property of your PV.
For snapshot
storage, set elasticsearch\_configuration.snapshot\_storage.use\_dynamic\_provisioning
to false. Then, create a PV manually and set
elasticsearch\_configuration.snapshot\_storage.existing\_claim\_name in the custom
resource file to the value of the name property of your PV, and set
elasticsearch\_configuration.snapshot\_storage.storage\_class\_name to the
storageClassName property of your PV.