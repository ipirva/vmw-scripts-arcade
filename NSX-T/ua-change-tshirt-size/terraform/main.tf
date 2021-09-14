# Terraform Provider
terraform {
  required_providers {
    vsphere = {
      source = "vsphere"
      version = "2.0.2"
    }
  }
}
# Variables
locals {
  # netmask to cidr lookup table
  local_netmask_cidr_map = {
      "0.0.0.0"         = "0"
      "128.0.0.0"       = "1"
      "192.0.0.0"       = "2"
      "224.0.0.0"       = "3"
      "240.0.0.0"       = "4"
      "248.0.0.0"       = "5"
      "252.0.0.0"       = "6"
      "254.0.0.0"       = "7"
      "255.0.0.0"       = "8"
      "255.128.0.0"     = "9"
      "255.192.0.0"     = "10"
      "255.224.0.0"     = "11"
      "255.240.0.0"     = "12"
      "255.248.0.0"     = "13"
      "255.252.0.0"     = "14"
      "255.254.0.0"     = "15"
      "255.255.0.0"     = "16"
      "255.255.128.0"   = "17"
      "255.255.192.0"   = "18"
      "255.255.224.0"   = "19"
      "255.255.240.0"   = "20"
      "255.255.248.0"   = "21"
      "255.255.252.0"   = "22"
      "255.255.254.0"   = "23"
      "255.255.255.0"   = "24"
      "255.255.255.128" = "25"
      "255.255.255.192" = "26"
      "255.255.255.224" = "27"
      "255.255.255.240" = "28"
      "255.255.255.248" = "29"
      "255.255.255.250" = "30"
      "255.255.255.252" = "31"
      "255.255.255.255" = "32"
    }
  # cidr to netmap lookup table 
  local_cidr_netmask_map = zipmap(values(local.local_netmask_cidr_map), keys(local.local_netmask_cidr_map))

  # variables for the nsx-t managers
  local_nsxt_manager_vm_hostname = flatten((split(",", replace(var.nsxt_manager_vm_hostname,"/[[:blank:]]+/",""))))
  length_local_nsxt_manager_vm_hostname = length(local.local_nsxt_manager_vm_hostname)
  local_vsphere_host = flatten((split(",", replace(var.vsphere_host,"/[[:blank:]]+/",""))))
  length_local_vsphere_host = length(local.local_vsphere_host)
  local_nsxt_manager_vm_ipv4_prefix = flatten((split(",", replace(var.nsxt_manager_vm_ipv4_prefix,"/[[:blank:]]+/",""))))
  length_local_nsxt_manager_vm_ipv4_prefix = length(local.local_nsxt_manager_vm_ipv4_prefix)

  local_nsxt_manager_vm_name = flatten((split(",", replace(var.nsxt_manager_vm_name, "/[[:blank:]]+/", ""))))
  local_vm_name_vsphere_host = zipmap(local.local_nsxt_manager_vm_name, local.local_vsphere_host)
}
# vSphere Credentials
provider "vsphere" {
  user                 = trimspace(var.vsphere_server_username)
  password             = var.vsphere_server_password
  vsphere_server       = trimspace(var.vsphere_server)
  allow_unverified_ssl = var.vsphere_server_allow_unverified_ssl
}
# Data source
data "vsphere_datacenter" "dc" {
  name = var.vsphere_dc
}
data "vsphere_compute_cluster" "cluster" {
  name          = trimspace(var.vsphere_compute_cluster)
  datacenter_id = data.vsphere_datacenter.dc.id
}
data "vsphere_datastore" "vsphere_ds" {
  name          = trimspace(var.vsphere_ds)
  datacenter_id = data.vsphere_datacenter.dc.id
}
 
data "vsphere_resource_pool" "resource_pool" {
  name          = trimspace(var.vsphere_resource_pool)
  datacenter_id = data.vsphere_datacenter.dc.id
}

data "vsphere_host" "vsphere_esxi_host" {
  for_each = "${local.local_vm_name_vsphere_host}"

  name          = each.value
  datacenter_id = data.vsphere_datacenter.dc.id
}

data "vsphere_distributed_virtual_switch" "dvs" {
  name          = trimspace(var.vsphere_network_dvs)
  datacenter_id = data.vsphere_datacenter.dc.id
}

data "vsphere_network" "vsphere_vm_network" {
  name          = trimspace(var.vsphere_vm_network)
  datacenter_id = data.vsphere_datacenter.dc.id
  distributed_virtual_switch_uuid = data.vsphere_distributed_virtual_switch.dvs.id
}

