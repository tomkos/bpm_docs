# Prepare your projects for the move to containers

To prepare your project for a container runtime environment and reduce the number of
incompatibilities and critical validation errors, you can take the following steps in advance:

- For process apps and toolkits:
    - Move your process apps and toolkits from desktop Process Designer to web Process Designer. As part of this move, you must convert
deprecated artifacts from desktop Process Designer to
web Process Designer. You can continue to run your
applications in the traditional environment and you don't have to make these changes later when you
move to containers. See Deprecated and removed features of IBM Business Automation Workflow.
    - Replace deprecated APIs in your applications.
    - Upgrade to the latest version of the system toolkits. Switch to container compatible versions of
system toolkits, if available. See System toolkits.
    - Refactor applications to externalize any custom J2EE or Java applications as separate services
that run in their own container.
- For case solutions:

- Remove all deprecated features.
- Remove Case Forms.
- Ensure that all custom Content Platform Engine (CPE) event
handlers will work in Content Platform Engine in a container environment.
- Ensure that all custom IBM® Content
Navigator
plug-ins  work in IBM Content
Navigator in a
container environment.For detailed steps for the Content Platform Engine and IBM Content
Navigator, see Moving an existing P8 domain to containers.

The target runtime environment for existing process apps, toolkits and case solutions is
traditional. You need to convert the target environment before you can install these projects to a
workflow server in a container. Consider completing your move in stages. You can convert the target
installation environment of your projects (and contained artifacts) to Traditional or
Container and continue to run them in the traditional runtime environment. Then, when
you're ready, you can switch them over to run in the container environment.

After you move your applications to run in a container, you might still have applications that
are running in a traditional environment and you might need to support both streams. You can use
branches to manage both streams. For example, you can create a branch for your traditional
application before you convert and keep the current branch for the application that is running in
the container. By separating the traditional and container branches, you can make fixes and
enhancements to either branch as required. See Working with projects.