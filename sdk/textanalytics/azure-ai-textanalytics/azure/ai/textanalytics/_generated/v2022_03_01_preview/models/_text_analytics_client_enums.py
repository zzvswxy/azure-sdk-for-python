# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class AnalyzeTextLROResultsKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enumeration of supported Text Analysis long-running operation task results.
    """

    SENTIMENT_ANALYSIS_LRO_RESULTS = "SentimentAnalysisLROResults"
    ENTITY_RECOGNITION_LRO_RESULTS = "EntityRecognitionLROResults"
    PII_ENTITY_RECOGNITION_LRO_RESULTS = "PiiEntityRecognitionLROResults"
    KEY_PHRASE_EXTRACTION_LRO_RESULTS = "KeyPhraseExtractionLROResults"
    ENTITY_LINKING_LRO_RESULTS = "EntityLinkingLROResults"
    HEALTHCARE_LRO_RESULTS = "HealthcareLROResults"
    EXTRACTIVE_SUMMARIZATION_LRO_RESULTS = "ExtractiveSummarizationLROResults"
    CUSTOM_ENTITY_RECOGNITION_LRO_RESULTS = "CustomEntityRecognitionLROResults"
    CUSTOM_SINGLE_LABEL_CLASSIFICATION_LRO_RESULTS = "CustomSingleLabelClassificationLROResults"
    CUSTOM_MULTI_LABEL_CLASSIFICATION_LRO_RESULTS = "CustomMultiLabelClassificationLROResults"

class AnalyzeTextLROTaskKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enumeration of supported long-running Text Analysis tasks.
    """

    SENTIMENT_ANALYSIS = "SentimentAnalysis"
    ENTITY_RECOGNITION = "EntityRecognition"
    PII_ENTITY_RECOGNITION = "PiiEntityRecognition"
    KEY_PHRASE_EXTRACTION = "KeyPhraseExtraction"
    ENTITY_LINKING = "EntityLinking"
    HEALTHCARE = "Healthcare"
    EXTRACTIVE_SUMMARIZATION = "ExtractiveSummarization"
    CUSTOM_ENTITY_RECOGNITION = "CustomEntityRecognition"
    CUSTOM_SINGLE_LABEL_CLASSIFICATION = "CustomSingleLabelClassification"
    CUSTOM_MULTI_LABEL_CLASSIFICATION = "CustomMultiLabelClassification"

class AnalyzeTextTaskKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enumeration of supported Text Analysis tasks.
    """

    SENTIMENT_ANALYSIS = "SentimentAnalysis"
    ENTITY_RECOGNITION = "EntityRecognition"
    PII_ENTITY_RECOGNITION = "PiiEntityRecognition"
    KEY_PHRASE_EXTRACTION = "KeyPhraseExtraction"
    LANGUAGE_DETECTION = "LanguageDetection"
    ENTITY_LINKING = "EntityLinking"

class AnalyzeTextTaskResultsKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enumeration of supported Text Analysis task results.
    """

    SENTIMENT_ANALYSIS_RESULTS = "SentimentAnalysisResults"
    ENTITY_RECOGNITION_RESULTS = "EntityRecognitionResults"
    PII_ENTITY_RECOGNITION_RESULTS = "PiiEntityRecognitionResults"
    KEY_PHRASE_EXTRACTION_RESULTS = "KeyPhraseExtractionResults"
    LANGUAGE_DETECTION_RESULTS = "LanguageDetectionResults"
    ENTITY_LINKING_RESULTS = "EntityLinkingResults"

