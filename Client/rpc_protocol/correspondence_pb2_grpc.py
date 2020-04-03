# -*-coding:utf-8-*-
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
    self.GetAllNotes = channel.unary_unary(
        '/Backend/GetAllNotes',
        request_serializer=correspondence__pb2.RequestStruct.SerializeToString,
        response_deserializer=correspondence__pb2.ResponseStruct.FromString,
        )
    self.GetTheNote = channel.unary_unary(
        '/Backend/GetTheNote',
        request_serializer=correspondence__pb2.RequestStruct.SerializeToString,
        response_deserializer=correspondence__pb2.ResponseStruct.FromString,
        )
    self.InsertANote = channel.unary_unary(
        '/Backend/InsertANote',
        request_serializer=correspondence__pb2.RequestStruct.SerializeToString,
        response_deserializer=correspondence__pb2.ResponseStruct.FromString,
        )
    self.ModifyTheNote = channel.unary_unary(
        '/Backend/ModifyTheNote',
        request_serializer=correspondence__pb2.RequestStruct.SerializeToString,
        response_deserializer=correspondence__pb2.ResponseStruct.FromString,
        )


class BackendServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SayHello(self, request, context):
    """用于测试
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SayHelloAgain(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllNotes(self, request, context):
    """正式接口
    ->数据库交互接口
    ->->公告界面
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTheNote(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InsertANote(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModifyTheNote(self, request, context):
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
      'GetAllNotes': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllNotes,
          request_deserializer=correspondence__pb2.RequestStruct.FromString,
          response_serializer=correspondence__pb2.ResponseStruct.SerializeToString,
      ),
      'GetTheNote': grpc.unary_unary_rpc_method_handler(
          servicer.GetTheNote,
          request_deserializer=correspondence__pb2.RequestStruct.FromString,
          response_serializer=correspondence__pb2.ResponseStruct.SerializeToString,
      ),
      'InsertANote': grpc.unary_unary_rpc_method_handler(
          servicer.InsertANote,
          request_deserializer=correspondence__pb2.RequestStruct.FromString,
          response_serializer=correspondence__pb2.ResponseStruct.SerializeToString,
      ),
      'ModifyTheNote': grpc.unary_unary_rpc_method_handler(
          servicer.ModifyTheNote,
          request_deserializer=correspondence__pb2.RequestStruct.FromString,
          response_serializer=correspondence__pb2.ResponseStruct.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Backend', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