data "vsphere_ovf_vm_template" "ovf" {
  for_each = "${local.local_vm_name_vsphere_host}"

  name = "${each.key}"
  host_system_id = "${data.vsphere_host.vsphere_esxi_host["${each.key}"].id}"

  resource_pool_id = "${data.vsphere_resource_pool.resource_pool.id}"
  datastore_id = "${data.vsphere_datastore.vsphere_ds.id}"
  remote_ovf_url = "${trimspace(var.nsxt_manager_ova_remote_path)}"
  allow_unverified_ssl_cert = true
  ovf_network_map = {
    "Network 1": "${data.vsphere_network.vsphere_vm_network.id}"
  }
  disk_provisioning = "thin"
  ip_protocol = "IPv4"
}

# Resources
# example for 2 NSX-T Manager VMs
# [
#       + {
#           + "host"                   = "esx04.cpod-go.az-fkd.cloud-garage.net"
#           + "vm_domain"              = "cpod-go.az-fkd.cloud-garage.net"
#           + "vm_hostname"            = "nsx-t-b.cpod-go.az-fkd.cloud-garage.net"
#           + "vm_ipv4_address"        = "172.17.23.124"
#           + "vm_ipv4_netmask"        = "255.255.255.0"
#           + "vm_ipv4_netmask_prefix" = "24"
#           + "vm_ipv4_prefix"         = "172.17.23.124/24"
#         },
#       + {
#           + "host"                   = "esx05.cpod-go.az-fkd.cloud-garage.net"
#           + "vm_domain"              = "cpod-go.az-fkd.cloud-garage.net"
#           + "vm_hostname"            = "nsx-t-c.cpod-go.az-fkd.cloud-garage.net"
#           + "vm_ipv4_address"        = "172.17.23.125"
#           + "vm_ipv4_netmask"        = "255.255.255.0"
#           + "vm_ipv4_netmask_prefix" = "24"
#           + "vm_ipv4_prefix"         = "172.17.23.125/24"
#         },
# ]
resource "null_resource" "nsxt_manager_vms" {
  count = "${length(local.local_nsxt_manager_vm_hostname)}"
  triggers = {
    vm_name = trimspace("${element(local.local_nsxt_manager_vm_name, count.index)}")
    vm_hostname = trimspace("${element(local.local_nsxt_manager_vm_hostname, count.index)}")
    vm_domain = join(".", slice(split(".", trimspace("${element(local.local_nsxt_manager_vm_hostname, count.index)}")), 1, length(split(".", trimspace("${element(local.local_nsxt_manager_vm_hostname, count.index)}")))))
    host = trimspace("${element(local.local_vsphere_host, count.index)}") # esxi host
    vm_ipv4_prefix = trimspace("${element(local.local_nsxt_manager_vm_ipv4_prefix, count.index)}") # 172.17.23.123/24
    vm_ipv4_address = trimspace(split("/", "${element(local.local_nsxt_manager_vm_ipv4_prefix, count.index)}")[0]) # 172.17.23.123
    vm_ipv4_netmask_prefix = trimspace(split("/", "${element(local.local_nsxt_manager_vm_ipv4_prefix, count.index)}")[1]) # 24
    vm_ipv4_netmask = lookup(local.local_cidr_netmask_map, split("/", "${element(local.local_nsxt_manager_vm_ipv4_prefix, count.index)}")[1], "default") # 255.255.255.0
  }
}
resource "vsphere_virtual_machine" "nsxt_manager_vm" {
  
  for_each = { 
    for index, item in "${null_resource.nsxt_manager_vms.*.triggers}":
      index => item
  }

  name             = each.value.vm_hostname
  resource_pool_id = data.vsphere_resource_pool.resource_pool.id
  folder           = trimspace(var.vsphere_folder)
  datastore_id     = data.vsphere_datastore.vsphere_ds.id
  datacenter_id    = data.vsphere_datacenter.dc.id
  host_system_id = "${data.vsphere_host.vsphere_esxi_host["${each.value.vm_name}"].id}"
  
  wait_for_guest_net_timeout = 0
  wait_for_guest_ip_timeout  = 0

  enable_logging = true

  num_cpus               = trimspace(var.nsxt_manager_vm_cpu_count_override) > 0 ? trimspace(var.nsxt_manager_vm_cpu_count_override) : data.vsphere_ovf_vm_template.ovf[each.value.vm_name].num_cpus
  num_cores_per_socket   = data.vsphere_ovf_vm_template.ovf[each.value.vm_name].num_cores_per_socket
  cpu_hot_add_enabled    = data.vsphere_ovf_vm_template.ovf[each.value.vm_name].cpu_hot_add_enabled
  cpu_hot_remove_enabled = data.vsphere_ovf_vm_template.ovf[each.value.vm_name].cpu_hot_remove_enabled
  nested_hv_enabled      = data.vsphere_ovf_vm_template.ovf[each.value.vm_name].nested_hv_enabled
  memory                 = trimspace(var.nsxt_manager_vm_memory_override) > 0 ? trimspace(var.nsxt_manager_vm_memory_override) : data.vsphere_ovf_vm_template.ovf[each.value.vm_name].memory
  memory_hot_add_enabled = data.vsphere_ovf_vm_template.ovf[each.value.vm_name].memory_hot_add_enabled
  annotation             = data.vsphere_ovf_vm_template.ovf[each.value.vm_name].annotation
  guest_id               = data.vsphere_ovf_vm_template.ovf[each.value.vm_name].guest_id
  alternate_guest_name   = data.vsphere_ovf_vm_template.ovf[each.value.vm_name].alternate_guest_name
  scsi_type              = data.vsphere_ovf_vm_template.ovf[each.value.vm_name].scsi_type
  scsi_controller_count  = data.vsphere_ovf_vm_template.ovf[each.value.vm_name].scsi_controller_count
  sata_controller_count  = data.vsphere_ovf_vm_template.ovf[each.value.vm_name].sata_controller_count

  dynamic "network_interface" {
    for_each = data.vsphere_ovf_vm_template.ovf[each.value.vm_name].ovf_network_map
    content {
      network_id = network_interface.value
    }
  }

  ovf_deploy {
    // Url to remote ovf/ova file
    remote_ovf_url = data.vsphere_ovf_vm_template.ovf[each.value.vm_name].remote_ovf_url
    allow_unverified_ssl_cert = true
    disk_provisioning = data.vsphere_ovf_vm_template.ovf[each.value.vm_name].disk_provisioning
    ip_protocol = data.vsphere_ovf_vm_template.ovf[each.value.vm_name].ip_protocol
    ovf_network_map = data.vsphere_ovf_vm_template.ovf[each.value.vm_name].ovf_network_map
    deployment_option = lower(trimspace(var.nsxt_manager_vm_deployment_size))
  }
 
  vapp {
    properties = {
      "nsx_passwd_0"           = var.nsxt_manager_vm_root_password
      "nsx_cli_passwd_0"       = var.nsxt_manager_vm_admin_password
      "nsx_cli_audit_passwd_0" = var.nsxt_manager_vm_audit_password
      "nsx_cli_username"       = trimspace(var.nsxt_manager_vm_admin_username) # admin username
      "nsx_cli_audit_username" = trimspace(var.nsxt_manager_vm_audit_username) # audit username
      "nsx_hostname"           = trimspace(each.value.vm_hostname) # hostname uses the domain name in this case
      "nsx_role"               = "NSX Manager" # NSX Global Manager and nsx-cloud-service-manager not yet allowed
      "nsx_gateway_0"          = trimspace(var.nsxt_manager_vm_ipv4_gateway)
      "nsx_ip_0"               = each.value.vm_ipv4_address
      "nsx_netmask_0"          = each.value.vm_ipv4_netmask
      "nsx_dns1_0"             = trimspace(var.nsxt_manager_vm_dns_serverlist)
      "nsx_domain_0"           = each.value.vm_domain
      "nsx_ntp_0"              = trimspace(var.nsxt_manager_vm_ntp_serverlist)
      "nsx_isSSHEnabled"       = title(tostring(var.nsxt_manager_vm_enable_ssh))
      "nsx_allowSSHRootLogin"  = title(tostring(var.nsxt_manager_vm_enable_root_ssh))
    }
  }

  provisioner "local-exec" {
    command = "${abspath(path.module)}/nsxt-wait-for-startup.sh"
    environment = {
      NSXT_MANAGER_HOSTNAME = each.value.vm_ipv4_address
      NSXT_USERNAME         = trimspace(var.nsxt_manager_vm_admin_username)
      NSXT_PASSWORD         = var.nsxt_manager_vm_admin_password
    }
    on_failure = fail
  }

  lifecycle {
    ignore_changes = [
      // it looks like some of the properties get deleted from the VM after it is deployed
      // just ignore them after the initial deployment
      vapp.0.properties,
    ]
  }

}