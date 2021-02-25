import functools
from sentence_transformers import SentenceTransformer, util, CrossEncoder
import time
import os
import pandas as pd
import pickle
import time
import hnswlib
import json

# bi-encoder
model=SentenceTransformer('msmarco-distilbert-base-v2')

top_k=20
embedding_size = 768
entry_count = 5600 #5600 alt
sentences_path = f'staticfiles/Book_{entry_count}.csv'
index_path = "./hnswlib.index"
# cross-encoder to improve quality
# cross_encoder=CrossEncoder('cross-encoder/ms-marco-TinyBERT-L-6')
embedding_cache_path = f"staticfiles/embeddings_{entry_count}.pkl"
# load database
@functools.cache
def get_db(db_path):
  return pd.read_csv(db_path).dropna()

@functools.cache
def create_embeddings(db_path, cache_path):
  db = get_db(db_path)
  embeddings=model.encode(db["Overview"].to_list(),show_progress_bar=True)
  with open(cache_path, "wb") as fOut:
    pickle.dump({'embeddings': embeddings}, fOut)
  return embeddings

@functools.cache
def get_embeddings(cache_path):
  if not os.path.exists(cache_path): return None
  with open(cache_path, "rb") as fIn:
    embeddings = pickle.load(fIn)['embeddings']
    return embeddings

def create_index(embeddings):
  index.init_index(max_elements = len(embeddings), ef_construction = 400, M = 64)
  index.add_items(embeddings, list(range(len(embeddings))))
  index.save_index(index_path)

@functools.cache
def get_index(index_path):
  index = hnswlib.Index(space = 'cosine', dim = embedding_size)
  if os.path.exists(index_path):
    print("Loading index...")
    index.load_index(index_path)
  index.set_ef(50)
  return index

def handleQuestionFactory(db, embeddings):
  def handleQuestion(question):
    db["question"] = question
    start = time.time()
    q_embedding=model.encode(question,convert_to_tensor=True, show_progress_bar=True)
    s_results = util.semantic_search(q_embedding,embeddings,top_k=top_k)
    results   = pd.DataFrame(s_results[0], columns=["corpus_id","score"])
    # sort/score results with the cross-encoder:
    # cross_inp = db.iloc[results.corpus_id][["question","Overview"]].to_numpy().tolist()
    # cross_sco=cross_encoder.predict(cross_inp, show_progress_bar=True)
    # results['cross_score']=cross_sco
    # results = results.sort_values("cross_score", ascending=True)
    end = time.time()
    results.duration = end-start
    result_merge = pd.merge(results,db,"inner",left_on="corpus_id", right_index=True).to_json(orient="records")
    parsed = json.loads(result_merge)
    return json.dumps(parsed, indent=4)
    # corpus_ids, distances = index.knn_query(q_embedding, k=top_k)
    # hits = [{'corpus_id': id, 'score': 1-score} for id, score in zip(corpus_ids[0], distances[0])]
    # hits = pd.DataFrame(sorted(hits, key=lambda x: x['score'], reverse=True))
  return handleQuestion

db = get_db(sentences_path)
embeddings = get_embeddings(embedding_cache_path) 
embeddings = embeddings if embeddings is not None else create_embeddings(sentences_path, embedding_cache_path)
# index = get_index(embeddings, index_path)
handleQuestion = handleQuestionFactory(db, embeddings)
