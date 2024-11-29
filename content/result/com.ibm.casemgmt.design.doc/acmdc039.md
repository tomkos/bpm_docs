# Solution assets

A solution definition refers to the solution assets as defined in the design object
store. A solution package, which is created when you export the solution, refers to the
archive file of the solution.

## Solution Document Generator tool (deprecated)

When you migrate your solutions from one environment to another, ensure that you migrate all of
the assets that are associated with your solution. You can generate documentation about the workflow
solution assets by running a command-line tool, the Creating a solution description document.

In Case Builder, the solution
designer can capture requirements directly into this tool. You can then generate a document that
presents the organization of the solution and its contents in an easy-to-read format. This solution
description document provides a way to communicate and share the configuration details of the
solution for review, discussion, and analysis.

## Solution Document Generator tool (deprecated)

When you migrate your solutions from one environment to another, ensure that you migrate all of
the assets that are associated with your solution. You can generate documentation about the workflow
solution assets by running a command-line tool, the Creating a solution description document.

In Case Builder, the solution
designer can capture requirements directly into this tool. You can then generate a document that
presents the organization of the solution and its contents in an easy-to-read format. This solution
description document provides a way to communicate and share the configuration details of the
solution for review, discussion, and analysis.

## Workflow assets

The development environment is typically in a dedicated
IBM
FileNet® P8 domain and includes a
design object store in which solutions are stored. Each time that you edit and save the solution in
Case Builder, a new version of the
assets is created. All of the versions of the assets are saved in the design object store, and each
version of the assets has a unique ID. When you deploy a solution, the latest version of the
solution assets is deployed with the solution.

When you export a solution by using the
Case administration client, the following
solution assets are included in the solution package.

| Solution asset                             | Defined by using               | Resides in          | Migration tool                                      | Deployment tool                                                   |
|--------------------------------------------|--------------------------------|---------------------|-----------------------------------------------------|-------------------------------------------------------------------|
| Solution definition file                   | Case Builder                   | Design object store | Case administration client, Case configuration tool | Case administration client, Case configuration tool, Case Builder |
| Content Platform Engine configuration file | Case Builder, Process Designer | Design object store | Case administration client, Case configuration tool | Case administration client, Case configuration tool, Case Builder |
| Solution workflow collection               | Case Builder, Process Designer | Design object store | Case administration client, Case configuration tool | Case administration client, Case configuration tool, Case Builder |
| Task workflows                             | Case Builder, Process Designer | Design object store | Case administration client, Case configuration tool | Case administration client, Case configuration tool, Case Builder |
| Pages                                      | Case Builder                   | Design object store | Case administration client, Case configuration tool | Case administration client, Case configuration tool, Case Builder |
| Business rules                             | Case Builder                   | Design object store | Case administration client, Case configuration tool | Case administration client, Case configuration tool, Case Builder |
| Case instance security                     | Case administration client     | Design object store | Case administration client                          | Case administration client                                        |
| Case history audit configuration           | Case administration client     | Design object store | Case administration client                          | Case administration client                                        |