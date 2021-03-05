# z/OSMF sample configuration

z/OSMF Ansible collection **ibm_zos_zosmf** is designed to unleash the z/OSMF capabilities to Ansible. It drives z/OSMF REST APIs to complete z/OS operations. Therefore, in order to run z/OSMF Ansible collection, you need to ensure z/OSMF is setup and run properly in z/OS side. Specifically:

- **zmf_workflow_XXX** requires z/OSMF Workflows

- **zmf_job_XXX** requires z/OSMF REST Jobs services

- **zmf_console_XXX** requires z/OSMF REST Console services and REST TSO services

If you already setup z/OSMF Core before, the above z/OSMF dependencies should already be there. Please skip below content. You could also use z/OSMF Security Configuration Assistant to validate security setup for the above z/OSMF services. 

If you haven't setup z/OSMF before, here is an approach to quickly enable z/OSMF in DEV/TEST system in order to try z/OSMF Ansible collection. Please be noticed, for Production system, please refer to z/OSMF Configuration Guide.

1. Setup z/OSMF nucleus. Please refer to [Create a z/OSMF nucleus on your system](https://www.ibm.com/support/knowledgecenter/en/SSLTBW_2.4.0/com.ibm.zos.v2r4.izua300/izulite_CreateTheNucleus.htm) which typically could take you 2 hours or so to setup z/OSMF nucleus in a sandbox system. 

2. Review and run [IZUANSEC](IZUANSEC) sample job for security setup needed by z/OSMF Ansible collection. Specifically, [IZUANSEC](IZUANSEC) sample job setup 
security for below z/OSMF services:

    - Workflows
    - REST Jobs services
    - REST TSO services
    - REST data set and file services
    - REST Console services

3. Optionally, if you would like to start a z/OSMF server only with z/OSMF services required by z/OSMF Ansible collection (E.g. for faster z/OSMF startup), you could follow below steps (require APAR PH24527 which is available at June 2020 applied):

    - 3.1. Create directory *`<zOSMF data directory>/configuration/settings/zosmf`* if it does not exist yet. *`<zOSMF data directory>`* is *`/global/zosmf`* by default and could be customized via z/OSMF parmlib `IZUPRMxx`. Here is an USS command example for your reference:

        ```
        mkdir -p /global/zosmf/configuration/settings/zosmf 
        ```

    - 3.2. Setup proper permission for the directory created in **3.1**. Here are the command examples: 
    
        ```
        chmod -R 770 /global/zosmf/configuration/settings         
        touch /global/zosmf/configuration/settings/zosmf/zosmf.json
        chown -R IZUSVR:IZUADMIN /global/zosmf/configuration/settings
        ```

        Please be noticed that `IZUSVR` is the default z/OSMF start task user id. `IZUADMIN` is the default z/OSMF administration user group.  

    - 3.3. Upload the sample [zosmf.json](zosmf.json) to the directory created in **3.1**. If you use FTP, please upload it with BIN mode.

4. Start z/OSMF server.