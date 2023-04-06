import csv
import json
import numpy as np
from scipy.spatial import distance

class EmbeddingsDatabase:
    def __init__(self):
        self.task_embeddings = {}
    
    def add_entry(self, task_index, embedding_vector):
        self.task_embeddings[task_index] = embedding_vector
    
    def load_from_csv(self, filename):
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                task_index = row[0]
                embedding_vector = [float(val) for val in row[1:]]
                self.add_entry(task_index, embedding_vector)
          
    
    def write_to_csv(self, filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for task_index, embedding_vector in self.task_embeddings.items():
                row = [task_index] + embedding_vector
                writer.writerow(row)

    def find_n_most_similar(self, embedding_vector, n):
        similarities = []
        for task_index, memory_embedding in self.task_embeddings.items():
            if memory_embedding is not None:
                cosine_sim = 1 - distance.cosine(embedding_vector, memory_embedding)
                similarities.append((task_index, cosine_sim))
            else:
                similarities.append((task_index, float('-inf')))
    
        sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
        return [task_index for task_index, sim in sorted_similarities[:n]]

class MemoryDatabase:
    def __init__(self):
        self.memories = []

    def add_memory(self, task_index, task, result):
        self.memories.append({'task_index': str(task_index), 'task': task,'result': result})
      
    def load_memories(self, file_path):
        with open(file_path, 'r') as f:
            memories = json.load(f)
        for memory in memories:
            self.add_memory(memory['task_index'], memory['task'], memory['result'])

    def save_memories(self, file_path):
        with open(file_path, 'w') as f:
            json.dump(self.memories, f)

    def link_embedding(self, file_path):
      self.embeddings_file_path = file_path
      self.embeddings = EmbeddingsDatabase()

    def get_memories_by_indexes(self, task_indexes):
        return [memory for memory in self.memories if memory['task_index'] in task_indexes]

class MemorySystem:
    def __init__(self, memory_path, embedding_path):
        self.memory_path = memory_path
        self.memory_database = MemoryDatabase()

        self.embedding_path = embedding_path
        self.embeddings = EmbeddingsDatabase()

    def query_memory(self, embedding_vector, n):
        indexes = self.embeddings.find_n_most_similar(embedding_vector, n)
        return self.memory_database.get_memories_by_indexes(indexes)

    def save_memory_system(self):
        self.memory_database.save_memories(self.memory_path)
        self.embeddings.write_to_csv(self.embedding_path)

    def load_memory_system(self):
        self.memory_database.load_memories(self.memory_path)
        self.embeddings.load_from_csv(self.embedding_path)

    def add_memory(self, task, result, vector):
        task_index = self.generate_index()
        self.memory_database.add_memory(task_index, task, result)
        self.embeddings.add_entry(task_index, vector)

    def generate_index(self):
        return len(self.embeddings.task_embeddings)+1
        

