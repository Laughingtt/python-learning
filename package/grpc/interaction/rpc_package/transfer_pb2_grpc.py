# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import transfer_pb2 as transfer__pb2


class TransferServerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.recv = channel.unary_unary(
        '/network.TransferServer/recv',
        request_serializer=transfer__pb2.Message.SerializeToString,
        response_deserializer=transfer__pb2.Empty.FromString,
        )
    self.send = channel.unary_unary(
        '/network.TransferServer/send',
        request_serializer=transfer__pb2.Message.SerializeToString,
        response_deserializer=transfer__pb2.Empty.FromString,
        )
    self.get_local_server = channel.unary_unary(
        '/network.TransferServer/get_local_server',
        request_serializer=transfer__pb2.RequestMeta.SerializeToString,
        response_deserializer=transfer__pb2.Message.FromString,
        )


class TransferServerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def recv(self, request, context):
    """接收远程的请求数据
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def send(self, request, context):
    """发送数据到本地服务,本地服务再调其他服务recv
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def get_local_server(self, request, context):
    """从本地服务获取数据
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TransferServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'recv': grpc.unary_unary_rpc_method_handler(
          servicer.recv,
          request_deserializer=transfer__pb2.Message.FromString,
          response_serializer=transfer__pb2.Empty.SerializeToString,
      ),
      'send': grpc.unary_unary_rpc_method_handler(
          servicer.send,
          request_deserializer=transfer__pb2.Message.FromString,
          response_serializer=transfer__pb2.Empty.SerializeToString,
      ),
      'get_local_server': grpc.unary_unary_rpc_method_handler(
          servicer.get_local_server,
          request_deserializer=transfer__pb2.RequestMeta.FromString,
          response_serializer=transfer__pb2.Message.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'network.TransferServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))