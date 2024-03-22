from research.cv_html_generator import build

if __name__ == '__main__':
    try:
        build()
        print("Done")
    except:
        print("Something happened and build() didn't run")