import zeep
from zeep.xsd import ComplexType, AnySimpleType

from app import settings
from app.modules.appointment.models import Appointment


def get_queue_info(code: str) -> list or str:
    wsdl = 'http://r29-rc.zdrav.netrika.ru/queues/MqService.svc?wsdl'
    client = zeep.Client(wsdl=wsdl)

    credentials = {
        'Organization': '0011a94b-8906-42ce-8cdf-da1e2dfd487f',
        'Token': '75f1ab74-7942-41a1-a1d8-b95d53c08216',
    }

    options = {
        'ReferralInfo': {
            'ProfileMedService': {'Code': code, 'System': 'urn:oid:1.2.643.2.69.1.1.1.56', 'Version': '1'}
        },
        'Target': {'Lpu': None},
    }

    soap_result = client.service.GetQueueInfo(credentials, options)
    if soap_result.ActiveProfiles == None:
        return None

    json = zeep.helpers.serialize_object(soap_result, dict)
    orgs_list = []
    data_list = json['ActiveProfiles']['ActiveProfile']
    for orgs in data_list:
        if 'TargetLpu' in orgs:
            orgs_list.append({orgs['Address']: orgs['TargetLpu']['Code']})

    return orgs_list


# print(get_queue_info(str(29)))


def register(data: dict)->dict or None:

    wsdl = 'http://r29-rc.zdrav.netrika.ru/queues/MqService.svc?wsdl'
    client = zeep.Client(wsdl=wsdl)

    credentials = {
        'Organization': '0011a94b-8906-42ce-8cdf-da1e2dfd487f',
        'Token': '75f1ab74-7942-41a1-a1d8-b95d53c08216',
    }

    referral = {
        "EventsInfo": {
            "Source": {
                "ReferralCreateDate": "2023-02-01T00:00:00.000+03:00",
                "ReferralReviewDate": "2023-02-01T00:00:00.000+03:00",
                "ReferralOutDate": "2023-02-01T00:00:00.000+03:00",
                "IsReferralReviewed": "true"
            }
        },
        "Patient": {
            "Person": {
                "BirthDate": str(data['patient']['birthdate']) + "T00:00:00.000+03:00",
                "HumanName": {
                    "FamilyName": str(data['patient']['family']),
                    "GivenName": str(data['patient']['given']),
                    "MiddleName": str(data['patient']['middle']),
                },
                "Sex": {
                    "Code": str(data['patient']['sex']),
                    "System": "urn:oid:1.2.643.5.1.13.2.1.1.156"
                },
            },
            "Documents": {
                "DocumentDto": {
                    "DocN": str(data['patient']['docnum_pfr']),
                    "DocumentType": {
                        "Code": "223",
                        "System": "urn:oid:1.2.643.2.69.1.1.1.59",
                    },
                    "ProviderName": "ПФР"
                },
                "DocumentDto": {
                    "DocN": str(data['patient']['docnum_polis']),
                    "DocumentType": {
                        "Code": "228",
                        "System": "urn:oid:1.2.643.2.69.1.1.1.59",
                    },
                    "ProviderName": "АРХАНГЕЛЬСКИЙ ФИЛИАЛ АО \"СТРАХОВАЯ КОМПАНИЯ \"СОГАЗ-МЕД\""
                }
            }
        },
        "ReferralInfo": {
            "Date": "2023-02-02T08:42:39.524+03:00",
            "ProfileMedService": {
                "Code": str(data['referral']['service']),
                "System": "urn:oid:1.2.643.2.69.1.1.1.56"
            },
            "ReferralType": {
                "Code": str(data['referral']['type']),
                "System": "urn:oid:1.2.643.2.69.1.1.1.55"
            },
        },
        "Source": {
            "Doctors": {
                "Doctor": {
                    "ContactDtos": {
                        "ContactDto": {
                            "ContactType": {
                                "Code": "3",
                                "System": "urn:oid:1.2.643.2.69.1.1.1.27",
                            },
                            "ContactValue": "emile@emile.com",
                        }
                    },
                    "Documents": {
                        "DocumentDto": {
                            "DocN": str(data['doctor']['docnum']),
                            "DocumentType": {
                                "Code": "223",
                                "System": "urn:oid:1.2.643.2.69.1.1.1.59",
                            },
                            "ProviderName": "ПФР"
                        }
                    },
                    "Lpu": {
                        "Code": str(credentials['Organization']),
                        "System": "urn:oid:1.2.643.2.69.1.1.1.64",
                    },
                    "Person": {
                        "HumanName": {
                            "FamilyName": str(data['doctor']['family']),
                            "GivenName": str(data['doctor']['given']),
                            "MiddleName": str(data['doctor']['middle']),
                        },
                        "IdPersonMis": str(data['doctor']['id']),
                        "Sex": {
                            "Code": str(data['doctor']['sex']),
                            "System": "urn:oid:1.2.643.5.1.13.2.1.1.156",
                        },
                    },
                    "Position": {
                        "Code": "33",
                        "System": "urn:oid:1.2.643.5.1.13.13.11.1102",
                    },
                    "Role": {"Code": "1",
                             "System": "urn:oid:1.2.643.2.69.1.1.1.66"},
                    "Speciality": {
                        "Code": "0",
                        "System": "urn:oid:1.2.643.5.1.13.13.11.1066",
                    },
                }
            },
            "IdReferralMis": str(data['referral']['id']),
            "Lpu": {
                "Code": str(credentials['Organization']),
                "System": "urn:oid:1.2.643.2.69.1.1.1.64"
            },
            "MainDiagnosis": {
                "DiagnosisInfo": {
                    "Comment": "12",
                    "DiagnosedDate": "2023-02-01T00:00:00.000+03:00",
                    "DiagnosisType": {
                        "Code": "1",
                        "System": "urn:oid:1.2.643.2.69.1.1.1.26",
                        "Version": "1",
                    },
                    "MkbCode": {
                        "Code": "A18",
                        "System": "urn:oid:1.2.643.5.1.13.13.11.1005",
                    },
                }
            }
        },
        "Target": {
            "Lpu": {
                "Code": str(data['referral']['target']),
                "System": "urn:oid:1.2.643.2.69.1.1.1.64",
            }
        },
    }

    result = {}
    try:
        soap_result = client.service.Register(credentials, referral)
        result['key'] = str(soap_result['IdMq'])
        result['code'] = soap_result['MqReferralStatus']['Code']

    except BaseException:
        return None


    return result


