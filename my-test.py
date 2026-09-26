import json
import os
import random
import streamlit as st

# 1. ОҚУШЫЛАРДЫ САҚТАУ БАЗАСЫ (Файлға жазу)
DATA_FILE = "students_tasks.json"


def load_students():
  if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
      return json.load(f)
  return [
      {"name": "Ақжол", "level": 3},
      {"name": "Мәдина", "level": 3},
      {"name": "Ерасыл", "level": 3},
  ]


def save_students(students_list):
  with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(students_list, f, ensure_ascii=False, indent=4)


# Оқушылар тізімі
if "students" not in st.session_state:
  st.session_state.students = load_students()

# 2. ЕСЕПТЕР БАЗАСЫ (Тек for, while, break, else)
task_bank = [
    {
        "task": (
            "1-ден N-ге дейінгі сандардың ішінен 7-ге бөлінетін алғашқы"
            " санды тапқанда циклды тоқтат (break қолдан)."
        )
    },
    {
        "task": (
            "Енгізілген санның жай немесе құрама екенін тексеретін цикл жаз"
            " (else қолдан)."
        )
    },
    {
        "task": (
            "Теріс сан енгізілгенге дейін барлық енгізілген оң сандарды"
            " қосып, соңында шығар."
        )
    },
]

# --- Сайттың интерфейсі ---
st.title("👨‍💻 Python Оқушылардың Деңгей Есептері")

# Жаңа оқушы қосу бөлімі
new_name = st.text_input("Жаңа оқушының атын енгізіңіз:")
if st.button("Оқушы қосу"):
  if new_name:
    st.session_state.students.append({"name": new_name, "level": 3})
    save_students(st.session_state.students)
    st.success(f"{new_name} тізімге қосылды!")

st.divider()

# Әр оқушыға жеке есеп шығарып беру
st.subheader("📋 Оқушыларға арналған тапсырмалар:")

if st.button("Есептерді тарату (Араластыру)"):
  for student in st.session_state.students:
    st.markdown(f"**Оқушы: {student['name']}**")
    # Әр оқушыға кездейсоқ 2 есеп таңдау
    shuffled = task_bank.copy()
    random.shuffle(shuffled)
    for i in range(2):
      st.write(f"  - {i+1}-есеп: {shuffled[i]['task']}")
    st.markdown("---")

# Қазіргі оқушылар тізімі
st.sidebar.subheader("Тіркелген оқушылар:")
for s in st.session_state.students:
  st.sidebar.text(s["name"])
