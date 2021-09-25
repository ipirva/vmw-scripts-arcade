# Variables
# VCSA server IP or hostname
variable "vsphere_server" {
    type = string
    description = "vSphere IP or DNS"
}
# VCSA username
variable "vsphere_server_username" {
    type = string
    description = "vSphere Server Username"
    default = "Administrator@vsphere.local"
}
# VCSA password
variable "vsphere_server_password" {
    type = string
    description = "vSphere Server Password"

  validation {
    condition     = var.vsphere_server_password != ""
    error_message = "The value for vSphere Server Password cannot be empty."
  }
}
variable "vsphere_server_allow_unverified_ssl" {
    type = bool
    default = true
    description = "vSphere Server Allow Unverified SSL "
}
variable "vsphere_dc" {
    type = string
    description = "vSphere Data Center"

  validation {
    condition     = trimspace(var.vsphere_dc) != ""
    error_message = "The value for vSphere DC cannot be empty."
  }
}
variable "vsphere_ds" {
    type = string
    description = "vSphere Datastore"

  validation {
    condition     = trimspace(var.vsphere_ds) != ""
    error_message = "The value for vSphere DS cannot be empty."
  }
}
variable "vsphere_compute_cluster" {
    type = string
    description = "vSphere Compute Cluster"

  validation {
    condition     = trimspace(var.vsphere_compute_cluster) != ""
    error_message = "The value for vSphere Compute Cluster cannot be empty."
  }
}
# for each new NSX Manager VM specify on which ESXi host it will be installed
variable "vsphere_host" {
  type = string
  description = "vSphere Host to Deploy NSX-T Manger VM on"
  # its size is the same as nsxt_manager_vm_name, nsxt_manager_vm_hostname ...
  # eg esx01.cpod-go.az-fkd.cloud-garage.net or
  # esx01.cpod-go.az-fkd.cloud-garage.net, esx02.cpod-go.az-fkd.cloud-garage.net or
  # esx01.cpod-go.az-fkd.cloud-garage.net, esx02.cpod-go.az-fkd.cloud-garage.net, esx03.cpod-go.az-fkd.cloud-garage.net
  validation {
    condition = can(regex("^([0-9A-Za-z_\\-\\.])+|(,([[:blank:]])?([0-9A-Za-z_\\-\\.])+){0,2}$",trimspace(var.vsphere_host)))
    error_message = "Must specify 1, 2 or 3 vSphere VM names for the NSX-T Manager VM(s)."
  }
}
variable "vsphere_folder" {
    type = string
    default = ""
    description = "vSphere Folder"
}
variable "vsphere_resource_pool" {
    type = string
    default = ""
    description = "vSphere Resource Pool"
}
variable "vsphere_vm_network" {
    type = string
    description = "vSphere Network Used for NSX Manager VM Network1 Interface"

  validation {
    condition     = can(regex("^([0-9A-Za-z_\\-\\.])+$",trimspace(var.vsphere_vm_network)))
    error_message = "The value for vSphere Network name is incorrectly formatted."
  }
}
variable "vsphere_network_dvs" {
    type = string
    description = "vSphere Network DVS Name"

  validation {
    condition     = can(regex("^([0-9A-Za-z_\\-\\.])+$",trimspace(var.vsphere_network_dvs)))
    error_message = "The value for vSphere Network DVS name is incorrectly formatted."
  }
}
# variables related to nsxt manager vm appliance
variable "nsxt_manager_vm_name" {
  # eg with or without domain name
  # mynsxtmanager-a.mydomain.io or 
  # mynsxtmanager-a.mydomain.io, mynsxtmanager-b.mydomain.io or
  # mynsxtmanager-a.mydomain.io, mynsxtmanager-b.mydomain.io, mynsxtmanager-c.mydomain.io
  type        = string 
  description = "NSX-T Manager VM Name in vSphere"
  
  validation {
    condition = can(regex("^([0-9A-Za-z_\\-\\.])+|(,([[:blank:]])?([0-9A-Za-z_\\-\\.])+){0,2}$",trimspace(var.nsxt_manager_vm_name)))
    error_message = "Must specify 1, 2 or 3 vSphere VM names for the NSX-T Manager VM(s)."
  }
}
variable "nsxt_manager_vm_hostname" {
  # eg mynsxtmanager-a.mydomain.io or 
  # mynsxtmanager-a.mydomain.io, mynsxtmanager-b.mydomain.io or
  # mynsxtmanager-a.mydomain.io, mynsxtmanager-b.mydomain.io, mynsxtmanager-c.mydomain.io
  type        = string
  description = "NSX-T Manager VM Hostname"

  validation {
    condition = can(regex("^([0-9A-Za-z_\\-\\.])+|(,([[:blank:]])?([0-9A-Za-z_\\-\\.])+){0,2}$",trimspace(var.nsxt_manager_vm_hostname)))
    error_message = "Must specify 1, 2 or 3 DNS hostname(s) for the NSX-T Manager VM(s)."
  }
}
variable "nsxt_manager_vm_deployment_size" {
  type        = string
  default     = "medium"
  description = "The deployment size of the NSX-T Manager Appliance. The default is \"medium\""

  validation {
    condition     = contains(["extrasmall","small", "medium", "large"], trimspace(var.nsxt_manager_vm_deployment_size))
    error_message = "The nsxt_manager_vm_deployment_size must be one of \"extrasmall\", \"small\", \"medium\", or \"large\"."
  }
}
variable "nsxt_manager_vm_cpu_count_override" {
  type        = number
  default     = 0
  description = "The number of CPUs the NSX-T Manager VM should have. Defaults to 0 which uses the CPU count of the deployment selected."

  validation {
    condition     = trimspace(var.nsxt_manager_vm_cpu_count_override) >= 0
    error_message = "The NSX-T Manager VM cpu_count_override value must greater than or equal to 0."
  }
}
variable "nsxt_manager_vm_memory_override" {
  type        = number
  default     = 0
  description = "The ammount of memory the NSX-T Manager VM should have. Defaults to 0 which uses the memory size of the deployment selected."

  validation {
    condition     = trimspace(var.nsxt_manager_vm_memory_override) >= 0
    error_message = "The NSX-T Manager VM memory_override value must greater than or equal to 0."
  }
}
variable "nsxt_manager_ova_remote_path" {
  type        = string # eg http://mydomain.io/Repository/nsx-unified-appliance-3.1.3.1.0.18504672.ova
  description = "NSX-T Manager VM OVA Remote Path HTTP/HTTPS"

  validation {
    condition     = can(regex("^(https?:\\/\\/)?([\\da-z\\.-]+)\\.([\\da-z]{2,6})([\\/\\w\\.-]*)*\\/?$",trimspace(var.nsxt_manager_ova_remote_path)))
    error_message = "The remote OVA path must be an HTTP(s) valid URL."
  }
}
variable "vsphere_ova_allow_unverified_ssl" {
    type = bool
    default = true
    description = "OVA Remote Path Allow Unverified SSL"
}
variable "nsxt_manager_vm_enable_ssh" {
  type        = bool
  default     = true
  description = "Enable SSH be enabled to the NSX-T Manager VM Appliance?"
}
variable "nsxt_manager_vm_enable_root_ssh" {
  type        = bool
  default     = true
  description = "Enable root login over SSH to the NSX-T Manager VM Appliance?"
}
variable "nsxt_manager_vm_admin_username" {
  type        = string
  default     = "admin"
  description = "NSX-T Manager VM Admin Username. Default is \"admin\"."
}
variable "nsxt_manager_vm_audit_username" {
  type        = string
  default     = "admin"
  description = "NSX-T Manager VM Audit Username. Default is \"audit\"."
}
variable "nsxt_manager_vm_root_password" {
    type = string
    description = "NSX-T Manager VM root user Password"  
    sensitive = true

  validation {
    condition     = trimspace(var.nsxt_manager_vm_root_password) != ""
    error_message = "The value for NSX-T Manager VM root user password cannot be empty."
  }
}
variable "nsxt_manager_vm_admin_password" {  
    type = string
    description = "NSX-T Manager VM admin user Password"  
    sensitive = true

  validation {
    condition     = trimspace(var.nsxt_manager_vm_admin_password) != ""
    error_message = "The value for NSX-T Manager VM admin user password cannot be empty."
  }
}
variable "nsxt_manager_vm_audit_password" {
    type = string
    description = "NSX-T Manager VM audit user Password"  
    sensitive = true

  validation {
    condition     = trimspace(var.nsxt_manager_vm_audit_password) != ""
    error_message = "The value for NSX-T Manager VM audit user password cannot be empty."
  }
}
variable "nsxt_manager_vm_ipv4_prefix" {
  # eg 172.17.23.10/24 or
  #172.17.23.10/24, 172.17.23.11/24 or
  #172.17.23.10/24, 172.17.23.11/24, 172.17.23.12/24
  type        = string 
  description = "NSX-T Manager VM(s) IPv4 Prefix(es)"

  validation {
    condition     = can(regex("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/([1-9]|[1-2][0-9]|3[0-1])(,[[:blank:]]?(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/([1-9]|[1-2][0-9]|3[0-1])){0,2}$", trimspace(var.nsxt_manager_vm_ipv4_prefix)))
    error_message = "The value for NSX-T Manager VM(s) interface(s) IP has an incorrect format."
  } 
}
# the NSX-T Manager VMs are on the same IPv4 subnet
variable "nsxt_manager_vm_ipv4_gateway" {
  type        = string # eg 172.17.23.1
  description = "NSX-T Manager VM Gateway IPv4"

  validation {
    condition     = can(regex("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", trimspace(var.nsxt_manager_vm_ipv4_gateway)))
    error_message = "The value for NSX-T Manager VM IPv4 gateway must be an IPv4 address."
  }
}
# variable "nsxt_manager_vm_ipv4_netmask" {
#   type        = string # eg 255.255.255.0
#   description = "NSX-T Manager VM IPv4 Netmask"

#   validation {
#     condition     = can(regex("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", trimspace(var.nsxt_manager_vm_ipv4_netmask)))
#     error_message = "The value for NSX-T Manager VM Interface IP Netmask is incorrect."
#   }
# }
variable "nsxt_manager_vm_dns_serverlist" {
  type        = string # space separated list, only the 1st 3 are considered (NSX-T)
  description = "DNS Server List for the NSX-T Manager VM"

  validation {
    condition     = can(regex("^((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))([[:blank:]](?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){0,}$",trimspace(var.nsxt_manager_vm_dns_serverlist)))
    error_message = "The value for DNS server list must be set in order to deploy the NSX-T Manager VM."
  }
}
variable "nsxt_manager_vm_ntp_serverlist" {
  type        = string # space separated list, only the 1st 3 are considered (NSX-T)
  description = "NTP Server List for the NSX-T Manager VM"

  validation {
    condition     = can(regex("^((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))([[:blank:]](?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){0,}$",trimspace(var.nsxt_manager_vm_ntp_serverlist)))
    error_message = "The value for NTP server list must be set in order to deploy the NSX-T Manager VM."
  }
}