data = {
    'patient': {'birthdate':'2002-08-01',
           'family':'test',
           'given':'test',
           'middle':'test',
           'sex':'2',
           'docnum_pfr':'58495102422',
           'docnum_polis':'2950430013004022'},
    'referral': {'type':'1',
            'service':'10',
            'id':'0',
            'target':'5824ffaf-2daf-48c2-8cda-8f02b9bbb9c7'},
    'doctor': {'family':'test',
          'given':'test',
          'middle':'test',
          'sex':'1',
          'id':'29',
          'docnum': '05513212414'}
}

print(register(data))


def create_appointment(appointment: Appointment):
    ...
    # todo: do smth
    client = zeep.Client(wsdl=settings.wsdl_url)

    Credentials: AnySimpleType = client.get_type('ns2:Credentials')
    Options = client.get_type('ns2:Options')
    ReferralInfo = client.get_type('ns2:ReferralInfo')
    ProfileMedService = client.get_type('ns2:ProfileMedService')
    Target = client.get_type('ns2:ReferralTarget')
    Coding = client.get_type('ns2:Coding')
    Referral = client.get_type('ns2:Referral')

    credentials = Credentials(
        Organization='5824ffaf-2daf-48c2-8cda-8f02b9bbb9c7',
        Token='75f1ab74-7942-41a1-a1d8-b95d53c08216')

    profile_med_service = Coding(Code='60',
                                 System='urn:oid:1.2.643.2.69.1.1.1.56',
                                 Version='1')

    referral_info = ReferralInfo(ProfileMedService=profile_med_service)

    lpu = Coding(Code='351a65d8-a359-4e2a-aeb6-9f8ede2b41d5',
                 System='urn:oid:1.2.643.2.69.1.1.1.64',
                 Version='219')

    target = Target(Lpu=lpu)

    options = Options(ReferralInfo=referral_info,
                      Target=target)

    soap_result = client.service.GetVersion()

    soap_result = client.service.GetQueueInfo(credentials, options)
    ...
