grades = [
    {"midTerm": 70, "homeWork": 70, "final": 70},
    {"midTerm": 75, "homeWork": 75, "final": 75},
    {"midTerm": 80, "homeWork": 80, "final": 80},
    {"midTerm": 85, "homeWork": 85, "final": 85},
    {"midTerm": 90, "homeWork": 90, "final": 90}
]
names = ["Ali", "Veli", "Ahmet", "Mehmet", "Zek"  ]
info=dict()

for grade in grades:
    avgGrade=(grade["midTerm"]+grade["homeWork"]+grade["final"])/3
    index = list.index(grades, grade)
    name = names[index]
    info[name] = avgGrade

info = sorted(info.items(), key=lambda x: x[1], reverse=True)

for p in info:
    print(p)
