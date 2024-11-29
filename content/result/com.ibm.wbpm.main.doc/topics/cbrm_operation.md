<!-- image -->

# Operation

For each operation, there are different targets, each of which is a business rule (rule set or
decision table):

- Default target (optional)
- List of targets scheduled by date/time ranges (OperationSelectionRecord)
- List of all available targets that can be used for that operation

Each operation must have at least one business rule target specified. This target can be an
OperationSelectionRecord with a specific start date and end date when the target should be scheduled
to be active. The operation can also have a single default target set which is used during execution
when no matching scheduled business rule target is found. The Operation class provides methods for
retrieving and setting the default business rule target as well as retrieving the list
(OperationSelectionRecordList) of scheduled business rule targets. Besides the default business rule
target and the scheduled business rule targets, there is a list of all available business rule
targets for the operation. This list will include those business rules targets which are scheduled
and the default business rule target as well as any other rule sets or decision tables which are not
scheduled for this operation. An unscheduled rule set or decision table is associated with the
operation through the available target list by the fact that it implicitly shares the operation
information. All business rule targets must support the input and output messages for their
operation. With each operation unique on an interface, the rule sets and decision tables for an
operation are unique from those rule sets and decision tables of another operation.

Any of the different rule sets and decision tables in the available targets list can be
scheduled to be active through the creation of an OperationSelectionRecord. Along with the
particular rule set or decision table from the available targets list, a start date and end date
must be specified. The start date must be before the end date. The dates can be for a time which
covers the current date as well as the past and the future. The time span of the dates cannot
overlap with any other OperationSelectionRecords once it is added to the
OperationSelectionRecordList and published. The start date and end date values are of type
java.util.Date. Any values which are specified will be treated as UTC values according to the
java.util.Date class. With the OperationSelectionRecord complete, it can be added to the
OperationSelectionRecordList to be scheduled along with other business rule targets. Gaps may exist
between the time spans of different OperationSelectionRecords. When a gap is encountered during
execution, the default target is used. If no default target has been specified, an exception will be
thrown. It is recommended to always specify a default business rule target.

A scheduled business rule target can be removed from the list of scheduled targets by removing
the OperationSelectionRecord from the OperationSelectionRecordList. Removing an
OperationSelectionRecord will not remove the business rule target from the list of available
business rule targets and it will not remove any other OperationSelectionRecords which have the same
business rule target scheduled.

Besides retrieving a rule set or decision table through the OperationSelectionRecordList or list
of available targets, the Operation class also allows for business rule targets to be retrieved by
name and target namespace property values. Through the methods on the Operation class, those rule
sets and decision tables which are listed in the available targets for that operation can be
queried. Rule sets and decision tables which might have matching name and target namespace values,
but are part of the available target lists of other operations, will not be included in the result
set. As a convenience, the getBusinessRulesByName, getBusinessRulesByTNS, and
getBusinessRulesByTNSAndName methods are provided to simplify retrieving specific rule sets and
decision tables.

The Operation class provides methods that support the following:

- Retrieve the operation name
- Retrieve the operation description
- Retrieve and set the default business rule target
- Retrieve the scheduled business rule targets (OperationSelectionRecordList)
- Retrieve the list of all available business rule targets
- Retrieve a rule set or decision table from the list of all available targets by name or target
namespace
- Retrieve the business rule group with which the operation is associated

The OperationSelectionRecordList class provides methods that support the following:

- Retrieve a specific OperationSelectionRecord by index value
- Remove a specific OperationSelectionRecord by index value
- Add a new OperationSelectionRecord to the list

The OperationSelectionRecord class provides methods that support the following:

- Retrieve and set the start date
- Retrieve and set the end date
- Retrieve and set the business rule target
- Retrieve the operation with which the OperationSelectionRecord is associated

Figure 1. Class diagram for Operation and related classes

<!-- image -->