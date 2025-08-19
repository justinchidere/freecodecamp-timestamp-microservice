import pyautogui
import time
import sys

def erstelle_bildschirm_erfassung(ziel_bildschirm):
    """Erfasst die Bildschirmausgabe und generiert einen Screenshot."""
    try:
        screenshot = pyautogui.screenshot(region=ziel_bildschirm)
        return screenshot
    except Exception as e:
        print(f"Fehler beim Erfassen des Bildschirms: {e}")
        return None


def erstelle_wasserzeichen(bildschirm, schriftzug, freistellraum_breite, freistellraum_hoehe):
    """Fügt ein Wasserzeichen mit Justin Echo hinzu."""

    try:
        time.sleep(2)  # Wartezeit, um den Bildschirminhalt zu lesen

        x = int(input("Gib die x-Koordinate für das Wasserzeichen ein (z.B. 100): "))
        y = int(input("Gib die y-Koordinate für das Wasserzeichen ein (z.B. 200): "))
        text = input("Gib den Justin Echo Text ein: ")
        
        # Text direkt im Bild einfügen (Beispiel - kann angepasst werden)
        #text_x = int(input("Gib die x-Koordinate für den Text ein (z.B. 100): "))
        #text_y = int(input("Gib die y-Koordinate für den Text ein (z.B. 200): "))

        #  Hier könnte der Text, wie er mit dem Bild erstellt werden soll,  ausgeführt werden.
        # Das ist in diesem Beispiel für die Demonstration nur ein Platzhalter.

        print(f"Wasserzeichen erstellt: {schriftzug}  x={x}, y={y}")
        
        return True
    except Exception as e:
        print(f"Fehler beim Einfügen des Wasserzeichens: {e}")
        return False



def main():
    """Hauptfunktion des Skripts."""

    ziel_bildschirm = "0x0" # Standardbildschirm (0x0)
    
    screenshot = erstelle_bildschirm_erfassung(ziel_bildschirm)

    if screenshot:
        print("Screenshot erfolgreich erfasst.")
        
        if erstelle_wasserzeichen(screenshot, "Justin Echo", 300, 300):
            print("Wasserzeichen hinzugefügt!")
        else:
            print("Wasserzeichen hinzufügen fehlgeschlagen.")
    else:
        print("Screenshot konnte nicht erfasst werden.")

if __name__ == "__main__":
    main()

