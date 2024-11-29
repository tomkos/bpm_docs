# Transaction log file

- Started transactions will neither be rolled back nor committed
- Artifacts will remain in the Java™ Virtual
Machine (JVM) since they are referenced or allocated by a transaction
but never garbage collected
- Database content (amongst others navigation state
of long running BPEL processes) remains in the Business Process  Choreographer
related tables and are never deleted
- Navigation messages of the Business Process Engine
(BPE) of long running processes are never processed further
- Service Component Architecture (SCA) messages that belong to a
process navigation and transaction remain on SCA-related queues

Deleting the transaction log from a development environment causes
the same problems. Because you can re-create business processes, deleting
the files from a test environment is not as damaging as deleting them
from a production environment.