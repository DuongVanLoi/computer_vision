# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/hyperparams.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/hyperparams.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n)object_detection/protos/hyperparams.proto\x12\x17object_detection.protos\"\xe5\x04\n\x0bHyperparams\x12\x39\n\x02op\x18\x01 \x01(\x0e\x32\'.object_detection.protos.Hyperparams.Op:\x04\x43ONV\x12\x39\n\x0bregularizer\x18\x02 \x01(\x0b\x32$.object_detection.protos.Regularizer\x12\x39\n\x0binitializer\x18\x03 \x01(\x0b\x32$.object_detection.protos.Initializer\x12I\n\nactivation\x18\x04 \x01(\x0e\x32/.object_detection.protos.Hyperparams.Activation:\x04RELU\x12\x38\n\nbatch_norm\x18\x05 \x01(\x0b\x32\".object_detection.protos.BatchNormH\x00\x12=\n\x0fsync_batch_norm\x18\t \x01(\x0b\x32\".object_detection.protos.BatchNormH\x00\x12\x38\n\ngroup_norm\x18\x07 \x01(\x0b\x32\".object_detection.protos.GroupNormH\x00\x12#\n\x14regularize_depthwise\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x1d\n\x0e\x66orce_use_bias\x18\x08 \x01(\x08:\x05\x66\x61lse\"\x16\n\x02Op\x12\x08\n\x04\x43ONV\x10\x01\x12\x06\n\x02\x46\x43\x10\x02\"7\n\nActivation\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04RELU\x10\x01\x12\n\n\x06RELU_6\x10\x02\x12\t\n\x05SWISH\x10\x03\x42\x12\n\x10normalizer_oneof\"\xa6\x01\n\x0bRegularizer\x12@\n\x0el1_regularizer\x18\x01 \x01(\x0b\x32&.object_detection.protos.L1RegularizerH\x00\x12@\n\x0el2_regularizer\x18\x02 \x01(\x0b\x32&.object_detection.protos.L2RegularizerH\x00\x42\x13\n\x11regularizer_oneof\"\"\n\rL1Regularizer\x12\x11\n\x06weight\x18\x01 \x01(\x02:\x01\x31\"\"\n\rL2Regularizer\x12\x11\n\x06weight\x18\x01 \x01(\x02:\x01\x31\"\xd8\x02\n\x0bInitializer\x12[\n\x1ctruncated_normal_initializer\x18\x01 \x01(\x0b\x32\x33.object_detection.protos.TruncatedNormalInitializerH\x00\x12[\n\x1cvariance_scaling_initializer\x18\x02 \x01(\x0b\x32\x33.object_detection.protos.VarianceScalingInitializerH\x00\x12U\n\x19random_normal_initializer\x18\x03 \x01(\x0b\x32\x30.object_detection.protos.RandomNormalInitializerH\x00\x12#\n\x19keras_initializer_by_name\x18\x04 \x01(\tH\x00\x42\x13\n\x11initializer_oneof\"@\n\x1aTruncatedNormalInitializer\x12\x0f\n\x04mean\x18\x01 \x01(\x02:\x01\x30\x12\x11\n\x06stddev\x18\x02 \x01(\x02:\x01\x31\"\xc5\x01\n\x1aVarianceScalingInitializer\x12\x11\n\x06\x66\x61\x63tor\x18\x01 \x01(\x02:\x01\x32\x12\x16\n\x07uniform\x18\x02 \x01(\x08:\x05\x66\x61lse\x12N\n\x04mode\x18\x03 \x01(\x0e\x32\x38.object_detection.protos.VarianceScalingInitializer.Mode:\x06\x46\x41N_IN\",\n\x04Mode\x12\n\n\x06\x46\x41N_IN\x10\x00\x12\x0b\n\x07\x46\x41N_OUT\x10\x01\x12\x0b\n\x07\x46\x41N_AVG\x10\x02\"=\n\x17RandomNormalInitializer\x12\x0f\n\x04mean\x18\x01 \x01(\x02:\x01\x30\x12\x11\n\x06stddev\x18\x02 \x01(\x02:\x01\x31\"z\n\tBatchNorm\x12\x14\n\x05\x64\x65\x63\x61y\x18\x01 \x01(\x02:\x05\x30.999\x12\x14\n\x06\x63\x65nter\x18\x02 \x01(\x08:\x04true\x12\x14\n\x05scale\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x07\x65psilon\x18\x04 \x01(\x02:\x05\x30.001\x12\x13\n\x05train\x18\x05 \x01(\x08:\x04true\"\x0b\n\tGroupNorm')
)



