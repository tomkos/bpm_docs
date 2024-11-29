- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Package
- Next Package

- Frames
- No Frames

- All Classes

# Package com.ibm.wbiserver.brules.mgmt.problem

- Class Summary 

Class
Description

Problem

This class represents one problem found during validation.

ProblemBusRuleNotInAvailTargetList

Problem class representing the error that the specified business rule is not in the
 available targets list.

ProblemCaseEdgeChildNodeMissing

Problem class representing the error that the case edge has no child node.

ProblemCaseEdgesAreMissing

A ConditionNode has no case edges.

ProblemCaseEdgeValueDefinitionMissing

Problem class representing the error that the case edge has no value definition.

ProblemDuplicatePropertyName

Problem class representing the error that a new property is being defined with the same
 name as an existing property on the specified entity.

ProblemInvalidActionValueTemplate

Problem class representing the error that the action value template being used to define
 the value for an action is not available to that action, i.e. it is not associated with
 the TreeActionTermDefinition for the action.

ProblemInvalidAttemptToSetValueTemplateInstance

Problem class representing the error that an attempt was made to set the value template
 instance of a part of a decision table when that part currently does not contains a value
 template instance.

ProblemInvalidBooleanValue

Problem class representing the error that the specified string value is not a valid value
 for a boolean parameter.

ProblemInvalidConditionValueTemplate

Problem class representing one of the following errors:
 
 The condition value template for a new condition value is not associated with the 
 condition term definition for the condition node to which the condition value is being 
 added.

ProblemNoTemplatesAvailableForNewActionNodes

This exception is thrown when calling
 ConditionNode.addConditionValueToThisLevel() if there are no
 available templates that can be used to fill in the newly-created empty
 ActionNodes.

ProblemOperationContainsNoTargets

This class represents a validation error where an operation has no default business rule 
 target and also has no business rule targets qualified by date ranges.

ProblemOverlappingRanges

This class represents a validation error where two operation selection records have 
 overlapping date ranges.

ProblemParmNotDefinedInTemplate

Problem class representing the error that a parameter value was specified for a parameter
 that is not defined on the template for which an instance is being created.

ProblemParmValueListContainsUnexpectedValue

Problem class representing the error that a parameter value was specified that does not
 correspond to any parameter on the specified template.

ProblemRootNodeIsMissing

Problem class representing the error that the tree block has no root node.

ProblemRuleBlockContainsNoRules

Problem class representing the error that the rule block contains no rules.

ProblemRuleNameAlreadyInUse

Problem class representing the error that the name of the new rule being added to the
 rule block is already in use for another rule in that rule block.

ProblemStartDateAfterEndDate

Problem class representing the error that the start date is after the end date.

ProblemTargetBusRuleNotSet

Problem class representing the error that the target business rule is not set for the
 specified operation selection record.

ProblemTemplateNotAssociatedWithRuleSet

Problem class representing the error that the template associated with the specified rule
 is not associated with the ruleset to which the rule is being added.

ProblemTemplateParameterNotSpecified

Problem class representing the error that a value was not specified for a template 
 parameter.

ProblemTNSAndNameAlreadyInUse

Problem class representing the error that the target name space and name specified for the
 new ruleset or decision table is already in use.

ProblemTreeActionTermIsMissing

Problem class representing the error that the tree block is missing a tree
 action term.

ProblemTreeConditionIsMissing

Problem class representing the error that the tree block is missing a tree
 condition term.

ProblemTypeConversionError

Problem class representing the error that the specified string value could not be
 converted to the data type of the specified parameter.

ProblemValueTemplateInstanceIsMissing

This problem occurs when a tree action should have a value template instance,
 but doesn't.

ProblemValueViolatesParmConstraints

Problem class representing the error that the specified value violates the constraints
 defined on the specified parameter.

ProblemWrongNumberOfParameterValues

Problem class representing the error that the number of parameter values specified does
 not equal the number of parameters.

ProblemWrongOperationForOpSelectionRecord

This class represents a validation error where an attempt was made to add an operation 
 selection record to an operation selection record list but the operation associated with 
 the selection record is not the same as the operation containing the operation selection 
 record list.
- Enum Summary 

Enum
Description

ValidationError

An enum used to identify validation errors that are detected.

- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Package
- Next Package

- Frames
- No Frames

- All Classes