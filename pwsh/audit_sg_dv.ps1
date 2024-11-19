# Read group names from a text file
$groups = Get-Content -Path "C:\temp\groups_dv.txt"

# Loop through each group and export the membership details
foreach ($group in $groups) {
    Get-ADGroupMember -Identity $group -Server "dvc.local" -Recursive | 
    Get-ADUser -Properties DisplayName, Created, Modified, Enabled | 
    Select-Object DisplayName, Created, Modified, Enabled | 
    Export-Csv -Path "C:\temp\$group.csv" -NoTypeInformation
}