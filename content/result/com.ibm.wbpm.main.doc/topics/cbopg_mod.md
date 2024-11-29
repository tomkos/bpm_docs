<!-- image -->

# Programming model

- Working with the IBM business object framework

The business object framework describes how data in the run time is modeled by applications, integrated into the run time, and represented in memory.
- Modeling business objects

Business object data that flows through the IBM Business Automation Workflow runtime is modeled using XML schemas. XML schemas are an alternative to document type definitions (DTDs) and can be used to extend functionality in the areas of data typing, inheritance, and presentation. XML schema provides a form for modeling the data types that is industry standard, widely adopted, and is platform and language neutral.
- Modeling business graphs

Business graphs relate to business objects in much the same way SDO DataGraphs relate to SDO DataObjects. When a top-level business object requires enrichment to be able to use the services provided by IBM Business Automation Workflow, it is wrapped with a business graph. The business graph wrapper provides the additional value add by adding data headers for storing information logically in memory, or physically when the business graph is serialized.
- Modeling business object type metadata

Business object type metadata can be added to business object definitions to enhance their value in the runtime environment. The business object framework allows you to design, annotate, and convert business object type metadata.

<!-- image -->