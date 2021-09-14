#!/usr/bin/env bash

'
Ionut Pirva september 2021
The script validates the status of NSX-T UA Management and Control components.
The script retieves an API endpoint until the status becomes STABLE

The script returns exit 0 in case of success and exit 1 in case of failure.

Terraform will not show the different echo as this file contains sensitive information (eg: password)
'
set -o errexit
set -o errtrace
set -o nounset
set -o pipefail
# set -o xtrace

resp=""
mstatus=""
cstatus=""

echo "Reading https://${NSXT_MANAGER_HOSTNAME}/api/v1/cluster/status ..."
while true; do
    resp=`curl --silent --insecure -H "Authorization: Basic $(echo -n ${NSXT_USERNAME}:${NSXT_PASSWORD} | base64)" https://${NSXT_MANAGER_HOSTNAME}/api/v1/cluster/status` || true
    mstatus=`echo $resp | jq -r '.mgmt_cluster_status.status'` || true
    cstatus=`echo $resp | jq -r '.control_cluster_status.status'` || true

    if [ "$mstatus" = "STABLE" ] && [ "$cstatus" = "STABLE" ]; then
        echo "NSX-T Manager Appliance has been started successfully."
        break
    else
        echo "NSX-T Manager Appliance status is not yet available."
    fi

    echo "Management Cluster status was $mstatus and Control Cluster status was $cstatus. Sleeping for 20 seconds."
    sleep 20
done

exit 0
