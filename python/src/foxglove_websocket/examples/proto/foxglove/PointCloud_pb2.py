# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: foxglove/PointCloud.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from foxglove import PackedElementField_pb2 as foxglove_dot_PackedElementField__pb2
from foxglove import Pose_pb2 as foxglove_dot_Pose__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x66oxglove/PointCloud.proto\x12\x08\x66oxglove\x1a!foxglove/PackedElementField.proto\x1a\x13\x66oxglove/Pose.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbd\x01\n\nPointCloud\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08\x66rame_id\x18\x02 \x01(\t\x12\x1c\n\x04pose\x18\x03 \x01(\x0b\x32\x0e.foxglove.Pose\x12\x14\n\x0cpoint_stride\x18\x04 \x01(\x07\x12,\n\x06\x66ields\x18\x05 \x03(\x0b\x32\x1c.foxglove.PackedElementField\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'foxglove.PointCloud_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POINTCLOUD._serialized_start=129
  _POINTCLOUD._serialized_end=318
# @@protoc_insertion_point(module_scope)