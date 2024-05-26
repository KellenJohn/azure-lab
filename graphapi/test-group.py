import asyncio
import json
from azure.identity.aio import ManagedIdentityCredential
from msgraph import GraphServiceClient

async def main():
    """
    使用托管身份憑證從 Microsoft Graph API 中獲取群組列表並印出每個群組的名稱和 ID。
    """

    # 使用托管身份憑證進行身份驗證
    credential = ManagedIdentityCredential()

    # 創建 GraphServiceClient 物件，用於與 Microsoft Graph API 進行交互
    graph_client = GraphServiceClient(credential)

    # 異步調用 Microsoft Graph API 來獲取群组列表
    groups_response = await graph_client.groups.get()

    # 提取群组列表
    groups = groups_response.value

    # 初始化一個空列表來儲存群组資訊
    groups_info = []

    # 遍歷每個群组，將詳細資訊以字典形式添加到列表中
    for group in groups:
        group_info = {
            "Group Display Name": group.display_name,
            "Group ID": group.id,
            "Description": group.description,
            "Mail": group.mail,
            "Mail Nickname": group.mail_nickname,
            "Visibility": group.visibility,
            "Created DateTime": group.created_date_time.strftime('%Y-%m-%d %H:%M:%S'),  # 將 datetime 物件轉 String
            "Group Types": group.group_types,
            "Security Enabled": group.security_enabled
        }
        groups_info.append(group_info)

    # 將群组資訊列表輸出為 JSON 格式
    json_output = json.dumps(groups_info, indent=4)
    print(json_output)

# 運行異步主函數
asyncio.run(main())
