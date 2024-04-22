# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network firewall update",
)
class Update(AAZCommand):
    """Update an Azure Firewall.
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/azurefirewalls/{}", "2022-01-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Azure Firewall name.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.firewall_policy = AAZStrArg(
            options=["--policy", "--firewall-policy"],
            help="Name or ID of the firewallPolicy associated with this azure firewall.",
            nullable=True,
        )
        _args_schema.threat_intel_mode = AAZStrArg(
            options=["--threat-intel-mode"],
            help="The operation mode for Threat Intelligence.",
            nullable=True,
            enum={"Alert": "Alert", "Deny": "Deny", "Off": "Off"},
        )
        _args_schema.virtual_hub = AAZStrArg(
            options=["--vhub", "--virtual-hub"],
            help="Name or ID of the virtualHub to which the firewall belongs.",
            nullable=True,
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            help="Resource tags.",
            nullable=True,
        )
        _args_schema.zones = AAZListArg(
            options=["-z", "--zones"],
            help="Space-separated list of availability zones into which to provision the resource. Allowed values: 1, 2, 3.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        zones = cls._args_schema.zones
        zones.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "HubIpAddresses"

        _args_schema = cls._args_schema
        _args_schema.addresses = AAZListArg(
            options=["--addresses"],
            arg_group="HubIpAddresses",
            help="The list of Public IP addresses associated with azure firewall or IP addresses to be retained.",
            nullable=True,
        )

        addresses = cls._args_schema.addresses
        addresses.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.addresses.Element
        _element.address = AAZStrArg(
            options=["address"],
            help="Public IP Address value.",
            nullable=True,
        )

        # define Arg Group "Parameters"

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.additional_properties = AAZDictArg(
            options=["--additional-properties"],
            arg_group="Properties",
            help="The additional properties used to further config this azure firewall.",
            nullable=True,
        )

        additional_properties = cls._args_schema.additional_properties
        additional_properties.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Virtual Hub Public Ip"

        _args_schema = cls._args_schema
        _args_schema.public_ip_count = AAZIntArg(
            options=["--count", "--public-ip-count"],
            arg_group="Virtual Hub Public Ip",
            help="Number of Public IP Address associated with azure firewall. It's used to add public ip addresses into this firewall.",
            nullable=True,
        )
        return cls._args_schema

    _args_azure_firewall_ip_configuration_update = None

    @classmethod
    def _build_args_azure_firewall_ip_configuration_update(cls, _schema):
        if cls._args_azure_firewall_ip_configuration_update is not None:
            _schema.m_conf_name = cls._args_azure_firewall_ip_configuration_update.m_conf_name
            _schema.public_ip_address = cls._args_azure_firewall_ip_configuration_update.public_ip_address
            return

        cls._args_azure_firewall_ip_configuration_update = AAZObjectArg(
            nullable=True,
        )

        azure_firewall_ip_configuration_update = cls._args_azure_firewall_ip_configuration_update
        azure_firewall_ip_configuration_update.m_conf_name = AAZStrArg(
            options=["m-conf-name"],
            help="Name of the resource that is unique within a resource group. This name can be used to access the resource.",
            nullable=True,
        )
        azure_firewall_ip_configuration_update.public_ip_address = AAZObjectArg(
            options=["public-ip-address"],
            help="Reference to the PublicIP resource. This field is a mandatory input if subnet is not null.",
            nullable=True,
        )
        cls._build_args_sub_resource_update(azure_firewall_ip_configuration_update.public_ip_address)

        _schema.m_conf_name = cls._args_azure_firewall_ip_configuration_update.m_conf_name
        _schema.public_ip_address = cls._args_azure_firewall_ip_configuration_update.public_ip_address

    _args_azure_firewall_rc_action_update = None

    @classmethod
    def _build_args_azure_firewall_rc_action_update(cls, _schema):
        if cls._args_azure_firewall_rc_action_update is not None:
            _schema.type = cls._args_azure_firewall_rc_action_update.type
            return

        cls._args_azure_firewall_rc_action_update = AAZObjectArg(
            nullable=True,
        )

        azure_firewall_rc_action_update = cls._args_azure_firewall_rc_action_update
        azure_firewall_rc_action_update.type = AAZStrArg(
            options=["type"],
            help="The type of action.",
            nullable=True,
            enum={"Allow": "Allow", "Deny": "Deny"},
        )

        _schema.type = cls._args_azure_firewall_rc_action_update.type

    _args_sub_resource_update = None

    @classmethod
    def _build_args_sub_resource_update(cls, _schema):
        if cls._args_sub_resource_update is not None:
            _schema.id = cls._args_sub_resource_update.id
            return

        cls._args_sub_resource_update = AAZObjectArg(
            nullable=True,
        )

        sub_resource_update = cls._args_sub_resource_update
        sub_resource_update.id = AAZStrArg(
            options=["id"],
            help="Resource ID.",
            nullable=True,
        )

        _schema.id = cls._args_sub_resource_update.id

    def _execute_operations(self):
        self.pre_operations()
        self.AzureFirewallsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.AzureFirewallsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class AzureFirewallsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/azureFirewalls/{azureFirewallName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "azureFirewallName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_azure_firewall_read(cls._schema_on_200)

            return cls._schema_on_200

    class AzureFirewallsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/azureFirewalls/{azureFirewallName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "azureFirewallName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_azure_firewall_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")
            _builder.set_prop("zones", AAZListType, ".zones")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("additionalProperties", AAZDictType, ".additional_properties")
                properties.set_prop("firewallPolicy", AAZObjectType)
                properties.set_prop("hubIPAddresses", AAZObjectType)
                properties.set_prop("sku", AAZObjectType)
                properties.set_prop("threatIntelMode", AAZStrType, ".threat_intel_mode")
                properties.set_prop("virtualHub", AAZObjectType)

            additional_properties = _builder.get(".properties.additionalProperties")
            if additional_properties is not None:
                additional_properties.set_elements(AAZStrType, ".")

            firewall_policy = _builder.get(".properties.firewallPolicy")
            if firewall_policy is not None:
                firewall_policy.set_prop("id", AAZStrType, ".firewall_policy")

            hub_ip_addresses = _builder.get(".properties.hubIPAddresses")
            if hub_ip_addresses is not None:
                hub_ip_addresses.set_prop("publicIPs", AAZObjectType)

            public_i_ps = _builder.get(".properties.hubIPAddresses.publicIPs")
            if public_i_ps is not None:
                public_i_ps.set_prop("addresses", AAZListType, ".addresses")
                public_i_ps.set_prop("count", AAZIntType, ".public_ip_count")

            addresses = _builder.get(".properties.hubIPAddresses.publicIPs.addresses")
            if addresses is not None:
                addresses.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.hubIPAddresses.publicIPs.addresses[]")
            if _elements is not None:
                _elements.set_prop("address", AAZStrType, ".address")

            virtual_hub = _builder.get(".properties.virtualHub")
            if virtual_hub is not None:
                virtual_hub.set_prop("id", AAZStrType, ".virtual_hub")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            zones = _builder.get(".zones")
            if zones is not None:
                zones.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_azure_firewall_ip_configuration_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("name", AAZStrType, ".m_conf_name")
        _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

        properties = _builder.get(".properties")
        if properties is not None:
            cls._build_schema_sub_resource_update(properties.set_prop("publicIPAddress", AAZObjectType, ".public_ip_address"))

    @classmethod
    def _build_schema_azure_firewall_rc_action_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("type", AAZStrType, ".type")

    @classmethod
    def _build_schema_sub_resource_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("id", AAZStrType, ".id")

    _schema_azure_firewall_ip_configuration_read = None

    @classmethod
    def _build_schema_azure_firewall_ip_configuration_read(cls, _schema):
        if cls._schema_azure_firewall_ip_configuration_read is not None:
            _schema.etag = cls._schema_azure_firewall_ip_configuration_read.etag
            _schema.id = cls._schema_azure_firewall_ip_configuration_read.id
            _schema.name = cls._schema_azure_firewall_ip_configuration_read.name
            _schema.properties = cls._schema_azure_firewall_ip_configuration_read.properties
            _schema.type = cls._schema_azure_firewall_ip_configuration_read.type
            return

        cls._schema_azure_firewall_ip_configuration_read = _schema_azure_firewall_ip_configuration_read = AAZObjectType()

        azure_firewall_ip_configuration_read = _schema_azure_firewall_ip_configuration_read
        azure_firewall_ip_configuration_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        azure_firewall_ip_configuration_read.id = AAZStrType()
        azure_firewall_ip_configuration_read.name = AAZStrType()
        azure_firewall_ip_configuration_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        azure_firewall_ip_configuration_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_azure_firewall_ip_configuration_read.properties
        properties.private_ip_address = AAZStrType(
            serialized_name="privateIPAddress",
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.public_ip_address = AAZObjectType(
            serialized_name="publicIPAddress",
        )
        cls._build_schema_sub_resource_read(properties.public_ip_address)
        properties.subnet = AAZObjectType()
        cls._build_schema_sub_resource_read(properties.subnet)

        _schema.etag = cls._schema_azure_firewall_ip_configuration_read.etag
        _schema.id = cls._schema_azure_firewall_ip_configuration_read.id
        _schema.name = cls._schema_azure_firewall_ip_configuration_read.name
        _schema.properties = cls._schema_azure_firewall_ip_configuration_read.properties
        _schema.type = cls._schema_azure_firewall_ip_configuration_read.type

    _schema_azure_firewall_rc_action_read = None

    @classmethod
    def _build_schema_azure_firewall_rc_action_read(cls, _schema):
        if cls._schema_azure_firewall_rc_action_read is not None:
            _schema.type = cls._schema_azure_firewall_rc_action_read.type
            return

        cls._schema_azure_firewall_rc_action_read = _schema_azure_firewall_rc_action_read = AAZObjectType()

        azure_firewall_rc_action_read = _schema_azure_firewall_rc_action_read
        azure_firewall_rc_action_read.type = AAZStrType()

        _schema.type = cls._schema_azure_firewall_rc_action_read.type

    _schema_azure_firewall_read = None

    @classmethod
    def _build_schema_azure_firewall_read(cls, _schema):
        if cls._schema_azure_firewall_read is not None:
            _schema.etag = cls._schema_azure_firewall_read.etag
            _schema.id = cls._schema_azure_firewall_read.id
            _schema.location = cls._schema_azure_firewall_read.location
            _schema.name = cls._schema_azure_firewall_read.name
            _schema.properties = cls._schema_azure_firewall_read.properties
            _schema.tags = cls._schema_azure_firewall_read.tags
            _schema.type = cls._schema_azure_firewall_read.type
            _schema.zones = cls._schema_azure_firewall_read.zones
            return

        cls._schema_azure_firewall_read = _schema_azure_firewall_read = AAZObjectType()

        azure_firewall_read = _schema_azure_firewall_read
        azure_firewall_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        azure_firewall_read.id = AAZStrType()
        azure_firewall_read.location = AAZStrType()
        azure_firewall_read.name = AAZStrType(
            flags={"read_only": True},
        )
        azure_firewall_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        azure_firewall_read.tags = AAZDictType()
        azure_firewall_read.type = AAZStrType(
            flags={"read_only": True},
        )
        azure_firewall_read.zones = AAZListType()

        properties = _schema_azure_firewall_read.properties
        properties.additional_properties = AAZDictType(
            serialized_name="additionalProperties",
        )
        properties.application_rule_collections = AAZListType(
            serialized_name="applicationRuleCollections",
        )
        properties.firewall_policy = AAZObjectType(
            serialized_name="firewallPolicy",
        )
        cls._build_schema_sub_resource_read(properties.firewall_policy)
        properties.hub_ip_addresses = AAZObjectType(
            serialized_name="hubIPAddresses",
        )
        properties.ip_configurations = AAZListType(
            serialized_name="ipConfigurations",
        )
        properties.ip_groups = AAZListType(
            serialized_name="ipGroups",
        )
        properties.management_ip_configuration = AAZObjectType(
            serialized_name="managementIpConfiguration",
        )
        cls._build_schema_azure_firewall_ip_configuration_read(properties.management_ip_configuration)
        properties.nat_rule_collections = AAZListType(
            serialized_name="natRuleCollections",
        )
        properties.network_rule_collections = AAZListType(
            serialized_name="networkRuleCollections",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.sku = AAZObjectType()
        properties.threat_intel_mode = AAZStrType(
            serialized_name="threatIntelMode",
        )
        properties.virtual_hub = AAZObjectType(
            serialized_name="virtualHub",
        )
        cls._build_schema_sub_resource_read(properties.virtual_hub)

        additional_properties = _schema_azure_firewall_read.properties.additional_properties
        additional_properties.Element = AAZStrType()

        application_rule_collections = _schema_azure_firewall_read.properties.application_rule_collections
        application_rule_collections.Element = AAZObjectType()

        _element = _schema_azure_firewall_read.properties.application_rule_collections.Element
        _element.etag = AAZStrType(
            flags={"read_only": True},
        )
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_azure_firewall_read.properties.application_rule_collections.Element.properties
        properties.action = AAZObjectType()
        cls._build_schema_azure_firewall_rc_action_read(properties.action)
        properties.priority = AAZIntType()
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.rules = AAZListType()

        rules = _schema_azure_firewall_read.properties.application_rule_collections.Element.properties.rules
        rules.Element = AAZObjectType()

        _element = _schema_azure_firewall_read.properties.application_rule_collections.Element.properties.rules.Element
        _element.description = AAZStrType()
        _element.fqdn_tags = AAZListType(
            serialized_name="fqdnTags",
        )
        _element.name = AAZStrType()
        _element.protocols = AAZListType()
        _element.source_addresses = AAZListType(
            serialized_name="sourceAddresses",
        )
        _element.source_ip_groups = AAZListType(
            serialized_name="sourceIpGroups",
        )
        _element.target_fqdns = AAZListType(
            serialized_name="targetFqdns",
        )

        fqdn_tags = _schema_azure_firewall_read.properties.application_rule_collections.Element.properties.rules.Element.fqdn_tags
        fqdn_tags.Element = AAZStrType()

        protocols = _schema_azure_firewall_read.properties.application_rule_collections.Element.properties.rules.Element.protocols
        protocols.Element = AAZObjectType()

        _element = _schema_azure_firewall_read.properties.application_rule_collections.Element.properties.rules.Element.protocols.Element
        _element.port = AAZIntType()
        _element.protocol_type = AAZStrType(
            serialized_name="protocolType",
        )

        source_addresses = _schema_azure_firewall_read.properties.application_rule_collections.Element.properties.rules.Element.source_addresses
        source_addresses.Element = AAZStrType()

        source_ip_groups = _schema_azure_firewall_read.properties.application_rule_collections.Element.properties.rules.Element.source_ip_groups
        source_ip_groups.Element = AAZStrType()

        target_fqdns = _schema_azure_firewall_read.properties.application_rule_collections.Element.properties.rules.Element.target_fqdns
        target_fqdns.Element = AAZStrType()

        hub_ip_addresses = _schema_azure_firewall_read.properties.hub_ip_addresses
        hub_ip_addresses.private_ip_address = AAZStrType(
            serialized_name="privateIPAddress",
        )
        hub_ip_addresses.public_i_ps = AAZObjectType(
            serialized_name="publicIPs",
        )

        public_i_ps = _schema_azure_firewall_read.properties.hub_ip_addresses.public_i_ps
        public_i_ps.addresses = AAZListType()
        public_i_ps.count = AAZIntType()

        addresses = _schema_azure_firewall_read.properties.hub_ip_addresses.public_i_ps.addresses
        addresses.Element = AAZObjectType()

        _element = _schema_azure_firewall_read.properties.hub_ip_addresses.public_i_ps.addresses.Element
        _element.address = AAZStrType()

        ip_configurations = _schema_azure_firewall_read.properties.ip_configurations
        ip_configurations.Element = AAZObjectType()
        cls._build_schema_azure_firewall_ip_configuration_read(ip_configurations.Element)

        ip_groups = _schema_azure_firewall_read.properties.ip_groups
        ip_groups.Element = AAZObjectType()

        _element = _schema_azure_firewall_read.properties.ip_groups.Element
        _element.change_number = AAZStrType(
            serialized_name="changeNumber",
            flags={"read_only": True},
        )
        _element.id = AAZStrType(
            flags={"read_only": True},
        )

        nat_rule_collections = _schema_azure_firewall_read.properties.nat_rule_collections
        nat_rule_collections.Element = AAZObjectType()

        _element = _schema_azure_firewall_read.properties.nat_rule_collections.Element
        _element.etag = AAZStrType(
            flags={"read_only": True},
        )
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_azure_firewall_read.properties.nat_rule_collections.Element.properties
        properties.action = AAZObjectType()
        properties.priority = AAZIntType()
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.rules = AAZListType()

        action = _schema_azure_firewall_read.properties.nat_rule_collections.Element.properties.action
        action.type = AAZStrType()

        rules = _schema_azure_firewall_read.properties.nat_rule_collections.Element.properties.rules
        rules.Element = AAZObjectType()

        _element = _schema_azure_firewall_read.properties.nat_rule_collections.Element.properties.rules.Element
        _element.description = AAZStrType()
        _element.destination_addresses = AAZListType(
            serialized_name="destinationAddresses",
        )
        _element.destination_ports = AAZListType(
            serialized_name="destinationPorts",
        )
        _element.name = AAZStrType()
        _element.protocols = AAZListType()
        _element.source_addresses = AAZListType(
            serialized_name="sourceAddresses",
        )
        _element.source_ip_groups = AAZListType(
            serialized_name="sourceIpGroups",
        )
        _element.translated_address = AAZStrType(
            serialized_name="translatedAddress",
        )
        _element.translated_fqdn = AAZStrType(
            serialized_name="translatedFqdn",
        )
        _element.translated_port = AAZStrType(
            serialized_name="translatedPort",
        )

        destination_addresses = _schema_azure_firewall_read.properties.nat_rule_collections.Element.properties.rules.Element.destination_addresses
        destination_addresses.Element = AAZStrType()

        destination_ports = _schema_azure_firewall_read.properties.nat_rule_collections.Element.properties.rules.Element.destination_ports
        destination_ports.Element = AAZStrType()

        protocols = _schema_azure_firewall_read.properties.nat_rule_collections.Element.properties.rules.Element.protocols
        protocols.Element = AAZStrType()

        source_addresses = _schema_azure_firewall_read.properties.nat_rule_collections.Element.properties.rules.Element.source_addresses
        source_addresses.Element = AAZStrType()

        source_ip_groups = _schema_azure_firewall_read.properties.nat_rule_collections.Element.properties.rules.Element.source_ip_groups
        source_ip_groups.Element = AAZStrType()

        network_rule_collections = _schema_azure_firewall_read.properties.network_rule_collections
        network_rule_collections.Element = AAZObjectType()

        _element = _schema_azure_firewall_read.properties.network_rule_collections.Element
        _element.etag = AAZStrType(
            flags={"read_only": True},
        )
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_azure_firewall_read.properties.network_rule_collections.Element.properties
        properties.action = AAZObjectType()
        cls._build_schema_azure_firewall_rc_action_read(properties.action)
        properties.priority = AAZIntType()
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.rules = AAZListType()

        rules = _schema_azure_firewall_read.properties.network_rule_collections.Element.properties.rules
        rules.Element = AAZObjectType()

        _element = _schema_azure_firewall_read.properties.network_rule_collections.Element.properties.rules.Element
        _element.description = AAZStrType()
        _element.destination_addresses = AAZListType(
            serialized_name="destinationAddresses",
        )
        _element.destination_fqdns = AAZListType(
            serialized_name="destinationFqdns",
        )
        _element.destination_ip_groups = AAZListType(
            serialized_name="destinationIpGroups",
        )
        _element.destination_ports = AAZListType(
            serialized_name="destinationPorts",
        )
        _element.name = AAZStrType()
        _element.protocols = AAZListType()
        _element.source_addresses = AAZListType(
            serialized_name="sourceAddresses",
        )
        _element.source_ip_groups = AAZListType(
            serialized_name="sourceIpGroups",
        )

        destination_addresses = _schema_azure_firewall_read.properties.network_rule_collections.Element.properties.rules.Element.destination_addresses
        destination_addresses.Element = AAZStrType()

        destination_fqdns = _schema_azure_firewall_read.properties.network_rule_collections.Element.properties.rules.Element.destination_fqdns
        destination_fqdns.Element = AAZStrType()

        destination_ip_groups = _schema_azure_firewall_read.properties.network_rule_collections.Element.properties.rules.Element.destination_ip_groups
        destination_ip_groups.Element = AAZStrType()

        destination_ports = _schema_azure_firewall_read.properties.network_rule_collections.Element.properties.rules.Element.destination_ports
        destination_ports.Element = AAZStrType()

        protocols = _schema_azure_firewall_read.properties.network_rule_collections.Element.properties.rules.Element.protocols
        protocols.Element = AAZStrType()

        source_addresses = _schema_azure_firewall_read.properties.network_rule_collections.Element.properties.rules.Element.source_addresses
        source_addresses.Element = AAZStrType()

        source_ip_groups = _schema_azure_firewall_read.properties.network_rule_collections.Element.properties.rules.Element.source_ip_groups
        source_ip_groups.Element = AAZStrType()

        sku = _schema_azure_firewall_read.properties.sku
        sku.name = AAZStrType()
        sku.tier = AAZStrType()

        tags = _schema_azure_firewall_read.tags
        tags.Element = AAZStrType()

        zones = _schema_azure_firewall_read.zones
        zones.Element = AAZStrType()

        _schema.etag = cls._schema_azure_firewall_read.etag
        _schema.id = cls._schema_azure_firewall_read.id
        _schema.location = cls._schema_azure_firewall_read.location
        _schema.name = cls._schema_azure_firewall_read.name
        _schema.properties = cls._schema_azure_firewall_read.properties
        _schema.tags = cls._schema_azure_firewall_read.tags
        _schema.type = cls._schema_azure_firewall_read.type
        _schema.zones = cls._schema_azure_firewall_read.zones

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["Update"]
