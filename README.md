# Python Object-Oriented Programming Concepts

This assignment demonstrates key Object-Oriented Programming concepts in Python through a SmartDevice class implementation. Each concept is practically demonstrated in the code and verified through unit tests.

## Core Concepts Explained

### 1. Objects and Classes
**Definition**: Classes are blueprints for creating objects, which are instances of that class. Objects encapsulate data and behavior.

**Implementation in SmartDevice**:
```python
class SmartDevice:
    def __init__(self, device_name, model_number, is_online=False):
        self.device_name = device_name
        self.model_number = model_number
```
Here, `SmartDevice` is the class, and each device created (like thermostat, lamp) is an object of this class. The test case `test_initialization()` verifies proper object creation:
```python
def test_initialization():
    device = SmartDevice("Thermostat", "T-1000")
    assert device.device_name == "Thermostat"  # Testing object attributes
```

### 2. Class Attributes
**Definition**: Attributes shared by all instances of a class. These are defined within the class but outside any method.

**Implementation**:
```python
class SmartDevice:
    device_count = 0     # Class attribute
    device_objects = {}  # Shared across all instances
```
The `device_count` tracks all instances, demonstrated in `test_device_count()`:
```python
def test_device_count():
    _ = SmartDevice("Lamp", "L-2000")
    assert SmartDevice.device_count == 2  # Counts all instances
```

### 3. Callable Class Attributes
**Definition**: Methods or attributes that can be called (executed) from the class or its instances.

**Implementation**:
```python
def update_status(instance_object, attribute, value):
    getattr(SmartDevice, "status")[attribute] = value
```
Tested in `test_update_status()`:
```python
def test_update_status():
    device = SmartDevice("Camera", "C-3000")
    device.update_status("battery", 80)
    assert device.get_status("battery") == 80
```

### 4. Classes are Callable
**Definition**: Classes can be made callable by implementing the `__call__` method, allowing instances to be used like functions.

**Implementation**:
```python
def __call__(self):
    return f"{self.device_name} (Model: {self.model_number})"
```
Verified in `test_callable_class()`:
```python
def test_callable_class():
    device = SmartDevice("Light", "L-6000")
    assert device() == "Light (Model: L-6000)"
```

### 5. Data Attributes
**Definition**: Instance-specific variables that store data unique to each object.

**Implementation**:
```python
def __init__(self, device_name, model_number, is_online=False):
    self.device_name = device_name    # Data attribute
    self.model_number = model_number  # Data attribute
```
Each instance has its own values for these attributes, as shown in `test_multiple_devices()`:
```python
def test_multiple_devices():
    device1 = SmartDevice("Microwave", "M-1100")
    device2 = SmartDevice("Oven", "O-1200")
```

### 6. Function Attributes
**Definition**: Methods that can be dynamically assigned or modified at runtime.

**Implementation**:
```python
def device_info(self):
    return {"state": self.status}
```
The method can be reassigned as shown in `test_device_info()`:
```python
def test_device_info():
    device = SmartDevice("Fan", "F-7000")
    device.device_info = lambda: {"name": device.device_name}
```

### 7. Initializing Class Attributes
**Definition**: Setting up class-level attributes when the class is defined.

**Implementation**:
```python
class SmartDevice:
    device_count = 0
    is_o
'''

<img width="1025" alt="image" src="https://github.com/user-attachments/assets/095a0d80-3e7e-4109-ad7d-be6d76170af8" />


