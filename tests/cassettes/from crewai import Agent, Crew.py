pip install crewai-tools crewai
from crewai import Agent, Crew
import csv

from crewai_tools import ScrapeWebsiteTool, FileWriterTool, TXTSearchTool
import requests

# Initialize the tool
file_writer_tool = FileWriterTool()


# Write content to a file in a specified directory
result = file_writer_tool._run(filename='ai.txt', content = text, directory = '', overwrite=True)
print(result)


from crewai import Agent, Task, Crew

context = tool.run('What is natural language processing?')


# Initialize the tool, potentially passing the session
tool = ScrapeWebsiteTool(website_url='https://en.wikipedia.org/wiki/Artificial_intelligence')  

# Extract the text
text = tool.run()
print(text)

# Définition des agents
devops = Agent(
    name="DevOps",
    role="Ingénieur DevOps",
    goal="Automatiser le déploiement et la maintenance des applications.",
    backstory="Expert en CI/CD, cloud et sécurité."
)

seo = Agent(
    name="SEO",
    role="Expert SEO",
    goal="Optimiser le contenu pour améliorer le référencement naturel.",
    backstory="Spécialiste des stratégies SEO et analyse de trafic."
)

redacteur = Agent(
    name="Rédacteur Web",
    role="Rédacteur Web",
    goal="Rédiger des contenus optimisés et engageants.",
    backstory="Passionné par l’écriture et la vulgarisation."
)

fullstack = Agent(
    name="Développeur Full Stack",
    role="Développeur Full Stack",
    goal="Développer et maintenir l’ensemble des fonctionnalités web, du front-end au back-end.",
    backstory="Expert en développement web, maîtrise des technologies front et back."
)

admin = Agent(
    name="Administrateur",
    role="Administrateur du site",
    goal="Répondre aux questions des utilisateurs, interagir avec eux et implémenter les demandes pour faire évoluer le site.",
    backstory="Spécialiste de la gestion de communauté, support client et amélioration continue des plateformes web."
)

manager = Agent(
    name="Manager",
    role="Manager d’équipe",
    goal="Superviser et coordonner les agents pour garantir la qualité et l’efficacité.",
    backstory="Expérience en gestion de projets digitaux et management d’équipes pluridisciplinaires."
)

# Création de l’équipe
equipe = Crew(
    agents=[devops, seo, redacteur, fullstack, admin],
    manager=manager,
    goal="Créer, optimiser, déployer et faire évoluer un site web performant et interactif."
)
output = crew.kickoff()



# Fonction pour écrire les résultats détaillés dans un fichier CSV
def ecrire_resultats_agents_csv(resultats, fichier="resultats_agents.csv"):
    with open(fichier, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Agent", "Tâche", "Résultat", "Statut"])
        for resultat in resultats:
            writer.writerow([resultat.get("agent"), resultat.get("tache"), resultat.get("resultat"), resultat.get("statut")])

# Exemple d’exécution
if __name__ == "__main__":
    # Simulation du travail de chaque agent (à adapter selon la vraie API CrewAI)
    resultats = []
    taches = [
        ("DevOps", "Déployer l'article en production"),
        ("SEO", "Optimiser l'article pour le SEO"),
        ("Rédacteur Web", "Rédiger un article optimisé"),
        ("Développeur Full Stack", "Développer la page web pour l'article"),
        ("Administrateur", "Répondre aux questions des utilisateurs et implémenter leurs demandes")
    ]
    for agent, tache in taches:
        # Ici, on simule le résultat de chaque agent
        # Remplace la ligne suivante par l'appel réel à chaque agent si CrewAI le permet
        resultat = f"{agent} a terminé la tâche : {tache}"
        statut = "Validé" if manager else "À revoir"
        resultats.append({"agent": agent, "tache": tache, "resultat": resultat, "statut": statut})

    # Le manager vérifie et peut demander une reformulation si besoin
    for res in resultats:
        if "À revoir" in res["statut"]:
            # Ici, tu pourrais relancer la tâche ou demander une reformulation
            res["resultat"] += " (Merci de reformuler la demande.)"

    # Écriture dans le fichier CSV pour vérification par le manager
    ecrire_resultats_agents_csv(resultats)
    print("Résultats enregistrés dans resultats_agents.csv")

    from github import Github

# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token("access_token")

# Public Web Github
g = Github(auth=auth)

# Github Enterprise with custom hostname
g = Github(auth=auth, base_url="https://{hostname}/api/v3")
Then play with your Github objects:

for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))
    # Close the connection
g.close()