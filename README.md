# Projet Goncourt

## Ce projet contient

* `docs` : les documents UML et le diagramme Entité-Association.
* `goncourt` : le code du projet.
* `sql` :

  * `seed.sql` : contient les données permettant de remplir la base de données.
  * `schema.sql` : contient le schéma permettant de créer la base de données.

## Utilisation de Commitlint + Husky

J'ai utilisé **Commitlint** et **Husky** afin de garder des commits propres et de respecter une convention pour les messages de commit.
**Commitlint** permet de vérifier que les messages de commit respectent certaines règles. Si le message ne respecte pas ces règles, le commit est refusé.
**Husky** permet d'exécuter automatiquement Commitlint lors d'un commit. Cela permet notamment d'appliquer les mêmes règles lorsqu'un commit est effectué depuis Git, PyCharm ou un autre IDE/client Git utilisant les hooks Git.

Par exemple, ce commit ne passera pas :

```bash
git commit -m "ajout du cours"
```

Alors que celui-ci passera :

```bash
git commit -m "feat: add course creation"
```

### Mise en place après un `git clone`

Après avoir cloné le projet , il faut installer les dépendances Node.js :

```bash
npm install
```

Cela permet d'installer les dépendances nécessaires à Commitlint et Husky présentes dans le `package.json`.
Les hooks Husky pourront ensuite vérifier automatiquement les prochains commits.

## Choix de conception pour le code

J'ai trouvé plus intéressant que ce soit la couche **Business** qui gère la connexion à la base de données.
J'ai également créé des requêtes génériques pour récupérer les informations des différentes tables.
Ces requêtes utilisent des paramètres comme le nom de la table et l'identifiant de la table afin d'éviter de réécrire les mêmes requêtes dans chaque DAO.
Les résultats récupérés sont ensuite passés dans un **parser propre à chaque table**, qui permet de transformer les données récupérées depuis la base de données en objets Python correspondants.

## Utilisation de ChatGPT

ChatGPT m'avait aidé à installer **Commitlint** et **Husky** dans un projet précédent.
ChatGPT m'a également aidé à générer les insertions SQL des romans présentes dans le fichier `seed.sql`.
