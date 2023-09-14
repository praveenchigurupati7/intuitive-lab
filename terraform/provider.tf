terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.0.0"
    }
  }
}

provider "azurerm" {
  features {}
}

terraform {
  backend "azurerm" {
    resource_group_name  = "tfstaterg"
    storage_account_name = "intutivetfstatesa"
    container_name       = "intutivetfstatesac"
    key                  = "feature.terraform.tfstate"
  }
}
