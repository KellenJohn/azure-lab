import io
from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential


# 替換成您的 Storage Account 名和 managed identity 的 ClientID
account_name = "your-storage-account"
managed_identity_client_id = "xxxxxxx"

class BlobContainerManager:
    def __init__(self, credential):
        """
        BlobContainerManager 初始化函數。

        Parameters:
          - credential: DefaultAzureCredential 物件，用於身份驗證。
        """
        self.credential = credential

    def list_containers(self, blob_service_client: BlobServiceClient):
        """
        列出 Blob 容器。

        Parameters:
          - blob_service_client: BlobServiceClient 物件，用於連接 Blob 服務。

        Returns:
          無返回值，只輸出容器名稱和 metadata。
        """
        try:
            containers = blob_service_client.list_containers(include_metadata=True)
            for container in containers:
                print(container['name'], container['metadata'])
        except Exception as e:
            print("An error occurred while listing containers:", e)

    def list_blobs(self, blob_service_client: BlobServiceClient, container_name):
        """
        列出指定 Blob 容器中的所有 Blob。

        Parameters:
          - blob_service_client: BlobServiceClient 物件，用於連接 Blob 服務。
          - container_name: 要列出其 Blob 的容器名稱。

        Returns:
          一個生成器，用於迭代指定 Blob 容器中的所有 Blob。每次迭代返回一個 BlobClient 物件。
        """
        try:
            blob_container_client = blob_service_client.get_container_client(container_name)
            blobs = blob_container_client.list_blobs()
            return blobs
        except Exception as e:
            print("An error occurred while listing blobs:", e)

    def upload_blob(self, blob_service_client: BlobServiceClient, container_name, blob_name, data):
        """
        將數據上傳到 Blob 中。

        Parameters:
          - blob_service_client: BlobServiceClient 物件，用於連接 Blob 服務。
          - container_name: 要上傳到的容器名稱。
          - blob_name: 要上傳的 Blob 名稱。
          - data: 要上傳的數據，可以是 ByteIO、字符串或文件。

        Returns:
          無返回值。
        """
        try:
            blob_container_client = blob_service_client.get_container_client(container_name)
            blob_client = blob_container_client.get_blob_client(blob_name)
            blob_client.upload_blob(data)
        except Exception as e:
            print("An error occurred while uploading blob:", e)

    def download_blob_to_stream(self, blob_service_client: BlobServiceClient, container_name, blob_name):
        """
        下載 Blob 内容到 io.BytesIO()。

        Parameters:
          - blob_service_client: BlobServiceClient 物件，用於連接 Blob 服務。
          - container_name: 要下載 Blob 的容器名稱。
          - blob_name: 要下載的 Blob 名稱。
  
        Returns:
          無返回值，只輸出下載的 bytes。
        """
        try:
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
            # 使用 readinto() 方法將 Blob 内容直接下載到指定的 bytes (io.BytesIO() 物件) 中，並返回讀取的 bytes
            stream = io.BytesIO()
            num_bytes = blob_client.download_blob().readinto(stream)
            print(f"Number of bytes: {num_bytes}")  # 輸出讀取的 bytes
        except Exception as e:
            print("An error occurred while downloading blob:", e)

# 創建 DefaultAzureCredential 物件
credential = DefaultAzureCredential(managed_identity_client_id=managed_identity_client_id)
# 創建 BlobServiceClient 物件
blob_service_client = BlobServiceClient.from_connection_string(connection_string, credential=credential)
# 創建 BlobContainerManager 物件
container_manager = BlobContainerManager(credential)

if __name__ == "__main__":
    # Demo Case
    # Sample1. 調用 list_containers 方法
    container_manager.list_containers(blob_service_client)
    print('------------------------------------------------------------------')
    # Sample2. 調用 download_blob_to_stream 方法
    container_manager.download_blob_to_stream(blob_service_client, container_name="container-name", blob_name="your-data.file")
    print('------------------------------------------------------------------')
    # Sample3.  使用 list_blobs 方法列出指定容器中的所有 Blob
    container_name = "container-name"
    blob_container_client = blob_service_client.get_container_client(container_name)
    blobs = blob_container_client.list_blobs()
    # 遞迴印出每個 Blob
    for blob in blobs:
        print(blob.name)
    print('------------------------------------------------------------------')
    # Sample4. 指定要上傳的 Blob 名稱
    blob_name = "your-data.file"
    # 指定要上傳的文件路徑
    file_path = "/your-path/your-data.file"
    # 使用 get_container_client 方法獲取 BlobContainerClient 物件
    blob_container_client = blob_service_client.get_container_client(container_name)
    # 使用 get_blob_client 方法獲取要上傳的 Blob 的 BlobClient 物件
    blob_client = blob_container_client.get_blob_client(blob_name)
    # 調用 upload_blob 方法將文件上傳到 Blob 中
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)
     
