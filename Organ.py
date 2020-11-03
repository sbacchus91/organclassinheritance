
"""
Shane Bacchus
Class: CS 521 - Fall 1
Date:10/17
Homework Problem # 2
Description of Problem (just a 1-2 line summary!):
Organ Class file with Heart and Brain children + Unit Tests
"""
class Organ:
    """Organ class serving as parent to Heart and Brain children"""

    def __init__(self, name='',organ_weight_grams='',vital_organ='',organ_system=''):
        self.name = name
        self.organ_weight_grams = organ_weight_grams
        self.vital_organ = vital_organ
        self.organ_system = organ_system

    def __repr__(self):
        """Returns Organ Attributes as dictionary"""
        return {'name':self.name, 'weight':self.organ_weight_grams, 'vital organ': self.vital_organ, 'organ system': self.organ_system}
        
    
class Heart (Organ):
    """Heart Class"""
    def __init__(self, heart_length_cm='', heart_weight_grams='', heart_thickness_cm='', heart_breadth_cm=''):
        self.name = 'Heart'
        self.vital_organ = True
        self.organ_system = 'Muscular System'
        self.heart_length_cm = heart_length_cm
        self.organ_weight_grams = heart_weight_grams
        self.heart_thickness_cm = heart_thickness_cm
        self.heart_breadth_cm = heart_breadth_cm
        
    
    def __repr__(self):
        """Returns Heart Attributes as dictionary"""
        return {'name':self.name, 'weight':self.organ_weight_grams, 'vital organ': self.vital_organ, 'organ system': self.organ_system, 'heart thickness': self.heart_thickness_cm, 'heart breadth': self.heart_breadth_cm, "heart length": self.heart_length_cm}

    def heart_status(self):
        """Returns status of Heart"""
        return 'pumping blood'

    def heart_weight_oz(self):
        """Returns Heart weight converted from grams to oz"""
        grams_to_oz = self.organ_weight_grams*.035
        return (float(grams_to_oz))

class Brain (Organ):
    """Brain Class"""
    
    def __init__(self, brain_volume='',brain_weight_gram=''):
        self.name = 'Brain'
        self.vital_organ = True
        self.organ_system = 'Nervous System'
        self.brain_volume = brain_volume
        self.organ_weight_grams = brain_weight_gram
    def __repr__(self):
        """Returns Brain Attributes as dictionary"""
        return {'name':self.name, 'weight':self.organ_weight_grams, 'vital organ': self.vital_organ, 'organ system': self.organ_system, 'brain volume': self.brain_volume}
    def brain_status(self):
        """Returns Status of Brain"""
        return 'thinking...'
    def brain_weight_oz(self):
        """Uses Heart Method to convert Brain Weight from grams to oz"""
        return Heart.heart_weight_oz(self) #  Used method from Heart Class
        


if __name__ == "__main__":
    #  Unit Tests
    heart = Heart(12, 280, 6.0, 9.0)
    #  Heart attribute Unit Tests
    heart_dictionary = heart.__repr__()
    assert heart_dictionary['name'] == 'Heart', 'Error, Heart name is not correct'
    assert heart_dictionary['weight'] == 280, 'Error, Heart weight is not correct'
    assert heart_dictionary['vital organ'] == True, 'Error, is heart vital organ is not correct'
    assert heart_dictionary['organ system'] == 'Muscular System', 'Error, Heart Organ System is not correct'
    assert heart_dictionary['heart thickness'] == 6.0, 'Error, heart thickness is not correct'
    assert heart_dictionary['heart breadth'] == 9.0, 'Error, heart breadth is not correct'
    assert heart_dictionary['heart length'] == 12, 'Error, heart length is not correct'

    #  Heart method Unit Tests
    heart_status_unit_test = 'pumping blood'
    heart_weight_oz_unit_test = 280*.035
    assert heart_status_unit_test == heart.heart_status(), "Error, heart status is not correct"
    assert heart_weight_oz_unit_test == heart.heart_weight_oz(), 'Error, heart grams to oz calc is wrong'
    
    brain = Brain(1260, 1370.0)
    #  Brain attribute Unit Tests
    brain_dictionary = brain.__repr__()
    assert brain_dictionary['name'] == 'Brain', 'Error, brain name is not correct'
    assert brain_dictionary['weight'] == 1370.0, 'Error, brain weight is not correct'
    assert brain_dictionary['vital organ'] == True, 'Error, is brain vital organ is not correct'
    assert brain_dictionary['organ system'] == 'Nervous System', 'Error, Brain Organ System is not correct'
    assert brain_dictionary['brain volume'] == 1260, 'Error, Brain Volume is not correct'

    #  Brain method Unit Tests
    brain_status_unit_test = 'thinking...'
    brain_weight_oz_unit_test = 1370*.035
    assert brain_status_unit_test == brain.brain_status(), "Error, brain status is not correct"
    assert brain_weight_oz_unit_test == brain.brain_weight_oz(), 'Error, brain grams to oz calc is wrong'

    

