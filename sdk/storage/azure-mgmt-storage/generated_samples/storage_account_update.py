# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.storage import StorageManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-storage
# USAGE
    python storage_account_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = StorageManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscription-id}",
    )

    response = client.storage_accounts.update(
        resource_group_name="res9407",
        account_name="sto8596",
        parameters={
            "properties": {
                "allowBlobPublicAccess": False,
                "allowSharedKeyAccess": True,
                "defaultToOAuthAuthentication": False,
                "enableExtendedGroups": True,
                "encryption": {
                    "keySource": "Microsoft.Storage",
                    "services": {
                        "blob": {"enabled": True, "keyType": "Account"},
                        "file": {"enabled": True, "keyType": "Account"},
                    },
                },
                "isLocalUserEnabled": True,
                "isSftpEnabled": True,
                "keyPolicy": {"keyExpirationPeriodInDays": 20},
                "minimumTlsVersion": "TLS1_2",
                "networkAcls": {
                    "defaultAction": "Allow",
                    "resourceAccessRules": [
                        {
                            "resourceId": "/subscriptions/a7e99807-abbf-4642-bdec-2c809a96a8bc/resourceGroups/res9407/providers/Microsoft.Synapse/workspaces/testworkspace",
                            "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
                        }
                    ],
                },
                "routingPreference": {
                    "publishInternetEndpoints": True,
                    "publishMicrosoftEndpoints": True,
                    "routingChoice": "MicrosoftRouting",
                },
                "sasPolicy": {"expirationAction": "Log", "sasExpirationPeriod": "1.15:59:59"},
            }
        },
    )
    print(response)


# x-ms-original-file: specification/storage/resource-manager/Microsoft.Storage/stable/2023-05-01/examples/StorageAccountUpdate.json
if __name__ == "__main__":
    main()
