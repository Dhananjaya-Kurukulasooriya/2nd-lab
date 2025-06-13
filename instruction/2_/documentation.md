Step 2: Configure Azure App Service Integration

This section details the integration of the pre-existing Azure App Service with your GitHub repository for continuous deployment, and the subsequent configuration of Managed Identity and Key Vault linkages.

    Access the Pre-Provisioned Azure App Service:

        Navigate to the overview blade of your pre-provisioned Azure App Service (e.g., securegreetingapp-yourname) within the Azure portal.

    Configure Deployment Center via GitHub:

        In the left-hand navigation pane, under the "Deployment" section, click "Deployment Center."

        For "Source," select the "GitHub" option.

        If an authorization prompt appears, click "Authorize" to grant Azure the necessary access to your GitHub account, adhering to any on-screen directives.

        For "Organization," select the pertinent GitHub organization or personal account.

        For "Repository," select the public GitHub repository that contains your app.py and requirements.txt files (e.g., SecureGreetingApp).

        For "Branch," select main or the specific branch housing your application's source code.

        For "Build Provider," select "GitHub Actions."

        Click the "Save" button located at the top to initiate the continuous deployment configuration. This action concurrently generates a GitHub Actions workflow definition file within your designated repository.

    Monitor GitHub Actions Workflow:

        Open a new browser tab and navigate to your GitHub repository (e.g., https://github.com/your-username/SecureGreetingApp).

        Click on the "Actions" tab. A newly initiated workflow run, triggered by the App Service setup, should be visible. Monitor its progression. This workflow is designed to build and deploy your Flask application to the Azure App Service. In the event of a workflow failure, it is advisable to review the detailed execution logs to identify and diagnose any encountered error conditions.

    Configure Flask Application Startup Command:

        In your App Service's left-hand navigation pane, under "Settings," click "Configuration."

        Select the "General settings" tab.

        Locate the "Startup Command" section.

        In the corresponding text field, input the following command: gunicorn --worker-class gevent --workers 4 --bind 0.0.0.0:8000 app:app

        Click the "Save" button positioned at the top of the Configuration blade. This command is fundamental for instructing the App Service on the proper execution of your Flask application within the Linux environment.

    Enable System-Assigned Managed Identity:

        In your App Service's left-hand navigation pane, under "Settings," click "Identity."

        Select the "System assigned" tab.

        Toggle the "Status" switch to "On."

        Click the "Save" button.

        Upon receiving the prompt "Enable system assigned managed identity?", confirm the action by clicking "Yes." This operation provisions an automatically managed identity for your App Service within Azure Active Directory, thereby enabling secure authentication with other Azure services, such as Key Vault, without the necessity of explicit credential management. The "Object ID" displayed may be noted for record-keeping, though it is not directly employed in subsequent procedural steps.

    Grant Key Vault Secret Access to App Service:

        Return to your Azure Key Vault's overview blade within the Azure portal.

        In the left-hand navigation pane, click "Access policies."

        Click the "+ Create" button at the top of the interface.

        For "Secret permissions," select the "Get" checkbox.

        Click "Next."

        For "Principal," click the "+ Select principal" button.

        In the search field, enter the name of your App Service (e.g., securegreetingapp-yourname) and select its corresponding Managed Identity from the presented results.

        Click the "Select" button at the bottom.

        Click "Next."

        Proceed to "Review + create," and then click "Create" to establish the access policy.

    Link Key Vault Secrets to App Service Settings:

        Return to your App Service's overview blade within the Azure portal.

        In the left-hand navigation pane, under "Settings," click "Configuration."

        Select the "Application settings" tab.

        Click the "New application setting" button to configure the greeting message:

            For "Name," specify GREETING_MESSAGE.

            For "Value," enter the following expression: @Microsoft.KeyVault(SecretUri=https://<your-keyvault-name>.vault.azure.net/secrets/GREETING-MESSAGE/)

            Important: Substitute <your-keyvault-name> with the actual name of your Azure Key Vault instance (e.g., mysecureappkv).

            For "Deployment slot setting," leave this option unchecked.

            Click "OK."

        Click the "New application setting" button again to configure the Blob SAS token:

            For "Name," specify BLOB_SAS_TOKEN.

            For "Value," enter the following expression: @Microsoft.KeyVault(SecretUri=https://<your-keyvault-name>.vault.azure.net/secrets/BLOB-SAS-TOKEN/)

            Important: Substitute <your-keyvault-name> with the actual name of your Azure Key Vault instance.

            For "Deployment slot setting," leave this option unchecked.

            Click "OK."

        Click the "New application setting" button one more time to configure the Blob Storage base URL:

            For "Name," specify BLOB_STORAGE_URL.

            For "Value," input the complete base URL for your image, excluding the SAS token. This URL will typically conform to the format https://<storage-account-name>.blob.core.windows.net/<container-name>/<image-name> (e.g., https://mysecureblobstorageyourname.blob.core.windows.net/images/secretimage.png).

            For "Deployment slot setting," leave this option unchecked.

            Click "OK."

        Finally, click the "Save" button located at the top of the Configuration blade.
