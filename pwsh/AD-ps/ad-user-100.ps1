# Function to generate random first and last names
function Get-RandomName {
    $firstNames = @("John", "Jane", "James", "Emily", "Michael", "Sarah", "David", "Laura", "Chris", "Olivia")
    $lastNames = @("Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor")
    $randomFirstName = $firstNames | Get-Random
    $randomLastName = $lastNames | Get-Random
    return "$randomFirstName $randomLastName"
}

# OU Names
$OUs = @("Finance", "Marketing", "RD", "Engineering", "HR")

# Domain root path
$DomainRoot = "DC=workzone,DC=local" # Replace with your domain
$DefaultPassword = "P@ssw0rd!"       # Default password for all accounts

# Create OUs and users
foreach ($OUName in $OUs) {
    # Create the OU
    $OUPath = "OU=$OUName,$DomainRoot"
    New-ADOrganizationalUnit -Name $OUName -Path $DomainRoot -ErrorAction SilentlyContinue

    # Create 20 users in the OU
    for ($i = 1; $i -le 20; $i++) {
        $name = Get-RandomName
        $username = "$OUName-User$i"
        $samAccountName = "$OUName-User$i"
        $password = ConvertTo-SecureString $DefaultPassword -AsPlainText -Force

        # Create the user account
        New-ADUser -Name $name `
                   -SamAccountName $samAccountName `
                   -UserPrincipalName "$samAccountName@workzone.local" `
                   -AccountPassword $password `
                   -PasswordNeverExpires $false `
                   -Enabled $true `
                   -Path $OUPath

        # Set password expiration settings
        switch ($OUName) {
            "Finance" {
                # Password Never Expires
                Set-ADUser -Identity $samAccountName -PasswordNeverExpires $true
            }
            "HR" { # Password Expires in 90 days
                $expiryDate = (Get-Date).AddDays(90)
                Set-ADUser -Identity $samAccountName -AccountExpirationDate $expiryDate
            }
            "Marketing" { # Password Expires in 90 days
                $expiryDate = (Get-Date).AddDays(90)
                Set-ADUser -Identity $samAccountName -AccountExpirationDate $expiryDate
            }
            "RD" { # Password Expires in 90 days
                $expiryDate = (Get-Date).AddDays(90)
                Set-ADUser -Identity $samAccountName -AccountExpirationDate $expiryDate
            }
            "Engineering" { # Password Expires in 30 days
                $expiryDate = (Get-Date).AddDays(30)
                Set-ADUser -Identity $samAccountName -AccountExpirationDate $expiryDate
            }
        }

        Write-Host "Created user: $name ($samAccountName) in OU: $OUName"
    }
}

Write-Host "All OUs and users created successfully!"