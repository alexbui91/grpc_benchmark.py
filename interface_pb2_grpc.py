# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import interface_pb2 as interface__pb2


class DANInterfaceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ping = channel.unary_unary(
                '/dan.DANInterface/ping',
                request_serializer=interface__pb2.Void.SerializeToString,
                response_deserializer=interface__pb2.Code.FromString,
                )
        self.test_size = channel.unary_unary(
                '/dan.DANInterface/test_size',
                request_serializer=interface__pb2.DoubleList.SerializeToString,
                response_deserializer=interface__pb2.DoubleList.FromString,
                )


class DANInterfaceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ping(self, request, context):
        """system API
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def test_size(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DANInterfaceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ping': grpc.unary_unary_rpc_method_handler(
                    servicer.ping,
                    request_deserializer=interface__pb2.Void.FromString,
                    response_serializer=interface__pb2.Code.SerializeToString,
            ),
            'test_size': grpc.unary_unary_rpc_method_handler(
                    servicer.test_size,
                    request_deserializer=interface__pb2.DoubleList.FromString,
                    response_serializer=interface__pb2.DoubleList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dan.DANInterface', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DANInterface(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dan.DANInterface/ping',
            interface__pb2.Void.SerializeToString,
            interface__pb2.Code.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def test_size(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dan.DANInterface/test_size',
            interface__pb2.DoubleList.SerializeToString,
            interface__pb2.DoubleList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
