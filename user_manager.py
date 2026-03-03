import json
import os
from datetime import datetime

class UserManager:
    def __init__(self, filename="user_preferences.json"):
        self.filename = filename
        self.preferences = self.load_preferences()

    def load_preferences(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except Exception:
                pass
        return {
            "saved_topics": [],
            "search_history": []
        }

    def save_preferences(self):
        with open(self.filename, 'w') as f:
            json.dump(self.preferences, f, indent=4)

    def add_topic(self, topic):
        topic = topic.strip().lower()
        if topic and topic not in self.preferences["saved_topics"]:
            self.preferences["saved_topics"].append(topic)
            self.save_preferences()

    def remove_topic(self, topic):
        topic = topic.strip().lower()
        if topic in self.preferences["saved_topics"]:
            self.preferences["saved_topics"].remove(topic)
            self.save_preferences()

    def get_saved_topics(self):
        return self.preferences.get("saved_topics", [])

    def add_search_history(self, search_query):
        query = search_query.strip()
        if query:
            entry = {
                "query": query,
                "timestamp": datetime.now().isoformat()
            }
            self.preferences["search_history"].append(entry)
            self.save_preferences()

    def get_search_history(self):
        return self.preferences.get("search_history", [])

    def clear_search_history(self):
        self.preferences["search_history"] = []
        self.save_preferences()
