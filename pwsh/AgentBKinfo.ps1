# Define the root directory of the shared folder
$rootPath = "\\10.11.159.192\Veeamagent"

# Define the path for the CSV output file
$outputCsvPath = "C:\Users\JCM186\Documents\FileDetails.csv"

# Initialize an array to hold file details
$fileDetails = @()

# Function to get details of files in a folder
function Get-FileDetails {
    param (
        [string]$folderPath
    )
    
    try {
        # Get all files in the folder
        $files = Get-ChildItem -Path $folderPath -File -ErrorAction Stop
        
        foreach ($file in $files) {
            # Filter files with .vbm extension
            if ($file.Extension -eq ".vbm") {
                # Extract the base filename without extension
                $baseFileName = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
                
                # Format the filename to start with SCRB
                $formattedFileName = "SCRB$baseFileName"
                
                # Create an object for the current file details
                $fileDetail = [PSCustomObject]@{
                    FileName             = $formattedFileName
                    FilePath             = $file.FullName
                    LastModifiedDate     = $file.LastWriteTime
                }
                
                # Add the object to the array
                $global:fileDetails += $fileDetail
            }
        }
    } catch {
        Write-Error ("Error accessing files in folder '$folderPath': $($_.Exception.Message)")
    }
}

# Function to recursively get details of files in folders
function Get-FolderDetails {
    param (
        [string]$path
    )
    
    try {
        # Get all directories in the specified path
        $directories = Get-ChildItem -Path $path -Directory -ErrorAction Stop
        
        foreach ($dir in $directories) {
            Write-Output ("Processing folder: $($dir.FullName)")
            # Get details for files in the current directory
            Get-FileDetails -folderPath $dir.FullName
            
            # Recursively get folder details for subdirectories
            Get-FolderDetails -path $dir.FullName
        }
    } catch {
        Write-Error ("Error accessing directories in path '$path': $($_.Exception.Message)")
    }
}

# Start processing from the root path
Write-Output ("Starting processing from root path: $rootPath")
Get-FolderDetails -path $rootPath

# Export the collected data to a CSV file
if (Test-Path $outputCsvPath) {
    Write-Output ("The file already exists. It will be overwritten.")
}

$fileDetails | Export-Csv -Path $outputCsvPath -NoTypeInformation

Write-Output ("Export complete. The CSV file is located at: $outputCsvPath")
