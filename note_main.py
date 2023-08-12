import os



note_name=""
def not_file(note_name):
    print(f"Файла с названием {note_name}.txt не существует ")

def build_note(note_text, note_name):
    with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
        file.write(note_text)
    print(f"Заметка {note_name} создана.")

def create_note(): 
    global note_name
    note_name = input("Введите название заметки: ")
    note_text = input("Введите текст заметки: ")
    build_note(note_text, note_name)

def read_note(note_name):
    try:
        with open(f"{note_name}.txt","r",encoding="utf-8") as file:
            text = file.read()
        print(text)
    except FileNotFoundError:
        not_file(note_name)


def read_note_2(note_name):
    if os.path.isfile(f"{note_name}.txt"):
        with open(f"{note_name}.txt","r",encoding="utf-8") as file:
            text = file.read()
        print(text)
    else:
        not_file(note_name)



def edit_note(note_name):
    if os.path.isfile(f"{note_name}.txt"):
        note_text = input("Введите текст заметки: ")
        build_note(note_text, note_name)
    else:
        not_file(note_name)


def delete_note(note_name):
    if os.path.isfile(f"{note_name}.txt"):
        os.remove(f"{note_name}.txt")
        print(f"Заметка {note_name}.txt удалена")
    else:
        not_file(note_name)


def choice_note(note_list):
    print(*note_list)
    chek = input("если передумали введите (нет): ")
    return chek


if __name__ =="__main__":

    note_list=[]
    
    while True:
        print("Что будем делать\n 1.Создать заметку\n 2.Изменить заметку\n 3.Удалить заметку\n 4.Выйти\n 5.Список заметок\n  ")
        do = input("Введите номер: ")
        if do == "1":
            create_note()
            note_list.append(note_name)
            
        if do == "2":
            chek = choice_note(note_list)
            if chek in note_list:
                edit_note(chek)
            elif chek == "нет":
                print("ОК")
            else:
                print(f"Блокнота {chek}.txt не найдено")
        if do == "3":
            print("Выберите заметку которую хотите удалить: ")
            chek = choice_note(note_list)
            if chek in note_list:
                delete_note(chek)
                note_list.remove(chek)
            elif chek == "нет":
                print("ОК")
            else:
                print(f"Блокнота {chek}.txt не найдено")
        if do == "5":
            if len(note_list)== 0:
                print("Нет созданных заметок\n")
            else:
                print(*note_list)  
        if do == "4":
            break
    
   