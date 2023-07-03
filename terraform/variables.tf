resource_group_name      = "macOSComplianceEnforcer"
location                 = "Australia East"
storage_account_name     = "macoscompliancestorage"
app_service_plan_name    = "macoscomplianceplan"
function_app_name        = "macoscomplianceapp"
key_vault_name           = "macosenforcervault"

# The following variables should be replaced with your desired Client ID, Client Secret, and Tenant ID. 
# These values can be found in the Azure Portal under Azure Active Directory > App Registrations > <your_app_registration> > Overview.
# the client secret can be found under Certificates & Secrets.
# The tenant id can be found in the Azure Portal under Azure Active Directory > Properties > Directory ID.

# Sorry :D

client_id                = "your_client_id"
client_secret            = "your_client_secret"
tenant_id                = "your_tenant_id"