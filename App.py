from Voice import Voice
from Face import Face
from threading import Thread

if __name__ == "__main__":
    voz = Voice("Oraculo", "Masculino")
    rosto = Face("Oraculo", "Raiva")

    thread_face = Thread(target=rosto.resposta, args=("chato"))
    # thread_voz = Thread(target=voz.ouvinte, args=(thread_face))