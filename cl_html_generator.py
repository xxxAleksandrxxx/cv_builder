# NAME AND JOB TITLE
def html_header(data_name, data_job_title):
    if any([data_name, data_job_title]):
        return f'''
            <div class="head_container">
                <div class="name">
                    <h1>{data_name}</h1>
                </div>
                <div class="job-title">
                    <h2>{data_job_title}</h2>
                </div>
            </div>
            <div class="vline"></div>
        '''
    else:
        return ""


# CONTACT INFO
def html_contactinfo(data_email, data_phone, data_linkedin="", data_github=""):
    if any([data_email, data_phone, data_linkedin, data_github]):
        data_contactinfo_html = f'''
                <table>
                    <tr>
                        <td>Email:</td>
                        <td><a href="{data_email}">{data_email}</a></td>
                        <td class="info_separator"></td>
                        <td>Linkedin:</td>
                        <td><a href="{data_linkedin}">{data_linkedin}</a></td>
                    </tr>
                        <td>Phone:</td>
                        <td>{data_phone}</td>
                        <td class="info_separator"></td>
                        <td>{["", "GitHub:"][len(data_github)!=0]}</td>
                        <td><a href="{data_github}">{data_github}</a></td>
                    <tr>
                    </tr>
                </table>

            '''
        return f'''
            <div class="contactinfo_container">
                {data_contactinfo_html}
            </div>
        '''


# COVER LETTER
def html_cover_letter(cover_letter):
    if cover_letter:
        cover_letter_html = f'''
                <div class="block">
                    {cover_letter.replace("\n", "<br />")}
                </div>
        '''
        return f'''
            <div class="bio">
                {cover_letter_html}
            </div>
        '''
    else:
        return ""


# HTML PAGE
def html_main(file_css, name, job_title, email, phone, github, linkedin, cover_letter):
    return f'''<!DOCTYPE html
        PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

    <head>
        
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
    <title>{name} CV</title>
    <link rel="stylesheet" type="text/css" href="{file_css}">

    </head>
    <body>
        
    <div id="cv_div">
        {html_header(name, job_title)}
        {html_contactinfo(email, phone, linkedin, github)}
        {html_cover_letter(cover_letter)}
    </div>
    </body>
    </html>'''


def build_cl(file_css, file_cl, db_data, job_title, phone_type, cover_letter):
    name = db_data["user"]["name"]
    email = db_data["user"]["email"]
    phone = db_data["user"]["phone"][phone_type]
    github = db_data["user"]["github"]
    linkedin = db_data["user"]["linkedin"]

    with open(file_cl, 'w') as f:
        try:
            f.write(html_main(file_css, name, job_title, email, phone, github, linkedin, cover_letter))
            print(f"Create {file_cl}: Done")
        except Exception as e:
            print("Error. didn't succeed with f.write(html_main)")
            print(e)