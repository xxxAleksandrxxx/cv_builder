import traceback  # to traceback errors and locate them in the code

import os          # to to get current file path
import webbrowser  # to open browser after cv is created

from cv_html_generator import build
from cl_html_generator import build_cl
# from database.db_risk import data as db
from database.db_test import data as db
# from database.db_engineer import data as db

# file_css = "../css/cv_helion.css"
file_css = "../css/cv.css"
file_cv = "output/cv.html"
file_cl = "output/cl.html"

phone = "th"  #th, uz_beeline, uz_mobile

job_title = "Data Scientist"

cover_letter_flag = False
cover_letter = '''Dear Hiring Manager,
I am excited to apply for the Experiment & Test Engineer position at Helion Energy, Inc. As an experienced engineer with a strong background in vacuum systems and knowledge in Data Science, I am confident that my skills and expertise align well with your company's mission to develop innovative fusion technologies for clean, safe, and abundant electricity.
I am particularly drawn to Helion Energy's unique approach to fusion, focusing on pulsed, non-ignition systems, direct electricity recovery, and the use of deuterium and helium-3 as fuel. I believe that my expertise in vacuum systems, combined with my passion for contributing to cutting-edge technologies in clean energy, make me an ideal candidate for this position.
As an engineer who thrives on solving complex problems and continuously expanding my knowledge, I am eager to join a team that values innovation, collaboration, and the pursuit of a sustainable energy future. I am confident that my skills and experience will enable me to make valuable contributions to Helion Energy's mission and help drive the company's success in developing transformative fusion technologies.
Thank you for considering my application. I look forward to the opportunity to discuss further how my expertise can contribute to Helion Energy's groundbreaking work in fusion research and clean energy solutions.

Sincerely,
Aleksandr Duk'''




if __name__ == '__main__':

    #Build CV
    try:
        build(
            file_css=file_css,
            file_cv=file_cv,
            db_data = db,
            job_title=job_title,
            phone_type=phone
        )
        webbrowser.open_new_tab("".join(["file:///", os.getcwd(), "/", file_cv]))
    except Exception as e:
        print("Something happened and build() didn't run")
        # print(e)
        traceback.print_exc()

    # Build CL
    # file_css, file_cl, db_data, job_title, phone_type, cover_letter
    if cover_letter_flag:
        try:
            build_cl(
                file_css,
                file_cl,
                db,
                job_title,
                phone,
                cover_letter
            )
            webbrowser.open_new_tab("".join(["file:///", os.getcwd(), "/", file_cl]))
        except Exception as e:
            print("Something happened and CL build() didn't run")
            traceback.print_exc()
            # print(e)