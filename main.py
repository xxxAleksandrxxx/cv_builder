import os          # to to get current file path
import webbrowser  # to open browser after cv is created

from cv_html_generator import build
from database.db_test import data as db


# file_css = "../css/cv_helion.css"
file_css = "../css/cv.css"
file_cv = "output/cv.html"


if __name__ == '__main__':
    try:
        build(
            file_css,
            file_cv,
            db,
            "Data Scientist",
            "th"  #th, uz_beeline, uz_mobile
        )
        webbrowser.open_new_tab("".join(["file:///", os.getcwd(), "/", file_cv]))
    except:
        print("Something happened and build() didn't run")
        print(Exception)