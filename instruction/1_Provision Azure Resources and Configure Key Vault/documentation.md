In modern cloud application development, securely handling sensitive configuration data like database connection strings, API keys, and access tokens is paramount, as embedding these **secrets** directly into code or repositories poses significant risks. This lab will focus on leveraging Azure Key Vault, a cloud service for securely storing secrets, to enhance the security of Azure Web Apps. We'll demonstrate how to store sensitive environment variables and highly sensitive Shared Access Signature (SAS) tokens within Key Vault, enabling your Azure Web Apps to dynamically and securely retrieve these values at runtime, eliminating hardcoding and establishing a best practice for secret management in your cloud applications.

This guide delineates the comprehensive process for deploying a Flask web application to Azure App Service. The methodology emphasizes the ` secure retrieval` of two distinct secrets—specifically, a textual *greeting message* and an *Azure Blob Storage Shared Access Signature (SAS) token*—from Azure Key Vault, facilitated by Azure Managed Identity. Subsequently, the application will demonstrate the display of an image directly sourced from Azure Blob Storage, utilizing the aforementioned SAS token. 

- [ ] Need to mention how we going to deploy the code.
- [ ] Need to define login steps.
- [ ] add the final keyvault ss
  
## Instructions
 
---

Create Blob Container and Upload Image to Storage Account:

1. Search for Storage Accounts in Azure portal and select Storage Accounts resource.
    
   ![1](./assets/image1.png)

2. In the left-hand **navigation pane**( `Overview` blade), under `Data storage` click `Containers`.

   ![2](./assets/snapshot5.png)

3. Click the `Add Container` button. and provide the required information as follow,

     ![3.a](./assets/snapshot6.png)

     `Name` = *images*.

     `Anonymous access level` select `Private (no anonymous access)` to enforce stringent security for the stored image.

     ![3.b](./assets/snapshot7.png)

4.  Click `Create`.
   
    ![4](./assets/image2.png)
   

5. Let's upload an image into the newly created **images** container. Go to the `images` container and Click the `Upload` button.

    ![5](./assets/snapshot8.png)

6. Click `Browse for files` and select a small image file (e.g., a .png or .jpg format) from your local machine. It is advisable to rename the file to a concise identifier such as *secretimage.png* if not already appropriately named and Click `Upload`.
   ![6](./assets/snapshot9.png)


     

---
Generate Shared Access Signature (SAS) Token for the Blob:

7. Within the images container in your Storage Account, locate and select the *secretimage.png* blob that was recently uploaded.From the blob's overview interface, click `Generate SAS` in the left-hand menu.

    ![7](./assets/snapshot10.png)

8. Provide the following details to generate the SAS token and Click `Generate SAS token and URL`.
    
   * **Permissions**= Select only the **Read** permission . This restrictive permission set is crucial for adherence to the principle of least privilege.
   * **Start and expiry date/time** define a practical expiration period (e.g., 24 hours from the current timestamp) suitable for the duration of the laboratory exercise.
   * For **Allowed IP addresses** this field may be left unpopulated or configured for enhanced security by specifying permissible IP ranges; however, this is not strictly required for the present laboratory scenario.
   * For **Allowed protocols**, select `HTTPS only`.

     ![8](./assets/snapshot11.png)

   Here we generate a *Shared Access Signature* to securely access and Read the image for a pre-define time period.

9. Crucially, copy only the **Blob SAS token** string and **Blob SAS URL** . This specific token will be securely stored within Azure Key Vault. It is imperative to avoid copying the "Blob SAS URL" or the "Blob URL."

    ![9](./assets/snapshot12.png)

    The values we need should be formatted like below:<p>
    **BLOB-SAS-URL**= ``` https://<storage-account-name>.blob.core.windows.net/<container-name>/<image-name>```</p>
    **BLOB-SAS-TOKEN** = sp=r&st=2025-06-14T20:57:30Z&se=2025-06-15T04:57:30Z&spr=https&sv=2024-11-04&sr=b&sig=###########################################
   
---


Create  **BLOB-SAS-TOKEN** , **BLOB-SAS-URL** and **GREETING-MESSAGE** Secret in Key Vault:

10.  Search for `key vault` in Azure Portal and select the `key vault name`.  
    
     ![10](./assets/snapshot.png)


11. In the left-hand navigation  `overview` blade , under the "Objects" section, click `Secrets.`
   
    ![11](./assets/snapshot1.png)

12. Click the `+ Generate/Import` button at the top of the interface and fill the required fields with following details, then click `Create`.

    ![12.a](./assets/snapshot2.png)
   * For **Upload options**, select **Manual**.
   * For **Name**, input **BLOB-SAS-TOKEN**.
   * For **Value**, paste the previously copied *Blob SAS token* string from Blob Storage.
   * All other configuration settings should retain their default values.
   ![12.b](./assets/snapshot13.png)


    

13. Same way lets create another secret for *SAS-BLOB_URL*, Click the `+ Generate/Import` button at the top of the interface and fill the required fields with following details, then Click `Create`.

   * For **Upload options**, select **Manual**.
   * For **Name**, input **BLOB-SAS-URL**.
   * For **Value**, paste the previously copied *Blob SAS URL* string from Blob Storage.
   * All other configuration settings should retain their default values.
   ![13](./assets/snapshot14.png)

14. Same way lets create another secret for **GREETING-MESSAGE**, Click the `+ Generate/Import` button at the top of the interface and fill the required fields with following details, then Click `Create`.
   * `Upload options` = `Manual`.
   * `Name`  = `GREETING-MESSAGE`. 
   * `Value` = *Hello from Azure Key Vault! This message is super secret..*
   * `Content Type` ,`Activation date` ,`Expiration date` and `Enabled` keep as it is. These are not mandatory required fields.

     ![14](./assets/snapshot3.png)



 

15. Once you complete up to this level, youre key vault should look like this.

    ![15](./assets/snapshot15.png)

Great job! You've successfully completed the lab requirements. You've skillfully **created Key Vault secrets**, **uploaded your image**, **generated a SAS token for secure access**, and **configured Key Vault with all the relevant secrets**. That's a crucial step in building secure cloud applications!



