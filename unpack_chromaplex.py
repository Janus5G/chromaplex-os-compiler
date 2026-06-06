#!/usr/bin/env python3
"""
ChromaPlex OS - Udpakningsscript
Læser chromaplex_os_package.json og gendanner hele projektstrukturen.
Kør med: python unpack_chromaplex.py
"""

import json
import os
import sys

def main():
    json_file = "chromaplex_os_package.json"
    
    if not os.path.exists(json_file):
        print(f"FEJL: {json_file} ikke fundet!")
        print(f"Placér JSON-filen i samme mappe som dette script.")
        sys.exit(1)
    
    print(f"📦 Indlæser {json_file}...")
    
    with open(json_file, 'r', encoding='utf-8') as f:
        package = json.load(f)
    
    metadata = package.get("metadata", {})
    print(f"📋 Projekt: {metadata.get('name', 'Ukendt')} v{metadata.get('version', '?')}")
    print(f"📝 Beskrivelse: {metadata.get('description', 'Ingen')}")
    print(f"👤 Forfatter: {metadata.get('author', 'Ukendt')}")
    print(f"📅 Oprettet: {metadata.get('created', 'Ukendt')}")
    
    sprog = metadata.get("languages", {})
    if sprog:
        print(f"🔤 Sprog:")
        for navn, beskrivelse in sprog.items():
            print(f"   - {navn}: {beskrivelse}")
    
    files = package.get("files", {})
    if not files:
        print("❌ Ingen filer fundet i JSON-pakken!")
        sys.exit(1)
    
    print(f"\n📂 Udpakker {len(files)} filer...\n")
    
    oprettet = 0
    for filsti, indhold in files.items():
        mappe = os.path.dirname(filsti)
        if mappe and not os.path.exists(mappe):
            os.makedirs(mappe, exist_ok=True)
            print(f"   📁 Opretter mappe: {mappe}/")
        
        try:
            with open(filsti, 'w', encoding='utf-8') as f:
                f.write(indhold)
            oprettet += 1
            stoerrelse = len(indhold)
            print(f"   ✅ {filsti} ({stoerrelse} bytes)")
        except Exception as e:
            print(f"   ❌ Fejl ved {filsti}: {e}")
    
    print(f"\n{'='*60}")
    print(f"🎉 FÆRDIG! {oprettet} filer udpakket.")
    print(f"{'='*60}")
    print(f"\nFor at installere ChromaPlex OS:")
    print(f"   cd {os.getcwd()}")
    print(f"   pip install -e .")
    print(f"\nFor at køre en test:")
    print(f"   python -m chromaplex_os.cli compile examples/hello.cpl -o hello.bin")
    print(f"   python -m chromaplex_os.cli run hello.bin")
    print(f"\nFor at generere visualisering:")
    print(f"   python -m chromaplex_os.visual_demo")
    print(f"")

if __name__ == "__main__":
    main()