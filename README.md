<div align="center">
<img src="https://raw.githubusercontent.com/CROUStillant-Developpement/CROUStillantAssets/main/logo.png" alt="CROUStillant Logo"/>
  
# DataGouvPy
CROUStillant est un projet qui a pour but de fournir les menus des restaurants universitaires en France et en Outre-Mer. 
Ce dépôt contient le code source d'une librairie interne de CROUStillant en Python qui permet d’interagir avec l'API de data.gouv.fr.

</div>
  
# 📖 • Sommaire

- [🚀 • Présentation](#--présentation)
- [⚙️ • Installation](#%EF%B8%8F--installation)
- [💻 • Développement](#--développement)
- [📄 • Utilisation](#--utilisation)
- [📃 • Crédits](#--crédits)
- [📝 • License](#--license)

# 🚀 • Présentation

DataGouvPy est une librairie Python qui permet d'interagir avec l'API de data.gouv.fr.  
Elle est conçue pour être utilisée avec la librairie [aiohttp](https://docs.aiohttp.org/en/stable/) pour effectuer des requêtes asynchrones.  

# ⚙️ • Installation

Pour installer la librairie, exécutez la commande suivante :

```bash
pip install git+https://github.com/CROUStillant-Developpement/DataGouvPy.git
```

# 💻 • Développement

Pour installer la librairie en mode de développement, exécutez les commandes suivantes :

1. Cloner le dépôt
```bash
git clone https://github.com/CROUStillant-Developpement/DataGouvPy.git
```

2. Créer un environnement virtuel et installer les dépendances
```bash
cd DataGouvPy
```

3. Créer un environnement virtuel
```bash	
uv venv
```

4. Installer les dépendances
```bash
uv sync
```

# 📄 • Utilisation

```python
import asyncio

from DataGouvPy import DataGouv
from aiohttp import ClientSession


async def main():
    """
    Exemple d'utilisation de la librairie DataGouvPy.
    """
    session = ClientSession()

    client = DataGouv(session=session, api_key="API KEY")

    # Uploader un jeu de données
    await client.upload_resource(
        dataset_id: str = "dataset_id",
        dataset: pd.DataFrame = pd.DataFrame(),
        resource_name: str = "resource_name",
        resource_description: str = "resource_description",
    )

    # Mettre à jour les métadonnées d'un dataset
    await client.update_dataset_metadata(
        dataset_id: str = "dataset_id",
        metadata: dict = {
            "owner": "owner_id",
            "title": "Titre du dataset", 
            "private": False,
            "description": "Description du dataset",
            "acronym": "Acronyme du dataset",
            "tags": [
                "tag1",
                "tag2",
            ],
            "license": "lov2", 
            "frequency": "daily",
            "temporal_coverage": {
                "start": "2025-01-01T00:00:00.000Z",
                "end": datetime.now().isoformat()
            },
            "spatial": {
                "granularity":"poi"
            }
        }
    )

    # Supprimer la ressource d'un dataset
    await client.delete_resource(
        dataset_id: str = "dataset_id",
        resource_id: str = "resource_id",
    )

    await session.close()


if __name__ == "__main__":
    asyncio.run(main())
```

# 📃 • Crédits

- [Paul Bayfield](https://github.com/PaulBayfield) - Fondateur du projet et développeur principal

# 📝 • License

CROUStillant est sous licence [Apache 2.0](LICENSE).

```
Copyright 2024 - 2025 CROUStillant Développement

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
