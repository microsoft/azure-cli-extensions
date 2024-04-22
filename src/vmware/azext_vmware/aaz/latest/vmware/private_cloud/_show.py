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
    "vmware private-cloud show",
)
class Show(AAZCommand):
    """Get a private cloud
    """

    _aaz_info = {
        "version": "2023-03-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.avs/privateclouds/{}", "2023-03-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.private_cloud_name = AAZStrArg(
            options=["-n", "--name", "--private-cloud-name"],
            help="Name of the private cloud",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[-\w\._]+$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PrivateCloudsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class PrivateCloudsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "privateCloudName", self.ctx.args.private_cloud_name,
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
                    "api-version", "2023-03-01",
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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.identity = AAZObjectType()
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.sku = AAZObjectType(
                flags={"required": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()

            properties = cls._schema_on_200.properties
            properties.availability = AAZObjectType()
            properties.circuit = AAZObjectType()
            _ShowHelper._build_schema_circuit_read(properties.circuit)
            properties.encryption = AAZObjectType()
            properties.endpoints = AAZObjectType()
            properties.extended_network_blocks = AAZListType(
                serialized_name="extendedNetworkBlocks",
            )
            properties.external_cloud_links = AAZListType(
                serialized_name="externalCloudLinks",
                flags={"read_only": True},
            )
            properties.identity_sources = AAZListType(
                serialized_name="identitySources",
            )
            properties.internet = AAZStrType()
            properties.management_cluster = AAZObjectType(
                serialized_name="managementCluster",
                flags={"required": True},
            )
            properties.management_network = AAZStrType(
                serialized_name="managementNetwork",
                flags={"read_only": True},
            )
            properties.network_block = AAZStrType(
                serialized_name="networkBlock",
                flags={"required": True},
            )
            properties.nsx_public_ip_quota_raised = AAZStrType(
                serialized_name="nsxPublicIpQuotaRaised",
                flags={"read_only": True},
            )
            properties.nsxt_certificate_thumbprint = AAZStrType(
                serialized_name="nsxtCertificateThumbprint",
                flags={"read_only": True},
            )
            properties.nsxt_password = AAZStrType(
                serialized_name="nsxtPassword",
                flags={"secret": True},
            )
            properties.provisioning_network = AAZStrType(
                serialized_name="provisioningNetwork",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.secondary_circuit = AAZObjectType(
                serialized_name="secondaryCircuit",
            )
            _ShowHelper._build_schema_circuit_read(properties.secondary_circuit)
            properties.vcenter_certificate_thumbprint = AAZStrType(
                serialized_name="vcenterCertificateThumbprint",
                flags={"read_only": True},
            )
            properties.vcenter_password = AAZStrType(
                serialized_name="vcenterPassword",
                flags={"secret": True},
            )
            properties.vmotion_network = AAZStrType(
                serialized_name="vmotionNetwork",
                flags={"read_only": True},
            )

            availability = cls._schema_on_200.properties.availability
            availability.secondary_zone = AAZIntType(
                serialized_name="secondaryZone",
            )
            availability.strategy = AAZStrType()
            availability.zone = AAZIntType()

            encryption = cls._schema_on_200.properties.encryption
            encryption.key_vault_properties = AAZObjectType(
                serialized_name="keyVaultProperties",
            )
            encryption.status = AAZStrType()

            key_vault_properties = cls._schema_on_200.properties.encryption.key_vault_properties
            key_vault_properties.auto_detected_key_version = AAZStrType(
                serialized_name="autoDetectedKeyVersion",
                flags={"read_only": True},
            )
            key_vault_properties.key_name = AAZStrType(
                serialized_name="keyName",
            )
            key_vault_properties.key_state = AAZStrType(
                serialized_name="keyState",
                flags={"read_only": True},
            )
            key_vault_properties.key_vault_url = AAZStrType(
                serialized_name="keyVaultUrl",
            )
            key_vault_properties.key_version = AAZStrType(
                serialized_name="keyVersion",
            )
            key_vault_properties.version_type = AAZStrType(
                serialized_name="versionType",
                flags={"read_only": True},
            )

            endpoints = cls._schema_on_200.properties.endpoints
            endpoints.hcx_cloud_manager = AAZStrType(
                serialized_name="hcxCloudManager",
                flags={"read_only": True},
            )
            endpoints.nsxt_manager = AAZStrType(
                serialized_name="nsxtManager",
                flags={"read_only": True},
            )
            endpoints.vcsa = AAZStrType(
                flags={"read_only": True},
            )

            extended_network_blocks = cls._schema_on_200.properties.extended_network_blocks
            extended_network_blocks.Element = AAZStrType()

            external_cloud_links = cls._schema_on_200.properties.external_cloud_links
            external_cloud_links.Element = AAZStrType()

            identity_sources = cls._schema_on_200.properties.identity_sources
            identity_sources.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.identity_sources.Element
            _element.alias = AAZStrType(
                flags={"required": True},
            )
            _element.base_group_dn = AAZStrType(
                serialized_name="baseGroupDN",
                flags={"required": True},
            )
            _element.base_user_dn = AAZStrType(
                serialized_name="baseUserDN",
                flags={"required": True},
            )
            _element.domain = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.password = AAZStrType(
                flags={"secret": True},
            )
            _element.primary_server = AAZStrType(
                serialized_name="primaryServer",
                flags={"required": True},
            )
            _element.secondary_server = AAZStrType(
                serialized_name="secondaryServer",
            )
            _element.ssl = AAZStrType()
            _element.username = AAZStrType(
                flags={"secret": True},
            )

            management_cluster = cls._schema_on_200.properties.management_cluster
            management_cluster.cluster_id = AAZIntType(
                serialized_name="clusterId",
                flags={"read_only": True},
            )
            management_cluster.cluster_size = AAZIntType(
                serialized_name="clusterSize",
                flags={"required": True},
            )
            management_cluster.hosts = AAZListType()
            management_cluster.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            hosts = cls._schema_on_200.properties.management_cluster.hosts
            hosts.Element = AAZStrType()

            sku = cls._schema_on_200.sku
            sku.name = AAZStrType(
                flags={"required": True},
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_circuit_read = None

    @classmethod
    def _build_schema_circuit_read(cls, _schema):
        if cls._schema_circuit_read is not None:
            _schema.express_route_id = cls._schema_circuit_read.express_route_id
            _schema.express_route_private_peering_id = cls._schema_circuit_read.express_route_private_peering_id
            _schema.primary_subnet = cls._schema_circuit_read.primary_subnet
            _schema.secondary_subnet = cls._schema_circuit_read.secondary_subnet
            return

        cls._schema_circuit_read = _schema_circuit_read = AAZObjectType()

        circuit_read = _schema_circuit_read
        circuit_read.express_route_id = AAZStrType(
            serialized_name="expressRouteID",
            flags={"read_only": True},
        )
        circuit_read.express_route_private_peering_id = AAZStrType(
            serialized_name="expressRoutePrivatePeeringID",
            flags={"read_only": True},
        )
        circuit_read.primary_subnet = AAZStrType(
            serialized_name="primarySubnet",
            flags={"read_only": True},
        )
        circuit_read.secondary_subnet = AAZStrType(
            serialized_name="secondarySubnet",
            flags={"read_only": True},
        )

        _schema.express_route_id = cls._schema_circuit_read.express_route_id
        _schema.express_route_private_peering_id = cls._schema_circuit_read.express_route_private_peering_id
        _schema.primary_subnet = cls._schema_circuit_read.primary_subnet
        _schema.secondary_subnet = cls._schema_circuit_read.secondary_subnet


__all__ = ["Show"]
