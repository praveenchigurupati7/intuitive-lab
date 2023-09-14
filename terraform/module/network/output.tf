output "vnet-name" {
  value = azurerm_virtual_network.vnet.name
}

output "nics" {
  value = toset([for nic in azurerm_network_interface.netowrk-interface : nic.id])
}