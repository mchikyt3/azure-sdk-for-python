# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, List, Mapping, Optional, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field
from .._vendor import FileType

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class BatchRequest(_model_base.Model):
    """Definition for the input batch translation request.

    All required parameters must be populated in order to send to server.

    :ivar source: Source of the input documents. Required.
    :vartype source: ~azure.ai.translation.document.models._models.SourceInput
    :ivar targets: Location of the destination for the output. Required.
    :vartype targets: list[~azure.ai.translation.document.models._models.TargetInput]
    :ivar storage_type: Storage type of the input documents source string. Known values are:
     "Folder" and "File".
    :vartype storage_type: str or ~azure.ai.translation.document.models.StorageInputType
    """

    source: "_models._models.SourceInput" = rest_field()
    """Source of the input documents. Required."""
    targets: List["_models._models.TargetInput"] = rest_field()
    """Location of the destination for the output. Required."""
    storage_type: Optional[Union[str, "_models._enums.StorageInputType"]] = rest_field(name="storageType")
    """Storage type of the input documents source string. Known values are: \"Folder\" and \"File\"."""


class DocumentFilter(_model_base.Model):
    """Document filter.

    :ivar prefix: A case-sensitive prefix string to filter documents in the source path for
     translation.
     For example, when using a Azure storage blob Uri, use the prefix
     to restrict sub folders for translation.
    :vartype prefix: str
    :ivar suffix: A case-sensitive suffix string to filter documents in the source path for
     translation.
     This is most often use for file extensions.
    :vartype suffix: str
    """

    prefix: Optional[str] = rest_field()
    """A case-sensitive prefix string to filter documents in the source path for
     translation.
     For example, when using a Azure storage blob Uri, use the prefix
     to restrict sub folders for translation."""
    suffix: Optional[str] = rest_field()
    """A case-sensitive suffix string to filter documents in the source path for
     translation.
     This is most often use for file extensions."""


class DocumentsStatus(_model_base.Model):
    """Documents Status Response.

    All required parameters must be populated in order to send to server.

    :ivar value: The detail status of individual documents. Required.
    :vartype value: list[~azure.ai.translation.document.models._models.DocumentStatus]
    :ivar next_link: Url for the next page.  Null if no more pages available.
    :vartype next_link: str
    """

    value: List["_models._models.DocumentStatus"] = rest_field()
    """The detail status of individual documents. Required."""
    next_link: Optional[str] = rest_field(name="nextLink")
    """Url for the next page.  Null if no more pages available."""


class DocumentStatus(_model_base.Model):
    """Document Status Response.

    All required parameters must be populated in order to send to server.

    :ivar path: Location of the document or folder.
    :vartype path: str
    :ivar source_path: Location of the source document. Required.
    :vartype source_path: str
    :ivar created_date_time_utc: Operation created date time. Required.
    :vartype created_date_time_utc: ~datetime.datetime
    :ivar last_action_date_time_utc: Date time in which the operation's status has been updated.
     Required.
    :vartype last_action_date_time_utc: ~datetime.datetime
    :ivar status: List of possible statuses for job or document. Required. Known values are:
     "NotStarted", "Running", "Succeeded", "Failed", "Cancelled", "Cancelling", and
     "ValidationFailed".
    :vartype status: str or ~azure.ai.translation.document.models.Status
    :ivar to: To language. Required.
    :vartype to: str
    :ivar error: This contains an outer error with error code, message, details, target and an
     inner error with more descriptive details.
    :vartype error: ~azure.ai.translation.document.models._models.TranslationError
    :ivar progress: Progress of the translation if available. Required.
    :vartype progress: float
    :ivar id: Document Id. Required.
    :vartype id: str
    :ivar character_charged: Character charged by the API.
    :vartype character_charged: int
    """

    path: Optional[str] = rest_field()
    """Location of the document or folder."""
    source_path: str = rest_field(name="sourcePath")
    """Location of the source document. Required."""
    created_date_time_utc: datetime.datetime = rest_field(name="createdDateTimeUtc", format="rfc3339")
    """Operation created date time. Required."""
    last_action_date_time_utc: datetime.datetime = rest_field(name="lastActionDateTimeUtc", format="rfc3339")
    """Date time in which the operation's status has been updated. Required."""
    status: Union[str, "_models._enums.Status"] = rest_field()
    """List of possible statuses for job or document. Required. Known values are: \"NotStarted\",
     \"Running\", \"Succeeded\", \"Failed\", \"Cancelled\", \"Cancelling\", and
     \"ValidationFailed\"."""
    to: str = rest_field()
    """To language. Required."""
    error: Optional["_models._models.TranslationError"] = rest_field()
    """This contains an outer error with error code, message, details, target and an
     inner error with more descriptive details."""
    progress: float = rest_field()
    """Progress of the translation if available. Required."""
    id: str = rest_field()
    """Document Id. Required."""
    character_charged: Optional[int] = rest_field(name="characterCharged")
    """Character charged by the API."""


