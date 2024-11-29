<!-- image -->

# Integration Designer artifacts
managed in source control

After a module is built, Integration Designer generates Java™ code for the authored artifacts
during the deployment process. Generated artifacts are usually Java classes based on the logic
defined in the authored BPM artifacts.

Since the staging modules
define the Java EE dependencies and optional web content, they generally
do not need to be modified or kept in source control.

| Artifacts                                                                                                                                                                       | File names                                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Assembly artifacts                                                                                                                                                              | .component, .module, .modulex, .import, .export, ibm-deploy.scaj2ee, sca.module.attributes, sca.library.attributes, sca.library          |
| Eclipse metadata                                                                                                                                                                | .settings folder, MANIFEST.MF, .classpath, .project                                                                                      |
| Business object maps                                                                                                                                                            | :map, .xsl, .xsl.smap                                                                                                                    |
| Business processes                                                                                                                                                              | .bpel, .bpelex, ProcNameArtifacts.wsdl                                                                                                   |
| Business rules                                                                                                                                                                  | .brg, .brgt.ruleset                                                                                                                      |
| Business state machines: (Note that the underlying .bpel file for the state machine is generated during application installation, and therefore not managed in source control.) | .sacl, .saclex                                                                                                                           |
| Data types (business objects)                                                                                                                                                   | .xsd                                                                                                                                     |
| Human tasks                                                                                                                                                                     | .tel, .itel (inline task only)                                                                                                           |
| Interface maps                                                                                                                                                                  | .ifm                                                                                                                                     |
| Interfaces                                                                                                                                                                      | .wsdl                                                                                                                                    |
| Mediations                                                                                                                                                                      | .medflow, .mfc, .mfcex                                                                                                                   |
| Relationships                                                                                                                                                                   | .rel, .rol                                                                                                                               |
| Selectors                                                                                                                                                                       | .sel, .selt                                                                                                                              |
| Solution projects                                                                                                                                                               | .project, projectSet.psf, solution.graphml                                                                                               |
| Visual snippets                                                                                                                                                                 | You can choose to manage the deployment of the generated .java files, in which case they should be stored in your source control system. |

## Files that should not be placed in source control

- ModuleBaseNameApp
- ModuleBaseNameWeb

In general, it is not advisable to add authored content
to a staging module. Do not add custom content, such as HTML or JSP
pages, to the web staging module. To avoid confusion, create a separate
web module for any custom web content, rather than rely on the ModuleBaseNameweb
staging module.

Do not keep the Eclipse metadata .runtime file
in source control. It can cause the migration wizard to fail.

- Physical Resources view: The .settings folder

You could find unexpected changes in a module or library due to changes in the .settings folder.