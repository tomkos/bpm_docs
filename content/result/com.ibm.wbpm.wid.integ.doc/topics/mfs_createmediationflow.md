<!-- image -->

# Creating a mediation flow

## About this task

## Procedure

1. Use the convID property to identify the conversation from
iteration to iteration.
2. Use the convEnded property to identify if the conversation
has ended by the IMS application
before the last iteration.
3. To include convID or convEnded information with the input
or output, create new data types (business objects) from the data
types that were generated for this MFS service, with added fields
to hold the convID or convEnded information.
4. Create an operation for each iteration in your conversation.
These operations must implement the interface you created for the
mediation flow, with the input and output mapped to the appropriate
data types that you created to hold the convID or convEnded information.
5. Select the Operation Map as the mediation flow template.
6. Use Transient Context to store information in a request
and response flow of an iteration, such as the business graph information.
7. Use Correlation Context to store information across a request
and response flow of an interation, such as the convID.
8. Add custom mediation code to retrieve the convID or convEnded
information from the context, based on the JCA interactions specification.
9. Add custom mediation code to end the conversation in the
last iteration by setting the interaction verb to 3 (SYNC\_END\_CONVERSATION).