import csv

encode = {}
# encode is a dictionary that has all the encoded labels
# dict{"column name": list of labels}
# corresponding numerical value is its index in the list
dict_path = "VAE_Insight/model/dict.csv"
with open(dict_path, 'r') as csv_file:  
    reader = csv.reader(csv_file)
    for row in reader:
        encode[row[0]] = row[1]

print(encode)


input_cols = ['VAERS_ID', 'AGE_YRS', 'SEX', 'ER_VISIT', 'HOSPITAL',
       'HOSPDAYS', 'DISABLE', 'RECOVD', 'NUMDAYS',  'V_ADMINBY',
       'V_FUNDBY',  'FORM_VERS',  
        'CUR_ILL_num', 'HISTORY_num', 'PRIOR_VAX_num','LAB_num', 'MEDS_num',
         'VAX_TYPE', 'VAX_MANU', 'VAX_DOSE_SERIES',
       'VAX_ROUTE', 'VAX_SITE']
output_cols = ['Injection site swelling', 'Injection site pain', 'Pyrexia', 'Erythema',
       'Pain', 'Pain in extremity', 'Injection site warmth', 'Headache',
       'Rash', 'Peripheral swelling', 'Nausea', 'Dizziness', 'Pruritus',
       'Skin warm', 'Urticaria', 'Chills', 'Fatigue', 'Vomiting', 'Swelling',
       'Injection site pruritus', 'Herpes zoster', 'Myalgia', 'Malaise',
       'Asthenia', 'Others']

def input_to_numeric(input_list): #presume dict input
    input_numeric = []
    for i in range(len(input_list)):
        if input_cols[i+1] in encode.keys():
            input_numeric.append(encode[input_cols[i+1]].index(input_list[i]))
        else:
            input_numeric.append(int(input_list[i]))
    return input_numeric


def output_to_str(output_list): #presume list output
    output_str = []
    for i in range(len(output_list)):
        if output_list[i] == 1:
            output_str.append(output_cols[i])      
    return output_str
        
 





