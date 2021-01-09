import os
import re

def str_replace_in_html(find, replacement):
    for dname, dirs, files in os.walk("../build"):
        for fname in files:
            if fname.endswith('.html'):
                fpath = os.path.join(dname, fname)
                
                try:
                    with open(fpath) as f:
                        s = f.read()
                    s = s.replace(find, replacement)
#                     print(s)
                    with open(fpath, "w") as f:
                        f.write(s)
    
                except IOError:
                    print("File not accessible")
              

def get_cdn_links():
    outfile = open("_tmp/cdn-links.txt", "w")  
    for dname, dirs, files in os.walk("jtnimoy.net/"):
        for fname in files:
            if fname.endswith('.html'):
                fpath = os.path.join(dname, fname)
                
                # ignores
                if ".ipynb_checkpoints" in dname:
                    continue
                if "_tmp" in dname:
                    continue;

                with open(fpath) as f:  
                    s = f.read()

                # find all urls                    
                urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', s)
                if (urls):             
                    for url in urls:

                        # write all links
                        # outfile.write(url + "\n")

                        # only write cdn links
                        if "cdn-jtnim" in url:
                            outfile.write(url + "\n")
