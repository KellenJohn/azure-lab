import io
import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential


class BlobContainerManager:
    def __init__(self, use_managed_identity: bool = True):
        """
        BlobContainerManager 初始化函數。

        Parameters:
            - credential: DefaultAzureCredential 物件，用於身份驗證。
            - 替換成您的 Storage Account 名和托管標識的客戶端 ID。
        """
        load_dotenv()

        self.account_name = os.getenv("ACCOUNT_NAME")
        self.managed_identity_client_id = os.getenv("MANAGED_IDENTITY_CLIENT_ID")
        self.connection_string = f"DefaultEndpointsProtocol=https;AccountName={self.account_name};"
        if use_managed_identity:
            self.credential = DefaultAzureCredential(managed_identity_client_id=self.managed_identity_client_id)
        else:
            self.access_key = os.getenv("ACCOUNT_KEY")
            self.connection_string += f"AccountKey={self.access_key};"
            self.credential = DefaultAzureCredential()

        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_string, credential=self.credential)

   def list_containers(self):
        """
        列出 Blob 容器。

        Parameters:
            - blob_service_client: BlobServiceClient 物件，用於連接 Blob 服務。

        Returns:
            無返回值，只輸出容器名稱和 metadata。
        """
        try:
            containers = self.blob_service_client.list_containers(include_metadata=True)
            for container in containers:
                print(container['name'], container['metadata'])
        except Exception as e:
            print("An error occurred while listing containers:", e)

    def list_blobs(self, container_name):
        """
        列出指定 Blob 容器中的所有 Blob。

        Parameters:
            - blob_service_client: BlobServiceClient 物件，用於連接 Blob 服務。
            - container_name: 要列出其 Blob 的容器名稱。

        Returns:
            一個生成器，用於迭代指定 Blob 容器中的所有 Blob。每次迭代返回一個 BlobClient 物件。
        """
        try:
            blob_container_client = self.blob_service_client.get_container_client(container_name)
            blobs = blob_container_client.list_blobs()
            return blobs
        except Exception as e:
            print("An error occurred while listing blobs:", e)

    def upload_blob(self, container_name, blob_name, data):
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
            blob_container_client = self.blob_service_client.get_container_client(container_name)
            blob_client = blob_container_client.get_blob_client(blob_name)
            blob_client.upload_blob(data)
        except Exception as e:
            print("An error occurred while uploading blob:", e)

    def download_blob_to_stream(self, container_name, blob_name):
        """
        下載 Blob 内容到 io.BytesIO()。

        Parameters:
            - blob_service_client: BlobServiceClient 物件，用於連接 Blob 服務。
            - container_name: 要下載 Blob 的容器名稱。
            - blob_name: 要下載的 Blob 名稱。

        Returns:
            無返回值，只輸出下載的 byteＳ。
        """
        try:
            blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=blob_name)

            # 使用 readinto() 方法將 Blob 内容直接下載到指定的字節流 (io.BytesIO() 物件) 中，並返回讀取的字節數
            stream = io.BytesIO()
            num_bytes = blob_client.download_blob().readinto(stream)
            print(f"Number of bytes: {num_bytes}")  # 輸出讀取的字節數 
        except Exception as e:
            print("An error occurred while downloading blob:", e)


if __name__ == "__main__":
    # 創建 BlobContainerManager 物件
    container_manager = BlobContainerManager()
    # 調用 list_containers 方法
    container_manager.list_containers()
    print('------------------------------------------------------------------')
    # 調用 download_blob_to_stream 方法
    container_manager.download_blob_to_stream(container_name="remote-check", blob_name="sample-data.csv")
    print('------------------------------------------------------------------')
    # 使用 list_blobs 方法列出指定容器中的所有 Blob
    container_name = "remote-check"
    blob_container_client = container_manager.blob_service_client.get_container_client(container_name)
    blobs = blob_container_client.list_blobs()
    # 遞迴印每个 Blob 的名稱
    for blob in blobs:
        print(blob.name)
    print('------------------------------------------------------------------')
