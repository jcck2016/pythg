# Variables
$DomainName = "workzone.local"
$SafeModePassword = ConvertTo-SecureString "P@ssword1" -AsPlainText -Force

# Step 1: Install the AD DS feature
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

Write-Host "AD DS feature installed successfully."

# Step 2: Promote the server to a domain controller and create a new forest
Install-ADDSForest `
    -DomainName $DomainName `
    -DomainNetbiosName "WORKZONE" `
    -SafeModeAdministratorPassword $SafeModePassword `
    -InstallDNS `
    -ForestMode "WinThreshold" `
    -DomainMode "WinThreshold" `
    -Force

Write-Host "Server promoted to Domain Controller with forest '$DomainName'."