class Association(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Describes if the entity is the subject of the text or if it describes someone else.
    """

    SUBJECT = "subject"
    OTHER = "other"

class Certainty(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Describes the entities certainty and polarity.
    """

    POSITIVE = "positive"
    POSITIVE_POSSIBLE = "positivePossible"
    NEUTRAL_POSSIBLE = "neutralPossible"
    NEGATIVE_POSSIBLE = "negativePossible"
    NEGATIVE = "negative"

class Conditionality(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Describes any conditionality on the entity.
    """

    HYPOTHETICAL = "hypothetical"
    CONDITIONAL = "conditional"

class DocumentSentimentValue(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Predicted sentiment for document (Negative, Neutral, Positive, or Mixed).
    """

    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"
    MIXED = "mixed"

class ErrorCode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Human-readable error code.
    """

    INVALID_REQUEST = "InvalidRequest"
    INVALID_ARGUMENT = "InvalidArgument"
    UNAUTHORIZED = "Unauthorized"
    FORBIDDEN = "Forbidden"
    NOT_FOUND = "NotFound"
    PROJECT_NOT_FOUND = "ProjectNotFound"
    OPERATION_NOT_FOUND = "OperationNotFound"
    AZURE_COGNITIVE_SEARCH_NOT_FOUND = "AzureCognitiveSearchNotFound"
    AZURE_COGNITIVE_SEARCH_INDEX_NOT_FOUND = "AzureCognitiveSearchIndexNotFound"
    TOO_MANY_REQUESTS = "TooManyRequests"
    AZURE_COGNITIVE_SEARCH_THROTTLING = "AzureCognitiveSearchThrottling"
    AZURE_COGNITIVE_SEARCH_INDEX_LIMIT_REACHED = "AzureCognitiveSearchIndexLimitReached"
    INTERNAL_SERVER_ERROR = "InternalServerError"
    SERVICE_UNAVAILABLE = "ServiceUnavailable"

class ExtractiveSummarizationSortingCriteria(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The sorting criteria to use for the results of Extractive Summarization.
    """

    #: Indicates that results should be sorted in order of appearance in the text.
    OFFSET = "Offset"
    #: Indicates that results should be sorted in order of importance (i.e. rank score) according to
    #: the model.
    RANK = "Rank"

class HealthcareEntityCategory(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Healthcare Entity Category.
    """

    BODY_STRUCTURE = "BODY_STRUCTURE"
    AGE = "AGE"
    GENDER = "GENDER"
    EXAMINATION_NAME = "EXAMINATION_NAME"
    DATE = "DATE"
    DIRECTION = "DIRECTION"
    FREQUENCY = "FREQUENCY"
    MEASUREMENT_VALUE = "MEASUREMENT_VALUE"
    MEASUREMENT_UNIT = "MEASUREMENT_UNIT"
    RELATIONAL_OPERATOR = "RELATIONAL_OPERATOR"
    TIME = "TIME"
    GENE_OR_PROTEIN = "GENE_OR_PROTEIN"
    VARIANT = "VARIANT"
    ADMINISTRATIVE_EVENT = "ADMINISTRATIVE_EVENT"
    CARE_ENVIRONMENT = "CARE_ENVIRONMENT"
    HEALTHCARE_PROFESSION = "HEALTHCARE_PROFESSION"
    DIAGNOSIS = "DIAGNOSIS"
    SYMPTOM_OR_SIGN = "SYMPTOM_OR_SIGN"
    CONDITION_QUALIFIER = "CONDITION_QUALIFIER"
    MEDICATION_CLASS = "MEDICATION_CLASS"
    MEDICATION_NAME = "MEDICATION_NAME"
    DOSAGE = "DOSAGE"
    MEDICATION_FORM = "MEDICATION_FORM"
    MEDICATION_ROUTE = "MEDICATION_ROUTE"
    FAMILY_RELATION = "FAMILY_RELATION"
    TREATMENT_NAME = "TREATMENT_NAME"

class InnerErrorCode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Human-readable error code.
    """

    INVALID_REQUEST = "InvalidRequest"
    INVALID_PARAMETER_VALUE = "InvalidParameterValue"
    KNOWLEDGE_BASE_NOT_FOUND = "KnowledgeBaseNotFound"
    AZURE_COGNITIVE_SEARCH_NOT_FOUND = "AzureCognitiveSearchNotFound"
    AZURE_COGNITIVE_SEARCH_THROTTLING = "AzureCognitiveSearchThrottling"
    EXTRACTION_FAILURE = "ExtractionFailure"
    INVALID_REQUEST_BODY_FORMAT = "InvalidRequestBodyFormat"
    EMPTY_REQUEST = "EmptyRequest"
    MISSING_INPUT_DOCUMENTS = "MissingInputDocuments"
    INVALID_DOCUMENT = "InvalidDocument"
    MODEL_VERSION_INCORRECT = "ModelVersionIncorrect"
    INVALID_DOCUMENT_BATCH = "InvalidDocumentBatch"
    UNSUPPORTED_LANGUAGE_CODE = "UnsupportedLanguageCode"
    INVALID_COUNTRY_HINT = "InvalidCountryHint"

class PiiCategory(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    ABA_ROUTING_NUMBER = "ABARoutingNumber"
    AR_NATIONAL_IDENTITY_NUMBER = "ARNationalIdentityNumber"
    AU_BANK_ACCOUNT_NUMBER = "AUBankAccountNumber"
    AU_DRIVERS_LICENSE_NUMBER = "AUDriversLicenseNumber"
    AU_MEDICAL_ACCOUNT_NUMBER = "AUMedicalAccountNumber"
    AU_PASSPORT_NUMBER = "AUPassportNumber"
    AU_TAX_FILE_NUMBER = "AUTaxFileNumber"
    AU_BUSINESS_NUMBER = "AUBusinessNumber"
    AU_COMPANY_NUMBER = "AUCompanyNumber"
    AT_IDENTITY_CARD = "ATIdentityCard"
    AT_TAX_IDENTIFICATION_NUMBER = "ATTaxIdentificationNumber"
    AT_VALUE_ADDED_TAX_NUMBER = "ATValueAddedTaxNumber"
    AZURE_DOCUMENT_DB_AUTH_KEY = "AzureDocumentDBAuthKey"
    AZURE_IAAS_DATABASE_CONNECTION_AND_SQL_STRING = "AzureIAASDatabaseConnectionAndSQLString"
    AZURE_IO_T_CONNECTION_STRING = "AzureIoTConnectionString"
    AZURE_PUBLISH_SETTING_PASSWORD = "AzurePublishSettingPassword"
    AZURE_REDIS_CACHE_STRING = "AzureRedisCacheString"
    AZURE_SAS = "AzureSAS"
    AZURE_SERVICE_BUS_STRING = "AzureServiceBusString"
    AZURE_STORAGE_ACCOUNT_KEY = "AzureStorageAccountKey"
    AZURE_STORAGE_ACCOUNT_GENERIC = "AzureStorageAccountGeneric"
    BE_NATIONAL_NUMBER = "BENationalNumber"
    BE_NATIONAL_NUMBER_V2 = "BENationalNumberV2"
    BE_VALUE_ADDED_TAX_NUMBER = "BEValueAddedTaxNumber"
    BRCPF_NUMBER = "BRCPFNumber"
    BR_LEGAL_ENTITY_NUMBER = "BRLegalEntityNumber"
    BR_NATIONAL_IDRG = "BRNationalIDRG"
    BG_UNIFORM_CIVIL_NUMBER = "BGUniformCivilNumber"
    CA_BANK_ACCOUNT_NUMBER = "CABankAccountNumber"
    CA_DRIVERS_LICENSE_NUMBER = "CADriversLicenseNumber"
    CA_HEALTH_SERVICE_NUMBER = "CAHealthServiceNumber"
    CA_PASSPORT_NUMBER = "CAPassportNumber"
    CA_PERSONAL_HEALTH_IDENTIFICATION = "CAPersonalHealthIdentification"
    CA_SOCIAL_INSURANCE_NUMBER = "CASocialInsuranceNumber"
    CL_IDENTITY_CARD_NUMBER = "CLIdentityCardNumber"
    CN_RESIDENT_IDENTITY_CARD_NUMBER = "CNResidentIdentityCardNumber"
    CREDIT_CARD_NUMBER = "CreditCardNumber"
    HR_IDENTITY_CARD_NUMBER = "HRIdentityCardNumber"
    HR_NATIONAL_ID_NUMBER = "HRNationalIDNumber"
    HR_PERSONAL_IDENTIFICATION_NUMBER = "HRPersonalIdentificationNumber"
    HR_PERSONAL_IDENTIFICATION_OIB_NUMBER_V2 = "HRPersonalIdentificationOIBNumberV2"
    CY_IDENTITY_CARD = "CYIdentityCard"
    CY_TAX_IDENTIFICATION_NUMBER = "CYTaxIdentificationNumber"
    CZ_PERSONAL_IDENTITY_NUMBER = "CZPersonalIdentityNumber"
    CZ_PERSONAL_IDENTITY_V2 = "CZPersonalIdentityV2"
    DK_PERSONAL_IDENTIFICATION_NUMBER = "DKPersonalIdentificationNumber"
    DK_PERSONAL_IDENTIFICATION_V2 = "DKPersonalIdentificationV2"
    DRUG_ENFORCEMENT_AGENCY_NUMBER = "DrugEnforcementAgencyNumber"
    EE_PERSONAL_IDENTIFICATION_CODE = "EEPersonalIdentificationCode"
    EU_DEBIT_CARD_NUMBER = "EUDebitCardNumber"
    EU_DRIVERS_LICENSE_NUMBER = "EUDriversLicenseNumber"
    EUGPS_COORDINATES = "EUGPSCoordinates"
    EU_NATIONAL_IDENTIFICATION_NUMBER = "EUNationalIdentificationNumber"
    EU_PASSPORT_NUMBER = "EUPassportNumber"
    EU_SOCIAL_SECURITY_NUMBER = "EUSocialSecurityNumber"
    EU_TAX_IDENTIFICATION_NUMBER = "EUTaxIdentificationNumber"
    FI_EUROPEAN_HEALTH_NUMBER = "FIEuropeanHealthNumber"
    FI_NATIONAL_ID = "FINationalID"
    FI_NATIONAL_IDV2 = "FINationalIDV2"
    FI_PASSPORT_NUMBER = "FIPassportNumber"
    FR_DRIVERS_LICENSE_NUMBER = "FRDriversLicenseNumber"
    FR_HEALTH_INSURANCE_NUMBER = "FRHealthInsuranceNumber"
    FR_NATIONAL_ID = "FRNationalID"
    FR_PASSPORT_NUMBER = "FRPassportNumber"
    FR_SOCIAL_SECURITY_NUMBER = "FRSocialSecurityNumber"
    FR_TAX_IDENTIFICATION_NUMBER = "FRTaxIdentificationNumber"
    FR_VALUE_ADDED_TAX_NUMBER = "FRValueAddedTaxNumber"
    DE_DRIVERS_LICENSE_NUMBER = "DEDriversLicenseNumber"
    DE_PASSPORT_NUMBER = "DEPassportNumber"
    DE_IDENTITY_CARD_NUMBER = "DEIdentityCardNumber"
    DE_TAX_IDENTIFICATION_NUMBER = "DETaxIdentificationNumber"
    DE_VALUE_ADDED_NUMBER = "DEValueAddedNumber"
    GR_NATIONAL_ID_CARD = "GRNationalIDCard"
    GR_NATIONAL_IDV2 = "GRNationalIDV2"
    GR_TAX_IDENTIFICATION_NUMBER = "GRTaxIdentificationNumber"
    HK_IDENTITY_CARD_NUMBER = "HKIdentityCardNumber"
    HU_VALUE_ADDED_NUMBER = "HUValueAddedNumber"
    HU_PERSONAL_IDENTIFICATION_NUMBER = "HUPersonalIdentificationNumber"
    HU_TAX_IDENTIFICATION_NUMBER = "HUTaxIdentificationNumber"
    IN_PERMANENT_ACCOUNT = "INPermanentAccount"
    IN_UNIQUE_IDENTIFICATION_NUMBER = "INUniqueIdentificationNumber"
    ID_IDENTITY_CARD_NUMBER = "IDIdentityCardNumber"
    INTERNATIONAL_BANKING_ACCOUNT_NUMBER = "InternationalBankingAccountNumber"
    IE_PERSONAL_PUBLIC_SERVICE_NUMBER = "IEPersonalPublicServiceNumber"
    IE_PERSONAL_PUBLIC_SERVICE_NUMBER_V2 = "IEPersonalPublicServiceNumberV2"
    IL_BANK_ACCOUNT_NUMBER = "ILBankAccountNumber"
    IL_NATIONAL_ID = "ILNationalID"
    IT_DRIVERS_LICENSE_NUMBER = "ITDriversLicenseNumber"
    IT_FISCAL_CODE = "ITFiscalCode"
    IT_VALUE_ADDED_TAX_NUMBER = "ITValueAddedTaxNumber"
    JP_BANK_ACCOUNT_NUMBER = "JPBankAccountNumber"
    JP_DRIVERS_LICENSE_NUMBER = "JPDriversLicenseNumber"
    JP_PASSPORT_NUMBER = "JPPassportNumber"
    JP_RESIDENT_REGISTRATION_NUMBER = "JPResidentRegistrationNumber"
    JP_SOCIAL_INSURANCE_NUMBER = "JPSocialInsuranceNumber"
    JP_MY_NUMBER_CORPORATE = "JPMyNumberCorporate"
    JP_MY_NUMBER_PERSONAL = "JPMyNumberPersonal"
    JP_RESIDENCE_CARD_NUMBER = "JPResidenceCardNumber"
    LV_PERSONAL_CODE = "LVPersonalCode"
    LT_PERSONAL_CODE = "LTPersonalCode"
    LU_NATIONAL_IDENTIFICATION_NUMBER_NATURAL = "LUNationalIdentificationNumberNatural"
    LU_NATIONAL_IDENTIFICATION_NUMBER_NON_NATURAL = "LUNationalIdentificationNumberNonNatural"
    MY_IDENTITY_CARD_NUMBER = "MYIdentityCardNumber"
    MT_IDENTITY_CARD_NUMBER = "MTIdentityCardNumber"
    MT_TAX_ID_NUMBER = "MTTaxIDNumber"
    NL_CITIZENS_SERVICE_NUMBER = "NLCitizensServiceNumber"
    NL_CITIZENS_SERVICE_NUMBER_V2 = "NLCitizensServiceNumberV2"
    NL_TAX_IDENTIFICATION_NUMBER = "NLTaxIdentificationNumber"
    NL_VALUE_ADDED_TAX_NUMBER = "NLValueAddedTaxNumber"
    NZ_BANK_ACCOUNT_NUMBER = "NZBankAccountNumber"
    NZ_DRIVERS_LICENSE_NUMBER = "NZDriversLicenseNumber"
    NZ_INLAND_REVENUE_NUMBER = "NZInlandRevenueNumber"
    NZ_MINISTRY_OF_HEALTH_NUMBER = "NZMinistryOfHealthNumber"
    NZ_SOCIAL_WELFARE_NUMBER = "NZSocialWelfareNumber"
    NO_IDENTITY_NUMBER = "NOIdentityNumber"
    PH_UNIFIED_MULTI_PURPOSE_ID_NUMBER = "PHUnifiedMultiPurposeIDNumber"
    PL_IDENTITY_CARD = "PLIdentityCard"
    PL_NATIONAL_ID = "PLNationalID"
    PL_NATIONAL_IDV2 = "PLNationalIDV2"
    PL_PASSPORT_NUMBER = "PLPassportNumber"
    PL_TAX_IDENTIFICATION_NUMBER = "PLTaxIdentificationNumber"
    PLREGON_NUMBER = "PLREGONNumber"
    PT_CITIZEN_CARD_NUMBER = "PTCitizenCardNumber"
    PT_CITIZEN_CARD_NUMBER_V2 = "PTCitizenCardNumberV2"
    PT_TAX_IDENTIFICATION_NUMBER = "PTTaxIdentificationNumber"
    RO_PERSONAL_NUMERICAL_CODE = "ROPersonalNumericalCode"
    RU_PASSPORT_NUMBER_DOMESTIC = "RUPassportNumberDomestic"
    RU_PASSPORT_NUMBER_INTERNATIONAL = "RUPassportNumberInternational"
    SA_NATIONAL_ID = "SANationalID"
    SG_NATIONAL_REGISTRATION_IDENTITY_CARD_NUMBER = "SGNationalRegistrationIdentityCardNumber"
    SK_PERSONAL_NUMBER = "SKPersonalNumber"
    SI_TAX_IDENTIFICATION_NUMBER = "SITaxIdentificationNumber"
    SI_UNIQUE_MASTER_CITIZEN_NUMBER = "SIUniqueMasterCitizenNumber"
    ZA_IDENTIFICATION_NUMBER = "ZAIdentificationNumber"
    KR_RESIDENT_REGISTRATION_NUMBER = "KRResidentRegistrationNumber"
    ESDNI = "ESDNI"
    ES_SOCIAL_SECURITY_NUMBER = "ESSocialSecurityNumber"
    ES_TAX_IDENTIFICATION_NUMBER = "ESTaxIdentificationNumber"
    SQL_SERVER_CONNECTION_STRING = "SQLServerConnectionString"
    SE_NATIONAL_ID = "SENationalID"
    SE_NATIONAL_IDV2 = "SENationalIDV2"
    SE_PASSPORT_NUMBER = "SEPassportNumber"
    SE_TAX_IDENTIFICATION_NUMBER = "SETaxIdentificationNumber"
    SWIFT_CODE = "SWIFTCode"
    CH_SOCIAL_SECURITY_NUMBER = "CHSocialSecurityNumber"
    TW_NATIONAL_ID = "TWNationalID"
    TW_PASSPORT_NUMBER = "TWPassportNumber"
    TW_RESIDENT_CERTIFICATE = "TWResidentCertificate"
    TH_POPULATION_IDENTIFICATION_CODE = "THPopulationIdentificationCode"
    TR_NATIONAL_IDENTIFICATION_NUMBER = "TRNationalIdentificationNumber"
    UK_DRIVERS_LICENSE_NUMBER = "UKDriversLicenseNumber"
    UK_ELECTORAL_ROLL_NUMBER = "UKElectoralRollNumber"
    UK_NATIONAL_HEALTH_NUMBER = "UKNationalHealthNumber"
    UK_NATIONAL_INSURANCE_NUMBER = "UKNationalInsuranceNumber"
    UK_UNIQUE_TAXPAYER_NUMBER = "UKUniqueTaxpayerNumber"
    USUK_PASSPORT_NUMBER = "USUKPassportNumber"
    US_BANK_ACCOUNT_NUMBER = "USBankAccountNumber"
    US_DRIVERS_LICENSE_NUMBER = "USDriversLicenseNumber"
    US_INDIVIDUAL_TAXPAYER_IDENTIFICATION = "USIndividualTaxpayerIdentification"
    US_SOCIAL_SECURITY_NUMBER = "USSocialSecurityNumber"
    UA_PASSPORT_NUMBER_DOMESTIC = "UAPassportNumberDomestic"
    UA_PASSPORT_NUMBER_INTERNATIONAL = "UAPassportNumberInternational"
    ORGANIZATION = "Organization"
    EMAIL = "Email"
    URL = "URL"
    AGE = "Age"
    PHONE_NUMBER = "PhoneNumber"
    IP_ADDRESS = "IPAddress"
    DATE = "Date"
    PERSON = "Person"
    ADDRESS = "Address"
    ALL = "All"
    DEFAULT = "Default"

class PiiDomain(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The PII domain used for PII Entity Recognition.
    """

    #: Indicates that entities in the Personal Health Information domain should be redacted.
    PHI = "phi"
    #: Indicates that no domain is specified.
    NONE = "none"

class RelationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of relation. Examples include: ``DosageOfMedication`` or 'FrequencyOfMedication', etc.
    """

    ABBREVIATION = "Abbreviation"
    DIRECTION_OF_BODY_STRUCTURE = "DirectionOfBodyStructure"
    DIRECTION_OF_CONDITION = "DirectionOfCondition"
    DIRECTION_OF_EXAMINATION = "DirectionOfExamination"
    DIRECTION_OF_TREATMENT = "DirectionOfTreatment"
    DOSAGE_OF_MEDICATION = "DosageOfMedication"
    FORM_OF_MEDICATION = "FormOfMedication"
    FREQUENCY_OF_MEDICATION = "FrequencyOfMedication"
    FREQUENCY_OF_TREATMENT = "FrequencyOfTreatment"
    QUALIFIER_OF_CONDITION = "QualifierOfCondition"
    RELATION_OF_EXAMINATION = "RelationOfExamination"
    ROUTE_OF_MEDICATION = "RouteOfMedication"
    TIME_OF_CONDITION = "TimeOfCondition"
    TIME_OF_EVENT = "TimeOfEvent"
    TIME_OF_EXAMINATION = "TimeOfExamination"
    TIME_OF_MEDICATION = "TimeOfMedication"
    TIME_OF_TREATMENT = "TimeOfTreatment"
    UNIT_OF_CONDITION = "UnitOfCondition"
    UNIT_OF_EXAMINATION = "UnitOfExamination"
    VALUE_OF_CONDITION = "ValueOfCondition"
    VALUE_OF_EXAMINATION = "ValueOfExamination"

class SentenceSentimentValue(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The predicted Sentiment for the sentence.
    """

    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"

class State(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    NOT_STARTED = "notStarted"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    PARTIALLY_SUCCEEDED = "partiallySucceeded"
    FAILED = "failed"
    CANCELLED = "cancelled"
    CANCELLING = "cancelling"

class StringIndexType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the method used to interpret string offsets.  Defaults to Text Elements (Graphemes)
    according to Unicode v8.0.0. For additional information see
    https://aka.ms/text-analytics-offsets.
    """

    #: Returned offset and length values will correspond to TextElements (Graphemes and Grapheme
    #: clusters) confirming to the Unicode 8.0.0 standard. Use this option if your application is
    #: written in .Net Framework or .Net Core and you will be using StringInfo.
    TEXT_ELEMENTS_V8 = "TextElements_v8"
    #: Returned offset and length values will correspond to Unicode code points. Use this option if
    #: your application is written in a language that support Unicode, for example Python.
    UNICODE_CODE_POINT = "UnicodeCodePoint"
    #: Returned offset and length values will correspond to UTF-16 code units. Use this option if your
    #: application is written in a language that support Unicode, for example Java, JavaScript.
    UTF16_CODE_UNIT = "Utf16CodeUnit"

class TargetRelationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type related to the target.
    """

    ASSESSMENT = "assessment"
    TARGET = "target"

class TokenSentimentValue(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Targeted sentiment in the sentence.
    """

    POSITIVE = "positive"
    MIXED = "mixed"
    NEGATIVE = "negative"

class WarningCodeValue(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Error code.
    """

    LONG_WORDS_IN_DOCUMENT = "LongWordsInDocument"
    DOCUMENT_TRUNCATED = "DocumentTruncated"
