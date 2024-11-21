# Import Active Directory module
Import-Module ActiveDirectory

# Domain to search
$DomainRoot = "DC=workzone,DC=local"

# Get all users in the domain
$allUsers = Get-ADUser -Filter * -SearchBase $DomainRoot -Properties DistinguishedName, Department

foreach ($user in $allUsers) {
    try {
        # Get the Distinguished Name of the user
        $dn = $user.DistinguishedName

        # Extract the OU part of the Distinguished Name
        $ouMatch = ($dn -split ',') -match '^OU='
        if ($ouMatch) {
            # Extract the OU name
            $ouName = ($ouMatch -replace '^OU=', '').Trim()

            # Update the Department attribute with the OU name
            Set-ADUser -Identity $user.DistinguishedName -Department $ouName
            Write-Host "Updated Department for user $($user.SamAccountName): $ouName"
        } else {
            Write-Host "No OU found for user $($user.SamAccountName). Skipping."
        }
    } catch {
        Write-Host "Error processing user $($user.SamAccountName): $_"
    }
}

Write-Host "Department attribute update completed for all users."
