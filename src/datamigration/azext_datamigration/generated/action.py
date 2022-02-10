# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


# pylint: disable=protected-access

# pylint: disable=no-self-use


import argparse
from collections import defaultdict
from knack.util import CLIError


class AddSourceSqlConnection(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.source_sql_connection = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'data-source':
                d['data_source'] = v[0]

            elif kl == 'authentication':
                d['authentication'] = v[0]

            elif kl == 'user-name':
                d['user_name'] = v[0]

            elif kl == 'password':
                d['password'] = v[0]

            elif kl == 'encrypt-connection':
                d['encrypt_connection'] = v[0]

            elif kl == 'trust-server-certificate':
                d['trust_server_certificate'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter source-sql-connection. All possible keys are:'
                    ' data-source, authentication, user-name, password, encrypt-connection, trust-server-certificate'
                    .format(k)
                )

        return d


class AddOfflineConfiguration(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.offline_configuration = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'offline':
                d['offline'] = v[0]

            elif kl == 'last-backup-name':
                d['last_backup_name'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter offline-configuration. All possible keys are:'
                    ' offline, last-backup-name'.format(k)
                )

        return d


class AddTargetLocation(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.target_location = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'storage-account-resource-id':
                d['storage_account_resource_id'] = v[0]

            elif kl == 'account-key':
                d['account_key'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter target-location. All possible keys are:'
                    ' storage-account-resource-id, account-key'.format(k)
                )

        return d