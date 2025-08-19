#!/usr/bin/env python3
"""
Script para executar os diferentes exemplos do projeto Streamlit
"""

import subprocess
import sys
import os
from pathlib import Path

def run_streamlit_app(app_path):
    """Executa um app Streamlit"""
    try:
        print(f"🚀 Iniciando {app_path}...")
        subprocess.run([sys.executable, "-m", "streamlit", "run", app_path], check=True)
    except KeyboardInterrupt:
        print("\n👋 App interrompido pelo usuário")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar {app_path}: {e}")
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {app_path}")

def main():
    """Função principal"""
    print("🚀 Tutorial de Data Apps com Streamlit")
    print("=" * 50)
    
    # Verificando se o Streamlit está instalado
    try:
        import streamlit
        print(f"✅ Streamlit {streamlit.__version__} encontrado")
    except ImportError:
        print("❌ Streamlit não encontrado. Instale com: pip install streamlit")
        return
    
    # Lista de apps disponíveis
    apps = {
        "1": ("app.py", "App Principal - Tutorial Completo"),
        "2": ("exemplos/exemplo_basico.py", "Exemplo Básico"),
        "3": ("exemplos/dashboard_vendas.py", "Dashboard de Vendas"),
        "4": ("exemplos/ml_app.py", "Machine Learning App")
    }
    
    print("\n📱 Apps disponíveis:")
    for key, (path, description) in apps.items():
        if os.path.exists(path):
            print(f"  {key}. {description}")
        else:
            print(f"  {key}. {description} (❌ não encontrado)")
    
    print("\n0. Sair")
    
    while True:
        try:
            choice = input("\n🎯 Escolha um app (0-4): ").strip()
            
            if choice == "0":
                print("👋 Até logo!")
                break
            elif choice in apps:
                app_path, description = apps[choice]
                if os.path.exists(app_path):
                    run_streamlit_app(app_path)
                    break
                else:
                    print(f"❌ Arquivo {app_path} não encontrado")
            else:
                print("❌ Opção inválida. Escolha 0-4.")
        except KeyboardInterrupt:
            print("\n👋 Até logo!")
            break

if __name__ == "__main__":
    main()
