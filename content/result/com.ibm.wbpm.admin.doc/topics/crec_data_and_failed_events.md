# Failed-event locations: Where does the data go?

By adhering to guidelines and preventive measures described in Planning
error prevention and recovery, all business events and associated
data will reliably accumulate in one of these locations.

If you do not adhere to sound architectural and application development
practices, then a percentage of inflight events may end up in an inconsistent
state, from which recovery cannot be attained. Under such circumstances,
(presumably identified during testing cycles) post recovery investigation
and clean up is necessary to correct the issue so that future recovery
activities are completely successful.

In order to accurately describe the following scenarios, it is
important to put the information in the context of a use case.

- Use case: recovering data from failed events

A use case provides a context for a recovery scenario. In the use case, a business has an application that receives a request to create a new Account.