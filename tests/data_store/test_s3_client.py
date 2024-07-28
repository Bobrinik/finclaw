from finclaw.data_store.storage_clients.S3Client import S3StoreClient


def test_store_client_path_1():
    store_client = S3StoreClient(bucket_name="test_bucket", region="us-east-1")
    result = store_client.get_store_path("my_path")
    assert result == "test_bucket/my_path"


def test_store_client_path_2():
    store_client = S3StoreClient(bucket_name="test_bucket", region="us-east-1")
    result = store_client.get_store_path("/my_path")
    assert result == "test_bucket/my_path"
