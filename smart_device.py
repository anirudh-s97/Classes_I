class SmartDevice:
    """Smart Device Class"""
    device_count = 0
    device_name = "smart"
    model_number = "1234"
    is_online = False
    instances = {}
    status = {}

    def __init__(self, device_name, model_number, is_online=False):
        self.device_name = device_name
        self.model_number = model_number
        self.is_online = is_online
        if id(self) not in SmartDevice.instances:
            SmartDevice.device_count += 1
            SmartDevice.instances[id(self)] = 1


    def __call__(self):
        
        return f"{self.device_name} (Model: {self.model_number})"
    
    def update_status(instance_object, attribute, value):
        getattr(SmartDevice, "status")[attribute] = value
    

    def get_status(instance_object, attribute):
        return getattr(SmartDevice, "status",).get(attribute, "Attribute not found")

    def toggle_online(instance_object):
        val = not(getattr(instance_object, "is_online"))
        setattr(instance_object, "is_online", val)


    def reset(*args):
        setattr(SmartDevice, "status", {})  
    
    def device_info(self):
        return {"state": self.status}