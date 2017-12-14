#!/home/my_bin/anaconda3/bin/python
import os

home = os.path.expanduser("~")
snippets_dir = os.path.join(home, ".dotfiles/org/snippets")
user_dir = os.path.join(home, ".dotfiles/org/user")
templates_dir = os.path.join(home, ".dotfiles/org/templates")

snippets={}
templates={}
templates['presentation'] = os.path.join(templates_dir,"presentation.xml")
templates['text'] = os.path.join(templates_dir,"text.xml")
# templates['paper'] = os.path.join(templates_dir,"paper.xml")
# templates['report'] = os.path.join(templates_dir,"report.xml")
# parse snippet dir, and get snippet name

snippet_name_list = os.listdir(snippets_dir)
for snippet_file_name in snippet_name_list:
    with open(os.path.join(snippets_dir,snippet_file_name)) as f1:
        # replace dir path with its contents
        snippets[snippet_file_name[0:-4]] = f1.read()

for template in ['presentation','text']:
    with open(os.path.join(templates_dir, template + ".xml"), 'r') as f1:
        my_styles = f1.read()
        for key in snippets.keys():
            target = '<' + key + '/>'
            replacement = snippets[key]
            my_styles = my_styles.replace(target,replacement)
        with open(os.path.join(user_dir, template + '.xml'),'w') as f2:
            f2.write(my_styles)
