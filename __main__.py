import pulumi
import pulumi_azure_native as azure_native

virtual_network=azure_native.network.VirtualNetwork("virtualNetwork",
    address_space=azure_native.network.AddressSpaceArgs(
      address_prefixes=["10.0.0.0/16"],  
    ),
    subnets=[azure_native.network.SubnetArgs(
        address_prefixes=["10.0.0.0/24"],
        name="all-resource-Subnet",
    ),],
    location="westeurope",
    resource_group_name="all-resource-RG",
    virtual_network_name="all-resource-VNET"
    
),

network_security_group=azure_native.network.NetworkSecurityGroup("NSG",
    location="westeurope",
    resource_group_name="all-resource-RG",
    network_security_group_name="all-resources-NSG",
    security_rules=[{
        "access": "Allow",
        "destinationAddressPrefix": "*",
        "destinationPortRange": "80",
        "direction": "Inbound",
        "name": "rule1",
        "priority": 130,
        "protocol": "*",
        "sourceAddressPrefix": "*",
        "sourcePortRange": "*",
        },],
    
),
publicIp=azure_native.network.PublicIPAddress("publicIPAddress",
    idle_timeout_in_minutes=4,
    location="westeurope",
    public_ip_address_version="IPv4",
    public_ip_allocation_method="Static",
    public_ip_address_name="all-resource-PUIP",
    resource_group_name="all-resource-RG",
    sku=azure_native.network.PublicIPAddressSkuArgs(
        name="Standard",
        tier="Global",
    ),
    tags={
        "environemt" : "Development",
    }

),
