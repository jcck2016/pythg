# Import the Veeam PowerShell module
#Add-PSSnapin VeeamPSSnapin

# Get all VMs and their last restore points
$vbrrestore = Get-VBRBackup | Get-VBRRestorePoint | Sort-Object VMName, CreationTime |
    Select-Object VMName, CreationTime, @{n='DaysSinceLastSuccess'; e={(New-TimeSpan -Start $_.CreationTime -End (Get-Date)).Days}} |
    Group-Object VMName |
    ForEach-Object { $_.Group | Select-Object -Last 1 }

# Export the results to a CSV file
$vbrrestore | Export-Csv -Path 'VM_Backup_Report4.csv' -NoTypeInformation

# Display the results
$vbrrestore | Format-Table -AutoSize