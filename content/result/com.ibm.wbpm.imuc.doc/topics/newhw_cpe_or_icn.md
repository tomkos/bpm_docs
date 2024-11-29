# Reconfiguring IBM Business Automation Workflow with an existing
external Content Platform Engine or an
external IBM Content
Navigator

## About this task

## Procedure

1 If IBM Business Automation Workflow wasconfigured with an external Content Platform Engine before migrating, performthe actions described in Configuring an existing external Content Platform Engine with these differences:
    - Because the object stores already exist, skip the steps to create the object stores.
    - Because you are not "Reassigning the BPM document store" scenario, use the value
NEW\_EXTERNAL\_OBJECT\_STORE for the -ecmEnvironment parameter in
the setBPMExternalECM command.
    - If you want to reuse the BPM content object store, specify the
-omitBPMContentStoreValidation parameter to true to omit the
check for an existing BPM content object store.
2. If IBM Business Automation Workflow was
configured with an external IBM Content
Navigator before
migrating, perform Configuring IBM Business Automation Workflow with an external IBM Content Navigator.