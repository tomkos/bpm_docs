<!-- image -->

# Transactional behavior of BPEL processes

- Transactional behavior of microflows

Microflows are short-lived BPEL processes. They can run either in a transaction, or in an activity session as specified on the SCA component of the microflow. Microflows that are executed as part of a transaction are explained here.
- Transactional behavior of long-running BPEL processes

A long-running BPEL process spans multiple transactions. Each transaction is triggered either by a Java™ Messaging Service (JMS) message or by a work-manager-based implementation.