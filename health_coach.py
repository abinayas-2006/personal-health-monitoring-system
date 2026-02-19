import json
from datetime import datetime

# -------- Load Data --------
def load_data():
    try:
        with open("health_data.json", "r") as f:
            return json.load(f)
    except:
        return []

# -------- Save Data --------
def save_data(data):
    with open("health_data.json", "w") as f:
        json.dump(data, f, indent=4)

print("🏥 Personal Health Coach AI\n")

profile = {}
profile["name"] = input("Name: ")
profile["age"] = int(input("Age: "))
profile["weight"] = float(input("Weight (kg): "))
profile["height"] = float(input("Height (cm): "))
profile["steps"] = int(input("Daily Steps: "))
profile["sleep"] = float(input("Hours of Sleep: "))
profile["goal"] = input("Your Health Goal (Weight Loss/Muscle Gain/Fitness): ")
profile["date"] = datetime.now().strftime("%Y-%m-%d")

# -------- BMI Calculation --------
height_m = profile["height"] / 100
bmi = profile["weight"] / (height_m ** 2)
profile["BMI"] = round(bmi, 2)

# -------- AI-Like Recommendations --------
print("\n📊 Health Summary")
print("----------------------------")
print("BMI:", profile["BMI"])

if bmi < 18.5:
    print("⚠ Underweight - Increase calorie intake.")
elif 18.5 <= bmi <= 24.9:
    print("✅ Normal weight - Maintain healthy routine.")
else:
    print("⚠ Overweight - Consider diet & exercise plan.")

if profile["sleep"] < 6:
    print("😴 Low sleep detected - Aim for 7-8 hours.")
else:
    print("🛌 Sleep pattern looks good.")

if profile["steps"] < 5000:
    print("🚶 Increase daily physical activity.")
else:
    print("💪 Good activity level!")

# Save
data = load_data()
data.append(profile)
save_data(data)

print("\n🎯 Personalized Suggestion:")

if profile["goal"].lower() == "weight loss":
    print("🥗 Reduce calories + 30 min cardio daily.")
elif profile["goal"].lower() == "muscle gain":
    print("🏋 Strength training + high protein diet.")
else:
    print("🏃 Maintain balanced diet and regular exercise.")

print("\n✅ Data Saved Successfully!")
