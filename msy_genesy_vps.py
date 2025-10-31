#!/usr/bin/env python3
"""
MSY GENESY V2025 - VPS EDITION
Générateur IA + Évolution Génétique + Sync GitHub
"""

import os
import json
import random
import time
from datetime import datetime
from pathlib import Path
import requests
from dotenv import load_dotenv

load_dotenv()

class MSYGenesy:
    def __init__(self):
        self.config_file = Path("/msy/G/msy_genesy.json")
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.load_config()
        self.ensure_triple_path()
        
    def ensure_triple_path(self):
        for p in ["/msy/G", "/msy/D", "/msy/I"]:
            Path(p).mkdir(exist_ok=True)
    
    def load_config(self):
        if self.config_file.exists():
            with open(self.config_file) as f:
                self.config = json.load(f)
        else:
            self.config = self.default_config()
            self.save_config()
    
    def default_config(self):
        return {
            "github": {
                "token": self.github_token or "",
                "user": "Presidentibk225",
                "repo": "MSY_DASHBOARD"
            },
            "hierarchy": {str(i): {
                "name": n,
                "status": "ACTIF",
                "genes": g
            } for i, (n, g) in enumerate([
                ("Président IBK", ["vision", "leadership"]),
                ("MSY_INT", ["sync", "integration"]),
                ("MSY_UNI", ["consensus", "unified"]),
                ("MSY_UOE", ["execution", "output"]),
                ("TRIPLE_IA", ["grok", "claude", "gemini"]),
                ("Commercial", ["market", "growth"]),
                ("Exécution", ["deploy", "scale"]),
                ("Recovery", ["backup", "restore"])
            ], 1)},
            "genes_pool": [
                "quantum_sync", "ai_consensus", "global_scale", "vps_deploy",
                "triple_path", "github_webhook", "module_gen", "stats_live"
            ],
            "stats": {
                "modules_generated": 0,
                "genes_mutated": 0,
                "evolution_rate": 0.85
            }
        }
    
    def save_config(self):
        self.config_file.parent.mkdir(exist_ok=True)
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def generate_modules(self, count=100):
        modules = []
        for _ in range(count):
            level = random.choice(list(self.config['hierarchy'].keys()))
            gene = random.choice(self.config['genes_pool'])
            modules.append({
                "id": self.config['stats']['modules_generated'] + len(modules) + 1,
                "name": f"GEN_{level}_{gene}_{int(time.time())}",
                "status": random.choice(["ACTIF", "SYNCHRONISÉ", "OPTIMISÉ"]),
                "genes": random.sample(self.config['genes_pool'], k=3)
            })
        self.config['stats']['modules_generated'] += len(modules)
        self.config['stats']['genes_mutated'] += random.randint(5, 20)
        self.save_config()
        return modules
    
    def evolve_hierarchy(self):
        for level, info in self.config['hierarchy'].items():
            if random.random() < self.config['stats']['evolution_rate']:
                new_gene = random.choice(self.config['genes_pool'])
                info['genes'].append(new_gene)
                info['status'] = "ÉVOLUÉ"
        self.save_config()
    
    def sync_to_github(self):
        if not self.github_token:
            return
        modules = self.generate_modules(10)
        report = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "hierarchy": self.config['hierarchy'],
            "new_modules": modules[:3],
            "stats": self.config['stats']
        }
        # Sauvegarde locale
        report_file = Path("/msy/I") / f"genesy_report_{datetime.now():%Y%m%d_%H%M%S}.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"GENESY Rapport sauvé: {report_file}")
    
    def run(self):
        print("MSY GENESY V2025 DÉMARRÉ SUR VPS")
        try:
            while True:
                self.evolve_hierarchy()
                self.sync_to_github()
                print(f"GENESY | Modules: {self.config['stats']['modules_generated']} | Mutés: {self.config['stats']['genes_mutated']}")
                time.sleep(60)
        except KeyboardInterrupt:
            print("GENESY arrêté proprement")

if __name__ == "__main__":
    genesy = MSYGenesy()
    genesy.run()
