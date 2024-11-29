<!-- image -->

# JNDI names and EJB import bindings

- EJB 2.1 JavaBeansThe default JNDI name preselected by Integration Designer
is the default EJB 2.1 binding, which takes the form ejb/ plus the home
interface, separated by slashes. 
For example, for the home interface of EJB 2.1
JavaBeans for com.mycompany.myremotebusinesshome, the
default binding is:ejb/com/mycompany/myremotebusinesshome
For EJB 2.1,
only remote EJB invocation is supported.
- EJB 3.0 JavaBeansThe default JNDI name
preselected by Integration Designer for the local JNDI is the fully
qualified class name of the local interface preceded by ejblocal:. For
example, for the fully qualified interface of the local interface
com.mycompany.mylocalbusiness, the preselected EJB 3.0 JNDI is:
ejblocal:com.mycompany.mylocalbusiness
For the remote interface
com.mycompany.myremotebusiness, the preselected EJB 3.0 JNDI is the fully qualified interface:
com.mycompany.myremotebusiness
The EJB 3.0 and 3.1 default application
bindings are described inEJB 3.0 and EJB 3.1 application bindings
overview.
Integration Designer will use the "short"
name as the default JNDI location for EJBs using the version 3.0 programming model.
Note: If the
deployed JNDI reference of the target EJB is different from the default JNDI binding location
because a custom mapping was used or configured, the target JNDI name must be properly specified.
You can specify the name in Integration Designer before deployment,
or, for the import binding, you can change the name in the administrative console (after
deployment) to match the JNDI name of the target EJB.

For more information on creating EJB bindings,
see the section devoted to Working with EJB bindings in the Integration Designer information
center.