class DocumentTranslateContent(_model_base.Model):
    """Document Translate Request Content.

    All required parameters must be populated in order to send to server.

    :ivar document: Document to be translated in the form. Required.
    :vartype document: bytes
    :ivar glossary: Glossary-translation memory will be used during translation in the form.
    :vartype glossary: list[bytes]
    """

    document: FileType = rest_field(is_multipart_file_input=True)
    """Document to be translated in the form. Required."""
    glossary: Optional[List[FileType]] = rest_field(is_multipart_file_input=True)
    """Glossary-translation memory will be used during translation in the form."""

    @overload
    def __init__(
        self,
        *,
        document: FileType,
        glossary: Optional[List[FileType]] = None,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class FileFormat(_model_base.Model):
    """File Format.

    All required parameters must be populated in order to send to server.

    :ivar format: Name of the format. Required.
    :vartype format: str
    :ivar file_extensions: Supported file extension for this format. Required.
    :vartype file_extensions: list[str]
    :ivar content_types: Supported Content-Types for this format. Required.
    :vartype content_types: list[str]
    :ivar default_version: Default version if none is specified.
    :vartype default_version: str
    :ivar versions: Supported Version.
    :vartype versions: list[str]
    :ivar type: Supported Type for this format.
    :vartype type: str
    """

    format: str = rest_field()
    """Name of the format. Required."""
    file_extensions: List[str] = rest_field(name="fileExtensions")
    """Supported file extension for this format. Required."""
    content_types: List[str] = rest_field(name="contentTypes")
    """Supported Content-Types for this format. Required."""
    default_version: Optional[str] = rest_field(name="defaultVersion")
    """Default version if none is specified."""
    versions: Optional[List[str]] = rest_field()
    """Supported Version."""
    type: Optional[str] = rest_field()
    """Supported Type for this format."""


class Glossary(_model_base.Model):
    """Glossary / translation memory for the request.

    All required parameters must be populated in order to send to server.

    :ivar glossary_url: Location of the glossary.
     We will use the file extension to extract the
     formatting if the format parameter is not supplied.

     If the translation
     language pair is not present in the glossary, it will not be applied. Required.
    :vartype glossary_url: str
    :ivar format: Format. Required.
    :vartype format: str
    :ivar version: Optional Version.  If not specified, default is used.
    :vartype version: str
    :ivar storage_source: Storage Source. "AzureBlob"
    :vartype storage_source: str or ~azure.ai.translation.document.models.StorageSource
    """

    glossary_url: str = rest_field(name="glossaryUrl")
    """Location of the glossary.
     We will use the file extension to extract the
     formatting if the format parameter is not supplied.
     
     If the translation
     language pair is not present in the glossary, it will not be applied. Required."""
    format: str = rest_field()
    """Format. Required."""
    version: Optional[str] = rest_field()
    """Optional Version.  If not specified, default is used."""
    storage_source: Optional[Union[str, "_models._enums.StorageSource"]] = rest_field(name="storageSource")
    """Storage Source. \"AzureBlob\""""


class InnerTranslationError(_model_base.Model):
    """New Inner Error format which conforms to Cognitive Services API Guidelines
    which is available at
    https://microsoft.sharepoint.com/%3Aw%3A/t/CognitiveServicesPMO/EUoytcrjuJdKpeOKIK_QRC8BPtUYQpKBi8JsWyeDMRsWlQ?e=CPq8ow.
    This
    contains required properties ErrorCode, message and optional properties target,
    details(key value pair), inner error(this can be nested).

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar code: Gets code error string. Required.
    :vartype code: str
    :ivar message: Gets high level error message. Required.
    :vartype message: str
    :ivar target: Gets the source of the error.
     For example it would be "documents" or
     "document id" in case of invalid document.
    :vartype target: str
    :ivar inner_error: New Inner Error format which conforms to Cognitive Services API Guidelines
     which is available at
    https://microsoft.sharepoint.com/%3Aw%3A/t/CognitiveServicesPMO/EUoytcrjuJdKpeOKIK_QRC8BPtUYQpKBi8JsWyeDMRsWlQ?e=CPq8ow.
     This
     contains required properties ErrorCode, message and optional properties target,
     details(key value pair), inner error(this can be nested).
    :vartype inner_error: ~azure.ai.translation.document.models._models.InnerTranslationError
    """

    code: str = rest_field()
    """Gets code error string. Required."""
    message: str = rest_field()
    """Gets high level error message. Required."""
    target: Optional[str] = rest_field(visibility=["read"])
    """Gets the source of the error.
     For example it would be \"documents\" or
     \"document id\" in case of invalid document."""
    inner_error: Optional["_models._models.InnerTranslationError"] = rest_field(name="innerError")
    """New Inner Error format which conforms to Cognitive Services API Guidelines
     which is available at
     https://microsoft.sharepoint.com/%3Aw%3A/t/CognitiveServicesPMO/EUoytcrjuJdKpeOKIK_QRC8BPtUYQpKBi8JsWyeDMRsWlQ?e=CPq8ow.  # pylint: disable=line-too-long
     This
     contains required properties ErrorCode, message and optional properties target,
     details(key value pair), inner error(this can be nested)."""


class SourceInput(_model_base.Model):
    """Source of the input documents.

    All required parameters must be populated in order to send to server.

    :ivar source_url: Location of the folder / container or single file with your documents.
     Required.
    :vartype source_url: str
    :ivar filter: Document filter.
    :vartype filter: ~azure.ai.translation.document.models._models.DocumentFilter
    :ivar language: Language code
     If none is specified, we will perform auto detect on the document.
    :vartype language: str
    :ivar storage_source: Storage Source. "AzureBlob"
    :vartype storage_source: str or ~azure.ai.translation.document.models.StorageSource
    """

    source_url: str = rest_field(name="sourceUrl")
    """Location of the folder / container or single file with your documents. Required."""
    filter: Optional["_models._models.DocumentFilter"] = rest_field()
    """Document filter."""
    language: Optional[str] = rest_field()
    """Language code
     If none is specified, we will perform auto detect on the document."""
    storage_source: Optional[Union[str, "_models._enums.StorageSource"]] = rest_field(name="storageSource")
    """Storage Source. \"AzureBlob\""""


class StartTranslationDetails(_model_base.Model):
    """Translation job submission batch request.

    All required parameters must be populated in order to send to server.

    :ivar inputs: The input list of documents or folders containing documents. Required.
    :vartype inputs: list[~azure.ai.translation.document.models._models.BatchRequest]
    """

    inputs: List["_models._models.BatchRequest"] = rest_field()
    """The input list of documents or folders containing documents. Required."""


class StatusSummary(_model_base.Model):
    """Status Summary.

    All required parameters must be populated in order to send to server.

    :ivar total: Total count. Required.
    :vartype total: int
    :ivar failed: Failed count. Required.
    :vartype failed: int
    :ivar success: Number of Success. Required.
    :vartype success: int
    :ivar in_progress: Number of in progress. Required.
    :vartype in_progress: int
    :ivar not_yet_started: Count of not yet started. Required.
    :vartype not_yet_started: int
    :ivar cancelled: Number of cancelled. Required.
    :vartype cancelled: int
    :ivar total_character_charged: Total characters charged by the API. Required.
    :vartype total_character_charged: int
    """

    total: int = rest_field()
    """Total count. Required."""
    failed: int = rest_field()
    """Failed count. Required."""
    success: int = rest_field()
    """Number of Success. Required."""
    in_progress: int = rest_field(name="inProgress")
    """Number of in progress. Required."""
    not_yet_started: int = rest_field(name="notYetStarted")
    """Count of not yet started. Required."""
    cancelled: int = rest_field()
    """Number of cancelled. Required."""
    total_character_charged: int = rest_field(name="totalCharacterCharged")
    """Total characters charged by the API. Required."""


class SupportedFileFormats(_model_base.Model):
    """List of supported file formats.

    All required parameters must be populated in order to send to server.

    :ivar value: list of objects. Required.
    :vartype value: list[~azure.ai.translation.document.models._models.FileFormat]
    """

    value: List["_models._models.FileFormat"] = rest_field()
    """list of objects. Required."""


class TargetInput(_model_base.Model):
    """Destination for the finished translated documents.

    All required parameters must be populated in order to send to server.

    :ivar target_url: Location of the folder / container with your documents. Required.
    :vartype target_url: str
    :ivar category: Category / custom system for translation request.
    :vartype category: str
    :ivar language: Target Language. Required.
    :vartype language: str
    :ivar glossaries: List of Glossary.
    :vartype glossaries: list[~azure.ai.translation.document.models._models.Glossary]
    :ivar storage_source: Storage Source. "AzureBlob"
    :vartype storage_source: str or ~azure.ai.translation.document.models.StorageSource
    """

    target_url: str = rest_field(name="targetUrl")
    """Location of the folder / container with your documents. Required."""
    category: Optional[str] = rest_field()
    """Category / custom system for translation request."""
    language: str = rest_field()
    """Target Language. Required."""
    glossaries: Optional[List["_models._models.Glossary"]] = rest_field()
    """List of Glossary."""
    storage_source: Optional[Union[str, "_models._enums.StorageSource"]] = rest_field(name="storageSource")
    """Storage Source. \"AzureBlob\""""


class TranslationError(_model_base.Model):
    """This contains an outer error with error code, message, details, target and an
    inner error with more descriptive details.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar code: Enums containing high level error codes. Required. Known values are:
     "InvalidRequest", "InvalidArgument", "InternalServerError", "ServiceUnavailable",
     "ResourceNotFound", "Unauthorized", and "RequestRateTooHigh".
    :vartype code: str or ~azure.ai.translation.document.models.TranslationErrorCode
    :ivar message: Gets high level error message. Required.
    :vartype message: str
    :ivar target: Gets the source of the error.
     For example it would be "documents" or
     "document id" in case of invalid document.
    :vartype target: str
    :ivar inner_error: New Inner Error format which conforms to Cognitive Services API Guidelines
     which is available at
    https://microsoft.sharepoint.com/%3Aw%3A/t/CognitiveServicesPMO/EUoytcrjuJdKpeOKIK_QRC8BPtUYQpKBi8JsWyeDMRsWlQ?e=CPq8ow.
     This
     contains required properties ErrorCode, message and optional properties target,
     details(key value pair), inner error(this can be nested).
    :vartype inner_error: ~azure.ai.translation.document.models._models.InnerTranslationError
    """

    code: Union[str, "_models._enums.TranslationErrorCode"] = rest_field()
    """Enums containing high level error codes. Required. Known values are: \"InvalidRequest\",
     \"InvalidArgument\", \"InternalServerError\", \"ServiceUnavailable\", \"ResourceNotFound\",
     \"Unauthorized\", and \"RequestRateTooHigh\"."""
    message: str = rest_field()
    """Gets high level error message. Required."""
    target: Optional[str] = rest_field(visibility=["read"])
    """Gets the source of the error.
     For example it would be \"documents\" or
     \"document id\" in case of invalid document."""
    inner_error: Optional["_models._models.InnerTranslationError"] = rest_field(name="innerError")
    """New Inner Error format which conforms to Cognitive Services API Guidelines
     which is available at
     https://microsoft.sharepoint.com/%3Aw%3A/t/CognitiveServicesPMO/EUoytcrjuJdKpeOKIK_QRC8BPtUYQpKBi8JsWyeDMRsWlQ?e=CPq8ow.  # pylint: disable=line-too-long
     This
     contains required properties ErrorCode, message and optional properties target,
     details(key value pair), inner error(this can be nested)."""


class TranslationsStatus(_model_base.Model):
    """Translation job Status Response.

    All required parameters must be populated in order to send to server.

    :ivar value: The summary status of individual operation. Required.
    :vartype value: list[~azure.ai.translation.document.models._models.TranslationStatus]
    :ivar next_link: Url for the next page.  Null if no more pages available.
    :vartype next_link: str
    """

    value: List["_models._models.TranslationStatus"] = rest_field()
    """The summary status of individual operation. Required."""
    next_link: Optional[str] = rest_field(name="nextLink")
    """Url for the next page.  Null if no more pages available."""


class TranslationStatus(_model_base.Model):
    """Translation job status response.

    All required parameters must be populated in order to send to server.

    :ivar id: Id of the operation. Required.
    :vartype id: str
    :ivar created_date_time_utc: Operation created date time. Required.
    :vartype created_date_time_utc: ~datetime.datetime
    :ivar last_action_date_time_utc: Date time in which the operation's status has been updated.
     Required.
    :vartype last_action_date_time_utc: ~datetime.datetime
    :ivar status: List of possible statuses for job or document. Required. Known values are:
     "NotStarted", "Running", "Succeeded", "Failed", "Cancelled", "Cancelling", and
     "ValidationFailed".
    :vartype status: str or ~azure.ai.translation.document.models.Status
    :ivar error: This contains an outer error with error code, message, details, target and an
     inner error with more descriptive details.
    :vartype error: ~azure.ai.translation.document.models._models.TranslationError
    :ivar summary: Status Summary. Required.
    :vartype summary: ~azure.ai.translation.document.models._models.StatusSummary
    """

    id: str = rest_field()
    """Id of the operation. Required."""
    created_date_time_utc: datetime.datetime = rest_field(name="createdDateTimeUtc", format="rfc3339")
    """Operation created date time. Required."""
    last_action_date_time_utc: datetime.datetime = rest_field(name="lastActionDateTimeUtc", format="rfc3339")
    """Date time in which the operation's status has been updated. Required."""
    status: Union[str, "_models._enums.Status"] = rest_field()
    """List of possible statuses for job or document. Required. Known values are: \"NotStarted\",
     \"Running\", \"Succeeded\", \"Failed\", \"Cancelled\", \"Cancelling\", and
     \"ValidationFailed\"."""
    error: Optional["_models._models.TranslationError"] = rest_field()
    """This contains an outer error with error code, message, details, target and an
     inner error with more descriptive details."""
    summary: "_models._models.StatusSummary" = rest_field()
    """Status Summary. Required."""
