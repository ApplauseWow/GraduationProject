# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: correspondence.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='correspondence.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x14\x63orrespondence.proto\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04para\x18\x01 \x01(\x0c\"\x1f\n\rHelloResponse\x12\x0e\n\x06result\x18\x01 \x01(\x0c\"\x1d\n\rRequestStruct\x12\x0c\n\x04para\x18\x01 \x01(\x0c\" \n\x0eResponseStruct\x12\x0e\n\x06result\x18\x01 \x01(\x0c\x32\xe7\x02\n\x07\x42\x61\x63kend\x12+\n\x08SayHello\x12\r.HelloRequest\x1a\x0e.HelloResponse\"\x00\x12\x30\n\rSayHelloAgain\x12\r.HelloRequest\x1a\x0e.HelloResponse\"\x00\x12\x34\n\x0fGetRecordsCount\x12\x0e.RequestStruct\x1a\x0f.ResponseStruct\"\x00\x12\x30\n\x0bGetAllNotes\x12\x0e.RequestStruct\x1a\x0f.ResponseStruct\"\x00\x12/\n\nGetTheNote\x12\x0e.RequestStruct\x1a\x0f.ResponseStruct\"\x00\x12\x30\n\x0bInsertANote\x12\x0e.RequestStruct\x1a\x0f.ResponseStruct\"\x00\x12\x32\n\rModifyTheNote\x12\x0e.RequestStruct\x1a\x0f.ResponseStruct\"\x00\x62\x06proto3'
)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='para', full_name='HelloRequest.para', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=52,
)


_HELLORESPONSE = _descriptor.Descriptor(
  name='HelloResponse',
  full_name='HelloResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='HelloResponse.result', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=85,
)


_REQUESTSTRUCT = _descriptor.Descriptor(
  name='RequestStruct',
  full_name='RequestStruct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='para', full_name='RequestStruct.para', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=116,
)


_RESPONSESTRUCT = _descriptor.Descriptor(
  name='ResponseStruct',
  full_name='ResponseStruct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='ResponseStruct.result', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=150,
)

DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloResponse'] = _HELLORESPONSE
DESCRIPTOR.message_types_by_name['RequestStruct'] = _REQUESTSTRUCT
DESCRIPTOR.message_types_by_name['ResponseStruct'] = _RESPONSESTRUCT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'correspondence_pb2'
  # @@protoc_insertion_point(class_scope:HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloResponse = _reflection.GeneratedProtocolMessageType('HelloResponse', (_message.Message,), {
  'DESCRIPTOR' : _HELLORESPONSE,
  '__module__' : 'correspondence_pb2'
  # @@protoc_insertion_point(class_scope:HelloResponse)
  })
_sym_db.RegisterMessage(HelloResponse)

RequestStruct = _reflection.GeneratedProtocolMessageType('RequestStruct', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTSTRUCT,
  '__module__' : 'correspondence_pb2'
  # @@protoc_insertion_point(class_scope:RequestStruct)
  })
_sym_db.RegisterMessage(RequestStruct)

ResponseStruct = _reflection.GeneratedProtocolMessageType('ResponseStruct', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSESTRUCT,
  '__module__' : 'correspondence_pb2'
  # @@protoc_insertion_point(class_scope:ResponseStruct)
  })
_sym_db.RegisterMessage(ResponseStruct)



_BACKEND = _descriptor.ServiceDescriptor(
  name='Backend',
  full_name='Backend',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=153,
  serialized_end=512,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='Backend.SayHello',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLORESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SayHelloAgain',
    full_name='Backend.SayHelloAgain',
    index=1,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLORESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetRecordsCount',
    full_name='Backend.GetRecordsCount',
    index=2,
    containing_service=None,
    input_type=_REQUESTSTRUCT,
    output_type=_RESPONSESTRUCT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllNotes',
    full_name='Backend.GetAllNotes',
    index=3,
    containing_service=None,
    input_type=_REQUESTSTRUCT,
    output_type=_RESPONSESTRUCT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTheNote',
    full_name='Backend.GetTheNote',
    index=4,
    containing_service=None,
    input_type=_REQUESTSTRUCT,
    output_type=_RESPONSESTRUCT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='InsertANote',
    full_name='Backend.InsertANote',
    index=5,
    containing_service=None,
    input_type=_REQUESTSTRUCT,
    output_type=_RESPONSESTRUCT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ModifyTheNote',
    full_name='Backend.ModifyTheNote',
    index=6,
    containing_service=None,
    input_type=_REQUESTSTRUCT,
    output_type=_RESPONSESTRUCT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BACKEND)

DESCRIPTOR.services_by_name['Backend'] = _BACKEND

# @@protoc_insertion_point(module_scope)