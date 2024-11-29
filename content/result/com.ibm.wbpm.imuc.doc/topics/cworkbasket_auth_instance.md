<!-- image -->

# Instance-based authorization roles for work baskets and business
categories

In addition, when a work basket is defined in Business Space, task
roles can also be defined for the tasks that are assigned to the work
basket.

## Instance-based roles for work baskets

| Role               | Authorized actions                                                                                          |
|--------------------|-------------------------------------------------------------------------------------------------------------|
| Reader             | Members of this role can view the work basket settings.                                                     |
| Opener             | Members of this role can open the work basket and view its tasks.                                           |
| Distributor        | Members of this role can distribute tasks from this work basket to one of its defined distribution targets. |
| Transfer initiator | Members of this role can transfer tasks out of the work basket.                                             |
| Appender           | Members of this role can add tasks to the work basket.                                                      |

| Work basket role     | Extends this task role   | Authorized actions                                                                                                                  |
|----------------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Task reader          | Reader                   | Members of this role can view the properties of the tasks in the work basket, but they cannot work on them.                         |
| Task editor          | Editor                   | Members of this role can work with the content of a task, but cannot claim or complete it.                                          |
| Task potential owner | Potential owner          | Members of this role can claim a task. If a potential owner is specified, then all users are considered to be members of this role. |
| Task administrator   | Administrator            | Members of this role can administer the tasks in the work basket.                                                                   |

## Instance-base role for business categories

| Role   | Authorized actions                                            |
|--------|---------------------------------------------------------------|
| Reader | Members of this role can view the business category settings. |