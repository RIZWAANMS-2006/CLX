import argparse as ap
import os
import sys

pl_list = {
    "py": 'print("Hello for python")',
    "js": 'console.log("Hello from javascript")',
    "java": 'public class {0}{{\n\tpublic static void main(String[] args){{\n\tSystem.out.println("Hello from java")\n}}\n}}',
    "cpp": '#include <iostream>\n\tint main(){{std::cout<<"Hello from cpp";return 0;}}',
    "c": '#include <stdio.h>\n\tint main(){{\n\tprintf("Hello from c");\nreturn 0;\n}}',
    "kt": 'fun main(){{\n\tprintln("Hello from kotlin")\n\t}}',
    "dart": 'void main(){{\n\tprint("Hello from dart")\n\t}}',
}

# try:

parser = ap.ArgumentParser(
    description="CLX - Custome Learner Xtream ToolKit",
    epilog='Example usage:python clx.py "my_project" -pl py js -b y',
    # exit_on_error=False,
)

parser.add_argument("project_name", help="Name of the project folder and its files")
parser.add_argument(
    "languages", nargs="+", help="List of programming languages (extensions only)"
)
parser.add_argument(
    "--no-code", action="store_true", help="Does not generate boilerplate code"
)
parser.add_argument(
    "--force",
    action="store_true",
    help="Forcefully created files which are not listed without boilerplate code",
)
argument = vars(parser.parse_args())
print(argument)
project_name = argument["project_name"].strip()
languages = argument["languages"]
code = not argument["no_code"]
force = argument["force"]

print(project_name, languages, code, sep=" ")

try:
    os.makedirs(project_name)
    print("Project folder created successfully.")
except:
    print("Project already exist")
    sys.exit()

try:
    for lang in languages:
        if lang in pl_list:
            with open(f"{project_name}/{project_name}.{lang}", "x") as f:
                if code:
                    f.write(pl_list[lang].format(project_name))
                
except Exception as e:
    print(f"Error: {e}")
