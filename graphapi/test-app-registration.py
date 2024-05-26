import asyncio
from azure.identity.aio import ManagedIdentityCredential
from msgraph import GraphServiceClient

async def main():
    """
    使用托管身份憑據從 Azure AD 中獲取所有應用註冊並印出每個應用的顯示名稱和 object ID。
    """

    # 使用托管身份憑證
    credential = ManagedIdentityCredential()

    # 創建 GraphServiceClient 實例
    graph_client = GraphServiceClient(credential)

    # 獲取應用註冊列表
    apps_response = await graph_client.applications.get()

    # 提取應用程式列表
    apps = apps_response.value

    # 打印每個應用的 object ID 和其他信息
    for app in apps:
        print(f"App Display Name: {app.display_name}, Object ID: {app.id}")

# 運行異步主函數
asyncio.run(main())
