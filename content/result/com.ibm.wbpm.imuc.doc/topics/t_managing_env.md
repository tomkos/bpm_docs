# Managing deployment environments

- Creating a new deployment environment based on an existing configuration

You can export the configuration properties from an existing deployment environment, modify the properties with the IBM Business Automation Workflow Configuration editor, and then create another deployment environment on a different IBM Business Automation Workflow installation that is similar to the exported deployment environment (a clone with modifications).
- Exporting configuration properties for comparison

You can export the configuration properties from two different deployment environments and compare them, using your own comparison tools, to understand the difference between two IBM Business Automation Workflow systems. You can also compare against V8.5.5 configurations, but you must take into account that the more recent version extracts more properties than the previous version.
- Extending and modifying a network deployment environment

You can adjust a network deployment environment to meet your current needs, including adding managed nodes and cluster members or removing managed nodes. To move a managed node to new hardware, first add a new managed node on the new computer and then remove the previous managed node from the old computer before disposing of it.
- Adding a network deployment environment

You can add multiple independent deployment environments for your applications in the same cell. However, you can add only one Workflow Center-based deployment environment in a single cell.