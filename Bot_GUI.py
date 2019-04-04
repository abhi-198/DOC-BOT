# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:06:50 2019

@author: Abhishek
"""
import pickle
import tkinter as tk
from tkinter import Scrollbar
from tkinter import messagebox

Symtoms = ['abdomen acute', 'abdominal bloating', 'abdominal tenderness', 'abnormal sensation', 'abnormally hard consistency', 'abortion', 'abscess bacterial', 'absences finding', 'achalasia', 'ache', 'adverse reaction adverse effect', 'agitation', 'air fluid level', 'alcohol binge episode', 'alcoholic withdrawal symptoms', 'ambidexterity', 'angina pectoris', 'anorexia', 'anosmia', 'aphagia', 'apyrexial', 'arthralgia', 'ascites', 'asterixis', 'asthenia', 'asymptomatic', 'ataxia', 'atypia', 'aura', 'awakening early', 'barking cough', 'bedridden bedridden', 'behavior hyperactive', 'behavior showing increased motor activity', 'blackout', 'blanch', 'bleeding of vagina', 'bowel sounds decreased', 'bradycardia', 'bradykinesia', 'breakthrough pain', 'breath sounds decreased', 'breath-holding spell', 'breech presentation', 'bruit', 'burning sensation', 'cachexia', 'cardiomegaly', 'cardiovascular finding cardiovascular event', 'catatonia', 'catching breath', 'charleyhorse', 'chest discomfort', 'chest tightness', 'chill', 'choke', 'cicatrisation', 'cicatrisation scar tissue', 'clammy skin', 'clonus', 'clumsiness', 'colic abdominal', 'consciousness clear', 'constipation', 'coordination abnormal', 'cough', 'cushingoid facies cushingoid \xa0habitus', 'cyanosis', 'cystic lesion', 'debilitation', 'decompensation', 'decreased body weight', 'decreased stool caliber', 'decreased translucency', 'diarrhea', 'difficulty', 'difficulty passing urine', 'disequilibrium', 'distended abdomen', 'distress respiratory', 'disturbed family', 'dizziness', 'dizzy spells', 'drool', 'drowsiness', 'drowsiness sleepy', 'dullness', 'dysarthria', 'dysdiadochokinesia', 'dysesthesia', 'dyspareunia', 'dyspnea', 'dyspnea on exertion', 'dysuria', 'ecchymosis', 'egophony', 'elation', 'emphysematous change', 'energy increased', 'enuresis', 'erythema', 'estrogen use', 'excruciating pain', 'exhaustion', 'extrapyramidal sign', 'extreme exhaustion', 'facial paresis', 'fall', 'fatigability', 'fatigue', 'fatigue tired', 'fear of falling', 'fecaluria', 'feces in rectum', 'feeling hopeless', 'feeling strange', 'feeling suicidal', 'feels hot/feverish', 'fever', 'flare', 'flatulence', 'floppy', 'flushing', 'focal seizures', 'food intolerance', 'formication', 'frail', 'fremitus', 'frothy sputum', 'gag', 'gasping for breath', 'general discomfort', 'general unsteadiness', 'giddy mood', 'gravida ', 'green sputum', 'groggy', 'guaiac positive', 'gurgle', 'hacking cough', 'haemoptysis', 'haemorrhage', 'hallucinations auditory', 'hallucinations visual', 'has religious belief', 'headache', 'heartburn', 'heavy feeling', 'heavy legs', "heberden's node", 'hematochezia', 'hematocrit decreased', 'hematuria', 'heme positive', 'hemianopsia homonymous', 'hemiplegia', 'hemodynamically stable', 'hepatomegaly', 'hepatosplenomegaly', 'hirsutism', 'hoard', 'hoarseness', 'homelessness', 'homicidal thoughts', 'hot flush', 'hunger', 'hydropneumothorax', 'hyperacusis', 'hypercapnia', 'hyperemesis', 'hyperhidrosis disorder', 'hyperkalemia', 'hypersomnia', 'hypersomnolence', 'hypertonicity', 'hyperventilation', 'hypesthesia', 'hypoalbuminemia', 'hypocalcemia result', 'hypokalemia', 'hypokinesia', 'hypometabolism', 'hyponatremia', 'hypoproteinemia', 'hypotension', 'hypothermia, natural', 'hypoxemia', 'immobile', 'impaired cognition', 'inappropriate affect', 'incoherent', 'indifferent mood', 'intermenstrual heavy bleeding', 'intoxication', 'irritable mood', 'jugular venous distention', 'labored breathing', 'lameness claudication', 'large-for-dates fetus', 'left \xa0atrial \xa0hypertrophy', 'lesion', 'lethargy', 'lightheadedness', 'lip smacking', 'loose associations', 'low back pain', 'lung nodule', 'macerated skin', 'macule', 'malaise', 'mass in breast', 'mass of body structure', 'mediastinal shift', 'mental status changes', 'metastatic lesion', 'milky', 'moan', 'monoclonal', 'monocytosis', 'mood depressed', 'moody', 'motor retardation', "murphy's sign", 'muscle hypotonia hypotonic', 'muscle twitch', 'myalgia', 'mydriasis', 'myoclonus', 'nasal discharge present', 'nasal flaring', 'nausea', 'nausea and vomiting', 'neck stiffness', 'neologism', 'nervousness', 'night sweat', 'nightmare', 'no known drug allergies', 'no status change', 'noisy respiration', 'non-productive cough', 'nonsmoker', 'numbness', 'numbness of hand', 'oliguria', 'orthopnea', 'orthostasis', 'out of breath', 'overweight', 'pain', 'pain abdominal', 'pain back', 'pain chest', 'pain foot', 'pain in lower limb', 'pain neck', 'painful swallowing', 'pallor', 'palpitation', 'panic', 'pansystolic murmur', 'para ', 'paralyse', 'paraparesis', 'paresis', 'paresthesia', 'passed stones', 'patient non compliance', 'pericardial friction rub', 'phonophobia', 'photophobia', 'photopsia', 'pin-point pupils', 'pleuritic pain', 'pneumatouria', 'polydypsia', 'polymyalgia', 'polyuria', 'poor dentition', 'poor feeding', 'posterior \xa0rhinorrhea', 'posturing', 'presence of q wave', 'pressure chest', 'previous pregnancies ', 'primigravida', 'prodrome', 'productive cough', 'projectile vomiting', 'prostate tender', 'prostatism', 'proteinemia', 'pruritus', 'pulse absent', 'pulsus \xa0paradoxus', 'pustule', 'qt interval prolonged', 'r wave feature', 'rale', 'rambling speech', 'rapid shallow breathing', 'red blotches', 'redness', 'regurgitates after swallowing', 'renal angle tenderness', 'rest pain', 'retch', 'retropulsion', 'rhd positive', 'rhonchus', 'rigor - temperature-associated observation', 'rolling of eyes', 'room spinning', 'satiety early', 'scar tissue', 'sciatica', 'scleral \xa0icterus', 'scratch marks', 'sedentary', 'seizure', 'sensory discomfort', 'shooting pain', 'shortness of breath', 'side pain', 'sinus rhythm', 'sleeplessness', 'sleepy', 'slowing of urinary stream', 'sneeze', 'sniffle', 'snore', 'snuffle', 'soft tissue swelling', 'sore to touch', 'spasm', 'speech slurred', 'splenomegaly', 'spontaneous rupture of membranes', 'sputum purulent', 'st segment depression', 'st segment elevation', "stahli's line", 'stiffness', 'stinging sensation', 'stool color yellow', 'stridor', 'stuffy nose', 'stupor', 'suicidal', 'superimposition', 'sweat sweating increased', 'swelling', 'symptom aggravating factors', 'syncope', 'syncope blackout history of - blackout', 'systolic ejection murmur', 'systolic murmur', 't wave inverted', 'tachypnea', 'tenesmus', 'terrify', 'thicken', 'throat sore', 'throbbing sensation quality', 'tinnitus', 'titubation', 'todd paralysis', 'tonic seizures', 'transaminitis', 'transsexual', 'tremor', 'tremor resting', 'tumor cell invasion', 'unable to concentrate', 'unconscious state', 'uncoordination', 'underweight underweight', 'unhappy', 'unresponsiveness', 'unsteady gait', 'unwell', 'urge incontinence', 'urgency of \xa0micturition', 'urinary hesitation', 'urinoma', 'verbal auditory hallucinations', 'verbally abusive behavior', 'vertigo', 'vision blurred', 'vomiting', 'weepiness', 'weight gain', 'welt', 'wheelchair bound', 'wheezing', 'withdraw', 'worry', 'yellow sputum']
Disease = ['hypertensive disease', 'diabetes', 'depression mental , depressive disorder', 'coronary arteriosclerosis ,coronary heart disease', 'pneumonia', 'failure heart congestive', 'accident \xa0cerebrovascular', 'asthma', 'myocardial infarction', 'hypercholesterolemia', 'infection', 'infection urinary tract', 'anemia', 'chronic obstructive airway disease', 'dementia', 'insufficiency renal', 'confusion', 'degenerative \xa0polyarthritis', 'hypothyroidism', 'anxiety state', 'malignant neoplasms primary malignant neoplasm', 'acquired \xa0immuno-deficiency syndrome HIV hiv infections', 'cellulitis', 'gastroesophageal reflux disease', 'septicemia systemic infection sepsis (invertebrate)', 'deep vein thrombosis', 'dehydration', 'neoplasm', 'embolism pulmonary', 'epilepsy', 'cardiomyopathy', 'chronic kidney failure', 'carcinoma', 'hepatitis C', 'peripheral vascular disease', 'psychotic disorder', 'hyperlipidemia', 'bipolar disorder', 'obesity', 'ischemia', 'cirrhosis', 'exanthema', 'benign prostatic hypertrophy', 'kidney failure acute', 'mitral valve insufficiency', 'arthritis', 'bronchitis', 'hemiparesis', 'osteoporosis', 'transient ischemic attack', 'adenocarcinoma', 'paranoia', 'pancreatitis', 'incontinence', 'paroxysmal \xa0dyspnea', 'hernia', 'malignant neoplasm of prostate carcinoma prostate', 'edema pulmonary', 'lymphatic diseases', 'stenosis aortic valve', 'malignant neoplasm of breast carcinoma breast', 'schizophrenia', 'diverticulitis', 'overload fluid', 'ulcer peptic', 'osteomyelitis', 'gastritis', 'bacteremia', 'failure kidney', 'sickle cell anemia', 'failure heart', 'upper respiratory infection', 'hepatitis', 'hypertension pulmonary', 'deglutition disorder', 'gout', 'thrombocytopaenia', 'hypoglycemia', 'pneumonia aspiration', 'colitis', 'diverticulosis', 'suicide attempt', 'Pneumocystis \xa0carinii \xa0pneumonia', 'hepatitis B', 'parkinson disease', 'lymphoma', 'hyperglycemia', 'encephalopathy', 'tricuspid valve insufficiency', "Alzheimer's disease", 'candidiasis oralcandidiasis', 'neuropathy', 'kidney disease', 'fibroid tumor', 'glaucoma', 'neoplasm metastasis', 'malignant tumor of colon carcinoma colon', 'ketoacidosis diabetic', 'tonic-clonic epilepsy tonic-clonic seizures', 'malignant \xa0neoplasms', 'respiratory failure', 'melanoma', 'gastroenteritis', 'malignant neoplasm of lung carcinoma of lung', 'manic disorder', 'personality disorder', 'primary carcinoma of the liver cells', 'emphysema pulmonary', 'hemorrhoids', 'spasm bronchial', 'obesity morbid', 'pyelonephritis', 'endocarditis', 'effusion pericardial pericardial effusion body substance', 'chronic alcoholic intoxication', 'pneumothorax', 'delirium', 'neutropenia', 'hyperbilirubinemia', 'influenza', 'dependence', 'thrombus', 'cholecystitis', 'hernia \xa0hiatal', 'migraine disorders', 'pancytopenia', 'cholelithiasis biliary calculus', 'tachycardia sinus', 'ileus', 'adhesion', 'delusion', 'affect labile', 'decubitus ulcer']

def add(event):
    sym = Entry1.get()
    if(len(sym)!=0):
        if sym in Symtoms:
            if sym not in Listbox1.get(0,'end'): 
                Listbox1.insert(tk.END, sym)
        else:
            messagebox.showerror("DOC-BOT Error","Please Select Symtoms from given List")
        Entry1.delete(0,'end')
    else:
        messagebox.showerror("DOC-BOT Error","Please Enter Symtoms")

def clear():
    Listbox1.delete(0,'end')

def predict():
    patient_sym = Listbox1.get(0,'end')
    if(len(patient_sym) != 0):
        sym_vect = [0]*398
        for sym in patient_sym:
            if sym in Symtoms:
                sym_vect[Symtoms.index(sym)]=1
    
        sym_vect = [sym_vect]
        index = int(DOC_model.predict(sym_vect))
        messagebox.showinfo("Disease Prediction",Disease[index]+"\nDoctor name - Room No.")
    else:
       messagebox.showerror("DOC-BOT Error","Please Enter Symtoms for Disease prediction")

def mainPanel():
    global top
    top = tk.Tk()
    top.geometry("812x620+151+41")
    top.title("DOC-BOT")
    top.configure(background = 'floral white')

    Frame1 = tk.Frame(top)
    Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(background="#c5ccd8")
                     
    Label1 = tk.Label(Frame1)
    Label1.place(relx=0.209, rely=0.032, height=51, width=194)
    Label1.configure(font="-family {Microsoft Tai Le} -size 18 -weight bold -underline 1")
    Label1.configure(background="#b3d8cf")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(foreground="#000000")
    Label1.configure(text='''DOC-BOT''')
    Label1.configure(width=194)
    
    Labelframe1 = tk.LabelFrame(Frame1)
    Labelframe1.place(relx=0.677, rely=0.016, relheight=0.976, relwidth=0.308)
    Labelframe1.configure(font="-family {Microsoft Tai Le} -size 10 -weight bold")
    Labelframe1.configure(relief='groove')
    Labelframe1.configure(foreground="black")
    Labelframe1.configure(text='''All Symtoms''')
    Labelframe1.configure(background="#d9d9d9")
    Labelframe1.configure(width=250)

    Listbox2 = tk.Listbox(Labelframe1)
    Listbox2.place(relx=0.02, rely=0.033, relheight=0.945, relwidth=0.936, bordermode='ignore')
    Listbox2.configure(background="white")
    Listbox2.configure(disabledforeground="#a3a3a3")
    Listbox2.configure(font="TkFixedFont")
    Listbox2.configure(foreground="#000000")
    Listbox2.configure(width=234)
    
    scrollbar = Scrollbar(Labelframe1, orient="vertical")
    scrollbar.config(command=Listbox2.yview)
    scrollbar.pack(side="right", fill="y")

    Listbox2.config(yscrollcommand=scrollbar.set)
 
    for sym in Symtoms:
        Listbox2.insert(tk.END, sym)
 
    Label2 = tk.Label(Frame1)
    Label2.place(relx=0.062, rely=0.161, height=21, width=94)
    Label2.configure(font="-family {Microsoft Tai Le} -size 10 -weight bold")
    Label2.configure(background="#d9d9d9")
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(foreground="#000000")
    Label2.configure(text='''Enter Symtoms''')
    Label2.configure(width=94)

    entry_var = tk.StringVar()
    
    global Entry1
    Entry1 = tk.Entry(Frame1)
    Entry1.place(relx=0.222, rely=0.161,height=20, relwidth=0.202)
    Entry1.configure(background="white",textvariable = entry_var)
    Entry1.configure(disabledforeground="#a3a3a3")
    Entry1.configure(foreground="#000000")
    Entry1.configure(insertbackground="black")

    global Listbox1
    Listbox1 = tk.Listbox(Frame1)
    Listbox1.place(relx=0.222, rely=0.274, relheight=0.277, relwidth=0.202)
    Listbox1.configure(background="white")
    Listbox1.configure(disabledforeground="#a3a3a3")
    Listbox1.configure(font="TkFixedFont")
    Listbox1.configure(foreground="#000000")
    Listbox1.configure(width=164)

    Entry1.bind("<Return>", add)

    Button2 = tk.Button(Frame1)
    Button2.place(relx=0.222, rely=0.629, height=24, width=97)
    Button2.configure(font="-family {Microsoft Tai Le} -size 10 -weight bold")
    Button2.configure(activebackground="#ececec" , command = predict)
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#d9d9d9")
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(text='''Predict Disease''')
    Button2.configure(width=97)
 
    Button3 = tk.Button(Frame1)
    Button3.place(relx=0.53, rely=0.629, height=24, width=69)
    Button3.configure(font="-family {Microsoft Tai Le} -size 10 -weight bold")
    Button3.configure(activebackground="#ececec", command = clear)
    Button3.configure(activeforeground="#000000")
    Button3.configure(background="#d9d9d9")
    Button3.configure(disabledforeground="#a3a3a3")
    Button3.configure(foreground="#000000")
    Button3.configure(highlightbackground="#d9d9d9")
    Button3.configure(highlightcolor="black")
    Button3.configure(pady="0")
    Button3.configure(text='''Clear List''')
    Button3.configure(width=69)
    
    top.mainloop()


if __name__ == "__main__":
    filename = 'DOC-BOT_model.sav'
    
    global DOC_model
    DOC_model = pickle.load(open(filename, 'rb'))
 
    mainPanel()