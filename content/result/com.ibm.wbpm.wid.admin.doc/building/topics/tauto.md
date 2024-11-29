<!-- image -->

# Specifying build activities for builds

## Before you begin

## About this task

## Procedure

1. In the Business Integration perspective, click the Build
Activities tab. (If the Build Activities tab
is not visible, open either the Business Integration view or the Physical
Resources view and then click the Show Build Activities
View icon .) The Build Activities view opens.
2 In the Select workspace activities to run duringa build section, select one of the following activities:
    - If you only want to have your business integration projects
validated during builds, select Validate.
    - If you want to have your projects validated and also generate
deploy code for your integration modules and component test projects
during builds, select Validate and update deploy code.
This is the default selection. If deploy code has not yet been generated,
selecting this button will invoke an immediate build and the generation
of deploy code.
    - If you want to have your projects validated and generate deploy
code, plus update any integration modules or component test projects
that currently reside on running servers, select Validate,
update deploy code, and update running servers. If deploy
code has not yet been generated, selecting this button will invoke
an immediate build and the generation of deploy code, plus any integration
modules or component test projects that currently reside on running servers
will be automatically updated when the build completes.