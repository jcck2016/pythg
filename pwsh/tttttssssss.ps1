param (
    [Parameter(Mandatory=$true)]
    [string]$Subnet
)

# Function to get all IP addresses in the subnet
function Get-IpAddresses {
    param (
        [string]$Subnet
    )
    $ips = @()
    $subnetParts = $Subnet.Split('/')
    $baseIp = [System.Net.IPAddress]::Parse($subnetParts[0])
    $prefixLength = [int]$subnetParts[1]
    $ipBytes = $baseIp.GetAddressBytes()
    $ipCount = [math]::Pow(2, 32 - $prefixLength) - 2

    for ($i = 1; $i -le $ipCount; $i++) {
        $ipBytes[3] = byte
        $ips += [System.Net.IPAddress]::new($ipBytes)
    }
    return $ips
}

# Function to get MAC address and manufacturer information
function Get-MacAddress {
    param (
        [string]$IpAddress
    )
    $arpOutput = arp -a $IpAddress
    $macAddress = ($arpOutput -match '([0-9A-F]{2}[:-]){5}([0-9A-F]{2})')[0]
    return $macAddress
}

WcBc0235!
P@swd2025!

Cutover ELZ N4Load balancer 8/21 - SCRB4LBUSNWK002 to be at IP address ...10.11.17.228, we have put the old SCRB4LBUSNWK001, a W2012 VM marked as “Do not turn on” for decomm later ... see RITM7126115 

3P%swd52^

# Function to get manufacturer information
function Get-Manufacturer {
    param (
        [string]$MacAddress
    )
    $oui = $MacAddress.Substring(0, 8).Replace('-', ':')
    $manufacturer = (Invoke-RestMethod -Uri "https://api.macvendors.com/$oui").Content
    return $manufacturer
}

# Main script
$ipAddresses = Get-IpAddresses -Subnet $Subnet

foreach ($ip in $ipAddresses) {
    if (Test-Connection -ComputerName $ip -Count 1 -Quiet) {
        $dnsEntry = [System.Net.Dns]::GetHostEntry($ip)
        $dnsName = $dnsEntry.HostName
        $macAddress = Get-MacAddress -IpAddress $ip
        $manufacturer = Get-Manufacturer -MacAddress $macAddress

        Write-Output "IP Address: $ip"
        Write-Output "DNS Name: $dnsName"
        Write-Output "MAC Address: $macAddress"
        Write-Output "Manufacturer: $manufacturer"
        Write-Output "-----------------------------------"
    }
}