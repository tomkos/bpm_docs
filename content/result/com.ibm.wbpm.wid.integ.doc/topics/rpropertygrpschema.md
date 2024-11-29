<!-- image -->

# Mediation primitive property group schema definition

```
<schema xmlns="http://www.w3.org/2001/XMLSchema" xmlns:propertygroup="http://www.ibm.com/propertygroup/6.0.1" targetNamespace="http://www.ibm.com/propertygroup/6.0.1">
	
	<element name="propertyGroups" type="propertygroup:BasePropertyGroups"/>
	<element name="description" type="string"/>
	
	<complexType name="PersistentFormatter">
	</complexType>
	
	<complexType name="StringFormatter">
		<complexContent>
			<extension base="propertygroup:PersistentFormatter">
				<attribute name="escapeCharacter" type="token" use="optional"/>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="StringListFormatter">
		<complexContent>
			<extension base="propertygroup:StringFormatter">
				<attribute name="separator" type="token" use="optional"/>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="StringTableFormatter">
		<complexContent>
			<extension base="propertygroup:StringFormatter">
				<attribute name="rowSeparator" type="token" use="optional"/>
				<attribute name="columnSeparator" type="token" use="optional"/>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="Qualifier">
	</complexType>
	
	<complexType name="TableColumnQualifier">
		<complexContent>
			<extension base="propertygroup:Qualifier">
				<attribute name="name" type="token" use="required"/>
				<attribute name="preferredWidth" type="token" use="required"/>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="TableLayoutQualifier">
		<complexContent>
			<extension base="propertygroup:Qualifier">
				<choice>
					<element maxOccurs="unbounded" minOccurs="0" name="column" type="propertygroup:TableColumnQualifier"/>
				</choice>
				<attribute name="preferredHeight" type="token" use="required"/>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="PropertyClassificationQualifier">
		<complexContent>
			<extension base="propertygroup:Qualifier">
				<attribute name="name" type="token" use="required"/>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="PropertyDescriptor">
		<choice>
			<element ref="propertygroup:description" minOccurs="0"/>
			<element name="persistentFormatter" type="propertygroup:PersistentFormatter" minOccurs="0"/>
			<element maxOccurs="unbounded" minOccurs="0" name="qualifier" type="propertygroup:Qualifier"/>
		</choice>
		<attribute name="id" type="token" use="optional"/>
		<attribute name="name" type="token" use="required"/>
		<attribute name="displayName" type="token" use="optional"/>
	</complexType>
	
	<complexType name="BasePropertyDescriptor">
		<complexContent>
			<extension base="propertygroup:PropertyDescriptor">
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="BaseProperty">
		<complexContent>
			<extension base="propertygroup:BasePropertyDescriptor">
				<attribute name="validationMessage" type="token" use="optional"/>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="BaseNodeProperty">
		<complexContent>
			<extension base="propertygroup:BaseProperty">
				<sequence>
					<element maxOccurs="0" minOccurs="0" name="children" type="propertygroup:BaseNodeProperty"/>
				</sequence>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="ValidValue">
		<sequence>
			<element ref="propertygroup:description" minOccurs="0"/>
		</sequence>
		<attribute name="displayValue" type="token" use="optional"/>
		<attribute name="value" type="token" use="required"/>
	</complexType>
	
	<complexType name="BaseSingleTypedProperty">
		<complexContent>
			<extension base="propertygroup:BaseProperty">
				<sequence>
					<element maxOccurs="unbounded" minOccurs="0" name="validValue" type="propertygroup:ValidValue"/>
				</sequence>
				<attribute name="defaultValue" type="token" use="optional"/>
				<attribute name="propertyType" type="token" use="required"/>
				<attribute name="expert" type="boolean" use="optional"/>
				<attribute name="hidden" type="boolean" use="optional"/>
				<attribute name="readOnly" type="boolean" use="optional"/>
				<attribute name="required" type="boolean" use="optional"/>
				<attribute name="sensitive" type="boolean" use="optional"/>
				<attribute name="validValuesEditable" type="boolean" use="optional"/>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="BaseMultiValuedProperty">
		<complexContent>
			<extension base="propertygroup:BaseSingleTypedProperty">
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="BaseBoundedMultiValuedProperty">
		<complexContent>
			<extension base="propertygroup:BaseMultiValuedProperty">
				<attribute name="boundedSize" type="token" use="optional"/>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="File">
		<attribute name="extension" type="token" use="optional"/>
		<attribute name="pattern" type="token" use="optional"/>
	</complexType>
	
	<complexType name="MultiFileProperty">
		<complexContent>
			<extension base="propertygroup:BaseMultiValuedProperty">
				<sequence>
					<element maxOccurs="unbounded" minOccurs="0" name="fileExtension" type="propertygroup:File"/>
				</sequence>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="MultiFolderProperty">
		<complexContent>
			<extension base="propertygroup:BaseMultiValuedProperty">
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="ConstraintMultiValuedProperty">
		<complexContent>
			<extension base="propertygroup:BaseBoundedMultiValuedProperty">
				<attribute name="pattern" type="token" use="optional"/>
				<attribute name="minValue" type="integer" use="optional"/>
				<attribute name="maxValue" type="integer" use="optional"/>
				<attribute name="maxLength" type="integer" use="optional"/>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="BaseSingleValuedProperty">
		<complexContent>
			<extension base="propertygroup:BaseSingleTypedProperty">
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="FileProperty">
		<complexContent>
			<extension base="propertygroup:BaseSingleValuedProperty">
				<sequence>
					<element maxOccurs="unbounded" minOccurs="0" name="fileExtension" type="propertygroup:File"/>
				</sequence>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="FolderProperty">
		<complexContent>
			<extension base="propertygroup:BaseSingleValuedProperty">
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="ConstraintSingleValuedProperty">
		<complexContent>
			<extension base="propertygroup:BaseSingleValuedProperty">
				<attribute name="pattern" type="token" use="optional"/>
				<attribute name="minValue" type="integer" use="optional"/>
				<attribute name="maxValue" type="integer" use="optional"/>
				<attribute name="maxLength" type="integer" use="optional"/>
				<attribute name="validValuesGeneratorClass" type="token" use="optional"/>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="PropertyGroup">
		<complexContent>
			<extension base="propertygroup:BaseProperty">
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="BasePropertyGroup">
		<complexContent>
			<extension base="propertygroup:PropertyGroup">
				<sequence>
					<element maxOccurs="unbounded" minOccurs="0" name="property" type="propertygroup:PropertyDescriptor"/>
					<element maxOccurs="unbounded" minOccurs="0" name="customProperty" type="propertygroup:CustomProperty"/>
				</sequence>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="CustomPropertyGroup">
		<complexContent>
			<extension base="propertygroup:PropertyGroup">
				<attribute name="class" type="token" use="optional"/>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="BasePropertyGroups">
		<complexContent>
			<extension base="propertygroup:BaseProperty">
				<sequence>
					<element maxOccurs="unbounded" minOccurs="0" name="propertyGroup" type="propertygroup:PropertyGroup"/>
				</sequence>
				<attribute name="resourceBundle" type="token" use="optional"/>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="BaseTreeProperty">
		<complexContent>
			<extension base="propertygroup:BaseProperty">
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="TableProperty">
		<complexContent>
			<extension base="propertygroup:PropertyDescriptor">
				<sequence>
					<element maxOccurs="unbounded" minOccurs="0" name="column" type="propertygroup:BaseSingleTypedProperty"/>
				</sequence>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="TreeProperty">
		<complexContent>
			<extension base="propertygroup:PropertyDescriptor">
				<sequence>
					<element maxOccurs="1" minOccurs="0" name="root" type="propertygroup:BaseNodeProperty"/>
				</sequence>
			</extension>
		</complexContent>
	</complexType>
	
	<complexType name="CustomProperty">
		<attribute name="class" type="token" use="required"/>
	</complexType>
	
</schema>
```