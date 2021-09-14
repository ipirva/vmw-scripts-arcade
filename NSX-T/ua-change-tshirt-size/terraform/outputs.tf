output "nsxt_manager_vm_details" {  
    description = "NSX-T Manager VM Details"  
    value       = null_resource.nsxt_manager_vms
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
output "vm_name_2_vsphere_host" {
    description = "NSX-T Manager VM 2 vSphere ESXi host mapping"
    value = local.local_vm_name_vsphere_host
}