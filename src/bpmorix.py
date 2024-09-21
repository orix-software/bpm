#!/usr/bin/env python3

import toml
import sys
import requests
import os
import gzip
import tarfile
import shutil
from datetime import datetime

toml_file = "bpmorix.tom"

def decompress_and_extract(filename, dependency_name):
    """Décompresse un fichier .gz et extrait une archive .tar"""
    try:
        # Décompression du fichier .gz
        with gzip.open(filename, 'rb') as f_in:
            with open(filename[:-4] + ".tar", 'wb') as f_out:  # Enlève '.tgz'
                f_out.writelines(f_in)
        os.remove(filename)
        os.makedirs('orixlibs/' + dependency_name, exist_ok=True)
        # Extraction du fichier .tar
        with tarfile.open(filename[:-4] + ".tar", 'r') as tar:
            tar.extractall(path='orixlibs/'+ dependency_name)  # Extrait dans le répertoire orixlibs
        os.remove(filename[:-4] + ".tar")

    except Exception as e:
        print(f"Erreur lors de la décompression ou de l'extraction : {e}")

def add_dependency_to_toml(file_path, dependency_str):
    """Ajoute une nouvelle dépendance dans la section 'dependency' du fichier TOML"""
    try:
        # Lire le fichier TOML
        with open(file_path, 'r') as file:
            data = toml.load(file)

        # Si la section "dependency" n'existe pas, la créer
        if "dependencies" not in data:
            data["dependencies"] = {}

        # Séparer le nom de la dépendance et la version
        try:
            dependency_name, dependency_version = dependency_str.split("@")
            dependency_name = dependency_name.strip()
            dependency_version = dependency_version.strip().strip('"').strip("'")
        except ValueError:
            print("Erreur de format : La chaîne doit être sous la forme 'nom@\"version\"'.")
            return

        # Ajouter ou mettre à jour la dépendance dans le fichier TOML
        data["dependencies"][dependency_name] = dependency_version

        value = download_file("http://repo.orix.oric.org/dists/" + dependency_version + "/tgz/6502/" + dependency_name + ".tgz", "orixlibs/" + dependency_name + ".tgz", dependency_name)

        if value == 0:
            # Écrire les modifications dans le fichier TOML
            with open(file_path, 'w') as file:
                toml.dump(data, file)

            print(f"{dependency_name} = {dependency_version} installed")
        else:
            print(f"{dependency_name} = {dependency_version} not found")

    except FileNotFoundError:
        print(f"Le fichier '{file_path}' n'a pas été trouvé.")
    except toml.TomlDecodeError:
        print(f"Erreur lors de la lecture du fichier TOML '{file_path}'.")

def download_file(url, local_filename, dependency_name):
    """Télécharge un fichier depuis une URL"""
    os.makedirs('orixlibs', exist_ok=True)
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si la requête a réussi

        with open(local_filename, 'wb') as f:
            f.write(response.content)

        decompress_and_extract(local_filename, dependency_name)
        return 0
    except requests.exceptions.RequestException as e:
        return 1

def install_dependency_from_toml(toml_file):
    try:
        # Lire le fichier TOML
        with open(toml_file, 'r') as file:
            data = toml.load(file)

        if "dependencies" in data:
            dependencies = data["dependencies"]
            print("Liste des dépendances :")
            for key, value in dependencies.items():
                value_download = download_file("http://repo.orix.oric.org/dists/" + value + "/tgz/6502/" + key + ".tgz", "orixlibs/" + key + ".tgz", key)
                if value_download == 0:
                    print(f"{key} = {value} installed")
                else:
                    print(f"{key} = {value} not found")

    except FileNotFoundError:
        print(f"Le fichier '{toml_file}' n'a pas été trouvé.")

def read_dependencies_from_toml(file_path):
    try:
        # Lire le fichier TOML
        with open(file_path, 'r') as file:
            data = toml.load(file)

        # Vérifier si la section "dependency" existe
        if "dependencies" in data:
            dependencies = data["dependencies"]
            print("Liste des dépendances :")
            for key, value in dependencies.items():
                print(f"{key} = {value}")
        else:
            print("La section 'dependencies' n'existe pas dans le fichier TOML.")
    except FileNotFoundError:
        print(f"Le fichier '{file_path}' n'a pas été trouvé.")
    except toml.TomlDecodeError:
        print(f"Erreur lors de la lecture du fichier TOML '{file_path}'.")

