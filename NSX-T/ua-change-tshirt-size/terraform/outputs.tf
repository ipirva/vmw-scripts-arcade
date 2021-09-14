output "nsxt_manager_vm_a" {  
    description = "NSX-T Manager VM Name - 1st VM"  
    value       = local.local_nsxt_manager_map
}
output "nsxt_manager_vm_b_c" {  
    description = "NSX-T Manager VM Name - 2nd and 3rd if deployed"  
    value       = "${null_resource.nsxt_manager_vms.*.triggers}"
}
output "nsxt_manager_vm_deployment_size" {  
    description = "NSX-T Manager T-Shirt Size"  
    value       = upper(var.nsxt_manager_vm_deployment_size)
}
output "nsxt_manager_vm_root_password" {  
    description = "NSX-T Manager VM root user Password"  
    value = var.nsxt_manager_vm_root_password
    sensitive = true
}
output "nsxt_manager_vm_admin_password" {  
    description = "NSX-T Manager VM admin user Password"  
    value       = var.nsxt_manager_vm_admin_password
    sensitive = true
}
output "nsxt_manager_vm_audit_password" {  
    description = "NSX-T Manager VM audit user Password"  
    value       = var.nsxt_manager_vm_audit_password
    sensitive = true
}
output "vsphere_esxi_hosts" {  
    description = "vSphere ESXi Hosts"  
    value       = var.vsphere_esxi_hosts
}