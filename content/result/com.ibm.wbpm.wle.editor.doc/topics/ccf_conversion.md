# Conversion of deprecated functions in imported process applications
and toolkits

Business Automation Workflow provides functions that enable you
to convert deprecated coach views from artifacts that were built in earlier versions into views from
the UI toolkit.

You can convert coach views from the deprecated Coaches and Responsive Coaches toolkits into UI
views that are based on newer technologies and can be used to build applications that run on
multiple device types.

- You do not have to convert a process application or toolkit that is created in Business Automation Workflow 24.0.0.0 .
    - Build the new process application or toolkit by using only mobile-ready views from the UI
toolkit for all the new coaches and coach content.
    - Avoid mixing non-responsive or responsive deprecated coach views and UI views in the same
coach.
- Convert a process application or toolkit that you imported from an earlier version of Business Automation Workflow or an IBM® BPM version. The conversion UI is enabled for processapplications or toolkits that depend on the deprecated Coaches or Responsive Coaches toolkits, or on the Content Management toolkit . In the conversion process,you replace the deprecated coach views in all or the specified artifacts that belong to the processapplication or toolkit with UI views. Remember:

- All the view instances in the artifacts selected for conversion remain intact and
unchanged.
- All the references to deprecated coach views in the Coaches and Responsive Coaches toolkits are
converted into UI views.
- All the references to deprecated Content Management coach views are
converted into corresponding views from the same Content Management toolkit.
- Some but not all the configuration options, bindings, implemented services, and values for
responsive device settings that are defined for a converted coach view are preserved after the
conversion.

- This is a best-effort conversion that ensures that each deprecated coach
view has at least one replacement in the UI toolkit. However, the conversion does not guarantee that
the behavior, the configuration options, bindings, and some of the implemented services and
responsive device settings of the resulting UI view remain identical to those of the original coach
view. That is why it is important that you test and reconfigure the UI view as necessary to ensure
that it works as expected. For example, if the implementation of a specified service in a
deprecated coach view is not preserved after conversion, you might need to recreate the service
implementation in the corresponding UI view.
- Post-conversion configuration is also required for custom JavaScript and CSS code that refers to
elements and classes in deprecated coach views. Differences in the CSS code for views require that
you verify and reconfigure the custom CSS to ensure that the CSS is still compatible with the
converted UI views.
- If you are using or converting to the UI views, you must add a dependency on the System Data 24.0.0.0 toolkit or a toolkit or process application
that has a theme. The UI views require theme definitions. The Carbon theme in
the System Data toolkit provides these theme definitions and it is the default theme for new process
applications.

- In the toolkit dependencies structure, go to the deepest level
that has no custom toolkit dependencies and start the conversion there.
- Convert the deprecated coach views in all artifacts for each toolkit dependency, one level at a
time, and work your way up until there are no dependencies left to convert.Tip:  Other
users might have already converted some toolkits that your process application is dependent on. If a
converted version of a toolkit exists, upgrade the toolkit to that version directly.
- For each toolkit dependency, at every level, follow this process:
    1 Check - Check whether a converted version of a toolkit dependency exists:
        - If it exists, skip step 2 and update the version of your toolkit to the converted version.
        - If it does not exist, continue with steps 2 - 5.
2. Convert - Convert the deprecated coach
views in all the listed artifacts for that toolkit.
3. Test and customize - Test the results of
the conversion in the artifacts and customize where necessary. Retest
the artifacts to ensure that they work as expected.
4. Refresh- (Optional) Refresh () to make sure that there are no more artifacts and dependencies left to convert for the
current toolkit.
5. Take snapshot - Take a snapshot of the
converted toolkit.
- Move up one level and, from the dependencies listed under UI Conversion or from the library, change the dependency
version to the version of the snapshot that you took.
- At the top application level, iterate through steps 2 - 4. Then retest and update the custom
artifacts as necessary.
- (For the Coaches toolkit only) From the library, remove the application's dependency on the
toolkit.Note:  The dependency on the Content Management toolkit is automatically
upgraded.

<!-- image -->

- At the top level, the process application (PA1) has one toolkit dependency: TKT1.
- TKT1 depends on TKT2 that depends on TKT3.
- At the lowest level, TKT3 has no toolkit dependencies.
- No converted version exists for any of the specified toolkits.

1. In the toolkit dependencies structure, go to the TKT3 level.
2 Apply the conversion process starting at the TKT3 level:
    1. Convert the deprecated coach views in all the artifacts in TKT3.
    2. When the conversion is complete, test the results of the conversion in the artifacts and make
adjustments where necessary. Retest the artifacts if necessary.
    3. (Optional) Click Refresh to make sure that the list of artifacts
for TKT3 is clean and there are no more dependencies.
    4. Take a snapshot of the TKT3 toolkit that has all the artifacts and dependencies converted.
    5. Move up one level to TKT2.
    6. In the list of toolkit dependencies for TKT2, change the toolkit version for TKT3 to its
snapshot version to remove TKT3 from the list of dependencies for TKT2.
    7. From the library, right-click the dependency of TKT3 on the Coaches toolkit and remove the
dependency. Repeat this step for TKT2.
3. Iterate through the same conversion process at TKT2 level, and then repeat the conversion
process for TKT1.
4. With all the toolkit dependencies converted, at the PA1 level iterate through steps a - c. Then
retest and update the custom artifacts as necessary. PA1 and all its artifacts are suitable for use
on multiple device types.
5. From the library, right-click the dependency of PA1 on the Coaches toolkit and remove the
dependency. The dependency on the Content Management toolkit is automatically upgraded.

- Mapping deprecated functions to UI functions

Through conversion, functions that are deprecated in Business Automation Workflow 24.0.0.0 are replaced with UI functions.
- Converting deprecated coach views into UI views

 For a process application or toolkit that you import from an IBM BPM version or a Business Automation Workflow version earlier than 24.0.0.0, you might want to convert the deprecated coach views in the artifacts that belong to the process application or toolkit into UI views.