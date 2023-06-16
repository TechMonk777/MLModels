from django.shortcuts import render,redirect
from .models import Disease,DiseaseInfo
import pickle

# Create your views here.

with open('models/diabetes_model.sav','rb') as f:
    loaded_model = pickle.load(f)

def encode_gender(label):
    if label == 'Female':
        return 0
    elif label =='Male':
        return 1
    else:
        return 2

def encode_smoking(label):
    if label == 'No Info':
        return 0
    elif label == 'Never':
        return 1
    elif label == 'Former':
        return 2
    elif label == 'Current':
        return 3
    elif label == 'Not Current':
        return 4
    else:
        return 5
def home(request):
    return render(request,'index.html')

def predictDiabetes(request):
    disease = Disease.objects.get(id=1)
    disease_info = DiseaseInfo.objects.filter(disease=disease)
    context = {
        'disease':disease,
        'disease_info':disease_info
    }
    #fetch data from a form after submitting it 
    if request.method == 'POST':
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        hypertension = request.POST.get('hypertension')
        heart_disease =request.POST.get('heart_disease')
        smoking_history = request.POST.get('smoking_history')
        bmi = request.POST.get('bmi')
        hb_level = request.POST.get('HbA1c_level')
        glucose = request.POST.get('blood_glucose_level')
        
        encoded_gender = encode_gender(gender)
        encode_smoking_history = encode_smoking(smoking_history)

        print("###",loaded_model.predict([[encoded_gender,age,0,1,encode_smoking_history,bmi,hb_level,glucose]]))
        return redirect(result,1)
    return render(request,'diabetes.html')

def predictHeartAttack(request):
    #fetch data from a form after submitting it 
    if request.method == 'POST':
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        exang = request.POST.get('exang')
        cp =request.POST.get('cp')
        bp = request.POST.get('bp')
        cholesterol = request.POST.get('chol')
        rest_ecg = request.POST.get('rest_ecg')
        thalach = request.POST.get('thalach')
        
    return render(request,'heart_attack.html')

def about(request):
    return render(request,'about.html')

def result(request,id):
    # 1 : Diabetes
    # 2 : Heart Attack
    disease = Disease.objects.get(id=id)
    disease_info = DiseaseInfo.objects.filter(disease=disease)
    context = {
        'disease':disease,
        'disease_info':disease_info
    }
    return render(request,'result.html',context)
