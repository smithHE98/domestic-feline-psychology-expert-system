from pyknow import *

disorders_list = []
disorders_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
        global disorders_list,disorders_symptoms,symptom_map,d_desc_map,d_treatment_map
        disorders = open("disorders.txt")
        disorders_t = disorders.read()
        disorders_list = disorders_t.split("\n")
        disorders.close()
        for disorder in disorders_list:
                disorder_s_file = open("disorder symptoms/" + disorder + ".txt")
                disorder_s_data = disorder_s_file.read()
                s_list = disorder_s_data.split("\n")
                disorders_symptoms.append(s_list)
                symptom_map[str(s_list)] = disorder
                disorder_s_file.close()
                disorder_s_file = open("disorder descriptions/" + disorder + ".txt")
                disorder_s_data = disorder_s_file.read()
                d_desc_map[disorder] = disorder_s_data
                disorder_s_file.close()
                disorder_s_file = open("disorder treatments/" + disorder + ".txt")
                disorder_s_data = disorder_s_file.read()
                d_treatment_map[disorder] = disorder_s_data
                disorder_s_file.close()
        

def identify_disorder(*arguments):
        symptom_list = []
        for symptom in arguments:
                symptom_list.append(symptom)
        # Handle key error
        return symptom_map[str(symptom_list)]

def get_details(disorder):
        return d_desc_map[disorder]

def get_treatments(disorder):
        return d_treatment_map[disorder]

def if_not_matched(disorder):
                print("")
                id_disorder = disorder
                disorder_details = get_details(id_disorder)
                treatments = get_treatments(id_disorder)
                print("")
                print("The most probable disorder that the cat has is %s\n" %(id_disorder))
                print("A short description of the disorder is given below: \n")
                print(disorder_details+"\n")
                print("The common medications and procedures to treat the disorder include: \n")
                print(treatments+"\n")

