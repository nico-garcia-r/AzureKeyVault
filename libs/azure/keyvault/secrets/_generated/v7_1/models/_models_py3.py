# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Dict, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Attributes(msrest.serialization.Model):
    """The object attributes managed by the KeyVault service.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar enabled: Determines whether the object is enabled.
    :vartype enabled: bool
    :ivar not_before: Not before date in UTC.
    :vartype not_before: ~datetime.datetime
    :ivar expires: Expiry date in UTC.
    :vartype expires: ~datetime.datetime
    :ivar created: Creation time in UTC.
    :vartype created: ~datetime.datetime
    :ivar updated: Last updated time in UTC.
    :vartype updated: ~datetime.datetime
    """

    _validation = {
        'created': {'readonly': True},
        'updated': {'readonly': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'not_before': {'key': 'nbf', 'type': 'unix-time'},
        'expires': {'key': 'exp', 'type': 'unix-time'},
        'created': {'key': 'created', 'type': 'unix-time'},
        'updated': {'key': 'updated', 'type': 'unix-time'},
    }

    def __init__(
        self,
        *,
        enabled: Optional[bool] = None,
        not_before: Optional[datetime.datetime] = None,
        expires: Optional[datetime.datetime] = None,
        **kwargs
    ):
        """
        :keyword enabled: Determines whether the object is enabled.
        :paramtype enabled: bool
        :keyword not_before: Not before date in UTC.
        :paramtype not_before: ~datetime.datetime
        :keyword expires: Expiry date in UTC.
        :paramtype expires: ~datetime.datetime
        """
        super(Attributes, self).__init__(**kwargs)
        self.enabled = enabled
        self.not_before = not_before
        self.expires = expires
        self.created = None
        self.updated = None


class BackupSecretResult(msrest.serialization.Model):
    """The backup secret result, containing the backup blob.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: The backup blob containing the backed up secret.
    :vartype value: bytes
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'base64'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(BackupSecretResult, self).__init__(**kwargs)
        self.value = None


class SecretBundle(msrest.serialization.Model):
    """A secret consisting of a value, id and its attributes.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: The secret value.
    :vartype value: str
    :ivar id: The secret id.
    :vartype id: str
    :ivar content_type: The content type of the secret.
    :vartype content_type: str
    :ivar attributes: The secret management attributes.
    :vartype attributes: ~azure.keyvault.v7_1.models.SecretAttributes
    :ivar tags: A set of tags. Application specific metadata in the form of key-value pairs.
    :vartype tags: dict[str, str]
    :ivar kid: If this is a secret backing a KV certificate, then this field specifies the
     corresponding key backing the KV certificate.
    :vartype kid: str
    :ivar managed: True if the secret's lifetime is managed by key vault. If this is a secret
     backing a certificate, then managed will be true.
    :vartype managed: bool
    """

    _validation = {
        'kid': {'readonly': True},
        'managed': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'SecretAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'kid': {'key': 'kid', 'type': 'str'},
        'managed': {'key': 'managed', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        value: Optional[str] = None,
        id: Optional[str] = None,
        content_type: Optional[str] = None,
        attributes: Optional["SecretAttributes"] = None,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        """
        :keyword value: The secret value.
        :paramtype value: str
        :keyword id: The secret id.
        :paramtype id: str
        :keyword content_type: The content type of the secret.
        :paramtype content_type: str
        :keyword attributes: The secret management attributes.
        :paramtype attributes: ~azure.keyvault.v7_1.models.SecretAttributes
        :keyword tags: A set of tags. Application specific metadata in the form of key-value pairs.
        :paramtype tags: dict[str, str]
        """
        super(SecretBundle, self).__init__(**kwargs)
        self.value = value
        self.id = id
        self.content_type = content_type
        self.attributes = attributes
        self.tags = tags
        self.kid = None
        self.managed = None


class DeletedSecretBundle(SecretBundle):
    """A Deleted Secret consisting of its previous id, attributes and its tags, as well as information on when it will be purged.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: The secret value.
    :vartype value: str
    :ivar id: The secret id.
    :vartype id: str
    :ivar content_type: The content type of the secret.
    :vartype content_type: str
    :ivar attributes: The secret management attributes.
    :vartype attributes: ~azure.keyvault.v7_1.models.SecretAttributes
    :ivar tags: A set of tags. Application specific metadata in the form of key-value pairs.
    :vartype tags: dict[str, str]
    :ivar kid: If this is a secret backing a KV certificate, then this field specifies the
     corresponding key backing the KV certificate.
    :vartype kid: str
    :ivar managed: True if the secret's lifetime is managed by key vault. If this is a secret
     backing a certificate, then managed will be true.
    :vartype managed: bool
    :ivar recovery_id: The url of the recovery object, used to identify and recover the deleted
     secret.
    :vartype recovery_id: str
    :ivar scheduled_purge_date: The time when the secret is scheduled to be purged, in UTC.
    :vartype scheduled_purge_date: ~datetime.datetime
    :ivar deleted_date: The time when the secret was deleted, in UTC.
    :vartype deleted_date: ~datetime.datetime
    """

    _validation = {
        'kid': {'readonly': True},
        'managed': {'readonly': True},
        'scheduled_purge_date': {'readonly': True},
        'deleted_date': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'SecretAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'kid': {'key': 'kid', 'type': 'str'},
        'managed': {'key': 'managed', 'type': 'bool'},
        'recovery_id': {'key': 'recoveryId', 'type': 'str'},
        'scheduled_purge_date': {'key': 'scheduledPurgeDate', 'type': 'unix-time'},
        'deleted_date': {'key': 'deletedDate', 'type': 'unix-time'},
    }

    def __init__(
        self,
        *,
        value: Optional[str] = None,
        id: Optional[str] = None,
        content_type: Optional[str] = None,
        attributes: Optional["SecretAttributes"] = None,
        tags: Optional[Dict[str, str]] = None,
        recovery_id: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword value: The secret value.
        :paramtype value: str
        :keyword id: The secret id.
        :paramtype id: str
        :keyword content_type: The content type of the secret.
        :paramtype content_type: str
        :keyword attributes: The secret management attributes.
        :paramtype attributes: ~azure.keyvault.v7_1.models.SecretAttributes
        :keyword tags: A set of tags. Application specific metadata in the form of key-value pairs.
        :paramtype tags: dict[str, str]
        :keyword recovery_id: The url of the recovery object, used to identify and recover the deleted
         secret.
        :paramtype recovery_id: str
        """
        super(DeletedSecretBundle, self).__init__(value=value, id=id, content_type=content_type, attributes=attributes, tags=tags, **kwargs)
        self.recovery_id = recovery_id
        self.scheduled_purge_date = None
        self.deleted_date = None


class SecretItem(msrest.serialization.Model):
    """The secret item containing secret metadata.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Secret identifier.
    :vartype id: str
    :ivar attributes: The secret management attributes.
    :vartype attributes: ~azure.keyvault.v7_1.models.SecretAttributes
    :ivar tags: A set of tags. Application specific metadata in the form of key-value pairs.
    :vartype tags: dict[str, str]
    :ivar content_type: Type of the secret value such as a password.
    :vartype content_type: str
    :ivar managed: True if the secret's lifetime is managed by key vault. If this is a key backing
     a certificate, then managed will be true.
    :vartype managed: bool
    """

    _validation = {
        'managed': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'SecretAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'managed': {'key': 'managed', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        attributes: Optional["SecretAttributes"] = None,
        tags: Optional[Dict[str, str]] = None,
        content_type: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword id: Secret identifier.
        :paramtype id: str
        :keyword attributes: The secret management attributes.
        :paramtype attributes: ~azure.keyvault.v7_1.models.SecretAttributes
        :keyword tags: A set of tags. Application specific metadata in the form of key-value pairs.
        :paramtype tags: dict[str, str]
        :keyword content_type: Type of the secret value such as a password.
        :paramtype content_type: str
        """
        super(SecretItem, self).__init__(**kwargs)
        self.id = id
        self.attributes = attributes
        self.tags = tags
        self.content_type = content_type
        self.managed = None


class DeletedSecretItem(SecretItem):
    """The deleted secret item containing metadata about the deleted secret.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Secret identifier.
    :vartype id: str
    :ivar attributes: The secret management attributes.
    :vartype attributes: ~azure.keyvault.v7_1.models.SecretAttributes
    :ivar tags: A set of tags. Application specific metadata in the form of key-value pairs.
    :vartype tags: dict[str, str]
    :ivar content_type: Type of the secret value such as a password.
    :vartype content_type: str
    :ivar managed: True if the secret's lifetime is managed by key vault. If this is a key backing
     a certificate, then managed will be true.
    :vartype managed: bool
    :ivar recovery_id: The url of the recovery object, used to identify and recover the deleted
     secret.
    :vartype recovery_id: str
    :ivar scheduled_purge_date: The time when the secret is scheduled to be purged, in UTC.
    :vartype scheduled_purge_date: ~datetime.datetime
    :ivar deleted_date: The time when the secret was deleted, in UTC.
    :vartype deleted_date: ~datetime.datetime
    """

    _validation = {
        'managed': {'readonly': True},
        'scheduled_purge_date': {'readonly': True},
        'deleted_date': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'SecretAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'managed': {'key': 'managed', 'type': 'bool'},
        'recovery_id': {'key': 'recoveryId', 'type': 'str'},
        'scheduled_purge_date': {'key': 'scheduledPurgeDate', 'type': 'unix-time'},
        'deleted_date': {'key': 'deletedDate', 'type': 'unix-time'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        attributes: Optional["SecretAttributes"] = None,
        tags: Optional[Dict[str, str]] = None,
        content_type: Optional[str] = None,
        recovery_id: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword id: Secret identifier.
        :paramtype id: str
        :keyword attributes: The secret management attributes.
        :paramtype attributes: ~azure.keyvault.v7_1.models.SecretAttributes
        :keyword tags: A set of tags. Application specific metadata in the form of key-value pairs.
        :paramtype tags: dict[str, str]
        :keyword content_type: Type of the secret value such as a password.
        :paramtype content_type: str
        :keyword recovery_id: The url of the recovery object, used to identify and recover the deleted
         secret.
        :paramtype recovery_id: str
        """
        super(DeletedSecretItem, self).__init__(id=id, attributes=attributes, tags=tags, content_type=content_type, **kwargs)
        self.recovery_id = recovery_id
        self.scheduled_purge_date = None
        self.deleted_date = None


class DeletedSecretListResult(msrest.serialization.Model):
    """The deleted secret list result.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: A response message containing a list of the deleted secrets in the vault along
     with a link to the next page of deleted secrets.
    :vartype value: list[~azure.keyvault.v7_1.models.DeletedSecretItem]
    :ivar next_link: The URL to get the next set of deleted secrets.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DeletedSecretItem]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(DeletedSecretListResult, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class Error(msrest.serialization.Model):
    """The key vault server error.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar inner_error: The key vault server error.
    :vartype inner_error: ~azure.keyvault.v7_1.models.Error
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'inner_error': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'inner_error': {'key': 'innererror', 'type': 'Error'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(Error, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.inner_error = None


class KeyVaultError(msrest.serialization.Model):
    """The key vault error exception.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar error: The key vault server error.
    :vartype error: ~azure.keyvault.v7_1.models.Error
    """

    _validation = {
        'error': {'readonly': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'Error'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(KeyVaultError, self).__init__(**kwargs)
        self.error = None


class SecretAttributes(Attributes):
    """The secret management attributes.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar enabled: Determines whether the object is enabled.
    :vartype enabled: bool
    :ivar not_before: Not before date in UTC.
    :vartype not_before: ~datetime.datetime
    :ivar expires: Expiry date in UTC.
    :vartype expires: ~datetime.datetime
    :ivar created: Creation time in UTC.
    :vartype created: ~datetime.datetime
    :ivar updated: Last updated time in UTC.
    :vartype updated: ~datetime.datetime
    :ivar recoverable_days: softDelete data retention days. Value should be >=7 and <=90 when
     softDelete enabled, otherwise 0.
    :vartype recoverable_days: int
    :ivar recovery_level: Reflects the deletion recovery level currently in effect for secrets in
     the current vault. If it contains 'Purgeable', the secret can be permanently deleted by a
     privileged user; otherwise, only the system can purge the secret, at the end of the retention
     interval. Possible values include: "Purgeable", "Recoverable+Purgeable", "Recoverable",
     "Recoverable+ProtectedSubscription", "CustomizedRecoverable+Purgeable",
     "CustomizedRecoverable", "CustomizedRecoverable+ProtectedSubscription".
    :vartype recovery_level: str or ~azure.keyvault.v7_1.models.DeletionRecoveryLevel
    """

    _validation = {
        'created': {'readonly': True},
        'updated': {'readonly': True},
        'recoverable_days': {'readonly': True},
        'recovery_level': {'readonly': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'not_before': {'key': 'nbf', 'type': 'unix-time'},
        'expires': {'key': 'exp', 'type': 'unix-time'},
        'created': {'key': 'created', 'type': 'unix-time'},
        'updated': {'key': 'updated', 'type': 'unix-time'},
        'recoverable_days': {'key': 'recoverableDays', 'type': 'int'},
        'recovery_level': {'key': 'recoveryLevel', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        enabled: Optional[bool] = None,
        not_before: Optional[datetime.datetime] = None,
        expires: Optional[datetime.datetime] = None,
        **kwargs
    ):
        """
        :keyword enabled: Determines whether the object is enabled.
        :paramtype enabled: bool
        :keyword not_before: Not before date in UTC.
        :paramtype not_before: ~datetime.datetime
        :keyword expires: Expiry date in UTC.
        :paramtype expires: ~datetime.datetime
        """
        super(SecretAttributes, self).__init__(enabled=enabled, not_before=not_before, expires=expires, **kwargs)
        self.recoverable_days = None
        self.recovery_level = None


class SecretListResult(msrest.serialization.Model):
    """The secret list result.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: A response message containing a list of secrets in the key vault along with a link
     to the next page of secrets.
    :vartype value: list[~azure.keyvault.v7_1.models.SecretItem]
    :ivar next_link: The URL to get the next set of secrets.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[SecretItem]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(SecretListResult, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class SecretProperties(msrest.serialization.Model):
    """Properties of the key backing a certificate.

    :ivar content_type: The media type (MIME type).
    :vartype content_type: str
    """

    _attribute_map = {
        'content_type': {'key': 'contentType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        content_type: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword content_type: The media type (MIME type).
        :paramtype content_type: str
        """
        super(SecretProperties, self).__init__(**kwargs)
        self.content_type = content_type


class SecretRestoreParameters(msrest.serialization.Model):
    """The secret restore parameters.

    All required parameters must be populated in order to send to Azure.

    :ivar secret_bundle_backup: Required. The backup blob associated with a secret bundle.
    :vartype secret_bundle_backup: bytes
    """

    _validation = {
        'secret_bundle_backup': {'required': True},
    }

    _attribute_map = {
        'secret_bundle_backup': {'key': 'value', 'type': 'base64'},
    }

    def __init__(
        self,
        *,
        secret_bundle_backup: bytes,
        **kwargs
    ):
        """
        :keyword secret_bundle_backup: Required. The backup blob associated with a secret bundle.
        :paramtype secret_bundle_backup: bytes
        """
        super(SecretRestoreParameters, self).__init__(**kwargs)
        self.secret_bundle_backup = secret_bundle_backup


class SecretSetParameters(msrest.serialization.Model):
    """The secret set parameters.

    All required parameters must be populated in order to send to Azure.

    :ivar value: Required. The value of the secret.
    :vartype value: str
    :ivar tags: A set of tags. Application specific metadata in the form of key-value pairs.
    :vartype tags: dict[str, str]
    :ivar content_type: Type of the secret value such as a password.
    :vartype content_type: str
    :ivar secret_attributes: The secret management attributes.
    :vartype secret_attributes: ~azure.keyvault.v7_1.models.SecretAttributes
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'secret_attributes': {'key': 'attributes', 'type': 'SecretAttributes'},
    }

    def __init__(
        self,
        *,
        value: str,
        tags: Optional[Dict[str, str]] = None,
        content_type: Optional[str] = None,
        secret_attributes: Optional["SecretAttributes"] = None,
        **kwargs
    ):
        """
        :keyword value: Required. The value of the secret.
        :paramtype value: str
        :keyword tags: A set of tags. Application specific metadata in the form of key-value pairs.
        :paramtype tags: dict[str, str]
        :keyword content_type: Type of the secret value such as a password.
        :paramtype content_type: str
        :keyword secret_attributes: The secret management attributes.
        :paramtype secret_attributes: ~azure.keyvault.v7_1.models.SecretAttributes
        """
        super(SecretSetParameters, self).__init__(**kwargs)
        self.value = value
        self.tags = tags
        self.content_type = content_type
        self.secret_attributes = secret_attributes


class SecretUpdateParameters(msrest.serialization.Model):
    """The secret update parameters.

    :ivar content_type: Type of the secret value such as a password.
    :vartype content_type: str
    :ivar secret_attributes: The secret management attributes.
    :vartype secret_attributes: ~azure.keyvault.v7_1.models.SecretAttributes
    :ivar tags: A set of tags. Application specific metadata in the form of key-value pairs.
    :vartype tags: dict[str, str]
    """

    _attribute_map = {
        'content_type': {'key': 'contentType', 'type': 'str'},
        'secret_attributes': {'key': 'attributes', 'type': 'SecretAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        content_type: Optional[str] = None,
        secret_attributes: Optional["SecretAttributes"] = None,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        """
        :keyword content_type: Type of the secret value such as a password.
        :paramtype content_type: str
        :keyword secret_attributes: The secret management attributes.
        :paramtype secret_attributes: ~azure.keyvault.v7_1.models.SecretAttributes
        :keyword tags: A set of tags. Application specific metadata in the form of key-value pairs.
        :paramtype tags: dict[str, str]
        """
        super(SecretUpdateParameters, self).__init__(**kwargs)
        self.content_type = content_type
        self.secret_attributes = secret_attributes
        self.tags = tags