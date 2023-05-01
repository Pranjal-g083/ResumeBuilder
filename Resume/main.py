from Cheetah.Template import Template
import os
import shutil


def CreatePDF(template_type, output_name, dict):
    file_dir = os.path.join(os.getcwd(), f'Template{template_type}\\')
    file_name = os.path.join(file_dir, 'template.tex')
    out_file_name = os.path.join(file_dir, 'output.tex')

    with open(file_name, 'r') as f:
        template_str = f.read()

    # preprocess skills
    for el in dict["Skills"]:
        el["SkillSetCommas"] = el["SkillSet"]
        el["SkillSet"] = el["SkillSet"].split(", ")
    # preprocess project
    for el in dict["Projects"]:
        el["Description"] = el["Description"].split("\n ")
    # preprocess courses
    for el in dict["KeyCourses"]:
        el["CourseCommas"] = el["Courses"]
        el["Courses"] = el["Courses"].split(", ")

    # preprocess workdone
    for el in dict["Experience"]:
        el["WorkDoneSplit"] = el["WorkDone"].split(". ")

    template = Template(template_str, searchList=[dict])
    template = template.__str__()

    with open(out_file_name, 'w') as f:
        f.write(template)
    
    os.chdir(file_dir)
    os.system(f'pdflatex -interaction=batchmode output.tex' )
    
    # For pdf
    os.rename(os.path.join(file_dir, 'output.pdf'), os.path.join(file_dir, output_name + '.pdf'))
    shutil.move(os.path.join(file_dir, output_name + '.pdf'), os.path.join(file_dir, '../', output_name + '.pdf'))
    
    # For latex
    os.rename(os.path.join(file_dir, 'output.tex'), os.path.join(file_dir, output_name + '.tex'))
    shutil.move(os.path.join(file_dir, output_name + '.tex'), os.path.join(file_dir, '../', output_name + '.tex'))
    
    os.chdir(os.path.join(file_dir, '../'))
    file_dir=os.path.join(file_dir, '../')
    shutil.move(os.path.join(file_dir, output_name + '.pdf'), os.path.join(file_dir, 'static/resume/assets', output_name + '.pdf'))
    shutil.move(os.path.join(file_dir, output_name + '.tex'), os.path.join(file_dir, 'static/resume/assets', output_name + '.tex'))
