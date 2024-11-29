# Converting case types from IBM Business Process Manager V8.5.5

## About this task

- Upgrading case types: Adding data change management to details UIs

Client-side human services for case details UIs that are created in Business Automation Workflow V8.5.6 contain a data change event handler. This event handler manages both the local and remote changes to data in the UI. After converting case types from V8.5.5 to a processes, you can add the event handler.
- Upgrading case types: Adding a case folder variable

Case types that are created in versions of Business Automation Workflow later than V8.5.5 automatically contain a system-generated private shared variable. This variable is a shared business object that mirrors the collection of properties for the case type definition. After you convert case types created in earlier versions of Business Automation Workflow to processes, you can add a folder variable to the process.