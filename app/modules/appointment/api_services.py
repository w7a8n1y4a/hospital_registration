import zeep
from zeep.xsd import ComplexType, AnySimpleType

from app import settings
from app.modules.appointment.models import Appointment


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
