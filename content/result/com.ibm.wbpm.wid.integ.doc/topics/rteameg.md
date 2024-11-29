<!-- image -->

# Example: Team development of mediation flows

1. He creates a new mediation flow and chooses to save the mediation
flow as multiple files.
2. The source interface of the mediation flow has three operations.
Developer A implements the flow for two of the operations, callHello
and callBonjour and saves the mediation flow.
3. He selects the mediation flow in the Business Integration view,
right-clicks and selects  Show Files. The Physical
Resources view opens with the mediation flow files highlighted: There are three
operations in the source interface (callBonjour, callHello and callHola).
A .mfcflow file is created for each of these operations.
4. Developer A checks the selected files into the team repository.

1. Developer B checks the mediation flow files out of the repository.
2. She implements operation callHola and saves the flow.
3. She selects the mediation flow, right-clicks, and selects Show
Files.The
.mfcflow file for the operation callHola and the file HelloWorldMediationFlow.mfc
have changed.
4. She synchronizes the HelloWorldMediationModule project with the
repository, and checks in the changed files.