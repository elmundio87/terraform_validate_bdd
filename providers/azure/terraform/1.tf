resource "azurerm_resource_group" "testrg" {
    name = "resourceGroupName"
    location = "westus"
}

resource "azurerm_storage_account" "testsa" {
    name = "storageaccountname"
    resource_group_name = "${azurerm_resource_group.testrg.name}"

    enable_blob_encryption = "True"
    
    tags {
      Platform = "${var.platform}"
      Name = "${var.platform}_${var.environment}_bar"
      Owner = "${var.owner}"
      Environment = "${var.environment}"
    }
}
