import asyncio
from azure.identity.aio import ManagedIdentityCredential
from msgraph import GraphServiceClient

async def main():
    """
    使用托管身份憑據從 Microsoft Graph API 中獲取當前用戶的訊息並印出結果。
    """

    # 使用托管身份憑證進行身份驗證
    credential = ManagedIdentityCredential()

    # 創建 GraphServiceClient 實例，用於與 Microsoft Graph API 進行交互
    graph_client = GraphServiceClient(credential)

    # 異步調用 Microsoft Graph API 來獲取當前用戶訊息
    me = await graph_client.me.get()

    # 印出獲取到的用戶訊息
    print(me)

# 運行異步主函數
asyncio.run(main())
