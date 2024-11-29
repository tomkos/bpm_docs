<!-- image -->

# Module deployment with the adapter or separately

- With module for use by single application: When the adapter files are
embedded in the module, you can deploy the module to any application server. Use an embedded adapter
when you have one module that uses the adapter or if multiple modules must run different versions of
the adapter. Using an embedded adapter enables you to upgrade the adapter in one module without the
risk of destabilizing other modules by changing their adapter version.
- On server for use by multiple applications: If you do not include the
adapter files in a module, you must install them as a stand-alone adapter on each application server
where you want to run the module. Use a stand-alone adapter when multiple modules can use the same
version of the adapter and you want to administer the adapter in a central location. Using a
stand-alone adapter can also reduce the resources that are required because you run only one adapter
instance for multiple modules.

An embedded adapter is bundled in an enterprise archive (EAR) file and is available only
to the application that it is packaged and deployed with. A stand-alone adapter is represented by a
stand-alone resource adapter archive (RAR) file. When deployed, it is available to all deployed
applications in the server instance.

When you create the project for your application by using
IBM® Integration
Designer, you can choose how to package the
adapter. You can either bundle the adapter with the EAR file or you can deploy the adapter as a
stand-alone RAR file. Your choice affects how the adapter is used in the runtime environment and how
the properties for the adapter are displayed on the administrative console.

Choosing either to
embed an adapter with your application or to deploy the adapter as a stand-alone module depends on
how you want to administer the adapter.

## Considerations for embedding an adapter in the application

An embedded adapter is bundled in an enterprise archive (EAR) file and is available only to the
application that it is packaged and deployed with. You are more likely to embed the adapter with the
application if you plan to run multiple versions, are concerned about potential disruptions when you
upgrade the adapter, or both. Use an embedded adapter when you have one module that uses the adapter
or if multiple modules need to run different versions of the adapter. You can administer it as one
module. With the adapter files embedded in the module, you can deploy the module to any application
server.

<!-- image -->

- You can deploy the module to any application server without more procedures that are related to
the stand-alone RAR file.
- Updating the adapter version for a new application does not affect older applications that are
deployed to the same server.
- You get class loader isolation, which means that you can have multiple versions of adapters
across EAR files that are deployed to the server. Class loader isolation prevents two similarly
named classes in different applications from interfering with each other. But a class loader affects
the packaging of applications and the behavior of packaged applications that are deployed on runtime
environments. Class loader isolation means that the adapter cannot load classes from another
application or module.
- Each application that the adapter is embedded in must be administered separately.
- You require additional JVM heap space as resources are used to load each adapter instance.
- When you must update an adapter, the related application must be updated and redeployed.

## Considerations for using a stand-alone adapter

You are more likely to deploy the adapter as a stand-alone module if you want one copy of the
adapter. In this case, you don't care about disruptions to multiple applications when you upgrade
the adapter.

<!-- image -->

- Multiple applications can refer to the same adapter instance, which saves JVM heap space and
server resources.
- Updating the stand-alone RAR instance updates the adapter for all associated applications.
Adapter upgrades are separated from an EAR update and might not require application updates.
- Stand-alone adapters have no class loader isolation. Only one version of a defined Java artifact
runs and the version and sequence of that artifact is undetermined. For example, when you use a
stand-alone adapter there is only one resource adapter version, one adapter foundation class (AFC)
version, or one third-party Java Archive (JAR) file version. All adapters that are deployed as
stand-alone adapters share one Adapter Foundation Classes (AFC) version, and all instances of a
defined adapter share the code version. All adapter instances that use a given third-party library
must share that library.
- Additional manual deployment steps are required for any EAR referencing a stand-alone adapter.
These steps can make it difficult to automate the deployment process.
- If you update any of the shared artifacts, all applications that use the artifacts are affected.
For instance, you might have an adapter that works with server version X. If you update the version
of the client application to version Y, your original application might stop working.
- AFC is compatible with previous versions, but the latest AFC version must be in every RAR file
that is deployed in a stand-alone way. For example, you might have more than one copy of a JAR file
in the class path of a configuration that uses a stand-alone adapter. The RAR file that is used is
randomly selected; therefore, each AFC must be the latest version.