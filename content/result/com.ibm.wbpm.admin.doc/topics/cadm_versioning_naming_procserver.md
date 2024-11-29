# Naming conventions for Workflow Server deployments

- Process application name acronym
- Process application snapshot acronym

| Type of name                         | Example               |
|--------------------------------------|-----------------------|
| Process application name             | Process Application 1 |
| Process application name acronym     | PA1                   |
| Process application snapshot         | 1.0.0                 |
| Process application snapshot acronym | 1.0.0                 |

A resource, such as a module or library, has the version context
as part of its identify.

| SCA module name   | Version-aware name   | Version-aware EAR/application name   |
|-------------------|----------------------|--------------------------------------|
| M1                | PA1-1.0.0-M1         | PA1-1.0.0-M1.ear                     |
| M2                | PA1-1.0.0-M2         | PA1-1.0.0-M2.ear                     |

| SCA process-application-scoped library name   | Version-aware name   | Version-aware JAR name   |
|-----------------------------------------------|----------------------|--------------------------|
| Lib1                                          | PA1-1.0.0-Lib1       | PA1-1.0.0-Lib1.jar       |
| Lib2                                          | PA1-1.0.0-Lib2       | PA1-1.0.0-Lib2.jar       |