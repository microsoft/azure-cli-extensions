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
    "network vhub route-map create",
)
class Create(AAZCommand):
    """Create a route map.

    :example: Create route map
        az network vhub route-map create -n route-map-name -g rg --vhub-name vhub-name
    """

    _aaz_info = {
        "version": "2022-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/virtualhubs/{}/routemaps/{}", "2022-05-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

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
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.route_map_name = AAZStrArg(
            options=["-n", "--name", "--route-map-name"],
            help="The name of the RouteMap.",
            required=True,
        )
        _args_schema.vhub_name = AAZStrArg(
            options=["--vhub-name"],
            help="The name of the VirtualHub containing the RouteMap.",
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.inbound_connection = AAZListArg(
            options=["--inbound-connection"],
            arg_group="Properties",
            help="List of connections which have this RoutMap associated for inbound traffic.",
        )
        _args_schema.outbound_connections = AAZListArg(
            options=["--outbound-connections"],
            arg_group="Properties",
            help="List of connections which have this RoutMap associated for outbound traffic.",
        )
        _args_schema.rules = AAZListArg(
            options=["--rules"],
            arg_group="Properties",
            help="List of RouteMap rules to be applied.",
        )

        inbound_connection = cls._args_schema.inbound_connection
        inbound_connection.Element = AAZStrArg()

        outbound_connections = cls._args_schema.outbound_connections
        outbound_connections.Element = AAZStrArg()

        rules = cls._args_schema.rules
        rules.Element = AAZObjectArg()

        _element = cls._args_schema.rules.Element
        _element.actions = AAZListArg(
            options=["actions"],
            help="List of actions which will be applied on a match.",
        )
        _element.match_criteria = AAZListArg(
            options=["match-criteria"],
            help="List of matching criterion which will be applied to traffic.",
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="The unique name for the rule.",
        )
        _element.next_step_if_matched = AAZStrArg(
            options=["next-step-if-matched"],
            help="Next step after rule is evaluated. Current supported behaviors are 'Continue'(to next rule) and 'Terminate'.",
            enum={"Continue": "Continue", "Terminate": "Terminate", "Unknown": "Unknown"},
        )

        actions = cls._args_schema.rules.Element.actions
        actions.Element = AAZObjectArg()

        _element = cls._args_schema.rules.Element.actions.Element
        _element.parameters = AAZListArg(
            options=["parameters"],
            help="List of parameters relevant to the action.For instance if type is drop then parameters has list of prefixes to be dropped.If type is add, parameters would have list of ASN numbers to be added",
        )
        _element.type = AAZStrArg(
            options=["type"],
            help="Type of action to be taken. Supported types are 'Remove', 'Add', 'Replace', and 'Drop.'",
            enum={"Add": "Add", "Drop": "Drop", "Remove": "Remove", "Replace": "Replace", "Unknown": "Unknown"},
        )

        parameters = cls._args_schema.rules.Element.actions.Element.parameters
        parameters.Element = AAZObjectArg()

        _element = cls._args_schema.rules.Element.actions.Element.parameters.Element
        _element.as_path = AAZListArg(
            options=["as-path"],
            help="List of AS paths.",
        )
        _element.community = AAZListArg(
            options=["community"],
            help="List of BGP communities.",
        )
        _element.route_prefix = AAZListArg(
            options=["route-prefix"],
            help="List of route prefixes.",
        )

        as_path = cls._args_schema.rules.Element.actions.Element.parameters.Element.as_path
        as_path.Element = AAZStrArg()

        community = cls._args_schema.rules.Element.actions.Element.parameters.Element.community
        community.Element = AAZStrArg()

        route_prefix = cls._args_schema.rules.Element.actions.Element.parameters.Element.route_prefix
        route_prefix.Element = AAZStrArg()

        match_criteria = cls._args_schema.rules.Element.match_criteria
        match_criteria.Element = AAZObjectArg()

        _element = cls._args_schema.rules.Element.match_criteria.Element
        _element.as_path = AAZListArg(
            options=["as-path"],
            help="List of AS paths which this criteria matches.",
        )
        _element.community = AAZListArg(
            options=["community"],
            help="List of BGP communities which this criteria matches.",
        )
        _element.match_condition = AAZStrArg(
            options=["match-condition"],
            help="Match condition to apply RouteMap rules.",
            enum={"Contains": "Contains", "Equals": "Equals", "NotContains": "NotContains", "NotEquals": "NotEquals", "Unknown": "Unknown"},
        )
        _element.route_prefix = AAZListArg(
            options=["route-prefix"],
            help="List of route prefixes which this criteria matches.",
        )

        as_path = cls._args_schema.rules.Element.match_criteria.Element.as_path
        as_path.Element = AAZStrArg()

        community = cls._args_schema.rules.Element.match_criteria.Element.community
        community.Element = AAZStrArg()

        route_prefix = cls._args_schema.rules.Element.match_criteria.Element.route_prefix
        route_prefix.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.RouteMapsCreateOrUpdate(ctx=self.ctx)()
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

    class RouteMapsCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/routeMaps/{routeMapName}",
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
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "routeMapName", self.ctx.args.route_map_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualHubName", self.ctx.args.vhub_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-05-01",
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
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("associatedInboundConnections", AAZListType, ".inbound_connection")
                properties.set_prop("associatedOutboundConnections", AAZListType, ".outbound_connections")
                properties.set_prop("rules", AAZListType, ".rules")

            associated_inbound_connections = _builder.get(".properties.associatedInboundConnections")
            if associated_inbound_connections is not None:
                associated_inbound_connections.set_elements(AAZStrType, ".")

            associated_outbound_connections = _builder.get(".properties.associatedOutboundConnections")
            if associated_outbound_connections is not None:
                associated_outbound_connections.set_elements(AAZStrType, ".")

            rules = _builder.get(".properties.rules")
            if rules is not None:
                rules.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.rules[]")
            if _elements is not None:
                _elements.set_prop("actions", AAZListType, ".actions")
                _elements.set_prop("matchCriteria", AAZListType, ".match_criteria")
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("nextStepIfMatched", AAZStrType, ".next_step_if_matched")

            actions = _builder.get(".properties.rules[].actions")
            if actions is not None:
                actions.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.rules[].actions[]")
            if _elements is not None:
                _elements.set_prop("parameters", AAZListType, ".parameters")
                _elements.set_prop("type", AAZStrType, ".type")

            parameters = _builder.get(".properties.rules[].actions[].parameters")
            if parameters is not None:
                parameters.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.rules[].actions[].parameters[]")
            if _elements is not None:
                _elements.set_prop("asPath", AAZListType, ".as_path")
                _elements.set_prop("community", AAZListType, ".community")
                _elements.set_prop("routePrefix", AAZListType, ".route_prefix")

            as_path = _builder.get(".properties.rules[].actions[].parameters[].asPath")
            if as_path is not None:
                as_path.set_elements(AAZStrType, ".")

            community = _builder.get(".properties.rules[].actions[].parameters[].community")
            if community is not None:
                community.set_elements(AAZStrType, ".")

            route_prefix = _builder.get(".properties.rules[].actions[].parameters[].routePrefix")
            if route_prefix is not None:
                route_prefix.set_elements(AAZStrType, ".")

            match_criteria = _builder.get(".properties.rules[].matchCriteria")
            if match_criteria is not None:
                match_criteria.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.rules[].matchCriteria[]")
            if _elements is not None:
                _elements.set_prop("asPath", AAZListType, ".as_path")
                _elements.set_prop("community", AAZListType, ".community")
                _elements.set_prop("matchCondition", AAZStrType, ".match_condition")
                _elements.set_prop("routePrefix", AAZListType, ".route_prefix")

            as_path = _builder.get(".properties.rules[].matchCriteria[].asPath")
            if as_path is not None:
                as_path.set_elements(AAZStrType, ".")

            community = _builder.get(".properties.rules[].matchCriteria[].community")
            if community is not None:
                community.set_elements(AAZStrType, ".")

            route_prefix = _builder.get(".properties.rules[].matchCriteria[].routePrefix")
            if route_prefix is not None:
                route_prefix.set_elements(AAZStrType, ".")

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
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.associated_inbound_connections = AAZListType(
                serialized_name="associatedInboundConnections",
            )
            properties.associated_outbound_connections = AAZListType(
                serialized_name="associatedOutboundConnections",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.rules = AAZListType()

            associated_inbound_connections = cls._schema_on_200_201.properties.associated_inbound_connections
            associated_inbound_connections.Element = AAZStrType()

            associated_outbound_connections = cls._schema_on_200_201.properties.associated_outbound_connections
            associated_outbound_connections.Element = AAZStrType()

            rules = cls._schema_on_200_201.properties.rules
            rules.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.rules.Element
            _element.actions = AAZListType()
            _element.match_criteria = AAZListType(
                serialized_name="matchCriteria",
            )
            _element.name = AAZStrType()
            _element.next_step_if_matched = AAZStrType(
                serialized_name="nextStepIfMatched",
            )

            actions = cls._schema_on_200_201.properties.rules.Element.actions
            actions.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.rules.Element.actions.Element
            _element.parameters = AAZListType()
            _element.type = AAZStrType()

            parameters = cls._schema_on_200_201.properties.rules.Element.actions.Element.parameters
            parameters.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.rules.Element.actions.Element.parameters.Element
            _element.as_path = AAZListType(
                serialized_name="asPath",
            )
            _element.community = AAZListType()
            _element.route_prefix = AAZListType(
                serialized_name="routePrefix",
            )

            as_path = cls._schema_on_200_201.properties.rules.Element.actions.Element.parameters.Element.as_path
            as_path.Element = AAZStrType()

            community = cls._schema_on_200_201.properties.rules.Element.actions.Element.parameters.Element.community
            community.Element = AAZStrType()

            route_prefix = cls._schema_on_200_201.properties.rules.Element.actions.Element.parameters.Element.route_prefix
            route_prefix.Element = AAZStrType()

            match_criteria = cls._schema_on_200_201.properties.rules.Element.match_criteria
            match_criteria.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.rules.Element.match_criteria.Element
            _element.as_path = AAZListType(
                serialized_name="asPath",
            )
            _element.community = AAZListType()
            _element.match_condition = AAZStrType(
                serialized_name="matchCondition",
            )
            _element.route_prefix = AAZListType(
                serialized_name="routePrefix",
            )

            as_path = cls._schema_on_200_201.properties.rules.Element.match_criteria.Element.as_path
            as_path.Element = AAZStrType()

            community = cls._schema_on_200_201.properties.rules.Element.match_criteria.Element.community
            community.Element = AAZStrType()

            route_prefix = cls._schema_on_200_201.properties.rules.Element.match_criteria.Element.route_prefix
            route_prefix.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
