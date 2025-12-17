from django.shortcuts import render

def calculate_bmi(request):
    bmi = None   # Default value

    if request.method == "POST":
        height = float(request.POST.get("height"))
        weight = float(request.POST.get("weight"))
        bmi = weight / (height * height)

        # Print to server console for debugging
        print("Height:", height)
        print("Weight:", weight)
        print("BMI calculated:", bmi)

    return render(request, "bmiapp/template.html", {"BMI": bmi})




# Create your views here.
