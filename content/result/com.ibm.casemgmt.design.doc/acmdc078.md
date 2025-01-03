# Solution application assets

Examples of solution application assets include image objects, custom rules, custom
servlets, widgets, and reporting templates. When you migrate your solutions from one environment to
another, ensure that you migrate all of the solution application assets that are associated with
your solution.

If your solution is
translated, you must migrate the translated user interface in your
case management application by exporting the translated assets from
the source domain and deploying them in the target domain. For more
information, see Migrating the translated user interface elements of your case management application.

## Other FileNet P8 assets

The
following assets are stored in Content Platform Engine or other components
that are managed by FileNet® P8 tools.

| Solution asset                                                           | Defined by using                                   | Resides in          | Migration tool                                               | Deployment tool               |
|--------------------------------------------------------------------------|----------------------------------------------------|---------------------|--------------------------------------------------------------|-------------------------------|
| Reused Content Platform Engine classes and properties                    | Administration Console for Content Platform Engine | Target object store | FileNet Deployment Manager                                   | FileNet Deployment Manager    |
| Reused queues and component queues                                       | Process Configuration Console                      | Target object store | Process Configuration Console and FileNet Deployment Manager | Process Configuration Console |
| Content Platform Engine marking sets                                     | Administration Console for Content Platform Engine | FileNet P8 domain   | FileNet Deployment Manager                                   | FileNet Deployment Manager    |
| Content Platform Engine event subscription                               | Administration Console for Content Platform Engine | Target object store | FileNet Deployment Manager                                   | FileNet Deployment Manager    |
| Content Platform Engine event code module                                | Administration Console for Content Platform Engine | Target object store | FileNet Deployment Manager                                   | FileNet Deployment Manager    |
| Content Platform Engine event workflow                                   | Process Designer                                   | Target object store | FileNet Deployment Manager                                   | FileNet Deployment Manager    |
| IBM FileNet eForms for P8 form template                                  | IBM FileNet eForms for P8 designer                 | Target object store | FileNet Deployment Manager                                   | FileNet Deployment Manager    |
| IBM Content Navigator search that is stored in the FileNet P8 repository | IBM Content Navigator                              | Target object store | FileNet Deployment Manager                                   | FileNet Deployment Manager    |

## Other IBM and
external assets

The items in this table represent assets
that are managed other IBM products
and tools, and external assets, such as custom widgets and services,
that are managed by external products and tools.

| Solution asset                                                                                  | Defined by using                                                                   | Resides in                                       | Migration tool                                                              | Deployment tool                                                                                                                                             |
|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|--------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IBM Content Navigator desktop                                                                   | IBM Content Navigator                                                              | IBM Content Navigator configuration database     | IBM Content Navigator administration tool                                   | IBM Content Navigator administration tool                                                                                                                   |
| IBM Operational Decision Manager rules project (formerly known as WebSphere® ILOG® JRules BRMS) | IBM Operational Decision Manager Rule Designer                                     | IBM Operational Decision Manager Decision Center |                                                                             |                                                                                                                                                             |
| IBM Operational Decision Manager rules application                                              | IBM Operational Decision Manager Rule Designer                                     | Application server                               |                                                                             | IBM Operational Decision Manager, Case administration client, FileNet Deployment Manager                                                                    |
| Reused  processesIBM Business Automation Workflow                                               | IBM Business Automation Workflow IBM FileNet Process Designer                      | Process center, Process server                   | Process center administration tool                                          | Process center administration tool                                                                                                                          |
| IBM Watson Explorer Analytical Components                                                       | IBM Watson Explorer Analytical Components administration console                   | File                                             | IBM Watson Explorer Analytical Components administration console            | IBM Watson Explorer Analytical Components administration console                                                                                            |
| Case Analyzer                                                                                   | Process Task Manager                                                               | OLAP database                                    | Process Task Manager                                                        | Microsoft SQL Server OLAP Services                                                                                                                          |
| External Data Service                                                                           | External tool                                                                      | External tool                                    | External tool                                                               | External tool                                                                                                                                               |
| Email templates that are checked in as documents                                                |                                                                                    | Target object store                              |                                                                             | FileNet Deployment Manager                                                                                                                                  |
| Widget: page                                                                                    | External tool such as a JavaScript editor, a Java editor, or a compression utility | Custom widgets package                           | Not applicable. Instead of migrating, you build the custom widgets package. | IBM Business Automation Workflow configuration toolFor a custom widgets package, you can also use the IBM Business Automation Workflow administration tool. |
| Widget: property editor                                                                         | External tool such as a JavaScript editor, a Java editor, or a compression utility | Extensions package                               | Not applicable. Instead of migrating, you build the extensions package.     | IBM Business Automation Workflow configuration tool                                                                                                         |
| Widget: other                                                                                   | External tool such as a JavaScript editor, a Java editor, or a compression utility | External tool                                    | External tool                                                               | External tool                                                                                                                                               |