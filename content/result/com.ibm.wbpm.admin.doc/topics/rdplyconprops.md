<!-- image -->

# Connection properties specified on a server or at design time

When you use a stand-alone adapter, you specify that the import or export configuration settings
come from a Java Naming and Directory Interface (JNDI) resource instead. You can also specify that
user and password settings come from a Java Authentication and Authorization Service (JAAS) alias.
The benefit of using JNDI and JAAS resources is that an environment-specific resource that a system
administrator sets up controls the configuration settings and, therefore, you do not need to be
aware of all the environment details. The drawback is that the resources need to be configured
before deployment with the proper names to tie those resources to the application; otherwise, the
adapter might not function properly.

When you use the external service wizard with adapters that access enterprise information system
(EIS) systems, the wizard detects the connection properties. When you build your import or export
component, you can use these properties and modify the settings as needed. Because you are not using
a stand-alone adapter and a JNDI resource, the settings are related to the settings defined in the
application EAR. Whoever develops the application must set the values at design time. Because some
environments might require different settings, the developer might have to modify the adapter
configuration after each deployment.

See Changing configuration properties for embedded adapters and
Changing configuration properties for stand-alone adapters in the
Administering the adapter module section for each adapter.