_HYPERPARAMS_OP = _descriptor.EnumDescriptor(
  name='Op',
  full_name='object_detection.protos.Hyperparams.Op',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONV', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FC', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=585,
  serialized_end=607,
)
_sym_db.RegisterEnumDescriptor(_HYPERPARAMS_OP)

_HYPERPARAMS_ACTIVATION = _descriptor.EnumDescriptor(
  name='Activation',
  full_name='object_detection.protos.Hyperparams.Activation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELU', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELU_6', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SWISH', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=609,
  serialized_end=664,
)
_sym_db.RegisterEnumDescriptor(_HYPERPARAMS_ACTIVATION)

_VARIANCESCALINGINITIALIZER_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='object_detection.protos.VarianceScalingInitializer.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FAN_IN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAN_OUT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAN_AVG', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1494,
  serialized_end=1538,
)
_sym_db.RegisterEnumDescriptor(_VARIANCESCALINGINITIALIZER_MODE)


_HYPERPARAMS = _descriptor.Descriptor(
  name='Hyperparams',
  full_name='object_detection.protos.Hyperparams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='object_detection.protos.Hyperparams.op', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regularizer', full_name='object_detection.protos.Hyperparams.regularizer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initializer', full_name='object_detection.protos.Hyperparams.initializer', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activation', full_name='object_detection.protos.Hyperparams.activation', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_norm', full_name='object_detection.protos.Hyperparams.batch_norm', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sync_batch_norm', full_name='object_detection.protos.Hyperparams.sync_batch_norm', index=5,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group_norm', full_name='object_detection.protos.Hyperparams.group_norm', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regularize_depthwise', full_name='object_detection.protos.Hyperparams.regularize_depthwise', index=7,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='force_use_bias', full_name='object_detection.protos.Hyperparams.force_use_bias', index=8,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HYPERPARAMS_OP,
    _HYPERPARAMS_ACTIVATION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='normalizer_oneof', full_name='object_detection.protos.Hyperparams.normalizer_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=71,
  serialized_end=684,
)


_REGULARIZER = _descriptor.Descriptor(
  name='Regularizer',
  full_name='object_detection.protos.Regularizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='l1_regularizer', full_name='object_detection.protos.Regularizer.l1_regularizer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='l2_regularizer', full_name='object_detection.protos.Regularizer.l2_regularizer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='regularizer_oneof', full_name='object_detection.protos.Regularizer.regularizer_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=687,
  serialized_end=853,
)


_L1REGULARIZER = _descriptor.Descriptor(
  name='L1Regularizer',
  full_name='object_detection.protos.L1Regularizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight', full_name='object_detection.protos.L1Regularizer.weight', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=855,
  serialized_end=889,
)


_L2REGULARIZER = _descriptor.Descriptor(
  name='L2Regularizer',
  full_name='object_detection.protos.L2Regularizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight', full_name='object_detection.protos.L2Regularizer.weight', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=891,
  serialized_end=925,
)


_INITIALIZER = _descriptor.Descriptor(
  name='Initializer',
  full_name='object_detection.protos.Initializer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='truncated_normal_initializer', full_name='object_detection.protos.Initializer.truncated_normal_initializer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variance_scaling_initializer', full_name='object_detection.protos.Initializer.variance_scaling_initializer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='random_normal_initializer', full_name='object_detection.protos.Initializer.random_normal_initializer', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keras_initializer_by_name', full_name='object_detection.protos.Initializer.keras_initializer_by_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='initializer_oneof', full_name='object_detection.protos.Initializer.initializer_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=928,
  serialized_end=1272,
)


_TRUNCATEDNORMALINITIALIZER = _descriptor.Descriptor(
  name='TruncatedNormalInitializer',
  full_name='object_detection.protos.TruncatedNormalInitializer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mean', full_name='object_detection.protos.TruncatedNormalInitializer.mean', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stddev', full_name='object_detection.protos.TruncatedNormalInitializer.stddev', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1274,
  serialized_end=1338,
)


_VARIANCESCALINGINITIALIZER = _descriptor.Descriptor(
  name='VarianceScalingInitializer',
  full_name='object_detection.protos.VarianceScalingInitializer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='factor', full_name='object_detection.protos.VarianceScalingInitializer.factor', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(2),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uniform', full_name='object_detection.protos.VarianceScalingInitializer.uniform', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='object_detection.protos.VarianceScalingInitializer.mode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VARIANCESCALINGINITIALIZER_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1341,
  serialized_end=1538,
)


_RANDOMNORMALINITIALIZER = _descriptor.Descriptor(
  name='RandomNormalInitializer',
  full_name='object_detection.protos.RandomNormalInitializer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mean', full_name='object_detection.protos.RandomNormalInitializer.mean', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stddev', full_name='object_detection.protos.RandomNormalInitializer.stddev', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1540,
  serialized_end=1601,
)


