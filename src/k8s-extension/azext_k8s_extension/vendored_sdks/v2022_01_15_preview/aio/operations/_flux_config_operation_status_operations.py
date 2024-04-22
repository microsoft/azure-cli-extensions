# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._flux_config_operation_status_operations import build_get_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class FluxConfigOperationStatusOperations:
    """FluxConfigOperationStatusOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.kubernetesconfiguration.v2022_01_15_preview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        cluster_rp: Union[str, "_models.ExtensionsClusterRp"],
        cluster_resource_name: Union[str, "_models.ExtensionsClusterResourceName"],
        cluster_name: str,
        flux_configuration_name: str,
        operation_id: str,
        **kwargs: Any
    ) -> "_models.OperationStatusResult":
        """Get Async Operation status.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS
         clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters).
        :type cluster_rp: str or
         ~azure.mgmt.kubernetesconfiguration.v2022_01_15_preview.models.ExtensionsClusterRp
        :param cluster_resource_name: The Kubernetes cluster resource name - either managedClusters
         (for AKS clusters) or connectedClusters (for OnPrem K8S clusters).
        :type cluster_resource_name: str or
         ~azure.mgmt.kubernetesconfiguration.v2022_01_15_preview.models.ExtensionsClusterResourceName
        :param cluster_name: The name of the kubernetes cluster.
        :type cluster_name: str
        :param flux_configuration_name: Name of the Flux Configuration.
        :type flux_configuration_name: str
        :param operation_id: operation Id.
        :type operation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: OperationStatusResult, or the result of cls(response)
        :rtype: ~azure.mgmt.kubernetesconfiguration.v2022_01_15_preview.models.OperationStatusResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.OperationStatusResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            cluster_rp=cluster_rp,
            cluster_resource_name=cluster_resource_name,
            cluster_name=cluster_name,
            flux_configuration_name=flux_configuration_name,
            operation_id=operation_id,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('OperationStatusResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/fluxConfigurations/{fluxConfigurationName}/operations/{operationId}'}  # type: ignore

