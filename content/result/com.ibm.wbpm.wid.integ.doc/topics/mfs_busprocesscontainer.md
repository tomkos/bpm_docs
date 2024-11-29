<!-- image -->

# Integrating IMS MFS applications
in BPEL processes

BPEL is an industry standard for specifying actions within business
processes with web services. BPEL provides means to formally specify
business processes and interaction protocols. A BPEL process implements
a potentially long-running service through the use of more elementary
services.

- Operations and iterations of a conversation

For conversational IMS MFS applications to participate in BPEL processes, create an operation for each iteration in the conversation. The conversation ID (convID) must be passed to subsequent iterations. The last iteration must end the conversation if the conversation is not ended by the application.
- Custom mediation and transformations

For IMS MFS applications, you must add custom mediation code and context objects to set the convID and convEnded values and to store contextual information for some of the operations.
- Generating MFS SCA services

For an MFS application to be a service that business integration developer can integrate into a BPEL process in IBM Integration Designer, you must generate an MFS SCA service.
- Creating a mediation flow

To create a mediation flow, create an operation for each iteration in the conversation. Include the convID and convEnded information in the input and output for each operation, and add custom mediation code to retrieve the convID and convEnded information from the context.