# Customizing context roots for the components in a deployment
environment

After you create a deployment environment, you
can customize the context root for all components in the environment
by using the BPMConfig script to add a prefix.
You can also customize the Heritage Process Portal context
root by adding a prefix that is specific to this component only.

Before
you create a deployment environment, you can also customize the context
roots by setting the context root properties in the BPMConfig properties
file that defines the configuration for that deployment environment.

## About this task

## Procedure

To customize the context roots in an existing deployment
environment, complete the following steps:

1. Stop all running servers in the deployment environment.
2. In a command-line environment, change to the directory
where the BPMConfig script is located on the deployment
manager node. For example:cd install\_root/bin
3 Run the script by using the following syntax: BPMConfig -update -profile profile\_name [-deDE\_name ] [-component component\_name ] -contextRootPrefixprefix where:-profile Specifies the deployment manager profile name. -de Specifies the name of the deployment environment to which the context root changes apply. Allthe components in the deployment environment will be configured with the changes.If there is onlyone deployment environment in the WebSphere cell, you can omit the -de option. -component Specifies a component for which a context root prefix can be set. The valid values areProcessPortal , CaseManager , and ContentNavigator . If you omit the -component option, the contextroot is updated for all components in the deployment environment. -contextRootPrefix Specifies the context root prefix that you want to set. This value requires a leading forwardslash (/). The specified prefix is added to the beginning of the default context root. If youspecify a leading forward slash (/) by itself, the -contextRootPrefix optionwill revert any customized context root back to the Business Automation Workflow default context root.Important: If you update the value of -contextRootPrefix , you must changeany hard-coded URLs in your existing applications. Examples:

BPMConfig -update -profile profile\_name [-de
DE\_name] [-component component\_name] -contextRootPrefix
prefix

If there is only
one deployment environment in the WebSphere cell, you can omit the -de
option.

    - To add a prefix of de\_prefix to the default context
root values for all components that are configured in the P1SR01 deployment
environment, enter the following command: ./BPMConfig
-update -profile DmgrProfile -de P1SR01 -contextRootPrefix /de\_prefix
    - To add a prefix of myportal to the default value
of the context root for the Heritage Process Portal component
in the P1SR01 deployment environment, enter the following
command:./BPMConfig -update -profile DmgrProfile -de
P1SR01 -component ProcessPortal -contextRootPrefix /myportal
    - To set a Heritage Process Portal context
root prefix (myportal), which is different from the
prefix (de\_prefix) that is used by the other components
in the P1SR01 deployment environment, run the following
commands in sequence:./BPMConfig -update -profile DmgrProfile
-de P1SR01 -contextRootPrefix /de\_prefix
./BPMConfig
-update -profile DmgrProfile -de P1SR01 -component ProcessPortal -contextRootPrefix
/myportal
4. Review the install\_root/logs/config/BPMConfig\_timestamp.log file
on the deployment manager node to confirm there were no errors.
5. Run the syncNode command on each node to obtain the latest configuration
file changes.

## Results

## What to do next

Update the web server plug-in. The web modules are updated
in the product applications when you run the BPMConfig -update
-contextRootPrefix command. If the product applications are
mapped to a web server, the plugin-cfg.xml file
for the web server must be updated with the new context roots. Any
web server plug-ins might need to be propagated (or generated and
propagated). For more information, see Plug-ins configuration in the WebSphere Application
Server product information.

Clear your browser cache before
you start IBM Business Automation Workflow user
interfaces.

Update your client applications to use the new custom
context root.

Any previously installed Process Designer must
be downloaded from Workflow Center and installed again because Process
Designer must use the new context root configuration.

## Related information

- syncNode command
- Configuration properties for the BPMConfig command