class Greetings(KnowledgeEngine):
        @DefFacts()
        def _initial_action(self):
                print("")
                print("Hello! This is an expert system used to diagnose mental disorders in cats.")
                print("Please input 'yes' or 'no' in order to help pinpoint issues.")
                print("Do you see any of the following symptoms in the cat?")
                print("")
                yield Fact(action="find_disorder")

        @Rule(Fact(action='find_disorder'), NOT(Fact(restlessness=W())),salience = 1)
        def symptom_0(self):
                self.declare(Fact(restlessness=input("Restlessness: ")))

        @Rule(Fact(action='find_disorder'), NOT(Fact(frustration=W())),salience = 1)
        def symptom_1(self):
                self.declare(Fact(frustration=input("Frustration: ")))

        @Rule(Fact(action='find_disorder'), NOT(Fact(biting=W())),salience = 1)
        def symptom_2(self):
                self.declare(Fact(biting=input("Biting: ")))

        @Rule(Fact(action='find_disorder'), NOT(Fact(aimless_wandering=W())),salience = 1)
        def symptom_3(self):
                self.declare(Fact(aimless_wandering=input("Aimless wandering: ")))

        @Rule(Fact(action='find_disorder'), NOT(Fact(hissing=W())),salience = 1)
        def symptom_4(self):
                self.declare(Fact(hissing=input("Hissing: ")))

        @Rule(Fact(action='find_disorder'), NOT(Fact(tremors=W())),salience = 1)
        def symptom_5(self):
                self.declare(Fact(tremors=input("Tremors: ")))

        @Rule(Fact(action='find_disorder'), NOT(Fact(fear=W())),salience = 1)
        def symptom_6(self):
                self.declare(Fact(fear=input("Fear: ")))

        @Rule(Fact(action='find_disorder'), NOT(Fact(confusion=W())),salience = 1)
        def symptom_7(self):
                self.declare(Fact(confusion=input("Confusion: ")))

        @Rule(Fact(action='find_disorder'), NOT(Fact(salivation=W())),salience = 1)
        def symptom_8(self):
                self.declare(Fact(salivation=input("Salivation: ")))

        @Rule(Fact(action='find_disorder'), NOT(Fact(vocalization=W())),salience = 1)
        def symptom_9(self):
                self.declare(Fact(vocalization=input("Wild vocalization: ")))

        @Rule(Fact(action='find_disorder'), NOT(Fact(over_grooming=W())),salience = 1)
        def symptom_10(self):
                self.declare(Fact(over_grooming=input("Over-grooming: ")))

        @Rule(Fact(action='find_disorder'), NOT(Fact(pacing=W())),salience = 1)
        def symptom_11(self):
                self.declare(Fact(pacing=input("Pacing: ")))

        @Rule(Fact(action='find_disorder'), NOT(Fact(startle_easily=W())),salience = 1)
        def symptom_12(self):
                self.declare(Fact(startle_easily=input("Startle easily: ")))

        @Rule(Fact(action='find_disorder'), NOT(Fact(repetitious_behavior=W())),salience = 1)
        def symptom_13(self):
                self.declare(Fact(repetitious_behavior=input("Repetitious behavior: ")))

        @Rule(Fact(action='find_disorder'),Fact(restlessness="no"),Fact(frustration="yes"),Fact(biting="yes"),Fact(aimless_wandering="no"),Fact(hissing="yes"),Fact(tremors="no"),Fact(fear="yes"),Fact(confusion="no"),Fact(salivation="no"),Fact(vocalizations="no"),Fact(over_grooming="no"),Fact(pacing="no"),Fact(startle_easily="no"),Fact(repetitious_behavior="no"))
        def disorder_0(self):
                self.declare(Fact(disorder="Aggression"))

        @Rule(Fact(action='find_disorder'),Fact(restlessness="yes"),Fact(frustration="no"),Fact(biting="no"),Fact(aimless_wandering="no"),Fact(hissing="no"),Fact(tremors="no"),Fact(fear="yes"),Fact(confusion="no"),Fact(salivation="no"),Fact(vocalizations="no"),Fact(over_grooming="no"),Fact(pacing="yes"),Fact(startle_easily="yes"),Fact(repetitious_behavior="no"))
        def disorder_1(self):
                self.declare(Fact(disorder="Anxiety"))

        @Rule(Fact(action='find_disorder'),Fact(restlessness="no"),Fact(frustration="yes"),Fact(biting="no"),Fact(aimless_wandering="no"),Fact(hissing="no"),Fact(tremors="no"),Fact(fear="yes"),Fact(confusion="no"),Fact(salivation="no"),Fact(vocalizations="no"),Fact(over_grooming="yes"),Fact(pacing="no"),Fact(startle_easily="no"),Fact(repetitious_behavior="no"))
        def disorder_2(self):
                self.declare(Fact(disorder="Displacement Activity"))

        @Rule(Fact(action='find_disorder'),Fact(restlessness="no"),Fact(frustration="no"),Fact(biting="yes"),Fact(aimless_wandering="no"),Fact(hissing="yes"),Fact(tremors="no"),Fact(fear="yes"),Fact(confusion="no"),Fact(salivation="no"),Fact(vocalizations="no"),Fact(over_grooming="no"),Fact(pacing="no"),Fact(startle_easily="yes"),Fact(repetitious_behavior="no"))
        def disorder_3(self):
                self.declare(Fact(disorder="Fear"))

        @Rule(Fact(action='find_disorder'),Fact(restlessness="no"),Fact(frustration="yes"),Fact(biting="no"),Fact(aimless_wandering="no"),Fact(hissing="no"),Fact(tremors="yes"),Fact(fear="no"),Fact(confusion="no"),Fact(salivation="yes"),Fact(vocalizations="yes"),Fact(over_grooming="yes"),Fact(pacing="no"),Fact(startle_easily="no"),Fact(repetitious_behavior="no"))
        def disorder_4(self):
                self.declare(Fact(disorder="Feline Hyperesthesia Syndrome"))

        @Rule(Fact(action='find_disorder'),Fact(restlessness="yes"),Fact(frustration="yes"),Fact(biting="yes"),Fact(aimless_wandering="no"),Fact(hissing="yes"),Fact(tremors="no"),Fact(fear="no"),Fact(confusion="no"),Fact(salivation="no"),Fact(vocalizations="no"),Fact(over_grooming="no"),Fact(pacing="no"),Fact(startle_easily="no"),Fact(repetitious_behavior="no"))
        def disorder_5(self):
                self.declare(Fact(disorder="Frustration"))

        @Rule(Fact(action='find_disorder'),Fact(restlessness="yes"),Fact(frustration="yes"),Fact(biting="no"),Fact(aimless_wandering="no"),Fact(hissing="no"),Fact(tremors="no"),Fact(fear="no"),Fact(confusion="no"),Fact(salivation="no"),Fact(vocalizations="yes"),Fact(over_grooming="no"),Fact(pacing="yes"),Fact(startle_easily="no"),Fact(repetitious_behavior="no"))
        def disorder_6(self):
                self.declare(Fact(disorder="Insomnia"))

        @Rule(Fact(action='find_disorder'),Fact(restlessness="no"),Fact(frustration="no"),Fact(biting="yes"),Fact(aimless_wandering="no"),Fact(hissing="yes"),Fact(tremors="no"),Fact(fear="yes"),Fact(confusion="no"),Fact(salivation="no"),Fact(vocalizations="no"),Fact(over_grooming="no"),Fact(pacing="no"),Fact(startle_easily="yes"),Fact(repetitious_behavior="no"))
        def disorder_7(self):
                self.declare(Fact(disorder="PTSD"))

        @Rule(Fact(action='find_disorder'),Fact(restlessness="yes"),Fact(frustration="yes"),Fact(biting="yes"),Fact(aimless_wandering="no"),Fact(hissing="yes"),Fact(tremors="no"),Fact(fear="yes"),Fact(confusion="no"),Fact(salivation="no"),Fact(vocalizations="yes"),Fact(over_grooming="no"),Fact(pacing="no"),Fact(startle_easily="no"),Fact(repetitious_behavior="no"))
        def disorder_8(self):
                self.declare(Fact(disorder="Redirected Behaviors"))

        @Rule(Fact(action='find_disorder'),Fact(restlessness="no"),Fact(frustration="no"),Fact(biting="no"),Fact(aimless_wandering="yes"),Fact(hissing="no"),Fact(tremors="yes"),Fact(fear="no"),Fact(confusion="yes"),Fact(salivation="no"),Fact(vocalizations="no"),Fact(over_grooming="no"),Fact(pacing="no"),Fact(startle_easily="no"),Fact(repetitious_behavior="no"))
        def disorder_9(self):
                self.declare(Fact(disorder="Senility"))

        @Rule(Fact(action='find_disorder'),Fact(restlessness="yes"),Fact(frustration="yes"),Fact(biting="no"),Fact(aimless_wandering="no"),Fact(hissing="no"),Fact(tremors="no"),Fact(fear="no"),Fact(confusion="no"),Fact(salivation="no"),Fact(vocalizations="no"),Fact(over_grooming="yes"),Fact(pacing="yes"),Fact(startle_easily="no"),Fact(repetitious_behavior="yes"))
        def disorder_10(self):
                self.declare(Fact(disorder="Stereotypic Behaviors"))

        @Rule(Fact(action='find_disorder'),Fact(restlessness="no"),Fact(frustration="yes"),Fact(biting="no"),Fact(aimless_wandering="no"),Fact(hissing="no"),Fact(tremors="no"),Fact(fear="no"),Fact(confusion="no"),Fact(salivation="no"),Fact(vocalizations="no"),Fact(over_grooming="yes"),Fact(pacing="no"),Fact(startle_easily="no"),Fact(repetitious_behavior="yes"))
        def disorder_11(self):
                self.declare(Fact(disorder="Vacuum Activity"))
                
        @Rule(Fact(action='find_disorder'),Fact(disorder=MATCH.disorder),salience = -998)
        def disorder(self, disorder):
                print("")
                id_disorder = disorder
                disorder_details = get_details(id_disorder)
                treatments = get_treatments(id_disorder)
                print("")
                print("The most probable disorder that the cat has is %s\n" %(id_disorder))
                print("A short description of the disorder is given below: \n")
                print(disorder_details+"\n")
                print("The common methods used to treat the disorder include: \n")
                print(treatments+"\n")

        @Rule(Fact(action='find_disorder'),
                  Fact(restlessness=MATCH.restlessness),
                  Fact(frustration=MATCH.frustration),
                  Fact(biting=MATCH.biting),
                  Fact(aimless_wandering=MATCH.aimless_wandering),
                  Fact(hissing=MATCH.hissing),
                  Fact(tremors=MATCH.tremors),
                  Fact(fear=MATCH.fear),
                  Fact(confusion=MATCH.confusion),
                  Fact(salivation=MATCH.salivation),
                  Fact(vocalization=MATCH.vocalization),
                  Fact(over_grooming=MATCH.over_grooming),
                  Fact(pacing=MATCH.pacing),
                  Fact(startle_easily=MATCH.startle_easily),
                  Fact(repetitious_behavior=MATCH.repetitious_behavior),
              NOT(Fact(disorder=MATCH.disorder)),salience = -999)

        def not_matched(self, restlessness, frustration, biting, aimless_wandering, hissing, tremors, fear, confusion, salivation, vocalization, over_grooming, pacing, startle_easily, repetitious_behavior):
                lis = [restlessness, frustration, biting, aimless_wandering, hissing, tremors, fear, confusion, salivation, vocalization, over_grooming, pacing, startle_easily, repetitious_behavior]
                max_count = 0
                max_disorder = ""
                for key,val in symptom_map.items():
                        count = 0
                        temp_list = eval(key)
                        for j in range(0,len(lis)):
                                if(temp_list[j] == lis[j] and lis[j] == "yes"):
                                        count = count + 1
                        if count > max_count:
                                max_count = count
                                max_disorder = val
                if_not_matched(max_disorder)


if __name__ == "__main__":
        preprocess()
        engine = Greetings()
        while(1):
                engine.reset()  # Prepare the engine for the execution
                engine.run()  # Run engine
                print("Would you like to diagnose any other symptoms?")
                if input() == "no":
                        exit()
                #print(engine.facts)
