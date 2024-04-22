# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['maintenance'] = '''
    type: group
    short-summary: Manage Maintenance
'''

helps['maintenance public-configuration'] = """
    type: group
    short-summary: Manage public maintenance configuration with maintenance
"""

helps['maintenance public-configuration list'] = """
    type: command
    short-summary: "Get Public Maintenance Configuration records."
    examples:
      - name: PublicMaintenanceConfigurations_List
        text: |-
               az maintenance public-configuration list
"""

helps['maintenance public-configuration show'] = """
    type: command
    short-summary: "Get Public Maintenance Configuration record."
    examples:
      - name: PublicMaintenanceConfigurations_GetForResource
        text: |-
               az maintenance public-configuration show --resource-name "configuration1"
"""

helps['maintenance applyupdate'] = """
    type: group
    short-summary: Manage apply update with maintenance
"""

helps['maintenance applyupdate list'] = """
    type: command
    short-summary: "Get Configuration records within a subscription."
    examples:
      - name: ApplyUpdates_List
        text: |-
               az maintenance applyupdate list
"""

helps['maintenance applyupdate show'] = """
    type: command
    short-summary: "Track maintenance updates to resource."
    examples:
      - name: ApplyUpdates_Get
        text: |-
               az maintenance applyupdate show --name "e9b9685d-78e4-44c4-a81c-64a14f9b87b6" --provider-name \
"Microsoft.Compute" --resource-group "examplerg" --resource-name "smdtest1" --resource-type "virtualMachineScaleSets"
"""

helps['maintenance applyupdate create'] = """
    type: command
    short-summary: "Apply maintenance updates to resource."
    examples:
      - name: ApplyUpdates_CreateOrUpdate
        text: |-
               az maintenance applyupdate create --provider-name "Microsoft.Compute" --resource-group "examplerg" \
--resource-name "smdtest1" --resource-type "virtualMachineScaleSets"
"""

helps['maintenance applyupdate create-or-update-parent'] = """
    type: command
    short-summary: "Apply maintenance updates to resource with parent."
    examples:
      - name: ApplyUpdates_CreateOrUpdateParent
        text: |-
               az maintenance applyupdate create-or-update-parent --provider-name "Microsoft.Compute" --resource-group \
"examplerg" --resource-name "smdvm1" --resource-parent-name "smdtest1" --resource-parent-type \
"virtualMachineScaleSets" --resource-type "virtualMachines"
"""

helps['maintenance applyupdate show-parent'] = """
    type: command
    short-summary: "Track maintenance updates to resource with parent."
    examples:
      - name: ApplyUpdates_GetParent
        text: |-
               az maintenance applyupdate show-parent --name "e9b9685d-78e4-44c4-a81c-64a14f9b87b6" --provider-name \
"Microsoft.Compute" --resource-group "examplerg" --resource-name "smdvm1" --resource-parent-name "smdtest1" \
--resource-parent-type "virtualMachineScaleSets" --resource-type "virtualMachines"
"""

helps['maintenance assignment'] = """
    type: group
    short-summary: Manage configuration assignment with maintenance
"""

helps['maintenance assignment list'] = """
    type: command
    short-summary: "List configurationAssignments for resource."
    examples:
      - name: ConfigurationAssignments_List
        text: |-
               az maintenance assignment list --provider-name "Microsoft.Compute" --resource-group "examplerg" \
--resource-name "smdtest1" --resource-type "virtualMachineScaleSets"
"""

helps['maintenance assignment show'] = """
    type: command
    short-summary: "Get configuration for resource."
    examples:
      - name: ConfigurationAssignments_Get
        text: |-
               az maintenance assignment show --name "workervmConfiguration" --provider-name "Microsoft.Compute" \
--resource-group "examplerg" --resource-name "smdtest1" --resource-type "virtualMachineScaleSets"
"""

helps['maintenance assignment create'] = """
    type: command
    short-summary: "Register configuration for resource."
    examples:
      - name: ConfigurationAssignments_CreateOrUpdate
        text: |-
               az maintenance assignment create --maintenance-configuration-id "/subscriptions/5b4b650e-28b9-4790-b3ab-\
ddbd88d727c4/resourcegroups/examplerg/providers/Microsoft.Maintenance/maintenanceConfigurations/configuration1" --name \
"workervmConfiguration" --provider-name "Microsoft.Compute" --resource-group "examplerg" --resource-name "smdtest1" \
--resource-type "virtualMachineScaleSets"
"""

helps['maintenance assignment update'] = """
    type: command
    short-summary: "Register configuration for resource."
"""

helps['maintenance assignment delete'] = """
    type: command
    short-summary: "Unregister configuration for resource."
    examples:
      - name: ConfigurationAssignments_Delete
        text: |-
               az maintenance assignment delete --name "workervmConfiguration" --provider-name "Microsoft.Compute" \
--resource-group "examplerg" --resource-name "smdtest1" --resource-type "virtualMachineScaleSets"
"""

helps['maintenance assignment create-or-update-parent'] = """
    type: command
    short-summary: "Register configuration for resource."
    examples:
      - name: ConfigurationAssignments_CreateOrUpdateParent
        text: |-
               az maintenance assignment create-or-update-parent --maintenance-configuration-id \
"/subscriptions/5b4b650e-28b9-4790-b3ab-ddbd88d727c4/resourcegroups/examplerg/providers/Microsoft.Maintenance/maintenan\
ceConfigurations/policy1" --name "workervmPolicy" --provider-name "Microsoft.Compute" --resource-group "examplerg" \
--resource-name "smdvm1" --resource-parent-name "smdtest1" --resource-parent-type "virtualMachineScaleSets" \
--resource-type "virtualMachines"
"""

helps['maintenance assignment delete-parent'] = """
    type: command
    short-summary: "Unregister configuration for resource."
    examples:
      - name: ConfigurationAssignments_DeleteParent
        text: |-
               az maintenance assignment delete-parent --name "workervmConfiguration" --provider-name \
"Microsoft.Compute" --resource-group "examplerg" --resource-name "smdvm1" --resource-parent-name "smdtest1" \
--resource-parent-type "virtualMachineScaleSets" --resource-type "virtualMachines"
"""

helps['maintenance assignment list-parent'] = """
    type: command
    short-summary: "List configurationAssignments for resource."
    examples:
      - name: ConfigurationAssignments_ListParent
        text: |-
               az maintenance assignment list-parent --provider-name "Microsoft.Compute" --resource-group "examplerg" \
--resource-name "smdtestvm1" --resource-parent-name "smdtest1" --resource-parent-type "virtualMachineScaleSets" \
--resource-type "virtualMachines"
"""

helps['maintenance assignment show-parent'] = """
    type: command
    short-summary: "Get configuration for resource."
    examples:
      - name: ConfigurationAssignments_GetParent
        text: |-
               az maintenance assignment show-parent --name "workervmPolicy" --provider-name "Microsoft.Compute" \
--resource-group "examplerg" --resource-name "smdvm1" --resource-parent-name "smdtest1" --resource-parent-type \
"virtualMachineScaleSets" --resource-type "virtualMachines"
"""

helps['maintenance configuration'] = """
    type: group
    short-summary: Manage maintenance configuration with maintenance
"""

helps['maintenance configuration list'] = """
    type: command
    short-summary: "Get Configuration records within a subscription."
    examples:
      - name: MaintenanceConfigurations_List
        text: |-
               az maintenance configuration list
"""

helps['maintenance configuration show'] = """
    type: command
    short-summary: "Get Configuration record."
    examples:
      - name: MaintenanceConfigurations_GetForResource
        text: |-
               az maintenance configuration show --resource-group "examplerg" --resource-name "configuration1"
      - name: MaintenanceConfigurations_GetForResource_GuestOSPatchLinux
        text: |-
               az maintenance configuration show --resource-group "examplerg" --resource-name "configuration1"
      - name: MaintenanceConfigurations_GetForResource_GuestOSPatchWindows
        text: |-
               az maintenance configuration show --resource-group "examplerg" --resource-name "configuration1"
"""

helps['maintenance configuration create'] = """
    type: command
    short-summary: "Create configuration record."
    parameters:
      - name: --install-patches-windows-parameters --windows-parameters
        short-summary: "Input parameters specific to patching a Windows machine. For Linux machines, do not pass this \
property."
        long-summary: |
            Usage: --install-patches-windows-parameters kb-numbers-to-exclude=XX kb-numbers-to-include=XX \
classifications-to-include=XX exclude-kbs-requiring-reboot=XX

            kb-numbers-to-exclude: Windows KBID to be excluded for patching.
            kb-numbers-to-include: Windows KBID to be included for patching.
            classifications-to-include: Classification category of patches to be patched
            exclude-kbs-requiring-reboot: Exclude patches which need reboot
      - name: --install-patches-linux-parameters --linux-parameters
        short-summary: "Input parameters specific to patching Linux machine. For Windows machines, do not pass this \
property."
        long-summary: |
            Usage: --install-patches-linux-parameters package-name-masks-to-exclude=XX package-name-masks-to-include=XX\
 classifications-to-include=XX

            package-name-masks-to-exclude: Package names to be excluded for patching.
            package-name-masks-to-include: Package names to be included for patching.
            classifications-to-include: Classification category of patches to be patched
    examples:
      - name: MaintenanceConfigurations_CreateOrUpdateForResource
        text: |-
               az maintenance configuration create --location "westus2" --maintenance-scope "OSImage" \
--maintenance-window-duration "05:00" --maintenance-window-expiration-date-time "9999-12-31 00:00" \
--maintenance-window-recur-every "Day" --maintenance-window-start-date-time "2020-04-30 08:00" \
--maintenance-window-time-zone "Pacific Standard Time" --namespace "Microsoft.Maintenance" --visibility "Custom" \
--resource-group "examplerg" --resource-name "configuration1"
"""

helps['maintenance configuration update'] = """
    type: command
    short-summary: "Patch configuration record."
    parameters:
      - name: --install-patches-windows-parameters --windows-parameters
        short-summary: "Input parameters specific to patching a Windows machine. For Linux machines, do not pass this \
property."
        long-summary: |
            Usage: --install-patches-windows-parameters kb-numbers-to-exclude=XX kb-numbers-to-include=XX \
classifications-to-include=XX exclude-kbs-requiring-reboot=XX

            kb-numbers-to-exclude: Windows KBID to be excluded for patching.
            kb-numbers-to-include: Windows KBID to be included for patching.
            classifications-to-include: Classification category of patches to be patched
            exclude-kbs-requiring-reboot: Exclude patches which need reboot
      - name: --install-patches-linux-parameters --linux-parameters
        short-summary: "Input parameters specific to patching Linux machine. For Windows machines, do not pass this \
property."
        long-summary: |
            Usage: --install-patches-linux-parameters package-name-masks-to-exclude=XX package-name-masks-to-include=XX\
 classifications-to-include=XX

            package-name-masks-to-exclude: Package names to be excluded for patching.
            package-name-masks-to-include: Package names to be included for patching.
            classifications-to-include: Classification category of patches to be patched
    examples:
      - name: MaintenanceConfigurations_UpdateForResource
        text: |-
               az maintenance configuration update --location "westus2" --maintenance-scope "OSImage" \
--maintenance-window-duration "05:00" --maintenance-window-expiration-date-time "9999-12-31 00:00" \
--maintenance-window-recur-every "Month Third Sunday" --maintenance-window-start-date-time "2020-04-30 08:00" \
--maintenance-window-time-zone "Pacific Standard Time" --namespace "Microsoft.Maintenance" --visibility "Custom" \
--resource-group "examplerg" --resource-name "configuration1"
"""

helps['maintenance configuration delete'] = """
    type: command
    short-summary: "Delete Configuration record."
    examples:
      - name: MaintenanceConfigurations_DeleteForResource
        text: |-
               az maintenance configuration delete --resource-group "examplerg" --resource-name "example1"
"""

helps['maintenance update'] = """
    type: group
    short-summary: Manage update with maintenance
"""

helps['maintenance update list'] = """
    type: command
    short-summary: "Get updates to resources."
    examples:
      - name: Updates_List
        text: |-
               az maintenance update list --provider-name "Microsoft.Compute" --resource-group "examplerg" \
--resource-name "smdtest1" --resource-type "virtualMachineScaleSets"
"""

helps['maintenance update list-parent'] = """
    type: command
    short-summary: "Get updates to resources."
    examples:
      - name: Updates_ListParent
        text: |-
               az maintenance update list-parent --provider-name "Microsoft.Compute" --resource-group "examplerg" \
--resource-name "1" --resource-parent-name "smdtest1" --resource-parent-type "virtualMachineScaleSets" --resource-type \
"virtualMachines"
"""
