# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.servicefabricmanagedclusters import ServiceFabricManagedClustersManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-servicefabricmanagedclusters
# USAGE
    python node_type_put_operation_dedicated_host_example.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ServiceFabricManagedClustersManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.node_types.begin_create_or_update(
        resource_group_name="resRg",
        cluster_name="myCluster",
        node_type_name="BE",
        parameters={
            "properties": {
                "capacities": {},
                "dataDiskSizeGB": 200,
                "dataDiskType": "StandardSSD_LRS",
                "hostGroupId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/testhostgroupRG/providers/Microsoft.Compute/hostGroups/testHostGroup",
                "isPrimary": False,
                "placementProperties": {},
                "vmImageOffer": "WindowsServer",
                "vmImagePublisher": "MicrosoftWindowsServer",
                "vmImageSku": "2019-Datacenter",
                "vmImageVersion": "latest",
                "vmInstanceCount": 10,
                "vmSize": "Standard_D8s_v3",
                "zones": ["1"],
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/servicefabricmanagedclusters/resource-manager/Microsoft.ServiceFabric/preview/2023-12-01-preview/examples/NodeTypePutOperationDedicatedHost_example.json
if __name__ == "__main__":
    main()
