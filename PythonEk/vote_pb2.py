# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: vote.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'vote.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nvote.proto\"\x1d\n\x0bVoteRequest\x12\x0e\n\x06VoteId\x18\x01 \x01(\t\"5\n\rCandidateData\x12\x15\n\rcandidateName\x18\x01 \x01(\t\x12\r\n\x05votes\x18\x02 \x01(\x05\"B\n\x0cVoteResponse\x12\x0e\n\x06VoteId\x18\x01 \x01(\t\x12\"\n\ncandidates\x18\x02 \x03(\x0b\x32\x0e.CandidateData2;\n\x0bVoteService\x12,\n\x0bgetVoteData\x12\x0c.VoteRequest\x1a\r.VoteResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vote_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_VOTEREQUEST']._serialized_start=14
  _globals['_VOTEREQUEST']._serialized_end=43
  _globals['_CANDIDATEDATA']._serialized_start=45
  _globals['_CANDIDATEDATA']._serialized_end=98
  _globals['_VOTERESPONSE']._serialized_start=100
  _globals['_VOTERESPONSE']._serialized_end=166
  _globals['_VOTESERVICE']._serialized_start=168
  _globals['_VOTESERVICE']._serialized_end=227
# @@protoc_insertion_point(module_scope)
