patient = ("Joseph Azran", 55, "120/80", 72)

print("Age:", patient[1], "Heart Rate:", patient[3])

patient_list = list(patient)
patient_list[3] = 70
patient = tuple(patient_list)

patients = (
    ("John", 35, "110/70", 68),
    ("James", 54, "130/65", 80),
    ("Randy", 44, "125/72", 76),
    ("David", 65, "140/75", 72),
    ("Becky", 56, "118/70", 70)
)

names = [p[0] for p in patients]
print("Updated patient:", patient)
print("All names:", names)