_BATCHNORM = _descriptor.Descriptor(
  name='BatchNorm',
  full_name='object_detection.protos.BatchNorm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='decay', full_name='object_detection.protos.BatchNorm.decay', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.999),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='center', full_name='object_detection.protos.BatchNorm.center', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='object_detection.protos.BatchNorm.scale', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epsilon', full_name='object_detection.protos.BatchNorm.epsilon', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.001),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='train', full_name='object_detection.protos.BatchNorm.train', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1603,
  serialized_end=1725,
)


_GROUPNORM = _descriptor.Descriptor(
  name='GroupNorm',
  full_name='object_detection.protos.GroupNorm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1727,
  serialized_end=1738,
)

_HYPERPARAMS.fields_by_name['op'].enum_type = _HYPERPARAMS_OP
_HYPERPARAMS.fields_by_name['regularizer'].message_type = _REGULARIZER
_HYPERPARAMS.fields_by_name['initializer'].message_type = _INITIALIZER
_HYPERPARAMS.fields_by_name['activation'].enum_type = _HYPERPARAMS_ACTIVATION
_HYPERPARAMS.fields_by_name['batch_norm'].message_type = _BATCHNORM
_HYPERPARAMS.fields_by_name['sync_batch_norm'].message_type = _BATCHNORM
_HYPERPARAMS.fields_by_name['group_norm'].message_type = _GROUPNORM
_HYPERPARAMS_OP.containing_type = _HYPERPARAMS
_HYPERPARAMS_ACTIVATION.containing_type = _HYPERPARAMS
_HYPERPARAMS.oneofs_by_name['normalizer_oneof'].fields.append(
  _HYPERPARAMS.fields_by_name['batch_norm'])
_HYPERPARAMS.fields_by_name['batch_norm'].containing_oneof = _HYPERPARAMS.oneofs_by_name['normalizer_oneof']
_HYPERPARAMS.oneofs_by_name['normalizer_oneof'].fields.append(
  _HYPERPARAMS.fields_by_name['sync_batch_norm'])
_HYPERPARAMS.fields_by_name['sync_batch_norm'].containing_oneof = _HYPERPARAMS.oneofs_by_name['normalizer_oneof']
_HYPERPARAMS.oneofs_by_name['normalizer_oneof'].fields.append(
  _HYPERPARAMS.fields_by_name['group_norm'])
_HYPERPARAMS.fields_by_name['group_norm'].containing_oneof = _HYPERPARAMS.oneofs_by_name['normalizer_oneof']
_REGULARIZER.fields_by_name['l1_regularizer'].message_type = _L1REGULARIZER
_REGULARIZER.fields_by_name['l2_regularizer'].message_type = _L2REGULARIZER
_REGULARIZER.oneofs_by_name['regularizer_oneof'].fields.append(
  _REGULARIZER.fields_by_name['l1_regularizer'])
_REGULARIZER.fields_by_name['l1_regularizer'].containing_oneof = _REGULARIZER.oneofs_by_name['regularizer_oneof']
_REGULARIZER.oneofs_by_name['regularizer_oneof'].fields.append(
  _REGULARIZER.fields_by_name['l2_regularizer'])
_REGULARIZER.fields_by_name['l2_regularizer'].containing_oneof = _REGULARIZER.oneofs_by_name['regularizer_oneof']
_INITIALIZER.fields_by_name['truncated_normal_initializer'].message_type = _TRUNCATEDNORMALINITIALIZER
_INITIALIZER.fields_by_name['variance_scaling_initializer'].message_type = _VARIANCESCALINGINITIALIZER
_INITIALIZER.fields_by_name['random_normal_initializer'].message_type = _RANDOMNORMALINITIALIZER
_INITIALIZER.oneofs_by_name['initializer_oneof'].fields.append(
  _INITIALIZER.fields_by_name['truncated_normal_initializer'])
_INITIALIZER.fields_by_name['truncated_normal_initializer'].containing_oneof = _INITIALIZER.oneofs_by_name['initializer_oneof']
_INITIALIZER.oneofs_by_name['initializer_oneof'].fields.append(
  _INITIALIZER.fields_by_name['variance_scaling_initializer'])
_INITIALIZER.fields_by_name['variance_scaling_initializer'].containing_oneof = _INITIALIZER.oneofs_by_name['initializer_oneof']
_INITIALIZER.oneofs_by_name['initializer_oneof'].fields.append(
  _INITIALIZER.fields_by_name['random_normal_initializer'])
_INITIALIZER.fields_by_name['random_normal_initializer'].containing_oneof = _INITIALIZER.oneofs_by_name['initializer_oneof']
_INITIALIZER.oneofs_by_name['initializer_oneof'].fields.append(
  _INITIALIZER.fields_by_name['keras_initializer_by_name'])
