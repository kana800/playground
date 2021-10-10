import sys
from datetime import datetime


class Person:
    def __init__(self,f_name,l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = f_name + l_name
        self.calendar = Calendar()

    def is_available(self,slot):
        return self.calendar.is_available(slot)

    def make_appointment(self,slot,record):
        return self.calendar.add_entry(slot,record)

class Patient(Person):

    def __init__(self,f_name,l_name):
        super().__init__(f_name,l_name)
        self.app_id = self.f_name[0]+self.l_name  #appointment id

class Doctor(Person):

    def __init__(self,f_name,l_name,speciality):
        super().__init__(f_name,l_name)
        self.speciality = speciality

class Calendar(object):

    def __init__(self):
        self.entries = {}

    def is_available(self,slot):
        return slot not in self.entries

    def add_entry(self,slot,record):
        self.entries[slot] = record

def schedule(doctor,patient,slot):

    if doctor.is_available(slot) == False:
        return f"Doctor {doctor.full_name} not available at {slot}"

    doctor.make_appointment(slot,patient.app_id)
    patient.make_appointment(slot,doctor.full_name)
