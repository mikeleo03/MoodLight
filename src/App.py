# File : App.py
# Berfungsi untuk menginisialisasi objek LandingPage dan memulai aplikasi

from GUI.LandingPage import LandingPage

# Memulai aplikasi MoodLight
if __name__ == "__main__":
    app = LandingPage()
    app.mainloop()