_INITIALIZER.fields_by_name['keras_initializer_by_name'].containing_oneof = _INITIALIZER.oneofs_by_name['initializer_oneof']
_VARIANCESCALINGINITIALIZER.fields_by_name['mode'].enum_type = _VARIANCESCALINGINITIALIZER_MODE
_VARIANCESCALINGINITIALIZER_MODE.containing_type = _VARIANCESCALINGINITIALIZER
DESCRIPTOR.message_types_by_name['Hyperparams'] = _HYPERPARAMS
DESCRIPTOR.message_types_by_name['Regularizer'] = _REGULARIZER
DESCRIPTOR.message_types_by_name['L1Regularizer'] = _L1REGULARIZER
DESCRIPTOR.message_types_by_name['L2Regularizer'] = _L2REGULARIZER
DESCRIPTOR.message_types_by_name['Initializer'] = _INITIALIZER
DESCRIPTOR.message_types_by_name['TruncatedNormalInitializer'] = _TRUNCATEDNORMALINITIALIZER
DESCRIPTOR.message_types_by_name['VarianceScalingInitializer'] = _VARIANCESCALINGINITIALIZER
DESCRIPTOR.message_types_by_name['RandomNormalInitializer'] = _RANDOMNORMALINITIALIZER
DESCRIPTOR.message_types_by_name['BatchNorm'] = _BATCHNORM
DESCRIPTOR.message_types_by_name['GroupNorm'] = _GROUPNORM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Hyperparams = _reflection.GeneratedProtocolMessageType('Hyperparams', (_message.Message,), {
  'DESCRIPTOR' : _HYPERPARAMS,
  '__module__' : 'object_detection.protos.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.Hyperparams)
  })
_sym_db.RegisterMessage(Hyperparams)

Regularizer = _reflection.GeneratedProtocolMessageType('Regularizer', (_message.Message,), {
  'DESCRIPTOR' : _REGULARIZER,
  '__module__' : 'object_detection.protos.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.Regularizer)
  })
_sym_db.RegisterMessage(Regularizer)

L1Regularizer = _reflection.GeneratedProtocolMessageType('L1Regularizer', (_message.Message,), {
  'DESCRIPTOR' : _L1REGULARIZER,
  '__module__' : 'object_detection.protos.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.L1Regularizer)
  })
_sym_db.RegisterMessage(L1Regularizer)

L2Regularizer = _reflection.GeneratedProtocolMessageType('L2Regularizer', (_message.Message,), {
  'DESCRIPTOR' : _L2REGULARIZER,
  '__module__' : 'object_detection.protos.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.L2Regularizer)
  })
_sym_db.RegisterMessage(L2Regularizer)

Initializer = _reflection.GeneratedProtocolMessageType('Initializer', (_message.Message,), {
  'DESCRIPTOR' : _INITIALIZER,
  '__module__' : 'object_detection.protos.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.Initializer)
  })
_sym_db.RegisterMessage(Initializer)

TruncatedNormalInitializer = _reflection.GeneratedProtocolMessageType('TruncatedNormalInitializer', (_message.Message,), {
  'DESCRIPTOR' : _TRUNCATEDNORMALINITIALIZER,
  '__module__' : 'object_detection.protos.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.TruncatedNormalInitializer)
  })
_sym_db.RegisterMessage(TruncatedNormalInitializer)

VarianceScalingInitializer = _reflection.GeneratedProtocolMessageType('VarianceScalingInitializer', (_message.Message,), {
  'DESCRIPTOR' : _VARIANCESCALINGINITIALIZER,
  '__module__' : 'object_detection.protos.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.VarianceScalingInitializer)
  })
_sym_db.RegisterMessage(VarianceScalingInitializer)

RandomNormalInitializer = _reflection.GeneratedProtocolMessageType('RandomNormalInitializer', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMNORMALINITIALIZER,
  '__module__' : 'object_detection.protos.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.RandomNormalInitializer)
  })
_sym_db.RegisterMessage(RandomNormalInitializer)

BatchNorm = _reflection.GeneratedProtocolMessageType('BatchNorm', (_message.Message,), {
  'DESCRIPTOR' : _BATCHNORM,
  '__module__' : 'object_detection.protos.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.BatchNorm)
  })
_sym_db.RegisterMessage(BatchNorm)

GroupNorm = _reflection.GeneratedProtocolMessageType('GroupNorm', (_message.Message,), {
  'DESCRIPTOR' : _GROUPNORM,
  '__module__' : 'object_detection.protos.hyperparams_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.GroupNorm)
  })
_sym_db.RegisterMessage(GroupNorm)


# @@protoc_insertion_point(module_scope)
