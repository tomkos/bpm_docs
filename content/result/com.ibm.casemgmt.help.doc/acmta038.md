# Cannot copy solutions that contain rule steps in a production
environment

## Symptoms

In a production environment, you try to copy a solution that contains a workflow with a rule step
by using the  Case administration client and
you receive an error message such as the following message:

The
original solution could not be validated. See the following error:
FNRPA0276e: The XPDL document for the original solution could not
be validated because of the following error: SM032\_T1:Rule Step1:[ERROR]
Definition not found for Queue: "ICM\_RuleOperations". (ICM\_RuleOperations)
SM032\_T1:Rule Step1:[ERROR] Execute instruction uses operation, executeRule,
which is not defined for queue ICM\_RuleOperations.

## Causes

## Resolving the problem