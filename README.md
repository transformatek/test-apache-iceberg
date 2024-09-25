# Test iceberg

Open in container
Minio Consol will be available at : [http://localhost:9001](http://localhost:9001)

```bash
cd src
python test_pyiceberg.py
```

Test using CLI
```bash
pyiceberg
pyiceberg --uri http://rest:8181 list 
pyiceberg --uri http://rest:8181 create namespace test
pyiceberg --uri http://rest:8181 list 
pyiceberg --uri http://rest:8181 list test
pyiceberg --uri http://rest:8181 describe test
```

Check data
```bash
pyiceberg
pyiceberg --uri http://rest:8181 list 
pyiceberg --uri http://rest:8181 list docs_example
pyiceberg --uri http://rest:8181 describe docs_example
pyiceberg --uri http://rest:8181 describe table docs_example.bids
# pyiceberg --uri http://rest:8181 drop table docs_example.bids
```

# Useful links

https://py.iceberg.apache.org/api
https://iceberg.apache.org