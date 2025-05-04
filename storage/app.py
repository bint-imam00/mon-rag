import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, Settings
from llama_index.core.indices.loading import load_index_from_storage
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from dotenv import load_dotenv
import gradio as gr
import logging
import time
from tenacity import retry, stop_after_attempt, wait_exponential
import traceback

# Configurer le logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Charger les variables d'environnement
load_dotenv()

# Obtenir l'URL d'Ollama depuis les variables d'environnement
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "localhost")
OLLAMA_URL = f"http://{OLLAMA_HOST}:11434"

try:
    # Configurer les paramètres globaux pour utiliser Ollama
    logger.info(f"Configuration des modèles Ollama sur {OLLAMA_URL}...")
    Settings.llm = Ollama(
        model="mistral:latest",
        request_timeout=300.0,
        temperature=0.7,
        context_window=4096,
        base_url=OLLAMA_URL
    )
    Settings.embed_model = OllamaEmbedding(
        model_name="mistral:latest",
        base_url=OLLAMA_URL
    )

    # 1. Charger les documents
    logger.info("Chargement des documents...")
    documents = SimpleDirectoryReader("data").load_data()
    logger.info(f"Nombre de documents chargés : {len(documents)}")

    # 2. Créer l'index avec les embeddings Ollama
    logger.info("Création de l'index...")
    index = VectorStoreIndex.from_documents(
        documents,
        show_progress=True
    )

    # 3. Sauvegarder l'index (optionnel)
    logger.info("Sauvegarde de l'index...")
    index.storage_context.persist(persist_dir="storage")

    # 4. Charger l'index (si déjà sauvegardé)
    logger.info("Chargement de l'index sauvegardé...")
    storage_context = StorageContext.from_defaults(persist_dir="storage")
    index = load_index_from_storage(storage_context)

    # 5. Créer un moteur de requête avec des paramètres optimisés
    logger.info("Création du moteur de requête...")
    query_engine = index.as_query_engine(
        similarity_top_k=2,  # Limiter le nombre de documents similaires
        streaming=True  # Activer le streaming pour une réponse plus rapide
    )

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def query_with_retry(question):
        try:
            logger.info(f"Tentative de requête avec la question : {question}")
            response = query_engine.query(question)
            logger.info(f"Réponse reçue : {response}")
            return response
        except Exception as e:
            logger.error(f"Erreur lors de la requête : {str(e)}")
            logger.error(f"Traceback : {traceback.format_exc()}")
            raise

    def answer_question(question):
        try:
            logger.info(f"Question reçue : {question}")
            start_time = time.time()
            response = query_with_retry(question)
            end_time = time.time()
            logger.info(f"Réponse générée en {end_time - start_time:.2f} secondes")
            return str(response)
        except Exception as e:
            error_msg = f"Une erreur s'est produite : {str(e)}\n{traceback.format_exc()}"
            logger.error(error_msg)
            return error_msg

    logger.info("Lancement de l'interface Gradio...")
    gr.Interface(
        fn=answer_question,
        inputs="textbox",
        outputs="text",
        title="Mon GPT RAG",
        description="Posez une question sur Aïcha MBAYE",
        allow_flagging="never"
    ).launch(server_name="0.0.0.0", server_port=7860)

except Exception as e:
    logger.error(f"Erreur lors de l'initialisation : {str(e)}")
    logger.error(f"Traceback : {traceback.format_exc()}")
    raise