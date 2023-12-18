#Demo Datasets
import numpy as np

demo_name_mapping = {
    'SEQN': 'SEQN',
    'RIAGENDR': 'Gender',
    'RIDSTATR': 'Interview_Status',
    'RIDAGEYR': 'Age_Years',
    'RIDRETH3': 'Race',
    'DMDBORN4': 'Birth_Country',
    'DMDYRUSZ': 'LengthStay_US',
    'DMDEDUC2': 'Education_20+',
    'DMDMARTZ': 'Marital_Status',
    'INDFMPIR': 'RatioIncome_Poverty'
}

diabetes_name_mapping = {
    'SEQN': 'SEQN',
    'DIQ010': 'diabetes',
    'DID040': 'diabetes_age',
    'DIQ160': 'pre-diabetes',
    'DIQ050': 'insulin',
    'DID060': 'insulin_Duration',
    'DIQ060U': 'insulin_unit_month',
    'DIQ070': 'medication',
    'DIQ230': 'diabetes_specialist_year',
    'DIQ240': 'seeing_specialist',
    'DIQ080': 'retinopathy',
    'DIQ280': 'last_A1c',
    'LBXGH' : 'lab_A1c',
    'LBDGLUSI': 'fasting_glucose'
    
}

htn_name_mapping= {
    'SEQN': 'SEQN',
    'BPQ020': 'hypertension',
    'BPD035': 'hypertension_age',
    'BPQ040A': 'prescription_htn',
    'BPQ050A': 'medication_htn',
    'BPQ080': 'cholesterol',
    'BPQ090D': 'prescription_cholesterol',
    'BPQ100D': 'medication_cholesterol',
    'LBXTC': 'lab_cholesterol',
    'BPXOSY1': 'bp_sys1',
    'BPXOSY2': 'bp_sys2',
    'BPXODI1': 'bp_dis1',
    'BPXODI2': 'bp_dis2',
    'LBDHDD': 'lab_hdl',
    'SMQ020': 'smoker'
}
cvs_name_mapping= {
    'CDQ001': 'chest_pain',
    'CDQ002': 'uphill_pain',
    'CDQ003': 'ord_pace',
    'CDQ005': 'stand_relieve_pain',
    'CDQ006' : 'time_relieve_pain',
    'CDQ010': 'sob_stairs'
}

meal_name_mapping= {
    'DBD895': 'outside_meals',
    'DBD900': 'fast_food_pizza',
    'DBD905': 'ready_to_eat_food',
    'DBD910': 'frozen_meals'
}

exercise_name_mapping = {
    'PAQ605': 'vigorious_work',
    'PAQ610': 'no_days_vigorious_work',
    'PAQ620': 'moderate_work',
    'PAQ625': 'no_months_moderate_work',
    'PAQ635': 'walk_bicycle',
    'PAQ640': 'days_walk_bicycle',
    'PAQ650': 'vigorious_recreational',
    'PAQ655': 'days_vigorious_recreational',
    'PAQ665': 'moderate_recreational',
    'PAQ670': 'days_moderate_recreational',
    'PAD680': 'minutes_sedentary'
}



def replace_values_with_nan(df, columns_to_replace, values_to_replace):
    """
    Replace specified values with NaN in selected columns of a DataFrame.

    Parameters:
    - df: DataFrame
    - columns_to_replace: List of columns to be considered for replacement
    - values_to_replace: List of values to be replaced with NaN

    Returns:
    - DataFrame with specified values replaced with NaN in selected columns
    """
    replace_dict = {col: {val: np.NaN for val in values_to_replace} for col in columns_to_replace}
    return df.replace(replace_dict)

def replace_nan_with_x(df, columns_to_replace, replacing_value):
    """
    Replace NaN values with x in selected columns of a DataFrame.

    Parameters:
    - df: DataFrame
    - columns_to_replace: List of columns to be considered for replacement
    - replacing_value: replace the value with x

    Returns:
    - DataFrame with NaN replaced with 0 in selected columns
    """
    for c in columns_to_replace:
        df[c]= df[c].fillna(value=replacing_value)
    return df

#for hypertension notebook
def replace_prescription(df, column_check, column_replace):
    # Your condition
    condition_1 = (df[column_check] == 1) & (df[column_replace].isin([7, 9]))
    condition_2 = (df[column_check] == 2) & (df[column_replace].isin([7, 9]))

    # Perform replacements
    df.loc[condition_1, column_replace] = 1
    df.loc[condition_2, column_replace] = 2
    return df