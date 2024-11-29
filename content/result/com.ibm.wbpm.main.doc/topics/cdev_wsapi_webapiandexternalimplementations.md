# Web API and external implementations (deprecated)

You can use external implementations to create your own implementation
of a service that is invoked as part of the process. When you do this,
you have access to the process context and this access is provided
by the web API.

When a process instance reaches a step handled by an external implementation,
the process server does not invoke the custom application. Instead,
after passing all necessary process data to the custom application,
the process server ceases its work on the process instance. When the
custom application completes, the process server resumes its work
on the process instance, using any updated process data received from
the custom application.