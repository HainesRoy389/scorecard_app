import os

def assemble_course_scorecard(tex_file_name, new_tex_file_output):
    # Local Variables

    # Statements

    # Grade Distribution Insertion
    insert_grade_distribution(tex_file_name, new_tex_file_output)

def insert_grade_distribution(input, output):
    # Local Declarations
    placeholder = '% INSERT_IMAGE_HERE' # String that is replaced

    # Insert grade distribution picture

    # LaTeX code to insert
    image_latex_code = r"""
    \includegraphics[width=0.95\linewidth, height=0.95\GradeVisH, keepaspectratio]{work-in-progress.png}
    """

    # File reading and writing
    try:
        # Read latex file
        with open(input, 'r') as f:
            content = f.read()

        # Check if the placeholder exists
        if placeholder in content:
            # Replace the placeholder with the LaTeX code
            new_content = content.replace(placeholder, image_latex_code)
            
            # Write the modified content to a new file
            with open(output, 'w') as f:
                f.write(new_content)
                
            print(f"Success! Image code inserted into '{output}'.")
        else:
            print(f"Error: Could not find the placeholder '{placeholder}' in '{input}'.")
            print("Please add that exact line to your .tex file where you want the image.")

    except FileNotFoundError:
        print(f"Error: The file '{input}' was not found.")

# 
assemble_course_scorecard('src\main.tex', 'src\output.tex')
