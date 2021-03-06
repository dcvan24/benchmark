#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *

SERIALIZATION_LIB = "serialization.lib"
SERIALIZATION_CLASS = "serialization.class"
SERIALIZATION_FORMAT = "serialization.format"
SERIALIZATION_DDL = "serialization.ddl"
SERIALIZATION_NULL_FORMAT = "serialization.null.format"
SERIALIZATION_LAST_COLUMN_TAKES_REST = "serialization.last.column.takes.rest"
SERIALIZATION_SORT_ORDER = "serialization.sort.order"
SERIALIZATION_USE_JSON_OBJECTS = "serialization.use.json.object"
FIELD_DELIM = "field.delim"
COLLECTION_DELIM = "colelction.delim"
LINE_DELIM = "line.delim"
MAPKEY_DELIM = "mapkey.delim"
QUOTE_CHAR = "quote.delim"
ESCAPE_CHAR = "escape.delim"
VOID_TYPE_NAME = "void"
BOOLEAN_TYPE_NAME = "boolean"
TINYINT_TYPE_NAME = "tinyint"
SMALLINT_TYPE_NAME = "smallint"
INT_TYPE_NAME = "int"
BIGINT_TYPE_NAME = "bigint"
FLOAT_TYPE_NAME = "float"
DOUBLE_TYPE_NAME = "double"
STRING_TYPE_NAME = "string"
CHAR_TYPE_NAME = "char"
VARCHAR_TYPE_NAME = "varchar"
DATE_TYPE_NAME = "date"
DATETIME_TYPE_NAME = "datetime"
TIMESTAMP_TYPE_NAME = "timestamp"
DECIMAL_TYPE_NAME = "decimal"
BINARY_TYPE_NAME = "binary"
LIST_TYPE_NAME = "array"
MAP_TYPE_NAME = "map"
STRUCT_TYPE_NAME = "struct"
UNION_TYPE_NAME = "uniontype"
LIST_COLUMNS = "columns"
LIST_COLUMN_TYPES = "columns.types"
PrimitiveTypes = set([
  "void",
  "boolean",
  "tinyint",
  "smallint",
  "int",
  "bigint",
  "float",
  "double",
  "string",
  "varchar",
  "char",
  "date",
  "datetime",
  "timestamp",
  "decimal",
  "binary",
])
CollectionTypes = set([
  "array",
  "map",
])
IntegralTypes = set([
  "tinyint",
  "smallint",
  "int",
  "bigint",
])
