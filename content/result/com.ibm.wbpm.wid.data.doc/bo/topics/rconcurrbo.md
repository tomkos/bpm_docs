<!-- image -->

# Concurrent access for business objects

- POJO: When you create POJO components, do not create static
or singleton references to a business object instance, as this practice
can potentially lead to sharing the same reference in multiple threads.
- Asynchronous Beans: When using asynchronous beans programming,
do not pass the same instance of a business object to multiple asynchronous
bean instances. This would lead to business object instance data being
processed in different threads at the same time.