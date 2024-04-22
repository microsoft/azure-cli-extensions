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
    "monitor data-collection rule association create",
)
class Create(AAZCommand):
    """Create an association.

    :example: Create association
        az monitor data-collection rule association create --name "myAssociation" --rule-id "/subscriptions/703362b3-f278-4e4b-9179- c76eaf41ffc2/resourceGroups/myResourceGroup/providers/Microsoft.Insights/dataCollectionRules/myCollectionRule" --resource "subscriptions/703362b3-f278-4e4b-9179- c76eaf41ffc2/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVm "
    """

    _aaz_info = {
        "version": "2022-06-01",
        "resources": [
            ["mgmt-plane", "/{resourceuri}/providers/microsoft.insights/datacollectionruleassociations/{}", "2022-06-01"],
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
        _args_schema.association_name = AAZStrArg(
            options=["-n", "--name", "--association-name"],
            help="The name of the association. The name is case insensitive.",
            required=True,
        )
        _args_schema.resource_uri = AAZStrArg(
            options=["--resource", "--resource-uri"],
            help="The identifier of the resource.",
            required=True,
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        _args_schema.data_collection_endpoint_id = AAZStrArg(
            options=["--endpoint-id", "--data-collection-endpoint-id"],
            help="The resource ID of the data collection endpoint that is to be associated.",
        )
        _args_schema.data_collection_rule_id = AAZStrArg(
            options=["--rule-id", "--data-collection-rule-id"],
            help="The resource ID of the data collection rule that is to be associated.",
        )
        _args_schema.description = AAZStrArg(
            options=["--description"],
            help="Description of the association.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.DataCollectionRuleAssociationsCreate(ctx=self.ctx)()
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

    class DataCollectionRuleAssociationsCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/{resourceUri}/providers/Microsoft.Insights/dataCollectionRuleAssociations/{associationName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "associationName", self.ctx.args.association_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceUri", self.ctx.args.resource_uri,
                    skip_quote=True,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-06-01",
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
                typ=AAZObjectType,
                typ_kwargs={"flags": {"client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("dataCollectionEndpointId", AAZStrType, ".data_collection_endpoint_id")
                properties.set_prop("dataCollectionRuleId", AAZStrType, ".data_collection_rule_id")
                properties.set_prop("description", AAZStrType, ".description")

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

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.data_collection_endpoint_id = AAZStrType(
                serialized_name="dataCollectionEndpointId",
            )
            properties.data_collection_rule_id = AAZStrType(
                serialized_name="dataCollectionRuleId",
            )
            properties.description = AAZStrType()
            properties.metadata = AAZObjectType(
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            metadata = cls._schema_on_200_201.properties.metadata
            metadata.provisioned_by = AAZStrType(
                serialized_name="provisionedBy",
                flags={"read_only": True},
            )
            metadata.provisioned_by_resource_id = AAZStrType(
                serialized_name="provisionedByResourceId",
                flags={"read_only": True},
            )

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
