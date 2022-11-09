"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import foxglove.Color_pb2
import foxglove.Point3_pb2
import foxglove.Pose_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class TriangleListPrimitive(google.protobuf.message.Message):
    """A primitive representing a set of triangles or a surface tiled by triangles"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POSE_FIELD_NUMBER: builtins.int
    POINTS_FIELD_NUMBER: builtins.int
    COLOR_FIELD_NUMBER: builtins.int
    COLORS_FIELD_NUMBER: builtins.int
    INDICES_FIELD_NUMBER: builtins.int
    @property
    def pose(self) -> foxglove.Pose_pb2.Pose:
        """Origin of triangles relative to reference frame"""
        pass
    @property
    def points(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[foxglove.Point3_pb2.Point3]:
        """Vertices to use for triangles, interpreted as a list of triples (0-1-2, 3-4-5, ...)"""
        pass
    @property
    def color(self) -> foxglove.Color_pb2.Color:
        """Solid color to use for the whole shape. One of `color` or `colors` must be provided."""
        pass
    @property
    def colors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[foxglove.Color_pb2.Color]:
        """Per-vertex colors (if specified, must have the same length as `points`). One of `color` or `colors` must be provided."""
        pass
    @property
    def indices(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Indices into the `points` and `colors` attribute arrays, which can be used to avoid duplicating attribute data.

        If omitted or empty, indexing will not be used. This default behavior is equivalent to specifying [0, 1, ..., N-1] for the indices (where N is the number of `points` provided).
        """
        pass
    def __init__(self,
        *,
        pose: typing.Optional[foxglove.Pose_pb2.Pose] = ...,
        points: typing.Optional[typing.Iterable[foxglove.Point3_pb2.Point3]] = ...,
        color: typing.Optional[foxglove.Color_pb2.Color] = ...,
        colors: typing.Optional[typing.Iterable[foxglove.Color_pb2.Color]] = ...,
        indices: typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["color",b"color","pose",b"pose"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["color",b"color","colors",b"colors","indices",b"indices","points",b"points","pose",b"pose"]) -> None: ...
global___TriangleListPrimitive = TriangleListPrimitive
