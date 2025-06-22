
# ARM Template
This template will deploy following Azure Resources,

    * Azure Free Tier Web app with python 3.9 as runtime.
    * Azure storage account with Hot tier access for Blob usage.
    * Azure keyvault without any access policy configurations.
on the location which resource group created for each lab.


To deploy the ARM template run the follwoing command and it should feed with some unique number to make all the resources are unique for each lab user.


``` bash

az deployment group create --resource-group appTest --template-file template.json --parameters appName=apptest<unique number> keyVaultName=apptestvault<unique number> storageAccountName=apptestblobstorage<same unique number>

```


# Azure Web App Infrastructure Compliance Policy

## Overview
This consolidated Azure Policy enforces security and compliance standards for Python web application infrastructure, restricting resource creation to only essential components while ensuring secure configurations.

---

##  **ALLOWED OPERATIONS**

### **Web Applications**
• Deploy Azure Web Apps with Python 3.9 runtime

• Configure HTTPS-only web applications

• Create Free tier (F1) App Service Plans only

• Enable system-assigned managed identity on web apps

• Add application settings and environment variables

• Configure web app runtime settings

• Set up source control connections

### **Storage Services**
• Create Storage Accounts with secure configuration 
(HTTPS-only, TLS 1.2)

• Deploy Standard_LRS storage accounts for cost optimization

• Create blob containers and upload files

• Generate SAS (Shared Access Signature) tokens

• Configure storage account access policies

• Use blob, file, queue, and table services

### **Key Management**
• Create Key Vaults with Standard tier pricing

• Configure Key Vault access policies

• Store secrets, keys, and certificates

• Set up secure Key Vault configurations

• Disable deployment features for enhanced security

### **General Operations**
• Deploy only approved resource types

• Configure resource tags and metadata

• Set up monitoring and logging

• Create resource groups for organization

---

##  **RESTRICTIONS & LIMITATIONS**

### **Resource Type Restrictions**
• **Blocked**: Virtual Machines (VMs)

• **Blocked**: Virtual Networks (VNets) and networking components
• **Blocked**: SQL Databases and managed instances

• **Blocked**: Container instances and Kubernetes services

• **Blocked**: Logic Apps and Function Apps

• **Blocked**: Any resource type not explicitly allowed

### **Pricing & Tier Restrictions**
• **No Paid App Service Plans** - Only Free tier (F1) allowed

• **No Premium Storage** - Standard_LRS recommended/enforced

• **No Premium Key Vault** - Standard tier only

### **Security Restrictions**
• **No HTTP-only Web Apps** - HTTPS enforcement mandatory

• **No Insecure Storage** - Must have HTTPS-only and TLS 1.2

• **No Public Blob Access** - Storage accounts must disable public access

• **No Key Vault Deployment Features** - Enhanced security by disabling VM/template deployment access

### **Configuration Restrictions**
• **No Non-Python Runtimes** - Only Python 3.9 supported

• **No Insecure TLS** - Minimum TLS 1.2 required

• **No Weak Storage Encryption** - Secure defaults enforced

