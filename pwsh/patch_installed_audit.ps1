# Define the output CSV file path
$outputFile = "C:\temp\InstalledSecurityUpdates.csv"

# Get the list of installed updates with history
$updateSession = New-Object -ComObject Microsoft.Update.Session
$updateSearcher = $updateSession.CreateUpdateSearcher()
$historyCount = $updateSearcher.GetTotalHistoryCount()
$updateHistory = $updateSearcher.QueryHistory(0, $historyCount)

# Create an array to store the update details
$updateDetails = @()

# Loop through each update and extract details
foreach ($update in $updateHistory) {
    $updateDetails += [PSCustomObject]@{
        Title       = $update.Title
        Description = $update.Description
        Date        = $update.Date
        Result      = $update.ResultCode
    }
}

# Export the update details to a CSV file
$updateDetails | Export-Csv -Path $outputFile -NoTypeInformation

Write-Output "All installed update history has been exported to $outputFile"