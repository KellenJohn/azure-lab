#### 使用托管身份憑證從 Microsoft Graph API 中獲取群組列表並印出每個群組的名稱和 ID。
##### test-group.py
* (MS list group ref)[https://learn.microsoft.com/en-us/graph/api/group-list?view=graph-rest-1.0&tabs=python]

```json
[
    {
        "Group Display Name": "GraphAPI",
        "Group ID": "fffffff-4847-443e-9a44-xxxxxxxxx",
        "Description": "GraphAPI",
        "Mail": null,
        "Mail Nickname": "09196145-7",
        "Visibility": null,
        "Created DateTime": "2024-05-25 15:09:00",
        "Group Types": [],
        "Security Enabled": true
    }
]
```


####  使用托管身份憑證從 Azure AD 中獲取所有應用註冊並印出每個應用的顯示名稱和object ID
##### test-me.py

```json
{
    "additional_data": {
        "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users/$entity"
    },
    "id": "ffffffc5-f5be-4be8-oooo-xxxxxxxxxxxx",
    "odata_type": "#microsoft.graph.user",
    "deleted_date_time": null,
    "about_me": null,
    "account_enabled": null,
    "activities": null,
    "age_group": null,
    "agreement_acceptances": null,
    "app_role_assignments": null,
    "assigned_licenses": null,
    "assigned_plans": null,
    "authentication": null,
    "authorization_info": null,
    "birthday": null,
    "business_phones": [],
    "calendar": null,
    "calendar_groups": null,
    "calendar_view": null,
    "calendars": null,
    "chats": null,
    "city": null,
    "cloud_clipboard": null,
    "company_name": null,
    "consent_provided_for_minor": null,
    "contact_folders": null,
    "contacts": null,
    "country": null,
    "created_date_time": null,
    "created_objects": null,
    "creation_type": null,
    "custom_security_attributes": null,
    "department": null,
    "device_enrollment_limit": null,
    "device_management_troubleshooting_events": null,
    "direct_reports": null,
    "display_name": "Stacy Fubar",
    "drive": null,
    "drives": null,
    "employee_experience": null,
    "employee_hire_date": null,
    "employee_id": null,
    "employee_leave_date_time": null,
    "employee_org_data": null,
    "employee_type": null,
    "events": null,
    "extensions": null,
    "external_user_state": null,
    "external_user_state_change_date_time": null,
    "fax_number": null,
    "followed_sites": null,
    "given_name": "Stacy",
    "hire_date": null,
    "identities": null,
    "im_addresses": null,
    "inference_classification": null,
    "insights": null,
    "interests": null,
    "is_resource_account": null,
    "job_title": null,
    "joined_teams": null,
    "last_password_change_date_time": null,
    "legal_age_group_classification": null,
    "license_assignment_states": null,
    "license_details": null,
    "mail": null,
    "mail_folders": null,
    "mail_nickname": null,
    "mailbox_settings": null,
    "managed_app_registrations": null,
    "managed_devices": null,
    "manager": null,
    "member_of": null,
    "messages": null,
    "mobile_phone": null,
    "my_site": null,
    "oauth2_permission_grants": null,
    "office_location": null,
    "on_premises_distinguished_name": null,
    "on_premises_domain_name": null,
    "on_premises_extension_attributes": null,
    "on_premises_immutable_id": null,
    "on_premises_last_sync_date_time": null,
    "on_premises_provisioning_errors": null,
    "on_premises_sam_account_name": null,
    "on_premises_security_identifier": null,
    "on_premises_sync_enabled": null,
    "on_premises_user_principal_name": null,
    "onenote": null,
    "online_meetings": null,
    "other_mails": null,
    "outlook": null,
    "owned_devices": null,
    "owned_objects": null,
    "password_policies": null,
    "password_profile": null,
    "past_projects": null,
    "people": null,
    "permission_grants": null,
    "photo": null,
    "photos": null,
    "planner": null,
    "postal_code": null,
    "preferred_data_location": null,
    "preferred_language": "en",
    "preferred_name": null,
    "presence": null,
    "print": null,
    "provisioned_plans": null,
    "proxy_addresses": null,
    "registered_devices": null,
    "responsibilities": null,
    "schools": null,
    "scoped_role_member_of": null,
    "security_identifier": null,
    "service_provisioning_errors": null,
    "settings": null,
    "show_in_address_list": null,
    "sign_in_activity": null,
    "sign_in_sessions_valid_from_date_time": null,
    "skills": null,
    "sponsors": null,
    "state": null,
    "street_address": null,
    "surname": "Fubar",
    "teamwork": null,
    "todo": null,
    "transitive_member_of": null,
    "usage_location": null,
    "user_principal_name": "fubar_hotmail.com#EXT#@fubarhotmail.onmicrosoft.com",
    "user_type": null
}
```


#### 使用托管身份憑據從 Microsoft Graph API 中獲取當前用戶的訊息並印出結果。
##### test-app-registration.py

```sh
App Display Name: mykeyvaultapp, Object ID: ffffffff-6325-oooo-a3f3-xxxxxxxxxxxx
App Display Name: EchoBot-MultiTenant, Object ID: ffffffff-727b-oooo-8014-xxxxxxxxxxxx
App Display Name: Miscrosoft GraphAPI, Object ID: ffffffff-f2e5-oooo-bb09-xxxxxxxxxxxx
App Display Name: Teams-Assistant-SRE, Object ID: ffffffff-7317-oooo-b566-xxxxxxxxxxxx
```
