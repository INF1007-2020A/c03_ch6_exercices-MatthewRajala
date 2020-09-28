#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> bool:
    if values is None:
        # TODO: Demander les valeurs ici
        liste_ordonnee = []
        while len(liste_ordonnee) < 10:
            liste_ordonnee.append(int(input("Veuillez entrer un nombre entier: ")))

        i = 0
        while i < (len(liste_ordonnee)-1):
            if liste_ordonnee[i] > liste_ordonnee[i+1]:
                print("La liste n'est pas ordonnée")
                return False
                break
            i+=1
    print("La liste est ordonnée")
    return True


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: Demander les mots ici
        mot1 = input("Veuillez entrer un premier mot: ")
        mot2 = input("Veuillez entrer un deuxième mot: ")

        liste_lettres_mot1 = sorted(mot1)
        liste_lettres_mot2 = sorted(mot2)

        if liste_lettres_mot1 == liste_lettres_mot2: # les mots sont consitués des mêmes lettres
            print("Les mots sont constitués des mêmes lettres")
            return True
        else:
            print("Les mots ne sont pas consitués des mêmes lettres")
            return False

def contains_doubles(items: list) -> bool:
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres

    return {}, []


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    name, result = best_grades(grades)
    print(f"{name} a la meilleure moyenne: {result}")
    
    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
