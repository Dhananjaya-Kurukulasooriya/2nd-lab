
Step 3: Test and Verify Deployment

This concluding phase involves the rigorous testing of the deployed application to confirm its intended functionality, including the secure retrieval of secrets and the successful display of the image.

    Restart App Service:

        In your App Service's left-hand navigation pane, click "Overview."

        Locate and click the "Restart" button situated at the top of the overview blade. Confirm the restart operation when prompted. This action is essential for the App Service to refresh its configuration, incorporate the newly applied Key Vault settings, and establish connections utilizing its Managed Identity.

    Access Application URL:

        Upon completion of the App Service restart (which may require a brief period), navigate to the "Overview" blade of your App Service.

        Locate the "URL" link (e.g., https://securegreetingapp-yourname.azurewebsites.net/) and click it to open the deployed application in a new browser tab.

    Validate Secret and Image Retrieval:

        Observe the content presented on the rendered web page. A prominent heading, "Welcome to My Secure App!," should be clearly visible.

        Directly beneath this heading, the greeting message: "Hello from Azure Key Vault! This message is super secret." should be displayed.

        Subsequently, the image sourced from Azure Blob Storage should be rendered within the page.

        This validation confirms that the Azure App Service has successfully utilized its Managed Identity to authenticate with Key Vault, retrieved both the GREETING-MESSAGE and BLOB-SAS-TOKEN secrets, and subsequently employed the SAS token to securely access and display the image from Azure Blob Storage.

    Update Secrets and Re-verify (Optional):

        Return to your Azure Key Vault's overview blade.

        In the left-hand navigation pane, click "Secrets," then select GREETING-MESSAGE.

        Click the "+ New Version" button at the top of the interface.

        Input a revised value for the secret (e.g., Updated Greeting: Hello from Key Vault v2!).

        Click "Create."

        Similarly, should there be a requirement to update the image or the SAS token, a new SAS token would be generated for your blob within the Storage Account (refer to Step 1.7), and subsequently, the BLOB-SAS-TOKEN secret in Key Vault would be updated with this new token.

        Return to your App Service "Overview" blade and initiate another "Restart" operation.

        Refresh the web application page in the browser. Any updated messages and the image (if the SAS token was refreshed for a new image or to renew access) should now be visible, thereby demonstrating the dynamic configuration update capability without necessitating any code modifications or redeployment.

    Troubleshooting Guidance (if required):

        In instances where secrets or the image are not displayed, or default messages/broken image icons are observed:

            Review the App Service logs (accessible in the left-hand navigation pane, under "Monitoring," by clicking "Log stream") for any error messages pertinent to Key Vault or Blob Storage access.

            Verify that the App Service's Managed Identity possesses the correct "Get" permission for secrets within Key Vault's "Access policies."

            Meticulously re-examine the precise SecretUri formats specified in your App Service's "Configuration" -> "Application settings," as typographical errors can impede successful retrieval.

            Ensure the BLOB-SAS-TOKEN stored in Key Vault is accurate and precisely matches the token generated for your blob.

            Confirm that the BLOB_STORAGE_URL application setting is correctly configured, representing the complete URL to the image excluding the SAS token.

            Verify that the permissions granted on the Blob Storage SAS token explicitly include "Read" access.

            Ascertain that the App Service has been restarted subsequent to all configuration modifications.

This laboratory exercise conclusively demonstrates the secure retrieval of secrets (including an access token) and the secure display of an image, leveraging Azure Key Vault, Managed Identity, and Azure Blob Storage, all within a GitHub-deployed Azure App Service environment.