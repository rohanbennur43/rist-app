# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import grpc_app.rist_app_pb2 as rist__app__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in rist_app_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class RistAppStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartRistApp = channel.unary_unary(
                '/RistApp.RistApp/StartRistApp',
                request_serializer=rist__app__pb2.RistAppconfig.SerializeToString,
                response_deserializer=rist__app__pb2.AppStatusResponse.FromString,
                _registered_method=True)
        self.StopRistApp = channel.unary_unary(
                '/RistApp.RistApp/StopRistApp',
                request_serializer=rist__app__pb2.Empty.SerializeToString,
                response_deserializer=rist__app__pb2.AppStatusResponse.FromString,
                _registered_method=True)
        self.StatusRistApp = channel.unary_unary(
                '/RistApp.RistApp/StatusRistApp',
                request_serializer=rist__app__pb2.Empty.SerializeToString,
                response_deserializer=rist__app__pb2.AppStatusResponse.FromString,
                _registered_method=True)
        self.UpdateRistApp = channel.unary_unary(
                '/RistApp.RistApp/UpdateRistApp',
                request_serializer=rist__app__pb2.RistAppconfig.SerializeToString,
                response_deserializer=rist__app__pb2.AppStatusResponse.FromString,
                _registered_method=True)


class RistAppServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartRistApp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopRistApp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StatusRistApp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRistApp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RistAppServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartRistApp': grpc.unary_unary_rpc_method_handler(
                    servicer.StartRistApp,
                    request_deserializer=rist__app__pb2.RistAppconfig.FromString,
                    response_serializer=rist__app__pb2.AppStatusResponse.SerializeToString,
            ),
            'StopRistApp': grpc.unary_unary_rpc_method_handler(
                    servicer.StopRistApp,
                    request_deserializer=rist__app__pb2.Empty.FromString,
                    response_serializer=rist__app__pb2.AppStatusResponse.SerializeToString,
            ),
            'StatusRistApp': grpc.unary_unary_rpc_method_handler(
                    servicer.StatusRistApp,
                    request_deserializer=rist__app__pb2.Empty.FromString,
                    response_serializer=rist__app__pb2.AppStatusResponse.SerializeToString,
            ),
            'UpdateRistApp': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRistApp,
                    request_deserializer=rist__app__pb2.RistAppconfig.FromString,
                    response_serializer=rist__app__pb2.AppStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RistApp.RistApp', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('RistApp.RistApp', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RistApp(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartRistApp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/RistApp.RistApp/StartRistApp',
            rist__app__pb2.RistAppconfig.SerializeToString,
            rist__app__pb2.AppStatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def StopRistApp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/RistApp.RistApp/StopRistApp',
            rist__app__pb2.Empty.SerializeToString,
            rist__app__pb2.AppStatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def StatusRistApp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/RistApp.RistApp/StatusRistApp',
            rist__app__pb2.Empty.SerializeToString,
            rist__app__pb2.AppStatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateRistApp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/RistApp.RistApp/UpdateRistApp',
            rist__app__pb2.RistAppconfig.SerializeToString,
            rist__app__pb2.AppStatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
