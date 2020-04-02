# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import correspondence_pb2 as correspondence__pb2


class BackendStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/Backend/SayHello',
        request_serializer=correspondence__pb2.HelloRequest.SerializeToString,
        response_deserializer=correspondence__pb2.HelloResponse.FromString,
        )
    self.SayHelloAgain = channel.unary_unary(
        '/Backend/SayHelloAgain',
        request_serializer=correspondence__pb2.HelloRequest.SerializeToString,
        response_deserializer=correspondence__pb2.HelloResponse.FromString,
        )


class BackendServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SayHello(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SayHelloAgain(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BackendServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=correspondence__pb2.HelloRequest.FromString,
          response_serializer=correspondence__pb2.HelloResponse.SerializeToString,
      ),
      'SayHelloAgain': grpc.unary_unary_rpc_method_handler(
          servicer.SayHelloAgain,
          request_deserializer=correspondence__pb2.HelloRequest.FromString,
          response_serializer=correspondence__pb2.HelloResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Backend', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
