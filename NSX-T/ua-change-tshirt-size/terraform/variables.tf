# Variables
variable "vsphere_server" {
    type = string
    description = "vSphere IP or DNS"
}
variable "vsphere_server_username" {
    type = string
    description = "vSphere Server Username"
    default = "Administrator@vsphere.local"
}
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
variable "vsphere_host" {
    type = string
    description = "vSphere Compute Host"

  validation {
    condition     = trimspace(var.vsphere_host) != ""
    error_message = "The value for vSphere Compute Host cannot be empty."
  }
}
# when the target NSX-T cluster has 3 VMs, we need 2 more vSphere ESXi hosts
variable "vsphere_extra_host" {
    type = string
    description = "vSphere Compute Host"
    default = ""
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
    description = "vSphere Network Used for VM Network1 Interface"

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
  type        = string # eg mynsxtmanager-a.mydomain.io
  description = "NSX-T Manager VM vSphere Name"
  
  validation {
    condition = can(regex("^([0-9A-Za-z_\\-\\.])+$",trimspace(var.nsxt_manager_vm_name)))
    error_message = "The value of NSX-T Manager VM name is incorrectly formatted."
  }
}
variable "nsxt_manager_vm_hostname" {
  type        = string # eg mynsxtmanager-a.mydomain.io
  description = "NSX-T Manager VM Hostname"

  validation {
    condition = can(regex("^([0-9A-Za-z_\\-\\.])+$",trimspace(var.nsxt_manager_vm_hostname)))
    error_message = "Must specify 1 DNS hostname for the extra NSX-T Manager VM nsxt-a."
  }
}
# when the target NSX-T cluster has 3 VMs, we need 2 more hostnames
variable "nsxt_manager_vm_extra_hostname" {
  type        = string # eg mynsxtmanager-b.mydomain.io, mynsxtmanager-c.mydomain.io
  description = "NSX-T Manager VM Hostname"
  default = ""

  validation {
    condition = can(regex("^(|([0-9A-Za-z_\\-\\.])+((,)[[:blank:]]?)([0-9A-Za-z_\\-\\.])+)$",trimspace(var.nsxt_manager_vm_extra_hostname)))
    error_message = "Must specify either nothing, or 2 DNS hostnames, one for each extra NSX-T Manager VM nsxt-b and nsxt-c."
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
  type        = string # eg 172.17.23.10/24
  description = "NSX-T Manager VM IPv4 Prefix"

  validation {
    condition     = can(regex("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/([1-9]|[1-2][0-9]|3[0-1])$", trimspace(var.nsxt_manager_vm_ipv4_prefix)))
    error_message = "The value for NSX-T Manager VM interface IP must be an IPv4 prefix."
  } 
}
# when the target NSX-T cluster has 3 VMs, we need 2 more IPv4 prefixes for the two VMs interfaces
# a list of 2 IPv4 or empty
variable "nsxt_manager_vm_ipv4_extra_prefix" {
  type        = string # eg 172.17.23.10/24, 172.17.23.11/24
  description = "NSX-T Manager VM IPv4 Prefixes"
  default = ""

  validation {
    condition     = can(regex("^(|((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/([1-9]|[1-2][0-9]|3[0-1]))((,){0,1}([[:blank:]]){0,1}((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/([1-9]|[1-2][0-9]|3[0-1])){0,1}){0,1})$", trimspace(var.nsxt_manager_vm_ipv4_extra_prefix)))
    error_message = "The value for NSX-T Manager VM Extra IPv4 must be empty or a comma separated list of two IPv4 addresses."
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
# variable defined by API call
# a script uses API call to populate the value of vsphere_esxi_hosts in an .auto.tfvars file
variable "vsphere_esxi_hosts" {
  type = map
  description = "The vSphere ESXi hosts and hosts ID."

  default = {
      "esx01.cpod-go.az-fkd.cloud-garage.net" = "host1",
      "esx02.cpod-go.az-fkd.cloud-garage.net" = "host2"
      }
}