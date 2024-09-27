
from pyiceberg.catalog import load_catalog
import pyarrow as pa
from pyarrow import csv
import duckdb

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

fn = '1000-sales-records.csv'
csv_data = csv.read_csv(fn)
# print(csv_data)

ns = catalog.list_namespaces()
print(ns)

# catalog.create_table(
#         identifier="docs_example.sales",
#         schema=csv_data.schema,
#     )

# table = catalog.load_table("docs_example.sales")
# table.append(csv_data)

table = catalog.load_table("docs_example.sales")
table_content = table.scan().to_arrow()
# print(table)
print(table_content)

# connect to an in-memory database
con = duckdb.connect()

# query the Apache Arrow Table "my_arrow_table" and return as an Arrow Table
results = con.execute("SELECT * FROM table_content WHERE id <= 3").arrow()
print(results)