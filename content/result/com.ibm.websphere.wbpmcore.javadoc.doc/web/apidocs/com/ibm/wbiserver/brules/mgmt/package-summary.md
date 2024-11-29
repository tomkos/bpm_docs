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

# Package com.ibm.wbiserver.brules.mgmt

- Interface Summary 

Interface
Description

BusinessRule

This interface represents a business rule, which can be either a ruleset or a 
 decision table.

BusinessRuleChangeDetector

This interface defines methods related to detecting whether or not changes have been
 made to an object or to any object that can be reached from it.

BusinessRuleGroup

An object implementing this interface represents one business rule group component in the 
 server.

BusinessRuleValidateable

This interface defines methods related to validating an object and any objects that can
 be reached from it.

Constraint

This is the base interface for all parameter value constraints.

EnumerationConstraint

This interface represents an enumeration constraint.

EnumerationItem

This interface represents a single valid value in an enumeration constraint.

Operation

An object implementing this interface represents an operation of a business rule group.

OperationSelectionRecord

This interface represents one selection record associated with an operation.

OperationSelectionRecordList

This interface represents a list of operation selection records.

Parameter

This interface represents one template parameter.

ParameterValue

This interface represents the value for one template parameter.

Property

This interface represents one property associated with some element of the API.

PropertyList

This interface represents a list of properties.

RangeConstraint

This interface represents a range constraint on a value.

Rule

This interface represents one rule within either a ruleset or a decision table.

RuleTemplate

This interface represents a rule template.

SystemDefinedProperty

This interface represents a system-defined property.

Template

This is the base interface for all templates.

TemplateInstanceRule

This interface represents a rule within either a ruleset or a decision table that is based on 
 a rule template.

UserDefinedProperty

This interface represents a user-defined property.
- Class Summary 

Class
Description

BusinessRuleManager

This class is the starting point for accessing information about business rules that are installed
 and available on the WPS server.

UnmodifiableIterator<E>

This class implements an unmodifiable iterator based on another iterator.
- Enum Summary 

Enum
Description

BusinessRuleType

An enum used to identify the type of a business rule.

Orientation

An enum used to identify the orientation of a tree condition.

ParameterDataType

Enum defining the possible data types for a parameter.

PresentationTimezone

Contains the possible values for the presentation time zone field of a business rule group.
- Exception Summary 

Exception
Description

BusinessRuleManagementException

This exception serves two purposes:
 
 It serves as the base class for all exceptions thrown by the business rule management API.

ChangeConflictException

This exception is thrown when the client attempts to publish changes but the underlying persistent
 data has been changed by another client since the data was originally retrieved by this client.

ChangesNotAllowedException

This is a RuntimeException that is thrown when a set method is called at a time
 when changes are temporarily not allowed.

DisplayNameNotChangeableException

This is a RuntimeException that is thrown when an attempt is made to change the
 display name of an object but changes are not allowed because the display name is
 synchronized to the name for that object.

SystemPropertyNotChangeableException

This is a RuntimeException that is thrown when an attempt is made to change the
 value of a system property.

ValidationException

This exception is thrown when a validation error is detected when data is being changed.

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