# Installing and updating advanced applications in the runtime environment

- Security considerations for runtime installation and deployment

Before you install a snapshot or deploy a service module in the runtime environment, consider any security requirements or restrictions associated with the snapshot, the module, or the environment.
- Versioning considerations for process applications that contain Java modules and projects

Process applications can contain custom Java EE modules and Java projects. When you co-deploy applications, the custom Java EE module for each version of the application must be unique.
- Versioning considerations for process applications that contain business rules and selectors

If you are deploying multiple versions of a process application that includes a business rule or selector component, be aware of the way that the associated metadata is used by the versions.
- Deploying an application that has an adapter binding

If your application used an adapter to get information from an enterprise information system (EIS), then your application is deployed with an adapter binding.
- Deploying service modules

After you develop and test a service module in IBM Integration Designer and are satisfied that the module is working as designed, you can deploy it into the runtime environment. Use the information in this topic to prepare for and complete a successful deployment.
- Using Ant scripts to automate builds and deployment

If you want to automate the builds and deployment of your applications, you can use Ant scripts to invoke the headless (command line) batch processing environments of either IBM® Integration Designer or IBM Workflow Server. These headless environments are used exclusively to perform batch processing of Integration Designer modules. You cannot use these headless environments to deploy modules contained in process applications or toolkits to either a IBM Workflow Center server or a process server on Workflow Center.
- Deploying BPEL process and human task applications

You can distribute Service Component Architecture (SCA) modules that contain BPEL processes or human tasks, or both, to deployment targets.