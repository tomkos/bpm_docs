# Scripting tools for managing process applications

The wsadmin scripting program and the PAL MBean provide
the same function; each wsadmin command has a corresponding method
on the MBean. The decision to use one or the other depends on your
preference and on the security configured for your environment. In
an environment with multiple security domains configured, consider
using MBean administrative tasks instead of wsadmin tasks.

- Administrative commands (AdminTasks)

 Traditional: 
The wsadmin scripting program is a powerful, non-graphical command interpreter environment that you can use to run administrative operations in a scripting language. You can use the wsadmin tool in connected mode to install, manage, and undeploy snapshots.
- The Process Application LifeCycle (PAL) MBean

 Traditional: 
The PALService managed bean (MBean) provides the same administrative scripting functionality as the wsadmin commands. In an environment with multiple security domains configured, consider using MBean administrative tasks instead of wsadmin tasks. You can also use the MBeans in other environments if you prefer to work with MBeans instead of wsadmin commands.