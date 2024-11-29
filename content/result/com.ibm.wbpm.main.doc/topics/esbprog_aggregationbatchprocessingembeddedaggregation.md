<!-- image -->

# Batch processing requiring embedded aggregation

The scenario is a personnel-based application that creates payslip information for specific
employees. The back-end service is represented by a Callout node and requires full employee records,
rather than the employee IDs, which arrive at the mediation flow. These employee records are created
by the mediation from two sources, an HR system and a Payroll system. The former stores information
concerning the employee's name, address, and vacation entitlement, while the latter contains
information regarding salary and department.

## Design the aggregation

Figure 1. Flow input and output

<!-- image -->

Figure 2. HR and Payroll Record

<!-- image -->

Figure 3. The inner and outer flow

<!-- image -->

Figure 4. EmployeeRecord array

<!-- image -->

Figure 5. PayslipStatus object

<!-- image -->