def remove_dependency_from_toml(file_path, dependency_name):
    """Supprime une dépendance de la section 'dependency' du fichier TOML"""
    try:
        with open(file_path, 'r') as file:
            data = toml.load(file)

        # Vérifier si la section "dependency" existe
        if "dependencies" in data and dependency_name in data["dependencies"]:
            del data["dependencies"][dependency_name]
            print(f"{dependency_name} uninstalled")
            shutil.rmtree("orixlibs/" + dependency_name)
        else:
            print(f"La dépendance '{dependency_name}' n'existe pas dans le fichier TOML.")

        # Écrire les modifications dans le fichier TOML
        with open(file_path, 'w') as file:
            toml.dump(data, file)

    except FileNotFoundError:
        print(f"Le fichier '{file_path}' n'a pas été trouvé.")
    except toml.TomlDecodeError:
        print(f"Erreur lors de la lecture du fichier TOML '{file_path}'.")

def init_toml(file_path):
    current_directory = os.getcwd()
    last_directory = os.path.basename(os.path.normpath(current_directory))
    now = datetime.now()

    # Récupérer l'année courante
    current_year = now.year

    # Déterminer le trimestre actuel
    current_month = now.month
    current_trimester = (current_month - 1) // 3 + 1

    # Afficher les résultats
    # print(f"Année courante : {current_year}")
    # print(f"Trimestre actuel : {current_trimester}")
    """Crée un fichier TOML avec des valeurs par défaut."""
    content = "[package]\nname = \"" + last_directory  + "\"\nversion = \"" + str(current_year) + "." + str(current_trimester) + "\"\nauthors = [ \"nobody@nobody.fr\" ]\nlicense = \"MIT OR Apache-2.0\"\nedition = \"2018\"\ncpu = \"6502\"\n\n[dependencies]\n"
    with open(file_path, 'w') as file:
        file.write(content)

    if not os.path.exists("VERSION"):
        content = str(current_year) + "." + str(current_trimester)
        with open("VERSION", 'w') as file:
            file.write(content)
    print(f"initialized")

def usage():
    print("Orix package manager\n")
    print("Usage : pbmorix [OPTIONS] [COMMAND]\n")
    print("\033[1;32mCommands:\033[0m")
    print("    \033[1;36minit\033[0m            Create a new bpmorix package")
    print("    \033[1;36mlist\033[0m            List packages")
    print("    \033[1;36madd         \033[0m    Add dependencies to a manifest file")
    print("    \033[1;36mremove      \033[0m    Remove dependencies from a manifest file")
    print("    \033[1;36minstall     \033[0m    install all dependencies from a manifest file")

#len(sys.argv) != 2 or 
def main():
    # Vérifier si l'argument 'list' est passé en ligne de commande
    if len(sys.argv) ==1:
        usage()
        sys.exit(1)

    if sys.argv[1] != 'list' and sys.argv[1] != 'add' and sys.argv[1] != 'remove' and sys.argv[1] != 'init' and sys.argv[1] != 'install':
        usage()
        sys.exit(1)


    action = sys.argv[1]


    if action == 'list':
        read_dependencies_from_toml(toml_file)
    elif action == 'add' and len(sys.argv) == 3:
        dependency_str = sys.argv[2]
        add_dependency_to_toml(toml_file, dependency_str)
    elif action == 'remove':
        if len(sys.argv) == 3:
            dependency_name = sys.argv[2]
            remove_dependency_from_toml(toml_file, dependency_name)
        else:
            print("remove needs an argument")
    elif action == 'install':
        install_dependency_from_toml(toml_file)
    elif action == 'init':
        if not os.path.exists(toml_file):
            init_toml(toml_file)
        else:
            print("Already initialized")


    # Lire et afficher les dépendances


if __name__ == "__main__":
    main()