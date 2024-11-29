# Managing external files

Adding these files to your process application ensures that all
required assets are available and installed when your project is ready
for testing or production.

- You must have write access to the current process application
or toolkit to add external files as assets.
- To avoid class loader problems, managed files must not contain any IBM® Business Automation Workflow classes.
- The managed files must be 100 MB or less.
- The managed file names must not be longer than 64 alphanumeric characters.

When you add external assets to be managed as part of your project, you can easily use those
files in your coaches and other implementations for activities, such as services. For example, when
you add a JavaScript (.js) file to be managed as part of
your project, you can use the functions and variables within the JS file in the scripts and
scriptlets that you develop throughout your project. JS files that are included as managed files are
able to access both dynamic library JAR files and any JAR files within the managed files
themselves.

Managed files are also included in the list of options that you
can select for:

- A custom CSS when customizing the style of a particular coach
or coach component.
- The default CSS or the default XSL for all coaches in a process
application or toolkit.
- The implementation of various process components, where appropriate.

- Configuring managed asset and managed asset classloader cache sizes

Depending on the number of process applications that use managed assets and the number of files in the managed assets, you might experience slow performance when you work with managed assets. If the managed asset classloader cache, managed asset cache, or both caches are too small, the caches must be refreshed often, which decreases performance. Tune the caches by setting configuration parameters in the 100Custom.xml file to define cache sizes for managed assets.
- Adding managed files

You can add external assets such as JAR or JS files for use in a project. You can also add files for use with  coaches or to override the transform XSL for one or more heritage coaches.
- Updating or replacing managed files

You can use the designer to update or replace external files that you are using in your project.