from user_agents import parse
import enum

class DeviceTypeEnum(str,enum.Enum):
    MOBILE= "Mobile"
    TABLET= "Tablet"
    PC = "PC"
    OTHER = ""
    


def device(user_agent):    
    ua = parse(user_agent)
    if ua.is_mobile:
        device_type = DeviceTypeEnum.MOBILE
    elif ua.is_tablet:
        device_type = DeviceTypeEnum.TABLET
    elif ua.is_pc:
        device_type = DeviceTypeEnum.PC
    else:
        device_type = DeviceTypeEnum.OTHER
    return {"device_type": device_type}