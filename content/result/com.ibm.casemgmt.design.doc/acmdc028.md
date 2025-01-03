# Creating and distributing solution templates

## About this task

At a minimum, a solution template must contain a solution definition file, which you create using
Case Builder. You create the
template in the Business Automation Workflow development domain or source environment, and then distribute it to be used at a different
development domain or target environment. You do not modify a solution template directly, you modify
the solution that you create from a solution template. You use the Case administration client to
move the case management solution template between environments.

You
can also distribute other types of assets:

- Other FileNet® P8 assets,
which are associated with the solution but managed by other FileNet P8 tools. These assets must
be migrated and deployed through FileNet Deployment
Manager and Process Configuration
Console.
- Other IBM® and external assets, which are developed outside
of Business Automation Workflow and
FileNet P8. Manual changes are
required to migrate and deploy these types of assets.

- Converting a solution into a template

You can convert a solution into a template. You use templates to quickly create new solutions that are based on the same design. The template contains all the solution design information and assets, but you cannot edit the template directly or create running cases from it.
- Distributing solutions as templates

Use the Case administration client to distribute solution templates to your customers for further development and customization.