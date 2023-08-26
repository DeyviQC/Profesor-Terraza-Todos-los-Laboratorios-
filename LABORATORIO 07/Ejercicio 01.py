persona = {
    'first_name': 'Edem',
    'last_name': 'Terraza',
    'age': 31,
    'country': 'Peru',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in persona:
    skills_lista = persona['skills']
    medio_index = len(skills_lista) // 2
    medio_skill = skills_lista[medio_index]
    print("Habilidad del medio:", medio_skill)
else:
    print("La persona no tiene habilidades registradas.")

if 'skills' in persona:
    skills_lista = persona['skills']
    if 'Python' in skills_lista:
        print("La persona tiene la habilidad 'Python'.")
    else:
        print("La persona no tiene la habilidad 'Python'.")
else:
    print("La persona no tiene habilidades registradas.")  

skills = persona.get('skills', [])

if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
    print("Él es un desarrollador frontend")
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print("Él es un desarrollador backend")
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print("Él es un desarrollador fullstack")
else:
    print("Título desconocido")