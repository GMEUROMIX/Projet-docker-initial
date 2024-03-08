import subprocess

def run_docker_compose():
    try:
        # Exécuter docker-compose run
        subprocess.run(["docker-compose", "up", "-d"], check=True)
    except subprocess.CalledProcessError as e:
        print("Erreur lors de l'exécution de docker-compose : ", e)

if __name__ == "__main__":
    run_docker_compose()
