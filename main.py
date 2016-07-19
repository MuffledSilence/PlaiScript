#Imports

import sys, os, time, guide, downloader
from time import sleep

#Base Variables

version = "0.0.2"
versionName = "The Basic Function One"
html_directory = "html"
html_pages = html_directory+"/pages.txt"
html_directory_files = []
python = sys.executable
current_date = time.localtime()
current_date = [current_date[0], current_date[1], current_date[2]]
last_checked_read = ""

#Functions

def list_html():
    for html_file in os.listdir(html_directory):
        html_directory_files.append(html_file)

def cleanup():
    for cleanup_html in os.listdir(html_directory):
        if cleanup_html != "pages.txt":
            if cleanup_html != "last_checked.txt":
                try:
                    os.remove(html_directory+"/"+cleanup_html)
                except WindowsError:
                    try:
                        os.rmdir(html_directory+"/"+cleanup_html)
                    except WindowsError:
                        for item in os.listdir(html_directory+"/"+cleanup_html):
                            os.remove(html_directory+"/"+cleanup_html+"/"+item)
                            print "Deleted", item
                        os.rmdir(html_directory+"/"+cleanup_html)
                print "Deleted ", cleanup_html
        else:
            pass

def date_check():
    #Returns True if same as last checked and False if different
    global last_checked_read
    list_html()
    if "last_checked.txt" in html_directory_files:
        pass
    else:
        last_checked = open(html_directory+"/last_checked.txt", 'w+')
    last_checked = open(html_directory+"/last_checked.txt", 'r')
    try:
        last_checked_read = [int(x) for x in ((last_checked.read()).strip("[]")).split(",")]
    except ValueError:
        last_checked_read = ["Never", "Never", "Never"]
    if current_date == last_checked_read:
        return True
    else:
        last_checked = open(html_directory+"/last_checked.txt", 'w')
        last_checked.write(str(current_date))
        return False
    last_checked.close()

def html_update_check():
    global last_checked_read
    update_check_result = date_check()
    if update_check_result == False:
        print "Last check {0}-{1}-{2}".format(last_checked_read[1], last_checked_read[2], last_checked_read[0])
        update_date_file = open(html_directory+"/last_checked.txt", 'w')
        update_date_file.write(str(current_date))
    elif update_check_result == True:
        print "Last check was today! {0}-{1}-{2}".format(last_checked_read[1], last_checked_read[2], last_checked_read[0])

def restart():
    os.execl(python, python, * sys.argv)

def select_download():
    try:
        download_select = int(raw_input("\nWhich would you like to download?\n"
                                    "  1. All\n"
                                    "  2. Single File\n"))
    except:
        print "Not a selection!"
        restart()
    if download_select == 1:
        downloader.get_all_pages()
    elif download_select == 2:
        downloader.get_page()
    else:
        print "Not a selection!"
        restart()


#Main
def main():
    html_update_check()
    print "Version: " + version + " " + versionName
    while True:
        main_selection = raw_input(" \nSelection:\n" +
                                   "   1. Download html files \n   2. Cleanup Files \n"
                                   "   3. Start Guide \n   Anything else to exit.\n")
        try:
            main_selection = int(main_selection)
        except:
            print "Exiting..."
            break
        if main_selection == 1:
            select_download()
        elif main_selection == 2:
            cleanup()
        elif main_selection == 3:
            guide.main()
        elif main_selection == 4:
            downloader.main()
        else:
            print "Exiting..."
            sleep(2)
            sys.exit()




if __name__ == '__main__':
    main()