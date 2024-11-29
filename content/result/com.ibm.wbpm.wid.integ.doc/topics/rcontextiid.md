<!-- image -->

# Input

<!-- image -->

Here is an image of the input node's details page properties:

<!-- image -->

- Correlation context specifies the business object that is persisted through the duration
of the request and response flows. The correlation context is specified in the input node in the
request flow and is used for passing values from the request flow to the response flow. Click
Browse to select a business object, or Reset to clear the field.
- Transient context specifies the business object that is available for the duration of the
current flow (either the request flow or the response flow). The transient context is specified in
the input node in the request flow, and is used to pass values between mediation primitives in the
same flow. Click Browse to select a business object, or Reset to clear the field.
- Shared Context specifies the business object to be used during aggregation operations
using the Fan Out / Fan In combination. It is specified in the input node of the request flow and is
not intended for general data storage. Click Browse to select a business object, or
Reset to clear the field.