<!-- image -->

# Nested aggregation

## Design the aggregation

The ordering system only accepts a single record, whereas the input into the mediation module is
a nested batch message. This introduces the need for aggregation, and in this case nested
aggregation, because the batch request message is repeated on an outlet basis, and then repeated on
an order basis. Orders are sent individually; the response from each order is stored into a single
response message, which can be aggregated later. This single response message shows the status of
all the elements in the batch request. To explore how this basic scenario is built, first examine
the business objects used, as shown in Figure 1
.

Figure 1. Business objects for batch order example

<!-- image -->

Figure 2. Result of batched order example

<!-- image -->

## Shared context

Figure 3. Aggregation levels

<!-- image -->

- Aggregate on an Outlet basis.
    - Aggregate on an Order basis.
        - Call the Order service.
        - Store the current Order service within the current Outlet response.
- Repeat for each Order associated with the Outlet.
- Store the current Outlet in the company-wide aggregation store.
- Repeat for each Outlet.
- Convert all results into a response message.

Figure 4. Shared outlet responses

<!-- image -->

## The flow detail

- Company-wide scope
- Outlet or Store scope
- Order scope

Figure 5. Aggregation block

<!-- image -->