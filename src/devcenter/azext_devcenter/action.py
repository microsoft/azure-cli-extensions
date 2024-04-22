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


import argparse
from collections import defaultdict
from knack.util import CLIError


class AddEmailNotification(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.email_notification = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for k, v in (x.split("=", 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError(
                f"usage error: {option_string} [KEY=VALUE ...]"
            ) from ValueError
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == "enabled":
                d["enabled"] = v[0]

            elif kl == "recipients":
                d["recipients"] = v[0]

            elif kl == "cc":
                d["cc"] = v[0]

            else:
                raise CLIError(
                    f"Unsupported Key {k} is provided for parameter email-notification. All possible keys are: enabled,"
                    f" recipients, cc"
                )

        return d


class AddWebhookNotification(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.webhook_notification = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for k, v in (x.split("=", 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError(
                f"usage error: {option_string} [KEY=VALUE ...]"
            ) from ValueError
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == "enabled":
                d["enabled"] = v[0]

            elif kl == "url":
                d["url"] = v[0]

            else:
                raise CLIError(
                    f"Unsupported Key {k} is provided for parameter webhook-notification. All possible keys are:"
                    f" enabled, url"
                )

        return d
