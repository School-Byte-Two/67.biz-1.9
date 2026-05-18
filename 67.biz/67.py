import ctypes
import os
import subprocess
import time
import tkinter as tk

LYDFORMATER = (".mp3", ".wav")


def mci_send(command):
    """Sender en ren tekstkommando direkte til Windows sitt lavnivå lydsystem."""
    buffer = ctypes.create_string_buffer(255)
    ctypes.windll.winmm.mciSendStringA(
        command.encode("utf-8"), buffer, 254, 0
    )


def main():
    try:
        mappe = os.path.dirname(os.path.abspath(__file__))
        if mappe == "":
            mappe = os.getcwd()

        print("67 " * 50)
        print("[INFO] Skanner etter lydfiler...")

        lyder_funnet = []
        for fil in os.listdir(mappe):
            if fil.lower().endswith(LYDFORMATER):
                full_sti = os.path.join(mappe, fil)
                lyder_funnet.append(full_sti)

        if not lyder_funnet:
            print("[ADVARSEL] Fant ingen lydfiler (.mp3 / .wav) i mappen!")
        else:
            print(f"[SUKSESS] Fant {len(lyder_funnet)} lydfiler.")

        # 1. Vent i nøyaktig 10 sekunder
        print("\n[VENT] Venter i 10 sekunder før det eksploderer...")
        time.sleep(10)

        # 2. SPAM 67 i terminalen
        print("\n" + "67 " * 5000)

        # Hent skjermstørrelse for popup-vinduene
        dummy = tk.Tk()
        sw = dummy.winfo_screenwidth()
        sh = dummy.winfo_screenheight()
        dummy.destroy()

        print("[SPAM] Skyter ut vinduer og lyd i maksimal hastighet...")
        id_teller = 0

        # 3. LYNRASK LØKKE: Ingen forsinkelser, alt skjer så fort prosessoren klarer
        for i in range(150):  # Økt til 150 siden det går så mye fortere nå
            # --- LYD-SPAM (Utløses umiddelbart) ---
            if lyder_funnet:
                for sti in lyder_funnet:
                    alias = f"spamlyd_{id_teller}"
                    mci_send(f'open "{sti}" type mpegvideo alias {alias}')
                    mci_send(f"play {alias} from 0")
                    id_teller += 1

            # --- ULTRA-RASK VINDU-SPAM ---
            try:
                root = tk.Tk()
                root.title("67")

                # Kalkulerer plassering på skjermen
                x = (i * 53) % (sw - 250)
                y = (i * 37) % (sh - 150)

                root.geometry(f"250x150+{x}+{y}")
                root.configure(bg="black")

                label = tk.Label(
                    root,
                    text="67",
                    font=("Arial", 48, "bold"),
                    fg="red",
                    bg="black",
                )
                label.pack(expand=True, fill="both")

                root.attributes("-topmost", True)

                # update() tvinger Windows til å tegne vinduet på skjermen NÅ
                root.update()
            except:
                pass

        # 4. Kjør alle .bat-filer til slutt (når den raske spammen er over)
        for fil in os.listdir(mappe):
            if fil.lower().endswith(".bat"):
                full_sti = os.path.join(mappe, fil)
                print(f"\n[KJØRER] Batchfil: {fil}")
                subprocess.run([full_sti], shell=True, check=True)

        # Rydd opp i Windows-lydminnet
        for i in range(id_teller):
            mci_send(f"close spamlyd_{i}")

    except Exception as e:
        print(f"\n[KRITISK FEIL] Noe feilet: {e}")

    print("\n[FERDIG] Prosessen er fullført.")
    input("Trykk ENTER for å lukke dette vinduet...")


if __name__ == "__main__":
    main()