from pyiceberg.catalog import load_catalog
import pyarrow as pa

catalog = load_catalog(
    "docs",
    **{
        "uri": "http://rest:8181",
        "s3.endpoint": "http://minio:9000",
        "py-io-impl": "pyiceberg.io.pyarrow.PyArrowFileIO",
        "s3.access-key-id": "admin",
        "s3.secret-access-key": "password",
    }
)

# catalog.create_namespace("docs_example")

ns = catalog.list_namespaces()
print(ns)

tables = catalog.list_tables("docs_example")
print(tables)


schema = pa.schema(
    [
        pa.field("foo", pa.string(), nullable=True),
        pa.field("bar", pa.int64(), nullable=False),
        pa.field("baz", pa.bool_(), nullable=True),
    ]
)

table_exists = catalog.table_exists("docs_example.bids")
print(table_exists)

# if not table_exists :
#     catalog.create_table(
#         identifier="docs_example.bids",
#         schema=schema,
#     )

table = catalog.load_table("docs_example.bids")
# Equivalent to:
# table = catalog.load_table(("docs_example", "bids"))
# The tuple syntax can be used if the namespace or table contains a dot.
# print(table)


df = pa.Table.from_pylist(
    [
        {"foo": "Amsterdam", "bar": 52, "baz": True},
        {"foo": "Alger", "bar": 2, "baz": False},
        {"foo": "Ain Temouchent", "bar": 52, "baz": True},
    ],
    schema=schema
)
table.append(df)

table = catalog.load_table("docs_example.bids")
print(table)

table_content = table.scan().to_arrow()

print(table_content)